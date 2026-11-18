"""V3-LOCAL-INFRA-002: bounded synthetic runtime checks; never changes baseline.

Only this task's nine pinned images/resources are used. No original .env is read.
Private synthetic inputs live outside Git. Evidence and command output are redacted.
Usage: python Validate-Runtime.py preflight|pull|native|start|services|boundary|cleanup|report
"""
import base64
import csv
import datetime as dt
import hashlib
import hmac
import http.client
import json
import os
from pathlib import Path
import re
import secrets
import smtplib
import socket
import struct
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

HERE = Path(__file__).resolve().parent
INFRA = HERE.parent.parent
ROOT = INFRA.parent
EXTERNAL = Path(os.environ['LOCALAPPDATA']) / 'Temp/opencode/V3-LOCAL-INFRA-002'
PRIVATE = EXTERNAL / 'private'
STATE = PRIVATE / 'state.json'
BASELINE = '094c966de745285bd5a8d1975312eb06d930d4a8'
S = {}
VALUES = {}
CHECKS = []
COMMANDS = []

def now():
    return dt.datetime.now(dt.timezone.utc).isoformat()

def need(ok, reason):
    if not ok:
        raise RuntimeError(reason)

def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest().upper()

def scrub(value):
    text = str(value)
    for key, val in VALUES.items():
        if re.search(r'PASSWORD|SECRET|ACCESS_KEY|_USER$', key) and val:
            text = text.replace(val, '[REDACTED]')
            text = text.replace(urllib.parse.quote(val, safe=''), '[REDACTED]')
    for user, password in [('RABBITMQ_USER', 'RABBITMQ_PASSWORD'),
                           ('GRAFANA_ADMIN_USER', 'GRAFANA_ADMIN_PASSWORD')]:
        if user in VALUES:
            token = base64.b64encode((VALUES[user]+':'+VALUES[password]).encode()).decode()
            text = text.replace(token, '[REDACTED_BASIC]')
    # Additional guard for generated credentials in upstream console messages.
    text = re.sub(r'(?i)((?:password|secret[_ -]?key|access[_ -]?key|authorization)\s*[:=]\s*)("[^"]*"|\S+)',
                  r'\1[REDACTED]', text)
    text = re.sub(r'(?i)((?:X-Amz-(?:Credential|Signature|Security-Token)|token)=)[^&\s"<>]+',
                  r'\1[REDACTED]', text)
    text = re.sub(r'(?i)Bearer\s+[A-Za-z0-9._~+/=-]+', 'Bearer [REDACTED]', text)
    return text

def write(name, obj):
    HERE.mkdir(parents=True, exist_ok=True)
    def sanitized(value):
        if isinstance(value, str):
            return scrub(value)
        if isinstance(value, dict):
            return {k:sanitized(v) for k,v in value.items()}
        if isinstance(value, (list, tuple)):
            return [sanitized(v) for v in value]
        return value
    # Redact string values BEFORE JSON serialization; never corrupt JSON quoting.
    text = json.dumps(sanitized(obj), indent=2, ensure_ascii=False) + '\n'
    (HERE / name).write_text(text, encoding='utf-8', newline='\n')

def load_checks():
    global CHECKS, COMMANDS
    if (HERE/'checks.json').exists():
        CHECKS = json.loads((HERE/'checks.json').read_text(encoding='utf-8'))
    if (HERE/'runtime-commands.json').exists():
        COMMANDS = json.loads((HERE/'runtime-commands.json').read_text(encoding='utf-8'))

def check(cid, service, expected, ok, actual, limitation='', blocked=False):
    # Never replace an earlier FAIL with a later PASS: append observations.
    status = 'BLOCKED' if blocked else ('PASS' if ok else 'FAIL')
    reference = 'observations/'+cid+'-'+str(len(CHECKS)+1)+'.json'
    (HERE/'observations').mkdir(exist_ok=True)
    write(reference, {'observedAt': now(), 'actual': actual})
    CHECKS.append({'checkIdentifier': cid, 'service': service, 'expectedResult': expected,
                   'actualResult': actual, 'status': status, 'evidenceReference': reference,
                   'remainingLimitation': limitation})
    write('checks.json', CHECKS)
    print(cid+': '+status, flush=True)
    return ok and not blocked

def process(args, stdin=None, timeout=120, env=None):
    started = now()
    try:
        # Binary stdin avoids Windows TextIOWrapper converting secret lines to CRLF.
        p = subprocess.run([str(a) for a in args], input=stdin.encode('utf-8') if isinstance(stdin,str) else stdin, capture_output=True,
                           timeout=timeout,
                           env=env, cwd=ROOT)
        result = {'code': p.returncode, 'stdout': p.stdout.decode('utf-8','replace'), 'stderr': p.stderr.decode('utf-8','replace')}
    except subprocess.TimeoutExpired as e:
        result = {'code': 124, 'stdout': '', 'stderr': 'bounded command timeout'}
    COMMANDS.append({'startedAt': started, 'arguments': [scrub(a) for a in args],
                     'stdin': 'NOT RECORDED' if stdin is not None else 'NONE',
                     'exitCode': result['code']})
    write('runtime-commands.json', COMMANDS)
    return result

def plain(args, **kw):
    r = process(args, **kw)
    need(r['code'] == 0, scrub(r['stderr']) or 'Command failed: '+str(args[:3]))
    return r['stdout'].strip()

def docker(args, **kw):
    prefix = ['docker.exe']
    if S.get('engine'):
        prefix += ['--host', S['engine'], '--config', str(PRIVATE/'docker-config')]
    return process(prefix+args, **kw)

def dtext(args, **kw):
    r = docker(args, **kw)
    need(r['code'] == 0, scrub(r['stderr']) or 'Docker operation failed')
    return r['stdout'].strip()

def inspect_one(kind, identity, template):
    return json.loads(dtext([kind, 'inspect', '--format', template, identity]))

CONTAINER_FORMAT = '''{"id":{{json .Id}},"name":{{json .Name}},"imageID":{{json .Image}},"imageReference":{{json .Config.Image}},"project":{{json (index .Config.Labels "com.docker.compose.project")}},"service":{{json (index .Config.Labels "com.docker.compose.service")}},"status":{{json .State.Status}},"running":{{json .State.Running}},"startedAt":{{json .State.StartedAt}},"restartCount":{{json .RestartCount}},"oomKilled":{{json .State.OOMKilled}},"ports":{{json .HostConfig.PortBindings}},"networks":{{json .NetworkSettings.Networks}},"mounts":{{json .Mounts}},"memory":{{json .HostConfig.Memory}},"nanoCPUs":{{json .HostConfig.NanoCpus}},"pidsLimit":{{json .HostConfig.PidsLimit}},"privileged":{{json .HostConfig.Privileged}},"networkMode":{{json .HostConfig.NetworkMode}},"securityOpt":{{json .HostConfig.SecurityOpt}},"capAdd":{{json .HostConfig.CapAdd}},"logConfig":{{json .HostConfig.LogConfig}},"restartPolicy":{{json .HostConfig.RestartPolicy}}}'''
NETWORK_FORMAT = '''{"id":{{json .Id}},"name":{{json .Name}},"driver":{{json .Driver}},"internal":{{json .Internal}},"project":{{json (index .Labels "com.docker.compose.project")}},"ipam":{{json .IPAM}},"containers":{{json .Containers}},"options":{{json .Options}}}'''
VOLUME_FORMAT = '''{"name":{{json .Name}},"driver":{{json .Driver}},"mountpoint":{{json .Mountpoint}},"createdAt":{{json .CreatedAt}},"project":{{json (index .Labels "com.docker.compose.project")}},"options":{{json .Options}}}'''
IMAGE_FORMAT = '''{"id":{{json .Id}},"repoTags":{{json .RepoTags}},"repoDigests":{{json .RepoDigests}},"architecture":{{json .Architecture}},"os":{{json .Os}}}'''

def inventory():
    containers = [inspect_one('container', i, CONTAINER_FORMAT) for i in dtext(['ps','-aq','--no-trunc']).splitlines()]
    networks = [inspect_one('network', i, NETWORK_FORMAT) for i in dtext(['network','ls','-q','--no-trunc']).splitlines()]
    volumes = [inspect_one('volume', i, VOLUME_FORMAT) for i in dtext(['volume','ls','-q']).splitlines()]
    images = [inspect_one('image', i, IMAGE_FORMAT) for i in sorted(set(dtext(['image','ls','-q','--no-trunc']).splitlines()))]
    return {'containers':containers,'networks':networks,'volumes':volumes,'images':images}

def save_state():
    STATE.write_text(json.dumps(S, indent=2), encoding='utf-8')

def read_state():
    global S, VALUES
    S = json.loads(STATE.read_text(encoding='utf-8'))
    VALUES = S['values']

def compose(args, envfile=None, timeout=180):
    # Every interpolated value is task-generated, never inherited from real env.
    env = os.environ.copy()
    env.update(VALUES)
    env['COMPOSE_DISABLE_ENV_FILE'] = '1'
    env.pop('COMPOSE_FILE', None)
    env.pop('COMPOSE_PROFILES', None)
    # Explicit envfile when testing an existing-volume password change.
    if envfile:
        env.pop('POSTGRES_APP_PASSWORD', None)
    return docker(['compose','--project-name',S['project'],'--env-file',str(envfile or PRIVATE/'runtime.env'),
                   '--project-directory',str(INFRA),'-f',str(INFRA/'compose.yaml'),
                   '-f',str(INFRA/'compose.seaweedfs.yaml')]+args, timeout=timeout, env=env)

def task_containers():
    ids = dtext(['ps','-aq','--filter','label=com.docker.compose.project='+S['project']]).splitlines()
    return {c['service']: c for c in [inspect_one('container',i,CONTAINER_FORMAT) for i in ids] if c['service']}

def task_container(service):
    ids=dtext(['ps','-aq','--filter','label=com.docker.compose.project='+S['project'],
               '--filter','label=com.docker.compose.service='+service]).splitlines()
    need(len(ids)==1, 'Expected one task-owned service: '+service)
    c=inspect_one('container',ids[0],CONTAINER_FORMAT)
    need(c['project'] == S['project'], 'Missing task-owned service: '+service)
    need(c['id'] not in S['beforeContainerIDs'], 'Pre-existing container must never be targeted')
    return c

def task_id(service):
    return task_container(service)['id']

def dexec(service, command, stdin=None, timeout=60):
    return docker(['exec','-i',task_id(service)]+command, stdin=stdin, timeout=timeout)

def wait_ready(service, seconds=120):
    deadline = time.monotonic()+seconds
    last = {}
    while time.monotonic() < deadline:
        try:c=task_container(service)
        except RuntimeError:return False, {'reason':'task container absent'}
        h = json.loads(dtext(['container','inspect','--format','{{json .State.Health}}',c['id']]))
        last = {'status':c['status'],'health':h.get('Status') if h else 'not-configured'}
        if c['status'] in ['exited','dead']:
            return False, last
        if h and h.get('Status') == 'healthy':
            return True, last
        if not h and c['running']:
            return True, last
        time.sleep(2)
    return False, last

def http(port, path, method='GET', obj=None, basic=None, data=None, headers=None):
    if S.get('internalHttpMode'):
        mapping={'RABBITMQ_UI_PORT':('broker','rabbitmq',15672),'PROMETHEUS_PORT':('telemetry','prometheus',9090),
                 'GRAFANA_PORT':('telemetry','grafana',3000),'MAILPIT_UI_PORT':('mail','mailpit',8025)}
        for key,(network,service,internal_port) in mapping.items():
            if int(VALUES[key])==int(port):
                if obj is not None:data=json.dumps(obj).encode()
                hs=dict(headers or {})
                if obj is not None:hs['Content-Type']='application/json'
                return curl_request(network,'http://'+service+':'+str(internal_port)+path,method,data,basic,hs)
    h = dict(headers or {})
    if obj is not None:
        data = json.dumps(obj).encode(); h['Content-Type']='application/json'
    if basic:
        h['Authorization']='Basic '+base64.b64encode((basic[0]+':'+basic[1]).encode()).decode()
    req = urllib.request.Request('http://127.0.0.1:'+str(port)+path, data=data, headers=h, method=method)
    # No environment proxy, no redirects to non-task endpoints.
    class NoRedirect(urllib.request.HTTPRedirectHandler):
        def redirect_request(self, req, fp, code, msg, headers, newurl):
            return None
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}), NoRedirect())
    try:
        with opener.open(req, timeout=8) as response:
            return response.status, response.read()
    except urllib.error.HTTPError as e:
        return e.code, e.read()

def preflight():
    global S, VALUES
    need(not STATE.exists(), 'A private session already exists; never overwrite it')
    head = plain(['git.exe','--no-optional-locks','rev-parse','HEAD'])
    branch = plain(['git.exe','--no-optional-locks','branch','--show-current'])
    need(head == BASELINE and branch == 'codex/v3-local-infra-001', 'Unexpected isolated baseline')
    static = json.loads((INFRA/'.validation/static-results.json').read_text(encoding='utf-8'))
    need(len(static['inputHashes']) == 17, 'Expected the original 17 verified artifacts')
    hashes = {}
    for name, fact in static['inputHashes'].items():
        actual = digest(INFRA/name); need(actual == fact['sha256'], 'Baseline artifact drift: '+name)
        hashes[name] = actual
    need(not (INFRA/'.env').exists(), 'Never reuse an actual env file in this workspace')
    engine = json.loads(plain(['docker.exe','context','inspect','--format','{{json .Endpoints.docker.Host}}']))
    need(engine.startswith('npipe://'), 'Only the observed local Docker Desktop engine is authorized')
    PRIVATE.mkdir(parents=True, exist_ok=False)
    sidline = plain(['whoami.exe','/user','/fo','csv','/nh'])
    sid = list(csv.reader([sidline]))[0][1]
    plain(['icacls.exe',str(PRIVATE),'/inheritance:r','/grant:r','*'+sid+':(OI)(CI)F','/grant:r','*S-1-5-18:(OI)(CI)F'])
    (PRIVATE/'docker-config').mkdir()
    (PRIVATE/'docker-config/config.json').write_text('{"auths":{}}', encoding='utf-8')
    project = 'v3li002-'+dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dt%H%M%S')+'-'+secrets.token_hex(3)
    VALUES = {}
    for line in (INFRA/'.env.example').read_text(encoding='utf-8').splitlines():
        if not line or line.startswith('#') or '=' not in line:
            continue
        key, value = line.split('=',1)
        if re.search('PASSWORD|SECRET|ACCESS_KEY|_USER$', key):
            value = 'li002'+secrets.token_hex(20)
        VALUES[key] = value
    VALUES['COMPOSE_PROJECT_NAME'] = project
    port_keys = [k for k in VALUES if k.endswith('_PORT')]
    sockets = []
    try:
        for key in port_keys:
            sock = socket.socket(); sock.bind(('127.0.0.1',0)); sockets.append(sock)
            VALUES[key] = str(sock.getsockname()[1])
    finally:
        for sock in sockets: sock.close()
    S = {'project':project,'engine':engine,'values':VALUES,'baselineHashes':hashes,'baselineHead':head,
         'createdAt':now(),'nativeContainers':[],'imageReferences':json.loads((INFRA/'image-references.json').read_text())['images']}
    before = inventory()
    need(not any(c['project'] == project for c in before['containers']), 'Project collision')
    need(not any(n['name'].startswith(project+'_') for n in before['networks']), 'Network collision')
    need(not any(v['name'].startswith(project+'_') for v in before['volumes']), 'Volume collision')
    used = {int(p['HostPort']) for c in before['containers'] for ps in (c['ports'] or {}).values() for p in (ps or [])}
    need(not used.intersection(int(VALUES[k]) for k in port_keys), 'Existing Docker port collision')
    info = json.loads(dtext(['info','--format','{"os":{{json .OSType}},"arch":{{json .Architecture}},"memory":{{.MemTotal}},"cpus":{{.NCPU}}}']))
    need(info['os']=='linux' and info['arch'] in ['x86_64','amd64'], 'Unsupported runtime platform')
    need(info['memory'] >= 7_000_000_000, 'Insufficient Docker memory for bounded parallel validation')
    S['beforeContainerIDs'] = [c['id'] for c in before['containers']]
    S['before'] = before
    (PRIVATE/'runtime.env').write_text('\n'.join(k+'='+v for k,v in VALUES.items())+'\n',encoding='utf-8')
    save_state()
    write('docker-before.json',before)
    write('session.json',{'task':'V3-LOCAL-INFRA-002','createdAt':now(),'project':project,'engine':engine,
                          'branch':branch,'head':head,'baseline17Hashes':hashes,
                          'ports':{k:int(VALUES[k]) for k in port_keys},'privateInputs':'OUTSIDE GIT; restricted ACL; never printed',
                          'preExistingCounts':{k:len(v) for k,v in before.items()},'engineResources':info})
    check('LIR002-PREFLIGHT','all','17 unchanged baseline files; unique project, ports, fresh volumes and local engine',True,
          {'baselineFiles':17,'project':project,'portCollision':False,'resourceCollision':False,'engine':info},
          'Shared Docker host is trusted. Existing live volume contents are not frozen or byte-snapshotted.')

def pull():
    rows=[]
    before_ids={i['id'] for i in S['before']['images']}
    all_ok=True
    for i in S['imageReferences']:
        ref=i['reference']
        existing=docker(['image','inspect','--format',IMAGE_FORMAT,ref])
        downloaded=existing['code'] != 0
        if downloaded:
            print('Pulling approved pinned image: '+i['service'],flush=True)
            r=docker(['pull','--platform','linux/amd64',ref],timeout=300)
            if r['code'] != 0:
                check('LIR002-IMAGE-'+i['service'],i['service'],'Only the exact allowed digest is available',False,r)
                all_ok=False; rows.append({'service':i['service'],'reference':ref,'status':'FAIL','downloadAttempted':True});continue
        actual=inspect_one('image',ref,IMAGE_FORMAT)
        expected_digest=ref.split('@')[1]
        ok=any(d.endswith('@'+expected_digest) for d in actual['repoDigests']) and actual['os']=='linux' and actual['architecture']=='amd64'
        all_ok=all_ok and ok
        row={'service':i['service'],'reference':ref,'actual':actual,'pullRequired':downloaded,
             'newImageID':actual['id'] not in before_ids,'status':'PASS' if ok else 'FAIL'}
        rows.append(row)
        check('LIR002-IMAGE-'+i['service'],i['service'],'Exact approved digest; linux/amd64',ok,row,
              'Digest identity is not a vulnerability scan or publisher attestation.')
    write('image-identity-verification.json',rows)
    need(all_ok,'Image identity/pull failure; do not start services')

def native_container(service, entrypoint, args, mount_files):
    ref=next(i['reference'] for i in S['imageReferences'] if i['service']==service)
    name=S['project']+'-native-'+service+'-'+secrets.token_hex(2)
    cmd=['create','--name',name,'--label','com.docker.compose.project='+S['project'],
         '--label','neshane.task=V3-LOCAL-INFRA-002','--network','none','--read-only',
         '--cap-drop','ALL','--security-opt','no-new-privileges:true','--memory','256m','--cpus','0.5',
         '--pids-limit','128','--log-driver','json-file','--log-opt','max-size=5m','--log-opt','max-file=2']
    for source,target in mount_files:
        cmd += ['--mount','type=bind,src='+str(source)+',dst='+target+',readonly']
    declared=json.loads(dtext(['image','inspect','--format','{{json .Config.Volumes}}',ref])) or {}
    for path in declared:
        # Native config tools must not leave unlabeled anonymous image volumes.
        cmd += ['--tmpfs',path+':rw,nosuid,noexec,size=16m']
    cmd += ['--entrypoint',entrypoint,ref]+args
    cid=dtext(cmd); S['nativeContainers'].append(cid);save_state()
    c=inspect_one('container',cid,CONTAINER_FORMAT)
    need(c['project']==S['project'] and cid not in S['beforeContainerIDs'],'Native container ownership mismatch')
    r=docker(['start','--attach',cid],timeout=90)
    logs=docker(['logs','--tail','150',cid])
    write('observations/native-'+service+'-'+cid[:12]+'.json',{'commandResult':r,'logs':logs,'containerID':cid,'network':'none'})
    return r

def native():
    collector=native_container('otel-collector','/otelcol-contrib',['validate','--config=/config.yaml'],
                               [(INFRA/'observability/otel-collector.yaml','/config.yaml')])
    check('LIR002-NATIVE-COLLECTOR','otel-collector','Native Collector config/components/OTTL validation exits zero',collector['code']==0,collector)
    prom=native_container('prometheus','/bin/promtool',['check','config','/config.yml'],
                          [(INFRA/'observability/prometheus.yml','/config.yml')])
    check('LIR002-NATIVE-PROMETHEUS','prometheus','Native promtool config validation exits zero',prom['code']==0,prom)
    tempo=native_container('tempo','/tempo',['-config.file=/config.yaml','-config.verify=true'],
                           [(INFRA/'observability/tempo.yaml','/config.yaml')])
    check('LIR002-NATIVE-TEMPO','tempo','Native Tempo configuration verification exits zero',tempo['code']==0,tempo,
          'An unsupported verify flag is a native validation failure, not permission to invent success; actual startup is separately observed.')
    # Grafana native loading/provisioning is assessed through its real startup and API.

def start():
    for key,val in VALUES.items():
        if key.endswith('_PORT'):
            sock=socket.socket()
            try:sock.bind(('127.0.0.1',int(val)))
            finally:sock.close()
    S['blockedServices']=[]
    if any(c['checkIdentifier']=='LIR002-NATIVE-COLLECTOR' and c['status']=='FAIL' for c in CHECKS):
        S['blockedServices'].append('otel-collector')
    save_state()
    allowed=[i['service'] for i in S['imageReferences'] if i['service'] not in S['blockedServices']]
    r=compose(['up','-d','--pull','never']+allowed,timeout=240)
    check('LIR002-START','all','Only task-owned pinned services start without pull or baseline edits',r['code']==0,r)
    # Observe each service separately even when another service fails.
    for service in ['postgres','redis','rabbitmq','mailpit','tempo','otel-collector','prometheus','grafana','seaweedfs']:
        if service in S['blockedServices']:
            check('LIR002-READY-'+service,service,'Start only native-valid configuration',False,
                  'Not started: native configuration rejected. Baseline is deliberately unchanged.',
                  'Fix requires a separately authorized baseline correction, not a weakened filter.',blocked=True)
            continue
        ok,actual=wait_ready(service,100)
        check('LIR002-READY-'+service,service,'Container remains running; configured health check is healthy',ok,actual,
              'No Docker healthcheck for Collector/Tempo/SeaweedFS: independent endpoint checks are also required.' if service in ['tempo','otel-collector','seaweedfs'] else '')
    boundaries()
    logs()

def boundaries():
    cs=task_containers(); rows=[]
    expected_network={'postgres':'postgres','redis':'redis','rabbitmq':'broker','mailpit':'mail',
                      'otel-collector':'telemetry','prometheus':'telemetry','grafana':'telemetry',
                      'tempo':'telemetry','seaweedfs':'experimental'}
    expected_limits={'postgres':(512,1),'redis':(384,0.5),'rabbitmq':(768,1),'mailpit':(128,0.5),
                     'otel-collector':(384,0.5),'prometheus':(512,0.5),'grafana':(384,0.5),
                     'tempo':(768,1),'seaweedfs':(512,0.5)}
    allowed_sources=set()
    for rel in ['postgres/10-development-role.sh','rabbitmq/rabbitmq.conf',
                'observability/otel-collector.yaml','observability/prometheus.yml',
                'observability/grafana-datasources.yaml','observability/tempo.yaml']:
        path=str((INFRA/rel).resolve()).replace('\\','/').lower()
        allowed_sources.add(path)
        drive=path[0];tail=path[2:]
        for prefix in ['/run/desktop/mnt/host/','/host_mnt/','/mnt/']:
            allowed_sources.add(prefix+drive+tail)
    expected_ports={'postgres':{'5432/tcp'},'redis':set(),'rabbitmq':{'5672/tcp','15672/tcp'},
                    'mailpit':{'1025/tcp','8025/tcp'},'otel-collector':{'4317/tcp','4318/tcp'},
                    'prometheus':{'9090/tcp'},'grafana':{'3000/tcp'},'tempo':set(),'seaweedfs':{'8333/tcp'}}
    port_variables={'postgres':{'5432/tcp':'POSTGRES_PORT'},'redis':{},
                    'rabbitmq':{'5672/tcp':'RABBITMQ_AMQP_PORT','15672/tcp':'RABBITMQ_UI_PORT'},
                    'mailpit':{'1025/tcp':'MAILPIT_SMTP_PORT','8025/tcp':'MAILPIT_UI_PORT'},
                    'otel-collector':{'4317/tcp':'OTLP_GRPC_PORT','4318/tcp':'OTLP_HTTP_PORT'},
                    'prometheus':{'9090/tcp':'PROMETHEUS_PORT'},'grafana':{'3000/tcp':'GRAFANA_PORT'},
                    'tempo':{},'seaweedfs':{'8333/tcp':'SEAWEEDFS_S3_PORT'}}
    for service,c in cs.items():
        actual_ports={k for k,v in (c['ports'] or {}).items() if v}
        ok=c['project']==S['project'] and c['name'].lstrip('/').startswith(S['project']+'-')
        ok=ok and actual_ports==expected_ports[service]
        ok=ok and all(p['HostIp']=='127.0.0.1' for ps in (c['ports'] or {}).values() for p in (ps or []))
        ok=ok and all(p['HostPort']==VALUES[port_variables[service][port]] for port,ps in (c['ports'] or {}).items() for p in (ps or []))
        ok=ok and not c['privileged'] and c['networkMode'] not in ['host'] and not c['capAdd']
        mem,cpu=expected_limits[service]
        ok=ok and c['memory']==mem*1024*1024 and c['nanoCPUs']==int(cpu*1_000_000_000) and c['pidsLimit']==256
        ok=ok and set(c['networks'])=={S['project']+'_'+expected_network[service]}
        ok=ok and c['restartPolicy']['Name']=='no' and bool(set(c['securityOpt'] or []).intersection({'no-new-privileges:true','no-new-privileges'}))
        ok=ok and c['logConfig']['Type']=='json-file' and c['logConfig']['Config'].get('max-size')=='5m' and c['logConfig']['Config'].get('max-file')=='2'
        for n in c['networks']:
            ni=inspect_one('network',n,NETWORK_FORMAT)
            ok=ok and ni['internal'] and ni['project']==S['project'] and n.startswith(S['project']+'_')
        for m in c['mounts']:
            if m['Type']=='bind':
                ok=ok and not m['RW'] and m['Source'].replace('\\','/').lower() in allowed_sources
                ok=ok and 'docker.sock' not in m['Source'] and Path(m['Source']).name != '.env'
            elif m['Type']=='volume':
                v=inspect_one('volume',m['Name'],VOLUME_FORMAT)
                ok=ok and v['project']==S['project'] and v['name'].startswith(S['project']+'_')
            else:ok=False
        rows.append({'service':service,'passed':ok,'container':c})
        check('LIR002-BOUNDARY-'+service,service,'Project ownership, loopback ports, segmented networks, limits, mounts and no host privileges',ok,c,
              'Metadata/control evidence on a trusted shared host, not hostile-host/tenant isolation acceptance.')
    write('security-boundary-verification.json',rows)

def logs():
    for service,c in task_containers().items():
        r=docker(['logs','--tail','200',c['id']])
        write('observations/log-'+service+'.json',r)

def postgres():
    admin=['sh','-c','exec psql -X -qAt -v ON_ERROR_STOP=1 -U "$POSTGRES_USER" -d "$POSTGRES_DB"']
    app=['sh','-c','PGPASSWORD="$POSTGRES_APP_PASSWORD" exec psql -X -qAt -v ON_ERROR_STOP=1 -h 127.0.0.1 -U neshane_dev_app -d neshane_dev --no-password']
    role=dexec('postgres',admin,"SELECT rolname,rolsuper,rolcreatedb,rolcreaterole,rolreplication,rolbypassrls FROM pg_roles WHERE rolname IN ('neshane_dev_admin','neshane_dev_app') ORDER BY rolname;\n")
    check('LIR002-PG-ROLES','postgres','Bootstrap superuser and app restricted attributes are distinct',role['code']==0 and 'neshane_dev_app|f|f|f|f|f' in role['stdout'] and 'neshane_dev_admin|t|' in role['stdout'],role)
    valid=dexec('postgres',app,'SELECT 1;\n')
    check('LIR002-PG-AUTH','postgres','App authenticates over TCP',valid['code']==0 and valid['stdout'].strip()=='1',valid)
    invalid=dexec('postgres',['sh','-c','PGPASSWORD=INVALID_SYNTHETIC_PASSWORD exec psql -X -qAt -h 127.0.0.1 -U neshane_dev_app -d neshane_dev --no-password -c "SELECT 1"'])
    check('LIR002-PG-INVALID','postgres','Incorrect password rejected',invalid['code']!=0 and 'password authentication failed' in invalid['stderr'],invalid)
    for suffix,sql in [('SUPERUSER','ALTER ROLE neshane_dev_app SUPERUSER;'),('ASSUME-ADMIN','SET ROLE neshane_dev_admin;'),('CREATE-ROLE','CREATE ROLE v3li002_forbidden;'),('CREATE-SCHEMA','CREATE SCHEMA v3li002_forbidden;')]:
        denied=dexec('postgres',app,sql+'\n')
        check('LIR002-PG-DENY-'+suffix,'postgres','Restricted app cannot perform privileged/schema administration',denied['code']!=0 and ('permission denied' in denied['stderr'] or 'must be superuser' in denied['stderr']),denied)
    seed=dexec('postgres',admin,"CREATE TABLE public.v3li002_probe (k text PRIMARY KEY, v text NOT NULL); GRANT SELECT,INSERT ON public.v3li002_probe TO neshane_dev_app;\n")
    value='synthetic-'+S['project']; data=dexec('postgres',app,"INSERT INTO public.v3li002_probe VALUES ('task', '"+value+"'); SELECT v FROM public.v3li002_probe WHERE k='task';\n")
    check('LIR002-PG-SYNTHETIC','postgres','Admin-owned disposable test fixture; limited app INSERT/SELECT',seed['code']==0 and data['code']==0 and value in data['stdout'],{'seed':seed,'data':data},'Synthetic fixture only; no product schema, migrations or RLS implementation.')
    restart=compose(['restart','postgres']);ok,health=wait_ready('postgres',100)
    after=dexec('postgres',app,"SELECT v FROM public.v3li002_probe WHERE k='task';\n")
    check('LIR002-PG-PERSIST','postgres','Synthetic row survives restart',restart['code']==0 and ok and value in after['stdout'],{'health':health,'read':after})
    postgres_existing_volume()

def postgres_existing_volume():
    app=['sh','-c','PGPASSWORD="$POSTGRES_APP_PASSWORD" exec psql -X -qAt -v ON_ERROR_STOP=1 -h 127.0.0.1 -U neshane_dev_app -d neshane_dev --no-password']
    value='synthetic-'+S['project']
    changed=PRIVATE/'changed-volume.env'; newpass='li002'+secrets.token_hex(20)
    # Add to redaction only, not the normal interpolation environment.
    VALUES['TEMP_CHANGED_PASSWORD']=newpass
    changed.write_text('\n'.join(k+'='+(newpass if k=='POSTGRES_APP_PASSWORD' else v) for k,v in VALUES.items() if k!='TEMP_CHANGED_PASSWORD')+'\n',encoding='utf-8')
    try:
        recreate=compose(['up','-d','--no-deps','--force-recreate','--pull','never','postgres'],envfile=changed)
        for attempt in range(30):
            accepting=dexec('postgres',['pg_isready','-U','neshane_dev_admin','-d','neshane_dev'])
            if accepting['code']==0:break
            time.sleep(1)
        new_auth=dexec('postgres',app,'SELECT 1;\n')
        old_auth=dexec('postgres',['sh','-c','read -r pw; export PGPASSWORD="$pw"; exec psql -X -qAt -h 127.0.0.1 -U neshane_dev_app -d neshane_dev --no-password -c "SELECT v FROM public.v3li002_probe WHERE k=\'task\'"'],VALUES['POSTGRES_APP_PASSWORD']+'\n')
        lg=docker(['logs','--tail','80',task_id('postgres')])
        check('LIR002-PG-EXISTING-VOLUME','postgres','Existing volume skips init: changed env does not rotate stored app password',recreate['code']==0 and new_auth['code']!=0 and old_auth['code']==0 and value in old_auth['stdout'] and 'Skipping initialization' in (lg['stdout']+lg['stderr']),{'changedPasswordRejected':new_auth['code']!=0,'originalPasswordAndRowRetained':old_auth['code']==0 and value in old_auth['stdout'],'originalPasswordProbe':old_auth,'inputTransport':'exact binary stdin; prior text-input observation remains preserved','logs':lg},'Expected configured readiness failure during changed-password experiment, not a production rotation implementation.')
    finally:
        restore=compose(['up','-d','--no-deps','--force-recreate','--pull','never','postgres'])
        ready,health=wait_ready('postgres',100)
        check('LIR002-PG-RESTORE-TASK-CONFIG','postgres','Task-only original synthetic config restored',restore['code']==0 and ready,health)

def redis():
    ping=dexec('redis',['redis-cli','-h','redis','PING'])
    config=dexec('redis',['redis-cli','--raw','CONFIG','GET','appendonly','maxmemory','maxmemory-policy'])
    check('LIR002-REDIS-CONNECT','redis','Internal service DNS/PING; expected AOF, 256MiB and noeviction',ping['stdout'].strip()=='PONG' and config['code']==0 and '268435456' in config['stdout'] and 'noeviction' in config['stdout'] and 'yes' in config['stdout'],{'ping':ping,'config':config},'Unauthenticated dev network only; no cache/session/tenant policy.')
    key='v3li002:'+S['project'];value='synthetic-aof'
    put=dexec('redis',['redis-cli','SET',key,value])
    sync=dexec('redis',['redis-cli','WAITAOF','1','0','3000'])
    restart=compose(['restart','redis']);ready,health=wait_ready('redis',90)
    get=dexec('redis',['redis-cli','--raw','GET',key])
    check('LIR002-REDIS-PERSIST','redis','Synthetic write is AOF-synchronized and survives process restart',put['code']==0 and sync['code']==0 and sync['stdout'].strip().splitlines()[0]=='1' and restart['code']==0 and ready and get['stdout'].strip()==value,{'set':put,'waitAof':sync,'health':health,'get':get},'Process restart only, not host power-loss or backup durability.')
    noports=not any(task_containers()['redis']['ports'].values()) if task_containers()['redis']['ports'] else True
    check('LIR002-REDIS-UNPUBLISHED','redis','No host-published Redis port',noports,{'portBindings':task_containers()['redis']['ports']})

def amqp_login(password):
    def short(b):return bytes([len(b)])+b
    def long(b):return struct.pack('>I',len(b))+b
    def frame(sock,payload):sock.sendall(struct.pack('>BHI',1,0,len(payload))+payload+b'\xce')
    def readn(sock,n):
        data=b''
        while len(data)<n:
            chunk=sock.recv(n-len(data))
            if not chunk:raise EOFError('AMQP peer closed during '+stage)
            data+=chunk
        return data
    def receive(sock):
        typ,ch,size=struct.unpack('>BHI',readn(sock,7));payload=readn(sock,size);need(readn(sock,1)==b'\xce','Invalid AMQP frame');return payload
    stage='connect'
    with socket.create_connection(('127.0.0.1',int(VALUES['RABBITMQ_AMQP_PORT'])),timeout=8) as sock:
        sock.settimeout(8);sock.sendall(b'AMQP\x00\x00\x09\x01');payload=receive(sock)
        need(payload[:4]==struct.pack('>HH',10,10),'No AMQP connection.start')
        inner=short(b'authentication_failure_close')+b't\x01'
        props=short(b'capabilities')+b'F'+long(inner)
        response=b'\x00'+VALUES['RABBITMQ_USER'].encode()+b'\x00'+password.encode()
        stage='authentication';frame(sock,struct.pack('>HH',10,11)+long(props)+short(b'PLAIN')+long(response)+short(b'en_US'))
        payload=receive(sock)
        if payload[:4]==struct.pack('>HH',10,50):
            return {'authenticated':False,'replyCode':struct.unpack('>H',payload[4:6])[0],'stage':stage}
        need(payload[:4]==struct.pack('>HH',10,30),'No AMQP tune')
        frame(sock,struct.pack('>HHHIH',10,31,0,131072,0))
        frame(sock,struct.pack('>HH',10,40)+short(b'neshane_dev')+b'\x00\x00')
        payload=receive(sock);opened=payload[:4]==struct.pack('>HH',10,41)
        if opened:frame(sock,struct.pack('>HHH',10,50,200)+b'\x00'+struct.pack('>HH',0,0))
        return {'authenticated':opened,'vhost':'neshane_dev','stage':'open'}

def rabbitmq():
    auth=(VALUES['RABBITMQ_USER'],VALUES['RABBITMQ_PASSWORD']);port=int(VALUES['RABBITMQ_UI_PORT'])
    status,body=http(port,'/api/overview',basic=auth)
    bad,_=http(port,'/api/overview',basic=(auth[0],'invalid-synthetic-password'))
    users=dexec('rabbitmq',['rabbitmqctl','list_users','--formatter=json'])
    permissions=dexec('rabbitmq',['rabbitmqctl','list_permissions','-p','neshane_dev','--formatter=json'])
    user_permissions=dexec('rabbitmq',['rabbitmqctl','list_user_permissions',auth[0],'--formatter=json'])
    try:
        permission_rows=json.loads(user_permissions['stdout'])
        scope_ok=len(permission_rows)==1 and permission_rows[0].get('vhost')=='neshane_dev' and all(permission_rows[0].get(k)=='.*' for k in ['configure','write','read'])
    except (ValueError,TypeError,KeyError):scope_ok=False
    check('LIR002-RABBIT-AUTH','rabbitmq','Valid management login works; invalid password rejected',status==200 and bad in [401,403],{'validHttpStatus':status,'invalidHttpStatus':bad})
    check('LIR002-RABBIT-PERMISSIONS','rabbitmq','Development user has management not administrator tag, dev vhost permissions only',users['code']==0 and 'management' in users['stdout'] and 'administrator' not in users['stdout'] and permissions['code']==0 and VALUES['RABBITMQ_USER'] in permissions['stdout'] and user_permissions['code']==0 and scope_ok,{'users':users,'developmentVhostPermissions':permissions,'allTaskUserPermissions':user_permissions},'No product messaging identity/topology is accepted.')
    if S.get('internalHttpMode'):
        probe=native_amqp_probe()
        check('LIR002-RABBIT-AMQP','rabbitmq','Native internal AMQP handshake accepts valid credentials/vhost and rejects invalid password',probe['code']==0 and 'AMQP_VALID_AND_INVALID_PASS' in probe['stdout'],probe,'Internal listener test; published host endpoint failure remains separately recorded.')
    else:
        valid=amqp_login(auth[1])
        try:invalid=amqp_login('invalid-synthetic-password')
        except EOFError as e:invalid={'authenticated':False,'peerClosedDuringAuthentication':'during authentication' in str(e),'observation':str(e)}
        rejected=not invalid['authenticated'] and (invalid.get('replyCode') in [403,530] or invalid.get('peerClosedDuringAuthentication',False))
        check('LIR002-RABBIT-AMQP','rabbitmq','AMQP valid login/vhost succeeds and bad password fails',valid['authenticated'] and rejected,{'valid':valid,'invalid':invalid})
    queue='v3li002-'+S['project'];path='/api/queues/neshane_dev/'+queue
    created,_=http(port,path,'PUT',{'durable':True,'auto_delete':False,'arguments':{}},auth)
    message='synthetic-message-'+S['project']
    published,payload=http(port,'/api/exchanges/neshane_dev/amq.default/publish','POST',{'properties':{'delivery_mode':2},'routing_key':queue,'payload':message,'payload_encoding':'string'},auth)
    routed=json.loads(payload).get('routed') if published==200 else False
    restart=compose(['restart','rabbitmq']);ready,health=wait_ready('rabbitmq',150)
    deadline=time.monotonic()+45
    consumed,contents=0,b''
    while time.monotonic()<deadline:
        try:
            consumed,contents=http(port,path+'/get','POST',{'count':1,'ackmode':'ack_requeue_false','encoding':'auto','truncate':5000},auth)
            if consumed==200:break
        except (OSError,urllib.error.URLError):pass
        time.sleep(2)
    records=json.loads(contents) if consumed==200 else []
    check('LIR002-RABBIT-PERSIST-MESSAGE','rabbitmq','Durable synthetic queue/persistent message survives restart and is consumed',created in [201,204] and routed and restart['code']==0 and ready and len(records)==1 and records[0].get('payload')==message,{'queueCreateStatus':created,'publishStatus':published,'routed':routed,'health':health,'consumeStatus':consumed,'payloadMatches':len(records)==1 and records[0].get('payload')==message},'Task-only disposable queue fixture, not product topology or delivery guarantees.')

def internal_get(service,path):
    return dexec('prometheus',['wget','-q','-O','-','--header=Accept: application/json','http://'+service+path],timeout=12)

def observability():
    blocked_collector='otel-collector' in S.get('blockedServices',[])
    col={'code':None,'reason':'Not started after native config rejection'} if blocked_collector else internal_get('otel-collector:13133','/')
    tempo=internal_get('tempo:3200','/ready')
    check('LIR002-COLLECTOR-HEALTH','otel-collector','Actual internal health extension responds successfully',col['code']==0,col,'Health extension is not proof of downstream ingestion.',blocked=blocked_collector)
    check('LIR002-TEMPO-HEALTH','tempo','Actual internal Tempo /ready succeeds',tempo['code']==0,tempo)
    pstatus,pbody=http(int(VALUES['PROMETHEUS_PORT']),'/api/v1/status/flags')
    flags=json.loads(pbody).get('data',{}) if pstatus==200 else {}
    check('LIR002-PROMETHEUS-RETENTION','prometheus','Native running configuration has 1d and 256MB retention',pstatus==200 and flags.get('storage.tsdb.retention.time') in ['1d','24h','24h0m0s'] and flags.get('storage.tsdb.retention.size') in ['256MB','256MiB'],{'httpStatus':pstatus,'retentionTime':flags.get('storage.tsdb.retention.time'),'retentionSize':flags.get('storage.tsdb.retention.size')},'Configured caps observed; 24-hour expiry is not time-travel tested.')
    gauth=(VALUES['GRAFANA_ADMIN_USER'],VALUES['GRAFANA_ADMIN_PASSWORD']);gport=int(VALUES['GRAFANA_PORT'])
    health,hbody=http(gport,'/api/health')
    check('LIR002-GRAFANA-NATIVE-HEALTH','grafana','Native server loads config and database; /api/health succeeds',health==200 and json.loads(hbody).get('database')=='ok',{'httpStatus':health,'health':json.loads(hbody)},'Startup, provisioning and APIs verify native loading; no invented validation-only CLI flag.')
    for uid in ['neshane-prometheus','neshane-tempo']:
        code,body=http(gport,'/api/datasources/uid/'+uid+'/health',basic=gauth)
        obj=json.loads(body) if body else {}
        check('LIR002-GRAFANA-'+uid.upper(),'grafana','Provisioned datasource backend connectivity is healthy',code==200 and obj.get('status')=='OK',{'httpStatus':code,'response':obj})
    if blocked_collector:
        return  # Explicit downstream BLOCKED records are completed by report().
    stamp=time.time_ns();marker='v3li002-private-sentinel-'+S['project']
    trace_id=secrets.token_hex(16);span_id=secrets.token_hex(8)
    attrs=[{'key':'neshane.synthetic','value':{'boolValue':True}},{'key':'private.synthetic','value':{'stringValue':marker}}]
    metric={'resourceMetrics':[{'resource':{'attributes':attrs},'scopeMetrics':[{'scope':{'name':marker,'attributes':[{'key':'private','value':{'stringValue':marker}}]},'metrics':[{'name':'neshane.synthetic.probe','description':marker,'sum':{'aggregationTemporality':2,'isMonotonic':True,'dataPoints':[{'asInt':'7','startTimeUnixNano':str(stamp-1000000000),'timeUnixNano':str(stamp),'attributes':[{'key':'private','value':{'stringValue':marker}}]}]}}]}]}]}
    mcode,mresponse=http(int(VALUES['OTLP_HTTP_PORT']),'/v1/metrics','POST',metric)
    span={'traceId':trace_id,'spanId':span_id,'name':marker,'kind':1,'startTimeUnixNano':str(stamp),'endTimeUnixNano':str(stamp+1000000),'attributes':[{'key':'private','value':{'stringValue':marker}}],'status':{'code':2,'message':marker},'events':[{'timeUnixNano':str(stamp),'name':marker}]}
    trace={'resourceSpans':[{'resource':{'attributes':attrs},'scopeSpans':[{'scope':{'name':marker},'spans':[span]}]}]}
    tcode,tresponse=http(int(VALUES['OTLP_HTTP_PORT']),'/v1/traces','POST',trace)
    check('LIR002-OTLP-ACCEPT','otel-collector','Synthetic metric and trace OTLP/HTTP accepted',mcode==200 and tcode==200,{'metricHttpStatus':mcode,'metricResponse':mresponse.decode(),'traceHttpStatus':tcode,'traceResponse':tresponse.decode()})
    query=urllib.parse.quote('{__name__=~"neshane_synthetic_probe.*"}',safe='')
    metrics={};metric_ok=False
    for attempt in range(16):
        code,body=http(int(VALUES['PROMETHEUS_PORT']),'/api/v1/query?query='+query)
        metrics=json.loads(body)
        result=metrics.get('data',{}).get('result',[])
        if result:metric_ok=any(float(r['value'][1])==7 for r in result);break
        time.sleep(2)
    check('LIR002-PROMETHEUS-INGEST','prometheus','OTLP synthetic metric scraped with value 7 and minimized labels',metric_ok and marker not in json.dumps(metrics),metrics,'Only bounded synthetic samples; no complete application health claim.')
    retrieved=None
    for attempt in range(20):
        r=internal_get('tempo:3200','/api/traces/'+trace_id)
        if r['code']==0:
            try:retrieved=json.loads(r['stdout']);break
            except json.JSONDecodeError:pass
        time.sleep(2)
    trace_text=json.dumps(retrieved)
    check('LIR002-TEMPO-RETRIEVE','tempo','Trace is retrievable; constant span/service and removed sensitive sentinels/events',retrieved is not None and 'synthetic-span' in trace_text and marker not in trace_text,{'traceID':trace_id,'response':retrieved},'No claim that all possible links/exemplars/IDs or malicious payloads are DLP-sanitized.')
    # Negative signals use distinct IDs/names; retain HTTP acceptance vs export distinction.
    rejected_trace=secrets.token_hex(16)
    negative=json.loads(json.dumps(trace));negative['resourceSpans'][0]['resource']['attributes']=[];negative['resourceSpans'][0]['scopeSpans'][0]['spans'][0]['traceId']=rejected_trace
    ncode,_=http(int(VALUES['OTLP_HTTP_PORT']),'/v1/traces','POST',negative)
    neg_metric=json.loads(json.dumps(metric));neg_metric['resourceMetrics'][0]['scopeMetrics'][0]['metrics'][0]['name']='v3li002.rejected'
    nmetric,_=http(int(VALUES['OTLP_HTTP_PORT']),'/v1/metrics','POST',neg_metric)
    time.sleep(4)
    absent=internal_get('tempo:3200','/api/traces/'+rejected_trace)
    q=urllib.parse.quote('{__name__=~"v3li002_rejected.*"}',safe='')
    code,body=http(int(VALUES['PROMETHEUS_PORT']),'/api/v1/query?query='+q)
    no_metric=json.loads(body).get('data',{}).get('result',[])==[]
    check('LIR002-TELEMETRY-NEGATIVES','otel-collector','Unmarked trace and disallowed metric are not exported',ncode==200 and nmetric==200 and absent['code']!=0 and no_metric,{'negativeTraceAcceptedForFiltering':ncode,'negativeMetricAcceptedForFiltering':nmetric,'traceReadExit':absent['code'],'disallowedMetricAbsent':no_metric},'Bounded observation, not universal non-export proof. Logs pipeline remains absent.')
    log_code,_=http(int(VALUES['OTLP_HTTP_PORT']),'/v1/logs','POST',{'resourceLogs':[{'resource':{'attributes':attrs},'scopeLogs':[{'logRecords':[{'timeUnixNano':str(stamp),'body':{'stringValue':marker}}]}]}]})
    check('LIR002-TELEMETRY-LOGS-DISABLED','otel-collector','No native OTLP logs pipeline accepts payloads',log_code in [404,405,501],{'otlpLogsHttpStatus':log_code},'No real sensitive content sent. A bounded sentinel/disabled-pipeline check is not complete DLP.')
def observability_auxiliary():
    cfg=internal_get('tempo:3200','/status/config')
    check('LIR002-TEMPO-RETENTION','tempo','Native running Tempo reports development 24h block retention',cfg['code']==0 and bool(re.search(r'block_retention:\s*(24h|1d)',cfg['stdout'])),{'exitCode':cfg['code'],'retentionLines':[l.strip() for l in cfg['stdout'].splitlines() if 'block_retention:' in l]},'Configured retention, not wall-clock expiry/durability proof.')
    # Verify attempted cross-network access using an available task-owned image tool.
    redis_ip=next(iter(task_containers()['redis']['networks'].values()))['IPAddress']
    probe=dexec('prometheus',['sh','-c','command -v nc >/dev/null && nc -w 3 '+redis_ip+' 6379 </dev/null'],timeout=8)
    available=dexec('prometheus',['sh','-c','command -v nc'],timeout=8)
    check('LIR002-NETWORK-DENY','boundary','Telemetry peer cannot establish TCP to the isolated Redis network',probe['code']!=0 and available['code']==0,{'probe':probe,'toolAvailable':available['code']==0},'Single task-owned cross-network connection attempt; metadata checks cover every service.',blocked=available['code']!=0)

def mailpit():
    subject='V3-LOCAL-INFRA-002 '+S['project'];text='Synthetic task-only message. No external recipient.'
    message='From: synthetic@example.invalid\r\nTo: nobody@example.invalid\r\nSubject: '+subject+'\r\n\r\n'+text+'\r\n'
    if S.get('internalHttpMode'):
        fixture=EXTERNAL/'fixtures/smtp.eml';fixture.parent.mkdir(exist_ok=True)
        fixture.write_bytes(message.encode())
        r=curl_run('mail','smtp://mailpit:1025',extra={'mail-from':'synthetic@example.invalid','mail-rcpt':'nobody@example.invalid','upload-file':'/fixture'},fixture=fixture)
        refusals={} if r['code']==0 else {'transport':'failed'}
    else:
        with smtplib.SMTP('127.0.0.1',int(VALUES['MAILPIT_SMTP_PORT']),timeout=10) as smtp:
            refusals=smtp.sendmail('synthetic@example.invalid',['nobody@example.invalid'],message)
    code,body=http(int(VALUES['MAILPIT_UI_PORT']),'/api/v1/messages')
    data=json.loads(body);messages=data.get('messages',[])
    check('LIR002-MAILPIT-DELIVERY','mailpit','Synthetic SMTP is captured and visible in task Mailpit',not refusals and code==200 and any(m.get('Subject')==subject for m in messages),{'smtpAccepted':not refusals,'httpStatus':code,'matchingMessages':sum(m.get('Subject')==subject for m in messages)},'No relay is configured; internal network and localhost binds checked. No external email delivery was requested.')

def s3(method,path,data=b'',bad=False,anonymous=False):
    if S.get('internalHttpMode'):
        credentials=None if anonymous else (VALUES['SEAWEEDFS_ACCESS_KEY'],'invalid-synthetic-secret' if bad else VALUES['SEAWEEDFS_SECRET_KEY'])
        return curl_request('experimental','http://seaweedfs:8333'+path,method,data if method in ['PUT','POST'] else None,credentials,{},aws=not anonymous)
    port=int(VALUES['SEAWEEDFS_S3_PORT']);host='127.0.0.1:'+str(port)
    timestamp=dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%SZ');day=timestamp[:8]
    content_hash=hashlib.sha256(data).hexdigest();headers={'Host':host,'x-amz-date':timestamp,'x-amz-content-sha256':content_hash}
    canonical_headers='host:'+host+'\nx-amz-content-sha256:'+content_hash+'\nx-amz-date:'+timestamp+'\n'
    signed='host;x-amz-content-sha256;x-amz-date';scope=day+'/us-east-1/s3/aws4_request'
    canonical=method+'\n'+path+'\n\n'+canonical_headers+'\n'+signed+'\n'+content_hash
    to_sign='AWS4-HMAC-SHA256\n'+timestamp+'\n'+scope+'\n'+hashlib.sha256(canonical.encode()).hexdigest()
    key=('AWS4'+('invalid-synthetic-secret' if bad else VALUES['SEAWEEDFS_SECRET_KEY'])).encode()
    for part in [day,'us-east-1','s3','aws4_request']:key=hmac.new(key,part.encode(),hashlib.sha256).digest()
    signature=hmac.new(key,to_sign.encode(),hashlib.sha256).hexdigest()
    if not anonymous:headers['Authorization']='AWS4-HMAC-SHA256 Credential='+VALUES['SEAWEEDFS_ACCESS_KEY']+'/'+scope+', SignedHeaders='+signed+', Signature='+signature
    return http(port,path,method,data=data if method in ['PUT','POST'] else None,headers=headers)

def seaweedfs():
    health=dexec('seaweedfs',['wget','-q','-O','-','http://127.0.0.1:12535/health'],timeout=12)
    check('LIR002-SEAWEED-HEALTH','seaweedfs','Source-confirmed internal admin health responds',health['code']==0,health,'Experimental mini only; this is not S3 authorization evidence.')
    key='/neshane-dev/'+S['project']+'.txt';payload=('Synthetic object '+S['project']+'\n').encode()
    code,body=s3('PUT',key,payload)
    gcode,got=s3('GET',key)
    expected=hashlib.sha256(payload).hexdigest();actual=hashlib.sha256(got).hexdigest()
    check('LIR002-SEAWEED-OBJECT','seaweedfs','Signed S3 PUT/GET succeeds with identical SHA-256',code in [200,201] and gcode==200 and actual==expected,{'putStatus':code,'getStatus':gcode,'expectedSha256':expected,'actualSha256':actual,'putResponse':body.decode(errors='replace')},'EXPERIMENTAL / DEV-ONLY; OD-017 is not resolved.')
    bad,bbody=s3('GET',key,bad=True);anon,abody=s3('GET',key,anonymous=True)
    check('LIR002-SEAWEED-AUTH','seaweedfs','Wrong signing secret and missing credentials are rejected',bad in [401,403] and anon in [401,403],{'invalidSignatureStatus':bad,'anonymousStatus':anon,'invalidResponse':bbody.decode(errors='replace'),'anonymousResponse':abody.decode(errors='replace')})
    restart=compose(['restart','seaweedfs'])
    after_code,after=0,b''
    for attempt in range(30):
        try:
            after_code,after=s3('GET',key)
            if after_code==200:break
        except (OSError,urllib.error.URLError,RuntimeError):pass
        time.sleep(1)
    check('LIR002-SEAWEED-PERSIST','seaweedfs','Synthetic object and credential configuration survive restart',restart['code']==0 and after_code==200 and hashlib.sha256(after).hexdigest()==expected,{'getStatus':after_code,'expectedSha256':expected,'afterRestartSha256':hashlib.sha256(after).hexdigest()},'Process restart only; no product storage, HA or power-loss guarantee.')

def services():
    for name,fn in [('postgres',postgres),('redis',redis),('rabbitmq',rabbitmq),('observability',observability),('observability-independent',observability_auxiliary),('mailpit',mailpit),('seaweedfs',seaweedfs)]:
        try:fn()
        except Exception as e:
            check('LIR002-SERVICE-BLOCKED-'+name,name,'Complete all bounded service checks',False,{'exception':scrub(e)},'Subsequent checks in this service group were not completed.',blocked=True)
    logs()

def curl_run(network,url,extra=None,fixture=None):
    """Short-lived approved Grafana-image client; no network/port weakening."""
    ref=next(i['reference'] for i in S['imageReferences'] if i['service']=='grafana')
    name=S['project']+'-probe-'+secrets.token_hex(4)
    opts={'url':url,'silent':None,'show-error':None,'connect-timeout':'3','max-time':'12',
          'proxy':'','max-redirs':'0','write-out':'\nLIR002_HTTP_STATUS:%{http_code}\n'}
    opts.update(extra or {})
    lines=[]
    for key,value in opts.items():
        if value is None:
            lines.append(key)
            continue
        values=value if isinstance(value,list) else [value]
        for v in values:
            v=str(v).replace('\\','\\\\').replace('"','\\"').replace('\n','\\n').replace('\r','\\r')
            lines.append(key+' = "'+v+'"')
    cmd=['create','--interactive','--name',name,'--label','com.docker.compose.project='+S['project'],
         '--label','neshane.task=V3-LOCAL-INFRA-002','--network',S['project']+'_'+network,
         '--read-only','--cap-drop','ALL','--security-opt','no-new-privileges:true',
         '--memory','128m','--cpus','0.25','--pids-limit','64','--log-driver','json-file',
         '--log-opt','max-size=5m','--log-opt','max-file=2','--tmpfs','/tmp:rw,nosuid,noexec,size=8m']
    if fixture:cmd+=['--mount','type=bind,src='+str(fixture)+',dst=/fixture,readonly']
    declared=json.loads(dtext(['image','inspect','--format','{{json .Config.Volumes}}',ref])) or {}
    for path in declared:cmd+=['--tmpfs',path+':rw,nosuid,noexec,size=8m']
    cmd+=['--entrypoint','/usr/bin/curl',ref,'--disable','--config','-']
    cid=dtext(cmd);S.setdefault('probeContainers',[]).append(cid);save_state()
    c=inspect_one('container',cid,CONTAINER_FORMAT)
    need(c['project']==S['project'] and cid not in S['beforeContainerIDs'],'Probe ownership mismatch')
    try:return docker(['start','--attach','--interactive',cid],stdin='\n'.join(lines)+'\n',timeout=25)
    finally:
        latest=inspect_one('container',cid,CONTAINER_FORMAT)
        if latest['running']:docker(['stop','--time','5',cid],timeout=20)
        removed=docker(['rm',cid]);need(removed['code']==0,'Task probe removal failed')
        S.setdefault('removedProbeContainers',[]).append(cid);save_state()

def curl_request(network,url,method='GET',data=None,basic=None,headers=None,aws=False):
    opts={'request':method};fixture=None
    if basic:opts['user']=basic[0]+':'+basic[1]
    if aws:opts['aws-sigv4']='aws:amz:us-east-1:s3'
    if headers:opts['header']=[k+': '+v for k,v in headers.items()]
    if data is not None:
        fixture=EXTERNAL/'fixtures/http-body.bin';fixture.parent.mkdir(exist_ok=True);fixture.write_bytes(data)
        opts['data-binary']='@/fixture'
    r=curl_run(network,url,opts,fixture)
    if r['code']!=0:raise RuntimeError('Internal approved-image HTTP client failed: '+scrub(r['stderr']))
    body,marker=r['stdout'].rsplit('\nLIR002_HTTP_STATUS:',1)
    return int(marker.strip()),body.encode()

def diagnose():
    tools=dexec('grafana',['sh','-c','command -v curl; command -v nc; command -v openssl'])
    write('observations/task-probe-tools.json',tools)
    need('/usr/bin/curl' in tools['stdout'],'Approved image does not provide the required HTTP client')
    # Record every published host path, not just generic downstream exceptions.
    ports={'postgres':['POSTGRES_PORT'],'rabbitmq':['RABBITMQ_AMQP_PORT','RABBITMQ_UI_PORT'],
           'mailpit':['MAILPIT_SMTP_PORT','MAILPIT_UI_PORT'],'prometheus':['PROMETHEUS_PORT'],
           'grafana':['GRAFANA_PORT'],'seaweedfs':['SEAWEEDFS_S3_PORT']}
    for service,keys in ports.items():
        for key in keys:
            try:
                with socket.create_connection(('127.0.0.1',int(VALUES[key])),timeout=3):ok=True
                error=None
            except OSError as e:ok=False;error=str(e)
            actual_ports=json.loads(dtext(['container','inspect','--format','{{json .NetworkSettings.Ports}}',task_id(service)]))
            check('LIR002-HOST-'+key,service,'Declared localhost development endpoint is reachable from this Windows host',ok,
                  {'port':int(VALUES[key]),'reachable':ok,'error':error,'actualDockerPorts':actual_ports},
                  'Internal-only Docker networks may suppress publishing on this engine; no network/bind is loosened to hide failure.')

def internal_services():
    S['internalHttpMode']=True
    save_state()
    for name,fn in [('rabbitmq',rabbitmq),('observability',observability),('mailpit',mailpit),('seaweedfs',seaweedfs)]:
        try:fn()
        except Exception as e:
            check('LIR002-INTERNAL-BLOCKED-'+name,name,'Complete independent checks over unchanged task networks',False,
                  {'exception':scrub(e)},'Host reachability failures and initial BLOCKED observations remain preserved.',blocked=True)
    logs()

def native_amqp_probe():
    path='/tmp/v3li002-amqp.escript'
    placed=dexec('rabbitmq',['sh','-c','test ! -e '+path+' && umask 077 && cat > '+path],(HERE/'amqp-probe.escript').read_text())
    need(placed['code']==0,'Cannot place unique task-local seekable AMQP probe')
    try:
        # escript seeks its header: /dev/stdin is not supported by this OTP image.
        return dexec('rabbitmq',['env','ERL_FLAGS=+S 1:1 +A 2','escript',path],timeout=30)
    finally:
        removed=dexec('rabbitmq',['rm','--',path])
        need(removed['code']==0,'Task-local AMQP probe file cleanup failed')

def amqp_only():
    r=native_amqp_probe()
    check('LIR002-RABBIT-AMQP-CORRECTED-PROBE','rabbitmq','Seekable native AMQP probe accepts valid credentials/vhost and rejects invalid password',r['code']==0 and 'AMQP_VALID_AND_INVALID_PASS' in r['stdout'],r,
          'Initial escript /dev/stdin espipe FAIL is retained as a harness failure; host path remains FAIL.')

def cleanup():
    # Explicit IDs/names only, each cross-checked against original inventory and
    # project ownership. Never prune, compose down -v, or touch pre-existing IDs.
    before=S['before'];deleted={'containers':[],'networks':[],'volumes':[]};errors=[]
    current=inventory()
    for c in current['containers']:
        if c['project']!=S['project']:continue
        try:
            need(c['id'] not in S['beforeContainerIDs'],'Never remove original container')
            if c['running']:
                r=docker(['stop','--time','20',c['id']],timeout=60);need(r['code']==0,r['stderr'])
            r=docker(['rm',c['id']]);need(r['code']==0,r['stderr']);deleted['containers'].append(c['id'])
        except Exception as e:errors.append(scrub(e))
    for n in current['networks']:
        if n['project']!=S['project']:continue
        try:
            need(n['id'] not in {i['id'] for i in before['networks']} and n['name'].startswith(S['project']+'_'),'Network ownership mismatch')
            latest=inspect_one('network',n['id'],NETWORK_FORMAT);need(not latest['containers'],'Task network still has attached peers')
            r=docker(['network','rm',n['id']]);need(r['code']==0,r['stderr']);deleted['networks'].append(n['id'])
        except Exception as e:errors.append(scrub(e))
    for v in current['volumes']:
        if v['project']!=S['project']:continue
        try:
            need(v['name'] not in {i['name'] for i in before['volumes']} and v['name'].startswith(S['project']+'_'),'Volume ownership mismatch')
            r=docker(['volume','rm',v['name']]);need(r['code']==0,r['stderr']);deleted['volumes'].append(v['name'])
        except Exception as e:errors.append(scrub(e))
    after=inventory();write('docker-after.json',after)
    preservation=[]
    for kind,key in [('containers','id'),('networks','id'),('volumes','name')]:
        lookup={i[key]:i for i in after[kind]}
        for original in before[kind]:
            actual=lookup.get(original[key]);ok=actual==original
            preservation.append({'kind':kind,'identity':original[key],'preserved':ok,
                                 'difference':None if ok else {'before':original,'after':actual}})
    images={i['id']:i for i in after['images']}
    for original in before['images']:
        actual=images.get(original['id']);ok=actual is not None
        if ok:ok=set(original['repoTags'] or []).issubset(actual['repoTags'] or []) and set(original['repoDigests'] or []).issubset(actual['repoDigests'] or [])
        preservation.append({'kind':'images','identity':original['id'],'preserved':ok,
                             'limitation':'Authorized pulls may add references; prior IDs/tags/digests must remain.'})
    remaining={k:[i.get('id',i.get('name')) for i in after[k] if i.get('project')==S['project']] for k in ['containers','networks','volumes']}
    check('LIR002-CLEANUP','cleanup','All explicitly identified task containers/networks/disposable volumes removed',not errors and not any(remaining.values()),{'removed':deleted,'remaining':remaining,'errors':errors},'Downloaded allowed images are intentionally retained and reported separately.')
    check('LIR002-PRESERVATION-DOCKER','preservation','Original container instance/state/config, networks/volumes and image references preserved',all(r['preserved'] for r in preservation),{'items':preservation},'Live pre-existing volumes/counters may evolve naturally; no live data freeze or byte-level content preservation is claimed.')
    unexpected={}
    for kind,key in [('containers','id'),('networks','id'),('volumes','name')]:
        old={i[key] for i in before[kind]}
        unexpected[kind]=[i[key] for i in after[kind] if i[key] not in old and i.get('project')!=S['project']]
    if any(unexpected.values()):
        check('LIR002-UNATTRIBUTED-RESOURCES','preservation','No unexplained new resources are silently ignored or removed',False,
              unexpected,'Ownership is ambiguous; left untouched for explicit review.',blocked=True)
    write('cleanup-report.json',{'removed':deleted,'previouslyRemovedTaskProbeContainers':S.get('removedProbeContainers',[]),'remaining':remaining,'unexpectedNewResourcesNotRemoved':unexpected,'errors':errors,'privateInputsRemoved':False})
    write('resource-preservation-report.json',{'items':preservation,'liveDataLimitation':'Active existing workload contents/counters were not read, frozen or snapshotted.'})
    baseline_ok=all(digest(INFRA/n)==h for n,h in S['baselineHashes'].items())
    check('LIR002-PRESERVATION-17','preservation','All 17 baseline artifacts byte-identical',baseline_ok,{'files':len(S['baselineHashes']),'allEqual':baseline_ok})
    r=process(['pwsh.exe','-NoProfile','-File','C:/Users/user/AppData/Local/Temp/opencode/V3-LOCAL-INFRA-001/Preserve-Original.ps1','-Verify'])
    check('LIR002-PRESERVATION-REPOSITORIES','preservation','Original Root index/files, Root Main, Backend and Frontend unchanged',r['code']==0,r)
    # Audit only task-generated synthetic secrets; never inspect original .env.
    sensitive=[v for k,v in VALUES.items() if re.search(r'PASSWORD|SECRET|ACCESS_KEY|_USER$',k)]
    changed=PRIVATE/'changed-volume.env'
    if changed.exists():
        for line in changed.read_text(encoding='utf-8').splitlines():
            if '=' in line:
                k,v=line.split('=',1)
                if re.search(r'PASSWORD|SECRET|ACCESS_KEY|_USER$',k):sensitive.append(v)
    for u,p in [('RABBITMQ_USER','RABBITMQ_PASSWORD'),('GRAFANA_ADMIN_USER','GRAFANA_ADMIN_PASSWORD')]:
        sensitive.append(base64.b64encode((VALUES[u]+':'+VALUES[p]).encode()).decode())
    leaks=[]
    for f in HERE.rglob('*'):
        if f.is_file() and f.suffix in ['.json','.md','.py','.escript']:
            text=f.read_text(encoding='utf-8')
            if any(v and (v in text or urllib.parse.quote(v,safe='') in text) for v in sensitive):leaks.append(str(f.relative_to(HERE)))
    check('LIR002-EVIDENCE-CREDENTIAL-SCAN','evidence','No generated credential value or Basic token in review artifacts',not leaks,
          {'matchingFiles':leaks,'originalEnvRead':False,'generatedCredentialValuesPrinted':False},
          'Known generated values only; not a claim of exhaustive DLP or inspection of original secrets.')
    image_rows=json.loads((HERE/'image-identity-verification.json').read_text(encoding='utf-8'))
    write('downloaded-images-report.json',{'downloaded':[i for i in image_rows if i.get('pullRequired')],
          'reusedWithoutPull':[i for i in image_rows if not i.get('pullRequired')],
          'imageDeletionPerformed':False,'limitation':'An initial interrupted pull was resumed for the same pinned reference; pre-existing tags/IDs are preserved.'})
    # Delete only explicit task-generated secret files after all Docker work.
    if not any(remaining.values()):
        for p in [PRIVATE/'runtime.env',PRIVATE/'changed-volume.env',STATE]:
            if p.exists():p.unlink()
        result=json.loads((HERE/'cleanup-report.json').read_text())
        result['privateInputsRemoved']=True;write('cleanup-report.json',result)

def report():
    # Missing downstream observations are explicitly BLOCKED, never omitted/PASS.
    planned = {
      'postgres': ['PG-ROLES','PG-AUTH','PG-INVALID','PG-DENY-SUPERUSER','PG-DENY-ASSUME-ADMIN','PG-DENY-CREATE-ROLE','PG-DENY-CREATE-SCHEMA','PG-SYNTHETIC','PG-PERSIST','PG-EXISTING-VOLUME','PG-RESTORE-TASK-CONFIG'],
      'redis': ['REDIS-CONNECT','REDIS-PERSIST','REDIS-UNPUBLISHED'],
      'rabbitmq': ['RABBIT-AUTH','RABBIT-PERMISSIONS','RABBIT-AMQP','RABBIT-PERSIST-MESSAGE'],
      'otel-collector': ['NATIVE-COLLECTOR','COLLECTOR-HEALTH','OTLP-ACCEPT','TELEMETRY-NEGATIVES','TELEMETRY-LOGS-DISABLED'],
      'prometheus': ['NATIVE-PROMETHEUS','PROMETHEUS-RETENTION','PROMETHEUS-INGEST'],
      'tempo': ['NATIVE-TEMPO','TEMPO-HEALTH','TEMPO-RETRIEVE','TEMPO-RETENTION'],
      'grafana': ['GRAFANA-NATIVE-HEALTH','GRAFANA-NESHANE-PROMETHEUS','GRAFANA-NESHANE-TEMPO'],
      'mailpit': ['MAILPIT-DELIVERY'],
      'seaweedfs': ['SEAWEED-HEALTH','SEAWEED-OBJECT','SEAWEED-AUTH','SEAWEED-PERSIST'],
      'boundary': ['NETWORK-DENY'],
    }
    observed={c['checkIdentifier'] for c in CHECKS}
    for service in ['postgres','redis','rabbitmq','mailpit','otel-collector','prometheus','grafana','tempo','seaweedfs']:
        for category in ['READY','BOUNDARY']:
            cid='LIR002-'+category+'-'+service
            if cid not in observed:
                check(cid,service,'Observe the corresponding service readiness/security boundary',False,
                      'No service observation: native/start/acquisition prerequisite was not completed.',
                      'Not treated as PASS or not-applicable.',blocked=True)
    for service, suffixes in planned.items():
        for suffix in suffixes:
            cid='LIR002-'+suffix
            if cid not in observed:
                check(cid, service, 'Complete the corresponding bounded service check', False,
                      'Not completed because a prerequisite or earlier service-group step failed.',
                      'No result fabricated; see earlier service/native/start observations.', blocked=True)
    counts={s:sum(c['status']==s for c in CHECKS) for s in ['PASS','FAIL','BLOCKED']}
    rows=['# V3-LOCAL-INFRA-002 — runtime validation report','',
          'Observed checks only; no baseline fixes, product implementation or production readiness.',
          'G-RUNTIME: BLOCKED. FE-BE: PENDING. AUTH/IAM: PENDING. Offline: PROHIBITED.',
          'SeaweedFS: EXPERIMENTAL / DEV-ONLY. OD-013/014/015/017 remain OPEN; GS-01/GS-04 retained.','',
          '## Actual results','',json.dumps(counts),'',
          '| Check | Service | Expected | Status | Evidence | Remaining limitation |',
          '| --- | --- | --- | --- | --- | --- |']
    for c in CHECKS:
        cells=[c['checkIdentifier'],c['service'],c['expectedResult'],c['status'],c['evidenceReference'],c['remainingLimitation']]
        rows.append('| '+' | '.join(scrub(str(x)).replace('|','/').replace('\n',' ') for x in cells)+' |')
    rows += ['', '## Preservation and cleanup', '',
             'See docker-before.json, docker-after.json, resource-preservation-report.json and cleanup-report.json.',
             'Registry images retained; pullRequired/newImageID are in image-identity-verification.json.',
             'Original actual .env was never read/reused. Synthetic inputs were outside Git with restricted ACL.',
             'No staging, commit or push. Baseline native/runtime failures are retained, not silently repaired.', '',
             '## Limits', '',
             'Finite synthetic observations and process restarts do not prove hostile-host isolation, power-loss durability,',
             'long-horizon retention, complete DLP, production IAM, product RLS, real workload readiness or Runtime acceptance.']
    (HERE/'runtime-validation-report.md').write_text(scrub('\n'.join(rows)+'\n'),encoding='utf-8',newline='\n')
    write('service-validation-matrix.json',CHECKS)
    write('residual-findings.json',{'findings':[c for c in CHECKS if c['status']!='PASS'],'statusCounts':counts,
                                  'governance':{'G-RUNTIME':'BLOCKED','FE-BE':'PENDING','AUTH/IAM':'PENDING','offline':'PROHIBITED'},
                                  'automaticClosures':0})
    print(json.dumps(counts),flush=True)

if __name__=='__main__':
    action=sys.argv[1] if len(sys.argv)>1 else ''
    load_checks()
    try:
        if action=='preflight':preflight()
        elif action=='report':report()
        else:
            read_state()
            {'pull':pull,'native':native,'start':start,'services':services,'diagnose':diagnose,'internal':internal_services,
             'volume':postgres_existing_volume,'amqp':amqp_only,'seaweed':seaweedfs,'boundary':boundaries,'cleanup':cleanup}[action]()
    except Exception as exc:
        check('LIR002-RUNNER-'+(action or 'MISSING'),'runner','Task step completes within isolation boundaries',False,
              {'exception':scrub(exc)},'Action stopped; investigate without changing baseline or existing resources.',blocked=True)
        sys.exit(1)
