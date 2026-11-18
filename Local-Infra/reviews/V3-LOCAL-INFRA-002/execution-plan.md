# V3-LOCAL-INFRA-002 — authorized runtime validation scope

Authority: current explicit owner conversation, Task ID `V3-LOCAL-INFRA-002`,
Title `Development Infrastructure Runtime Validation`. This supersedes the earlier
V3-LOCAL-INFRA-001 no-runtime restriction prospectively for this isolated validation
only. It authorizes pulls of exactly the nine already pinned images, task-owned
development containers, synthetic checks/restarts and removal of explicitly
identified task-created disposable resources. It authorizes no baseline fixes,
product implementation, existing-resource modification, production, staging,
commit, push, architecture closure or Runtime acceptance.

Workspace: `E:\Neshane-CRM-V3-V3-LOCAL-INFRA-001`;
branch `codex/v3-local-infra-001`; HEAD
`094c966de745285bd5a8d1975312eb06d930d4a8`.
All 17 original artifacts are hash-pinned in `session.json` and must remain unchanged.
The static validator and V3-LOCAL-INFRA-001 original-preservation verifier were
rerun successfully before this review directory was created. No actual `.env` is
read or reused. Old no-runtime statements remain historical task scope, not a
current claim that this new authorized runtime task is prohibited.

## Isolation and evidence

- `docker-before.json` records pre-existing container instances, network/volume
  descriptors and image IDs/references without reading environment arrays, volume
  contents or original credentials. Existing live workloads are not stopped.
- Use the unique project and dynamically reserved free loopback ports in
  `session.json`, fresh project-scoped volumes and the local Docker Desktop named
  pipe only. The original default-port services remain untouched.
- Synthetic credentials are randomly generated into a restricted-ACL external
  private directory. Docker uses an empty private client credential configuration;
  no original registry/app credentials are reused. No actual env values, Basic
  tokens or expanded Compose configuration are included in evidence.
- Every Docker operation is recorded in `runtime-commands.json`, with secret
  redaction and no recorded stdin. Generated SQL, SMTP, OTLP and S3 probes contain
  only task-owned synthetic fixtures. No other image/tool container is permitted.
- Native validation containers have no network, a read-only root, resource limits,
  no privileges/capabilities, read-only exact config binds and tmpfs replacing any
  image-declared anonymous volume. Grafana native loading is observed through real
  startup/provisioning and health APIs, not an invented config-check CLI.
- `LIR002-*` IDs are local observation identifiers, not approved roadmap Task IDs.
  Every result includes expected/actual/status/evidence/limitation. Missing downstream
  observations become BLOCKED. Actual FAILs and harness failures are retained; a
  subsequent observation never overwrites an earlier one.

## Service checks

PostgreSQL: bootstrap/app attributes and TCP authentication, bad-password rejection,
denied privilege escalation/role/schema creation, a tiny administrator-owned
synthetic table with limited app grants, restart persistence and changed-env versus
stored-password behavior on the NEW task volume. Restore only the task's original
synthetic configuration afterward. This is no product schema/migration/RLS.

Redis: task-network service DNS/PING, configured AOF/memory/noeviction, tiny key
round-trip and WAITAOF/restart persistence, no host publication and a bounded
cross-network TCP denial attempt using an already approved task image's tool.

RabbitMQ: listener diagnostics, management/API and actual AMQP handshake positive/
negative authentication, CLI user tags/vhost permissions, disposable durable queue
and persistent synthetic message retained across restart then consumed. This is
test-fixture topology only, never product messaging or Outbox/Inbox.

Collector/Prometheus/Tempo/Grafana: native configurations/startup, actual internal
health and external loopback endpoints, OTLP/HTTP synthetic metric/trace admission,
Prometheus scrape/query, Tempo trace-by-ID, Grafana datasource backend health,
development retention settings and rejection/minimization sentinels. No real
application/customer telemetry. The synthetic marker is not authentication or DLP.

Mailpit: reserved `.invalid` addresses, local synthetic SMTP capture and API visibility;
no relay, external recipient or real email data.

SeaweedFS: separate experimental config, exact original digest, source-confirmed
mini startup, internal admin health, host-loopback SigV4 S3 PUT/GET and SHA-256,
invalid/missing credential denial and restart persistence. Remains EXPERIMENTAL /
DEV-ONLY; OD-017 is not resolved.

## Cleanup

Never use global prune, broad selectors, compose down -v or pre-existing IDs. For
each current project-labeled resource, cross-check it was absent from the before
inventory, verify task ownership, then stop/remove only its explicit ID/name.
Containers precede empty networks and disposable volumes. Check original metadata/
instance/role identities and references afterward. Original live data/counters may
evolve naturally; they are not read or frozen, and byte-level live-volume equality
must not be claimed. Downloaded allowed images are retained and reported separately.
Remove explicit task-generated private credential files only after resource cleanup.

Original Root/index, Root Main, Backend and Frontend preservation is verified again
with the existing snapshot tool. Any unresolved cleanup/preservation issue is a
reported FAIL/BLOCKED, never an authorization to touch unrelated resources.

G-RUNTIME remains BLOCKED. FE-BE and AUTH/IAM authorization PENDING.
Offline continuation PROHIBITED. OD-013/014/015/017 and GS-01/GS-04 unchanged.
