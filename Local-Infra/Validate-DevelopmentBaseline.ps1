[CmdletBinding()]
param()
$ErrorActionPreference='Stop'
Set-StrictMode -Version Latest
$Root=$PSScriptRoot
$Output=Join-Path $Root '.validation'
[void][IO.Directory]::CreateDirectory($Output)
$Docker=(Get-Command docker.exe -ErrorAction Stop).Source
function Need([bool]$Value,[string]$Reason){if(-not $Value){throw $Reason}}
function Json([string]$Path){Get-Content -LiteralPath $Path -Raw | ConvertFrom-Json -AsHashtable}
function WriteText([string]$Path,[string]$Text){[IO.File]::WriteAllText($Path,$Text,[Text.UTF8Encoding]::new($false))}

# Read only the tracked/example template, NEVER .env or .secrets contents.
$Values=[ordered]@{}
foreach($line in Get-Content -LiteralPath (Join-Path $Root '.env.example')){
 if($line -notmatch '^([A-Z][A-Z0-9_]*)=(.*)$'){continue}
 $key=$Matches[1];$value=$Matches[2]
 Need (-not $Values.Contains($key)) "Duplicate template key: $key"
 if($key -match 'PASSWORD|SECRET|ACCESS_KEY|_USER$'){
  Need ($value -like 'REPLACE_*') "Non-placeholder credential in template: $key"
  $value='SYNTHETIC_ONLY_'+$key
 }
 if($key -eq 'COMPOSE_PROJECT_NAME'){$value='neshane-v3li001-static'}
 $Values[$key]=$value
}
function EnvFile([string]$Name,[string[]]$Omit=@()){
 $path=Join-Path $Output $Name
 WriteText $path (($Values.Keys | Where-Object {$_ -notin $Omit} | ForEach-Object {$_+'='+$Values[$_]}) -join "`n")
 return $path
}
function Compose([string[]]$Files,[string]$EnvPath,[switch]$Quiet){
 $s=[Diagnostics.ProcessStartInfo]::new($Docker)
 $s.WorkingDirectory=$Root;$s.UseShellExecute=$false
 $s.RedirectStandardOutput=$true;$s.RedirectStandardError=$true
 # No inherited secret-bearing environment, Docker config, COMPOSE_FILE/profiles,
 # or shell-variable override. Keep only OS executable-discovery variables.
 $s.Environment.Clear()
 foreach($name in @('PATH','SystemRoot','WINDIR','TEMP','TMP','ProgramFiles','ProgramData','LOCALAPPDATA')){
  $v=[Environment]::GetEnvironmentVariable($name);if($null -ne $v){$s.Environment[$name]=$v}
 }
 $s.Environment['DOCKER_CONFIG']=Join-Path $Output 'empty-docker-config'
 [void][IO.Directory]::CreateDirectory($s.Environment['DOCKER_CONFIG'])
 $s.Environment['COMPOSE_DISABLE_ENV_FILE']='1'
 foreach($a in @('compose','--env-file',$EnvPath,'--project-directory',$Root)) {[void]$s.ArgumentList.Add($a)}
 foreach($file in $Files){[void]$s.ArgumentList.Add('--file');[void]$s.ArgumentList.Add($file)}
 foreach($a in @('config','--no-env-resolution')){[void]$s.ArgumentList.Add($a)}
 if($Quiet){[void]$s.ArgumentList.Add('--quiet')}else{[void]$s.ArgumentList.Add('--format');[void]$s.ArgumentList.Add('json')}
 $p=[Diagnostics.Process]::Start($s)
 $out=$p.StandardOutput.ReadToEndAsync();$err=$p.StandardError.ReadToEndAsync();$p.WaitForExit()
 $r=@{exitCode=$p.ExitCode;output=$out.GetAwaiter().GetResult();error=$err.GetAwaiter().GetResult()};$p.Dispose()
 # Never print/write expanded model; only synthetic secrets exist in this child.
 return $r
}
$Synthetic=EnvFile 'synthetic-input.env'
$Base=Join-Path $Root 'compose.yaml';$Experiment=Join-Path $Root 'compose.seaweedfs.yaml'
$allText=([IO.File]::ReadAllText($Base))+([IO.File]::ReadAllText($Experiment))
$used=@([regex]::Matches($allText,'(?<!\$)\$\{(?<key>[A-Z][A-Z0-9_]*)[^}]*\}') | ForEach-Object {$_.Groups['key'].Value} | Sort-Object -Unique)
foreach($key in $used){Need ($Values.Contains($key)) "Variable absent from template: $key"}
Need ($Values.Count -eq $used.Count) 'Unused/missing template variable'
$baseResult=Compose @($Base) $Synthetic
Need ($baseResult.exitCode -eq 0) 'Base Compose config failed (expanded output intentionally not printed)'
$combined=Compose @($Base,$Experiment) $Synthetic
Need ($combined.exitCode -eq 0) 'Experimental Compose config failed (expanded output intentionally not printed)'
$baseModel=$baseResult.output | ConvertFrom-Json -AsHashtable
$model=$combined.output | ConvertFrom-Json -AsHashtable
Need ($baseModel.services.Count -eq 8 -and -not $baseModel.services.ContainsKey('seaweedfs') -and $model.services.Count -eq 9) 'Experimental isolation/service inventory mismatch'

# Parse all YAML with Compose's strict YAML loader. An x-* wrapper deliberately
# validates YAML syntax, NOT native Collector/Tempo/application configuration.
$yamlFiles=@(Get-ChildItem -LiteralPath $Root -Recurse -File | Where-Object {$_.Extension -in @('.yml','.yaml') -and -not $_.FullName.StartsWith($Output+[IO.Path]::DirectorySeparatorChar)})
foreach($file in $yamlFiles){
 $wrapper=Join-Path $Output ('syntax-'+$file.Name+'.yaml')
 $body=([IO.File]::ReadAllText($file.FullName) -split "`n" | ForEach-Object {'  '+$_.TrimEnd("`r")}) -join "`n"
 WriteText $wrapper ("services:`n  yaml-static:`n    image: scratch`nx-parsed-document:`n"+$body+"`n")
 $syntax=Compose @($wrapper) $Synthetic -Quiet
 Need ($syntax.exitCode -eq 0) ('YAML syntax failed: '+$file.Name)
}
$requiredBase=@('COMPOSE_PROJECT_NAME','POSTGRES_PASSWORD','POSTGRES_APP_PASSWORD','RABBITMQ_USER','RABBITMQ_PASSWORD','GRAFANA_ADMIN_USER','GRAFANA_ADMIN_PASSWORD')
$requiredExperimental=@('SEAWEEDFS_ACCESS_KEY','SEAWEEDFS_SECRET_KEY','SEAWEEDFS_ADMIN_USER','SEAWEEDFS_ADMIN_PASSWORD')
$negativeChecks=0
foreach($key in $requiredBase){$r=Compose @($Base) (EnvFile ('missing-'+$key+'.env') @($key)) -Quiet;Need ($r.exitCode -ne 0) "Missing variable accepted: $key";$negativeChecks++}
foreach($key in $requiredExperimental){$r=Compose @($Base,$Experiment) (EnvFile ('missing-'+$key+'.env') @($key)) -Quiet;Need ($r.exitCode -ne 0) "Missing experimental variable accepted: $key";$negativeChecks++}
$baseWithoutExperiment=Compose @($Base) (EnvFile 'base-only.env' $requiredExperimental) -Quiet
Need ($baseWithoutExperiment.exitCode -eq 0) 'Base unexpectedly requires experimental credentials'

$lock=Json (Join-Path $Root 'image-references.json')
Need ($lock.images.Count -eq 9) 'Image lock inventory differs'
$expectedServices=@('postgres','redis','rabbitmq','mailpit','otel-collector','prometheus','grafana','tempo','seaweedfs')
Need (@(Compare-Object @($model.services.Keys | Sort-Object) @($expectedServices | Sort-Object)).Count -eq 0) 'Unexpected service'
$published=0;$mounts=0;$health=0
foreach($name in $model.services.Keys){
 $service=$model.services[$name];$image=$service.image
 $reference=@($lock.images | Where-Object service -eq $name)
 Need ($reference.Count -eq 1 -and $image -ceq $reference[0].reference -and $image -match '@sha256:[a-f0-9]{64}$' -and $image -notmatch ':latest(?:@|$)') "Unverified/floating image: $name"
 Need (-not $service.ContainsKey('container_name') -and -not $service.ContainsKey('privileged') -and -not $service.ContainsKey('network_mode') -and -not $service.ContainsKey('devices') -and -not $service.ContainsKey('cap_add') -and -not $service.ContainsKey('pid')) "Forbidden host/privilege setting: $name"
 Need ($service.restart -eq 'no' -and $service.mem_limit -gt 0 -and $service.cpus -gt 0 -and $service.pids_limit -gt 0 -and $service.security_opt -contains 'no-new-privileges:true') "Missing development guardrail: $name"
 if($service.ContainsKey('ports')){foreach($port in $service.ports){Need ($port.host_ip -eq '127.0.0.1' -and [int]$port.published -gt 0 -and [int]$port.published -lt 65536) "Non-loopback/invalid port: $name";$published++}}
 foreach($network in $service.networks.Keys){Need (-not $model.networks[$network].ContainsKey('external')) 'Network is not task-scoped'}
 if($service.ContainsKey('volumes')){foreach($v in $service.volumes){if($v.type -eq 'bind'){Need ($v.read_only -and $v.source.StartsWith($Root+[IO.Path]::DirectorySeparatorChar,[StringComparison]::OrdinalIgnoreCase) -and (Test-Path -LiteralPath $v.source -PathType Leaf) -and [IO.Path]::GetFileName($v.source) -ne '.env') 'Unsafe/missing bind mount';$mounts++}else{Need ($v.type -eq 'volume' -and $model.volumes.ContainsKey($v.source) -and -not $model.volumes[$v.source].ContainsKey('external')) 'External/unapproved volume'}}}
 if($service.ContainsKey('healthcheck')){$health++}
}
Need ($health -eq 6 -and $published -eq 10 -and $mounts -eq 6 -and $model.volumes.Count -eq 8) 'Port/health/mount/volume accounting differs'
Need (-not $model.services.redis.ContainsKey('ports') -and -not $model.services.tempo.ContainsKey('ports') -and $model.services.seaweedfs.ports.Count -eq 1) 'Unnecessary experimental/data port exposure'
# Host ingress requires a non-internal gateway; only networks without any published
# service may be internal. This encodes the corrected Docker Desktop networking model.
foreach($netName in $model.networks.Keys){
 $onNet=@($model.services.Keys | Where-Object {$model.services[$_].networks.ContainsKey($netName)})
 $publishedOnNet=@($onNet | Where-Object {$model.services[$_].ContainsKey('ports') -and $model.services[$_].ports.Count -gt 0})
 $isInternal=($model.networks[$netName].ContainsKey('internal') -and $model.networks[$netName].internal)
 if($publishedOnNet.Count -gt 0){Need (-not $isInternal) 'Published host ports require a non-internal network (Docker Desktop suppresses publication on internal networks)'}
 else{Need ($isInternal) 'Unpublished network should remain internal for egress isolation'}
}
Need ($model.services.grafana.depends_on.prometheus.condition -eq 'service_healthy' -and $model.services.'otel-collector'.depends_on.tempo.condition -eq 'service_started') 'Readiness dependency misrepresented'
$collector=[IO.File]::ReadAllText((Join-Path $Root 'observability/otel-collector.yaml'))
Need ($collector.Contains('filter/synthetic') -and $collector.Contains('error_mode: propagate') -and -not($collector -match '(?m)^\s+logs:|^\s+debug:') -and $collector.Contains('queue_size: 256')) 'Sensitive telemetry/bounds regression'
$pg=[IO.File]::ReadAllText((Join-Path $Root 'postgres/10-development-role.sh'))
Need ($pg.Contains('NOSUPERUSER NOCREATEDB NOCREATEROLE NOREPLICATION NOBYPASSRLS') -and $pg.Contains('\getenv app_password POSTGRES_APP_PASSWORD') -and $pg -notmatch '(?i)CREATE\s+(TABLE|SCHEMA)|ENABLE\s+ROW\s+LEVEL') 'Development DB identity/product-scope regression'
$readme=[IO.File]::ReadAllText((Join-Path $Root 'README.md'))
foreach($word in @('G-RUNTIME','BLOCKED','PENDING','OD-013','OD-014','OD-015','OD-017','GS-01','GS-04','PROHIBITED','runtime-validation-plan.md','POSTGRES_APP_PASSWORD','127.0.0.1','postgres_data','redis_data','rabbitmq_data','mailpit_data','prometheus_data','grafana_data','tempo_data','seaweedfs_data')){Need ($readme.Contains($word)) "Documentation boundary/inventory missing: $word"}

$files=@(Get-ChildItem -LiteralPath $Root -Recurse -File -Force | Where-Object {
 -not $_.FullName.StartsWith($Output+[IO.Path]::DirectorySeparatorChar) -and
 -not $_.FullName.Contains([IO.Path]::DirectorySeparatorChar+'.secrets'+[IO.Path]::DirectorySeparatorChar) -and
 -not $_.FullName.Contains([IO.Path]::DirectorySeparatorChar+'reviews'+[IO.Path]::DirectorySeparatorChar) -and
 ($_.Name -eq '.env.example' -or ($_.Name -ne '.env' -and $_.Name -notlike '.env.*'))
})
$hashes=[ordered]@{}
foreach($file in $files){
 $text=[Text.UTF8Encoding]::new($false,$true).GetString([IO.File]::ReadAllBytes($file.FullName))
 Need (-not $text.Contains([char]0) -and $text -notmatch '(?m)^-----BEGIN (?:[A-Z ]*PRIVATE KEY|CERTIFICATE)-----' -and $text -notmatch '(?i)AKIA[0-9A-Z]{16}|gh[pousr]_[a-zA-Z0-9]{30,}') 'Potential embedded credential/binary file'
 Need ($file.Name -notin @('seaweedfs-test.txt','seaweedfs-downloaded.txt') -and $file.Length -gt 0) 'Transferred temporary artifact/empty placeholder'
 $rel=[IO.Path]::GetRelativePath($Root,$file.FullName).Replace('\','/')
 # Absolute no-index paths do not reliably load directory attributes on Windows.
 # Check original LF bytes, without persistent Git config or staging changes.
 $whitespace=@(& git.exe --no-optional-locks -c core.autocrlf=false diff --no-index --check -- NUL $file.FullName 2>&1)
 Need ($LASTEXITCODE -in @(0,1) -and $whitespace.Count -eq 0) "Git whitespace check failed: $rel"
 $hashes[$rel]=@{bytes=$file.Length;sha256=(Get-FileHash -LiteralPath $file.FullName).Hash}
}
$staged=@(& git.exe --no-optional-locks -C (Split-Path $Root) diff --cached --name-only)
Need ($LASTEXITCODE -eq 0 -and $staged.Count -eq 0) 'Isolated workspace has staged files'
$result=@{task='V3-LOCAL-INFRA-001';recordedAt=[DateTimeOffset]::Now.ToString('o');outcome='PASS — STATIC CHECKS ONLY';yamlDocuments=$yamlFiles.Count;composeModels=2;requiredVariableNegativeChecks=$negativeChecks;templateVariables=$Values.Count;imageReferences=9;publishedLoopbackPorts=$published;dockerHealthchecks=$health;internalNetworks=$model.networks.Count;persistentVolumes=$model.volumes.Count;readOnlyScopedBindMounts=$mounts;actualEnvRead=$false;inheritedEnvironmentCleared=$true;expandedModelPrintedOrSaved=$false;imagePulls=0;containerStarts=0;applicationOrInfrastructureWorkloads=0;nativeConfigurationValidation='NOT EXECUTED';runtimeValidation='NOT EXECUTED — SEPARATE AUTHORIZATION REQUIRED';registryChecks='Recorded separately in image-references.json; this script is offline';secretScan='Non-secret task files only; actual .env/.secrets excluded; heuristic scan is not exhaustive DLP';inputHashes=$hashes;governance=@{gRuntime='BLOCKED';feBe='PENDING';authIam='PENDING';offline='PROHIBITED';openDecisions=@('OD-013','OD-014','OD-015','OD-017');gs01='RETAINED';gs04='RETAINED'}}
WriteText (Join-Path $Output 'static-results.json') (($result | ConvertTo-Json -Depth 30)+"`n")
'PASS: YAML/Compose, synthetic env completeness/negative checks, nine pinned image references, loopback/network/mount/resource boundaries, documentation, credential-placeholder scan and Git whitespace. No runtime execution.'
