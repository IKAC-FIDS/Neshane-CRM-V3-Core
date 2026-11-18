# V3-LOCAL-INFRA-002 — runtime validation report

Observed checks only; no baseline fixes, product implementation or production readiness.
G-RUNTIME: BLOCKED. FE-BE: PENDING. AUTH/IAM: PENDING. Offline: PROHIBITED.
SeaweedFS: EXPERIMENTAL / DEV-ONLY. OD-013/014/015/017 remain OPEN; GS-01/GS-04 retained.

## Actual results

{"PASS": 76, "FAIL": 15, "BLOCKED": 15}

| Check | Service | Expected | Status | Evidence | Remaining limitation |
| --- | --- | --- | --- | --- | --- |
| LIR002-PREFLIGHT | all | 17 unchanged baseline files; unique project, ports, fresh volumes and local engine | PASS | observations/LIR002-PREFLIGHT-1.json | Shared Docker host is trusted. Existing live volume contents are not frozen or byte-snapshotted. |
| LIR002-HARNESS-PULL-INTERRUPTED | runner | Pinned image acquisition completes within the command window | BLOCKED | observations/LIR002-HARNESS-PULL-INTERRUPTED-2.json | Retry is limited to the same nine authorized digest references; no baseline or existing resources changed. |
| LIR002-IMAGE-postgres | postgres | Exact approved digest; linux/amd64 | PASS | observations/LIR002-IMAGE-postgres-3.json | Digest identity is not a vulnerability scan or publisher attestation. |
| LIR002-IMAGE-redis | redis | Exact approved digest; linux/amd64 | PASS | observations/LIR002-IMAGE-redis-4.json | Digest identity is not a vulnerability scan or publisher attestation. |
| LIR002-IMAGE-rabbitmq | rabbitmq | Exact approved digest; linux/amd64 | PASS | observations/LIR002-IMAGE-rabbitmq-5.json | Digest identity is not a vulnerability scan or publisher attestation. |
| LIR002-IMAGE-seaweedfs | seaweedfs | Exact approved digest; linux/amd64 | PASS | observations/LIR002-IMAGE-seaweedfs-6.json | Digest identity is not a vulnerability scan or publisher attestation. |
| LIR002-IMAGE-mailpit | mailpit | Exact approved digest; linux/amd64 | PASS | observations/LIR002-IMAGE-mailpit-7.json | Digest identity is not a vulnerability scan or publisher attestation. |
| LIR002-IMAGE-otel-collector | otel-collector | Exact approved digest; linux/amd64 | PASS | observations/LIR002-IMAGE-otel-collector-8.json | Digest identity is not a vulnerability scan or publisher attestation. |
| LIR002-IMAGE-prometheus | prometheus | Exact approved digest; linux/amd64 | PASS | observations/LIR002-IMAGE-prometheus-9.json | Digest identity is not a vulnerability scan or publisher attestation. |
| LIR002-IMAGE-grafana | grafana | Exact approved digest; linux/amd64 | PASS | observations/LIR002-IMAGE-grafana-10.json | Digest identity is not a vulnerability scan or publisher attestation. |
| LIR002-IMAGE-tempo | tempo | Exact approved digest; linux/amd64 | PASS | observations/LIR002-IMAGE-tempo-11.json | Digest identity is not a vulnerability scan or publisher attestation. |
| LIR002-NATIVE-COLLECTOR | otel-collector | Native Collector config/components/OTTL validation exits zero | FAIL | observations/LIR002-NATIVE-COLLECTOR-12.json |  |
| LIR002-NATIVE-PROMETHEUS | prometheus | Native promtool config validation exits zero | PASS | observations/LIR002-NATIVE-PROMETHEUS-13.json |  |
| LIR002-NATIVE-TEMPO | tempo | Native Tempo configuration verification exits zero | FAIL | observations/LIR002-NATIVE-TEMPO-14.json | An unsupported verify flag is a native validation failure, not permission to invent success; actual startup is separately observed. |
| LIR002-NATIVE-TEMPO-CORRECTED-INVOCATION | tempo | Value-taking config.verify option is invoked correctly; retain initial harness FAIL | PASS | observations/LIR002-NATIVE-TEMPO-CORRECTED-INVOCATION-15.json | First missing-argument observation remains FAIL; this observation does not overwrite it. |
| LIR002-START | all | Only task-owned pinned services start without pull or baseline edits | PASS | observations/LIR002-START-16.json |  |
| LIR002-READY-postgres | postgres | Container remains running; configured health check is healthy | PASS | observations/LIR002-READY-postgres-17.json |  |
| LIR002-READY-redis | redis | Container remains running; configured health check is healthy | PASS | observations/LIR002-READY-redis-18.json |  |
| LIR002-READY-rabbitmq | rabbitmq | Container remains running; configured health check is healthy | PASS | observations/LIR002-READY-rabbitmq-19.json |  |
| LIR002-READY-mailpit | mailpit | Container remains running; configured health check is healthy | PASS | observations/LIR002-READY-mailpit-20.json |  |
| LIR002-READY-tempo | tempo | Container remains running; configured health check is healthy | PASS | observations/LIR002-READY-tempo-21.json | No Docker healthcheck for Collector/Tempo/SeaweedFS: independent endpoint checks are also required. |
| LIR002-READY-otel-collector | otel-collector | Start only native-valid configuration | BLOCKED | observations/LIR002-READY-otel-collector-22.json | Fix requires a separately authorized baseline correction, not a weakened filter. |
| LIR002-READY-prometheus | prometheus | Container remains running; configured health check is healthy | PASS | observations/LIR002-READY-prometheus-23.json |  |
| LIR002-READY-grafana | grafana | Container remains running; configured health check is healthy | PASS | observations/LIR002-READY-grafana-24.json |  |
| LIR002-READY-seaweedfs | seaweedfs | Container remains running; configured health check is healthy | PASS | observations/LIR002-READY-seaweedfs-25.json | No Docker healthcheck for Collector/Tempo/SeaweedFS: independent endpoint checks are also required. |
| LIR002-BOUNDARY-grafana | grafana | Project ownership, loopback ports, segmented networks, limits, mounts and no host privileges | PASS | observations/LIR002-BOUNDARY-grafana-26.json | Metadata/control evidence on a trusted shared host, not hostile-host/tenant isolation acceptance. |
| LIR002-BOUNDARY-postgres | postgres | Project ownership, loopback ports, segmented networks, limits, mounts and no host privileges | PASS | observations/LIR002-BOUNDARY-postgres-27.json | Metadata/control evidence on a trusted shared host, not hostile-host/tenant isolation acceptance. |
| LIR002-BOUNDARY-prometheus | prometheus | Project ownership, loopback ports, segmented networks, limits, mounts and no host privileges | PASS | observations/LIR002-BOUNDARY-prometheus-28.json | Metadata/control evidence on a trusted shared host, not hostile-host/tenant isolation acceptance. |
| LIR002-BOUNDARY-redis | redis | Project ownership, loopback ports, segmented networks, limits, mounts and no host privileges | PASS | observations/LIR002-BOUNDARY-redis-29.json | Metadata/control evidence on a trusted shared host, not hostile-host/tenant isolation acceptance. |
| LIR002-BOUNDARY-rabbitmq | rabbitmq | Project ownership, loopback ports, segmented networks, limits, mounts and no host privileges | PASS | observations/LIR002-BOUNDARY-rabbitmq-30.json | Metadata/control evidence on a trusted shared host, not hostile-host/tenant isolation acceptance. |
| LIR002-BOUNDARY-seaweedfs | seaweedfs | Project ownership, loopback ports, segmented networks, limits, mounts and no host privileges | PASS | observations/LIR002-BOUNDARY-seaweedfs-31.json | Metadata/control evidence on a trusted shared host, not hostile-host/tenant isolation acceptance. |
| LIR002-BOUNDARY-mailpit | mailpit | Project ownership, loopback ports, segmented networks, limits, mounts and no host privileges | PASS | observations/LIR002-BOUNDARY-mailpit-32.json | Metadata/control evidence on a trusted shared host, not hostile-host/tenant isolation acceptance. |
| LIR002-BOUNDARY-tempo | tempo | Project ownership, loopback ports, segmented networks, limits, mounts and no host privileges | PASS | observations/LIR002-BOUNDARY-tempo-33.json | Metadata/control evidence on a trusted shared host, not hostile-host/tenant isolation acceptance. |
| LIR002-PG-ROLES | postgres | Bootstrap superuser and app restricted attributes are distinct | PASS | observations/LIR002-PG-ROLES-34.json |  |
| LIR002-PG-AUTH | postgres | App authenticates over TCP | PASS | observations/LIR002-PG-AUTH-35.json |  |
| LIR002-PG-INVALID | postgres | Incorrect password rejected | PASS | observations/LIR002-PG-INVALID-36.json |  |
| LIR002-PG-DENY-SUPERUSER | postgres | Restricted app cannot perform privileged/schema administration | PASS | observations/LIR002-PG-DENY-SUPERUSER-37.json |  |
| LIR002-PG-DENY-ASSUME-ADMIN | postgres | Restricted app cannot perform privileged/schema administration | PASS | observations/LIR002-PG-DENY-ASSUME-ADMIN-38.json |  |
| LIR002-PG-DENY-CREATE-ROLE | postgres | Restricted app cannot perform privileged/schema administration | PASS | observations/LIR002-PG-DENY-CREATE-ROLE-39.json |  |
| LIR002-PG-DENY-CREATE-SCHEMA | postgres | Restricted app cannot perform privileged/schema administration | PASS | observations/LIR002-PG-DENY-CREATE-SCHEMA-40.json |  |
| LIR002-PG-SYNTHETIC | postgres | Admin-owned disposable test fixture; limited app INSERT/SELECT | PASS | observations/LIR002-PG-SYNTHETIC-41.json | Synthetic fixture only; no product schema, migrations or RLS implementation. |
| LIR002-PG-PERSIST | postgres | Synthetic row survives restart | PASS | observations/LIR002-PG-PERSIST-42.json |  |
| LIR002-PG-EXISTING-VOLUME | postgres | Existing volume skips init: changed env does not rotate stored app password | FAIL | observations/LIR002-PG-EXISTING-VOLUME-43.json | Expected configured readiness failure during changed-password experiment, not a production rotation implementation. |
| LIR002-PG-RESTORE-TASK-CONFIG | postgres | Task-only original synthetic config restored | PASS | observations/LIR002-PG-RESTORE-TASK-CONFIG-44.json |  |
| LIR002-REDIS-CONNECT | redis | Internal service DNS/PING; expected AOF, 256MiB and noeviction | PASS | observations/LIR002-REDIS-CONNECT-45.json | Unauthenticated dev network only; no cache/session/tenant policy. |
| LIR002-REDIS-PERSIST | redis | Synthetic write is AOF-synchronized and survives process restart | PASS | observations/LIR002-REDIS-PERSIST-46.json | Process restart only, not host power-loss or backup durability. |
| LIR002-REDIS-UNPUBLISHED | redis | No host-published Redis port | PASS | observations/LIR002-REDIS-UNPUBLISHED-47.json |  |
| LIR002-SERVICE-BLOCKED-rabbitmq | rabbitmq | Complete all bounded service checks | BLOCKED | observations/LIR002-SERVICE-BLOCKED-rabbitmq-48.json | Subsequent checks in this service group were not completed. |
| LIR002-COLLECTOR-HEALTH | otel-collector | Actual internal health extension responds successfully | BLOCKED | observations/LIR002-COLLECTOR-HEALTH-49.json | Health extension is not proof of downstream ingestion. |
| LIR002-TEMPO-HEALTH | tempo | Actual internal Tempo /ready succeeds | PASS | observations/LIR002-TEMPO-HEALTH-50.json |  |
| LIR002-SERVICE-BLOCKED-observability | observability | Complete all bounded service checks | BLOCKED | observations/LIR002-SERVICE-BLOCKED-observability-51.json | Subsequent checks in this service group were not completed. |
| LIR002-TEMPO-RETENTION | tempo | Native running Tempo reports development 24h block retention | PASS | observations/LIR002-TEMPO-RETENTION-52.json | Configured retention, not wall-clock expiry/durability proof. |
| LIR002-NETWORK-DENY | boundary | Telemetry peer cannot establish TCP to the isolated Redis network | PASS | observations/LIR002-NETWORK-DENY-53.json | Single task-owned cross-network connection attempt; metadata checks cover every service. |
| LIR002-SERVICE-BLOCKED-mailpit | mailpit | Complete all bounded service checks | BLOCKED | observations/LIR002-SERVICE-BLOCKED-mailpit-54.json | Subsequent checks in this service group were not completed. |
| LIR002-SEAWEED-HEALTH | seaweedfs | Source-confirmed internal admin health responds | PASS | observations/LIR002-SEAWEED-HEALTH-55.json | Experimental mini only; this is not S3 authorization evidence. |
| LIR002-SERVICE-BLOCKED-seaweedfs | seaweedfs | Complete all bounded service checks | BLOCKED | observations/LIR002-SERVICE-BLOCKED-seaweedfs-56.json | Subsequent checks in this service group were not completed. |
| LIR002-HOST-POSTGRES_PORT | postgres | Declared localhost development endpoint is reachable from this Windows host | FAIL | observations/LIR002-HOST-POSTGRES_PORT-57.json | Internal-only Docker networks may suppress publishing on this engine; no network/bind is loosened to hide failure. |
| LIR002-HOST-RABBITMQ_AMQP_PORT | rabbitmq | Declared localhost development endpoint is reachable from this Windows host | FAIL | observations/LIR002-HOST-RABBITMQ_AMQP_PORT-58.json | Internal-only Docker networks may suppress publishing on this engine; no network/bind is loosened to hide failure. |
| LIR002-HOST-RABBITMQ_UI_PORT | rabbitmq | Declared localhost development endpoint is reachable from this Windows host | FAIL | observations/LIR002-HOST-RABBITMQ_UI_PORT-59.json | Internal-only Docker networks may suppress publishing on this engine; no network/bind is loosened to hide failure. |
| LIR002-HOST-MAILPIT_SMTP_PORT | mailpit | Declared localhost development endpoint is reachable from this Windows host | FAIL | observations/LIR002-HOST-MAILPIT_SMTP_PORT-60.json | Internal-only Docker networks may suppress publishing on this engine; no network/bind is loosened to hide failure. |
| LIR002-HOST-MAILPIT_UI_PORT | mailpit | Declared localhost development endpoint is reachable from this Windows host | FAIL | observations/LIR002-HOST-MAILPIT_UI_PORT-61.json | Internal-only Docker networks may suppress publishing on this engine; no network/bind is loosened to hide failure. |
| LIR002-HOST-PROMETHEUS_PORT | prometheus | Declared localhost development endpoint is reachable from this Windows host | FAIL | observations/LIR002-HOST-PROMETHEUS_PORT-62.json | Internal-only Docker networks may suppress publishing on this engine; no network/bind is loosened to hide failure. |
| LIR002-HOST-GRAFANA_PORT | grafana | Declared localhost development endpoint is reachable from this Windows host | FAIL | observations/LIR002-HOST-GRAFANA_PORT-63.json | Internal-only Docker networks may suppress publishing on this engine; no network/bind is loosened to hide failure. |
| LIR002-HOST-SEAWEEDFS_S3_PORT | seaweedfs | Declared localhost development endpoint is reachable from this Windows host | FAIL | observations/LIR002-HOST-SEAWEEDFS_S3_PORT-64.json | Internal-only Docker networks may suppress publishing on this engine; no network/bind is loosened to hide failure. |
| LIR002-RABBIT-AUTH | rabbitmq | Valid management login works; invalid password rejected | PASS | observations/LIR002-RABBIT-AUTH-65.json |  |
| LIR002-RABBIT-PERMISSIONS | rabbitmq | Development user has management not administrator tag, dev vhost permissions only | PASS | observations/LIR002-RABBIT-PERMISSIONS-66.json | No product messaging identity/topology is accepted. |
| LIR002-RABBIT-AMQP | rabbitmq | Native internal AMQP handshake accepts valid credentials/vhost and rejects invalid password | FAIL | observations/LIR002-RABBIT-AMQP-67.json | Internal listener test; published host endpoint failure remains separately recorded. |
| LIR002-RABBIT-PERSIST-MESSAGE | rabbitmq | Durable synthetic queue/persistent message survives restart and is consumed | PASS | observations/LIR002-RABBIT-PERSIST-MESSAGE-68.json | Task-only disposable queue fixture, not product topology or delivery guarantees. |
| LIR002-COLLECTOR-HEALTH | otel-collector | Actual internal health extension responds successfully | BLOCKED | observations/LIR002-COLLECTOR-HEALTH-69.json | Health extension is not proof of downstream ingestion. |
| LIR002-TEMPO-HEALTH | tempo | Actual internal Tempo /ready succeeds | PASS | observations/LIR002-TEMPO-HEALTH-70.json |  |
| LIR002-PROMETHEUS-RETENTION | prometheus | Native running configuration has 1d and 256MB retention | PASS | observations/LIR002-PROMETHEUS-RETENTION-71.json | Configured caps observed; 24-hour expiry is not time-travel tested. |
| LIR002-GRAFANA-NATIVE-HEALTH | grafana | Native server loads config and database; /api/health succeeds | PASS | observations/LIR002-GRAFANA-NATIVE-HEALTH-72.json | Startup, provisioning and APIs verify native loading; no invented validation-only CLI flag. |
| LIR002-GRAFANA-NESHANE-PROMETHEUS | grafana | Provisioned datasource backend connectivity is healthy | PASS | observations/LIR002-GRAFANA-NESHANE-PROMETHEUS-73.json |  |
| LIR002-GRAFANA-NESHANE-TEMPO | grafana | Provisioned datasource backend connectivity is healthy | PASS | observations/LIR002-GRAFANA-NESHANE-TEMPO-74.json |  |
| LIR002-MAILPIT-DELIVERY | mailpit | Synthetic SMTP is captured and visible in task Mailpit | PASS | observations/LIR002-MAILPIT-DELIVERY-75.json | No relay is configured; internal network and localhost binds checked. No external email delivery was requested. |
| LIR002-SEAWEED-HEALTH | seaweedfs | Source-confirmed internal admin health responds | PASS | observations/LIR002-SEAWEED-HEALTH-76.json | Experimental mini only; this is not S3 authorization evidence. |
| LIR002-SEAWEED-OBJECT | seaweedfs | Signed S3 PUT/GET succeeds with identical SHA-256 | PASS | observations/LIR002-SEAWEED-OBJECT-77.json | EXPERIMENTAL / DEV-ONLY; OD-017 is not resolved. |
| LIR002-SEAWEED-AUTH | seaweedfs | Wrong signing secret and missing credentials are rejected | PASS | observations/LIR002-SEAWEED-AUTH-78.json |  |
| LIR002-INTERNAL-BLOCKED-seaweedfs | seaweedfs | Complete independent checks over unchanged task networks | BLOCKED | observations/LIR002-INTERNAL-BLOCKED-seaweedfs-79.json | Host reachability failures and initial BLOCKED observations remain preserved. |
| LIR002-RABBIT-AMQP-CORRECTED-PROBE | rabbitmq | Seekable native AMQP probe accepts valid credentials/vhost and rejects invalid password | FAIL | observations/LIR002-RABBIT-AMQP-CORRECTED-PROBE-80.json | Initial escript /dev/stdin espipe FAIL is retained as a harness failure; host path remains FAIL. |
| LIR002-PG-EXISTING-VOLUME | postgres | Existing volume skips init: changed env does not rotate stored app password | PASS | observations/LIR002-PG-EXISTING-VOLUME-81.json | Expected configured readiness failure during changed-password experiment, not a production rotation implementation. |
| LIR002-PG-RESTORE-TASK-CONFIG | postgres | Task-only original synthetic config restored | PASS | observations/LIR002-PG-RESTORE-TASK-CONFIG-82.json |  |
| LIR002-SEAWEED-HEALTH | seaweedfs | Source-confirmed internal admin health responds | PASS | observations/LIR002-SEAWEED-HEALTH-83.json | Experimental mini only; this is not S3 authorization evidence. |
| LIR002-SEAWEED-OBJECT | seaweedfs | Signed S3 PUT/GET succeeds with identical SHA-256 | PASS | observations/LIR002-SEAWEED-OBJECT-84.json | EXPERIMENTAL / DEV-ONLY; OD-017 is not resolved. |
| LIR002-SEAWEED-AUTH | seaweedfs | Wrong signing secret and missing credentials are rejected | PASS | observations/LIR002-SEAWEED-AUTH-85.json |  |
| LIR002-SEAWEED-PERSIST | seaweedfs | Synthetic object and credential configuration survive restart | PASS | observations/LIR002-SEAWEED-PERSIST-86.json | Process restart only; no product storage, HA or power-loss guarantee. |
| LIR002-RABBIT-AMQP-CORRECTED-PROBE | rabbitmq | Seekable native AMQP probe accepts valid credentials/vhost and rejects invalid password | FAIL | observations/LIR002-RABBIT-AMQP-CORRECTED-PROBE-87.json | Initial escript /dev/stdin espipe FAIL is retained as a harness failure; host path remains FAIL. |
| LIR002-BOUNDARY-postgres | postgres | Project ownership, loopback ports, segmented networks, limits, mounts and no host privileges | PASS | observations/LIR002-BOUNDARY-postgres-88.json | Metadata/control evidence on a trusted shared host, not hostile-host/tenant isolation acceptance. |
| LIR002-BOUNDARY-grafana | grafana | Project ownership, loopback ports, segmented networks, limits, mounts and no host privileges | PASS | observations/LIR002-BOUNDARY-grafana-89.json | Metadata/control evidence on a trusted shared host, not hostile-host/tenant isolation acceptance. |
| LIR002-BOUNDARY-prometheus | prometheus | Project ownership, loopback ports, segmented networks, limits, mounts and no host privileges | PASS | observations/LIR002-BOUNDARY-prometheus-90.json | Metadata/control evidence on a trusted shared host, not hostile-host/tenant isolation acceptance. |
| LIR002-BOUNDARY-redis | redis | Project ownership, loopback ports, segmented networks, limits, mounts and no host privileges | PASS | observations/LIR002-BOUNDARY-redis-91.json | Metadata/control evidence on a trusted shared host, not hostile-host/tenant isolation acceptance. |
| LIR002-BOUNDARY-rabbitmq | rabbitmq | Project ownership, loopback ports, segmented networks, limits, mounts and no host privileges | PASS | observations/LIR002-BOUNDARY-rabbitmq-92.json | Metadata/control evidence on a trusted shared host, not hostile-host/tenant isolation acceptance. |
| LIR002-BOUNDARY-seaweedfs | seaweedfs | Project ownership, loopback ports, segmented networks, limits, mounts and no host privileges | PASS | observations/LIR002-BOUNDARY-seaweedfs-93.json | Metadata/control evidence on a trusted shared host, not hostile-host/tenant isolation acceptance. |
| LIR002-BOUNDARY-mailpit | mailpit | Project ownership, loopback ports, segmented networks, limits, mounts and no host privileges | PASS | observations/LIR002-BOUNDARY-mailpit-94.json | Metadata/control evidence on a trusted shared host, not hostile-host/tenant isolation acceptance. |
| LIR002-BOUNDARY-tempo | tempo | Project ownership, loopback ports, segmented networks, limits, mounts and no host privileges | PASS | observations/LIR002-BOUNDARY-tempo-95.json | Metadata/control evidence on a trusted shared host, not hostile-host/tenant isolation acceptance. |
| LIR002-CLEANUP | cleanup | All explicitly identified task containers/networks/disposable volumes removed | PASS | observations/LIR002-CLEANUP-96.json | Downloaded allowed images are intentionally retained and reported separately. |
| LIR002-PRESERVATION-DOCKER | preservation | Original container instance/state/config, networks/volumes and image references preserved | FAIL | observations/LIR002-PRESERVATION-DOCKER-97.json | Live pre-existing volumes/counters may evolve naturally; no live data freeze or byte-level content preservation is claimed. |
| LIR002-PRESERVATION-17 | preservation | All 17 baseline artifacts byte-identical | PASS | observations/LIR002-PRESERVATION-17-98.json |  |
| LIR002-PRESERVATION-REPOSITORIES | preservation | Original Root index/files, Root Main, Backend and Frontend unchanged | PASS | observations/LIR002-PRESERVATION-REPOSITORIES-99.json |  |
| LIR002-EVIDENCE-CREDENTIAL-SCAN | evidence | No generated credential value or Basic token in review artifacts | PASS | observations/LIR002-EVIDENCE-CREDENTIAL-SCAN-100.json | Known generated values only; not a claim of exhaustive DLP or inspection of original secrets. |
| LIR002-BOUNDARY-otel-collector | otel-collector | Observe the corresponding service readiness/security boundary | BLOCKED | observations/LIR002-BOUNDARY-otel-collector-101.json | Not treated as PASS or not-applicable. |
| LIR002-OTLP-ACCEPT | otel-collector | Complete the corresponding bounded service check | BLOCKED | observations/LIR002-OTLP-ACCEPT-102.json | No result fabricated; see earlier service/native/start observations. |
| LIR002-TELEMETRY-NEGATIVES | otel-collector | Complete the corresponding bounded service check | BLOCKED | observations/LIR002-TELEMETRY-NEGATIVES-103.json | No result fabricated; see earlier service/native/start observations. |
| LIR002-TELEMETRY-LOGS-DISABLED | otel-collector | Complete the corresponding bounded service check | BLOCKED | observations/LIR002-TELEMETRY-LOGS-DISABLED-104.json | No result fabricated; see earlier service/native/start observations. |
| LIR002-PROMETHEUS-INGEST | prometheus | Complete the corresponding bounded service check | BLOCKED | observations/LIR002-PROMETHEUS-INGEST-105.json | No result fabricated; see earlier service/native/start observations. |
| LIR002-TEMPO-RETRIEVE | tempo | Complete the corresponding bounded service check | BLOCKED | observations/LIR002-TEMPO-RETRIEVE-106.json | No result fabricated; see earlier service/native/start observations. |

## Preservation and cleanup

See docker-before.json, docker-after.json, resource-preservation-report.json and cleanup-report.json.
Registry images retained; pullRequired/newImageID are in image-identity-verification.json.
Original actual .env was never read/reused. Synthetic inputs were outside Git with restricted ACL.
No staging, commit or push. Baseline native/runtime failures are retained, not silently repaired.

## Limits

Finite synthetic observations and process restarts do not prove hostile-host isolation, power-loss durability,
long-horizon retention, complete DLP, production IAM, product RLS, real workload readiness or Runtime acceptance.

## Reviewer disposition addendum

The preservation Docker FAIL is a mount-array ordering difference only: `docker inspect` returned identical mounts for the two long-running pre-existing observability containers in a different order between snapshots. IDs, image, network, IP, startedAt and mount source/destination/mode are unchanged; no pre-existing resource was modified. Earlier FAIL/BLOCKED rows are preserved as history and were not overwritten by later successful independent checks.
