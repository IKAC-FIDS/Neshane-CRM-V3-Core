# Local-Infra — V3-LOCAL-INFRA-001

**DEVELOPMENT-ONLY / SYNTHETIC WORKLOADS. STATICALLY REVIEWED, NOT RUNTIME VERIFIED.**

Task authority: explicit owner conversation `V3-LOCAL-INFRA-001 — Local-Infra
Development Baseline Hardening`, branch `codex/v3-local-infra-001`, based on Root
Main `094c966de745285bd5a8d1975312eb06d930d4a8`. Authorization is limited to isolated
correction and static checks. No containers, image pulls, application/infrastructure
workloads, staging, commit, push, product implementation or production use are
authorized. Commands marked **future runtime** below are documentation, NOT current
execution permission. Actual task timing/results are in `validation-report.md`.

G-RUNTIME = **BLOCKED**. FE-BE authorization = **PENDING**. AUTH/IAM authorization =
**PENDING**. Offline continuation = **PROHIBITED**. OD-013, OD-014, OD-015 and OD-017
remain OPEN; GS-01 and GS-04 are retained. This does not change any Root ADR or
approve migration tooling, product RLS, IAM, object storage or an observability
architecture. Services still own their data, roles, schemas and migrations.

## Prerequisites and configuration

- Windows PowerShell 7 and Docker Compose v2.40.3 or compatible Compose v2. A Linux
  container engine is needed only for the separately authorized future runtime plan.
- Planned runtime platform is linux/amd64. Registry metadata includes that platform;
  other architectures need review. Docker/Compose config parsing does not prove an
  engine's runtime/resource/network capabilities.
- Budget about 6 GiB free memory plus disk for task-owned synthetic volumes; limits
  total approximately 4 GiB without the experiment. Do not run against existing
  customer environments or attach unrelated volumes/networks.
- Do not reuse/copy the original preservation checkout's `.env` or existing volumes.
  `.env.example` has placeholders only, not usable or approved credentials.

For a future authorized local run, copy `.env.example` to a NEW ignored `.env` in
this worktree, replace every `REPLACE_...` value with a different newly generated
synthetic-only value, and set a unique `COMPOSE_PROJECT_NAME` for this worktree/task.
This task did not create/read a real `.env`. Never print it or attach it to evidence.

Required base variables: `COMPOSE_PROJECT_NAME`, `POSTGRES_PASSWORD`,
`POSTGRES_APP_PASSWORD`, `RABBITMQ_USER`, `RABBITMQ_PASSWORD`,
`GRAFANA_ADMIN_USER`, `GRAFANA_ADMIN_PASSWORD`. The two PostgreSQL passwords must
differ. The experimental file additionally requires `SEAWEEDFS_ACCESS_KEY`,
`SEAWEEDFS_SECRET_KEY`, `SEAWEEDFS_ADMIN_USER`, `SEAWEEDFS_ADMIN_PASSWORD`.
Optional port variables and defaults are listed in `.env.example` and below.

Compose environment variables are visible to Docker administrators and privileged
host processes; `.env` is not a secret manager. Restrict its host ACL and use no real
credential/customer/tenant/session data. Shell variables override env-file values;
avoid unrelated exported configuration. Never capture expanded `docker compose
config` output, inspect environment arrays or password-bearing SQL/commands.
The static validator instead uses an isolated child environment and synthetic values.

## Inventory, ports and networks

All published ports bind **127.0.0.1**. No fixed container, network or volume names;
Compose prefixes resources with the project name. Different project names do not
avoid fixed host port collisions: change the documented port variables as needed.

| Service | Version (also digest-pinned) | Host default -> container | Dedicated network | Readiness |
| --- | --- | --- | --- | --- |
| PostgreSQL | 17.12 | 15432 -> 5432 | postgres | TCP authenticated SELECT 1 as restricted app user |
| Redis | 7.4.12 | **none** | redis | redis-cli PING, not authorization proof |
| RabbitMQ | 4.2.9-management | AMQP 15673 -> 5672; UI 25672 -> 15672 | broker | running + local alarms + listener connectivity |
| Mailpit | 1.34.0 | SMTP 11025 -> 1025; UI 18025 -> 8025 | mail | image-provided /mailpit readyz |
| Collector | 0.164.0 | OTLP gRPC 14317 -> 4317; HTTP 14318 -> 4318 | telemetry | internal health extension :13133; no Docker healthcheck |
| Prometheus | 3.7.3 | 19090 -> 9090 | telemetry | /-/ready |
| Grafana | 13.2.1 | 13000 -> 3000 | telemetry | /api/health; waits for healthy Prometheus |
| Tempo | 3.1.1 | **none**; HTTP API :3200, OTLP :4317/:4318 internal | telemetry | internal /ready; no Docker healthcheck |
| SeaweedFS | 4.50, original digest | experimental S3 18333 -> 8333 only | experimental | internal admin /health :12535; no Docker healthcheck |

Networks are project-scoped bridges; **segmentation is the isolation boundary**
(one network per service group), not container egress isolation. Only the
unpublished Redis network keeps `internal: true`; networks that publish a host
port must not be internal because Docker Desktop suppresses host port publication
on internal networks (confirmed by the V3-LOCAL-INFRA-003 A/B test). Only telemetry
components share a network; data/broker/mail/experimental networks are separate.
Host publication is not authentication or hostile-host isolation. Docker
administrators can attach peers; no app gets a network attachment implicitly.
Redis has no host access and no other configured peer; any later attachment or
exposure needs exact task authorization.

Restart policy is `no`, not persistent auto-restart. Services have memory/CPU/PID and
log-rotation limits and no-new-privileges. Suitable non-root images retain upstream
users; PostgreSQL/RabbitMQ/Redis/SeaweedFS retain required upstream initialization
and privilege-drop behavior, not forced users that break volume ownership. No
privileged mode, host networking, broad host mounts or Docker socket. Resource
limits are development guardrails, not capacity objectives or isolation proof.

## PostgreSQL: initialization is not migration or rotation

Fresh, empty `postgres_data` only: official entrypoint creates bootstrap superuser
`neshane_dev_admin` and database `neshane_dev`; the read-only init script creates
`neshane_dev_app` with NOSUPERUSER, NOCREATEDB, NOCREATEROLE, NOREPLICATION and
NOBYPASSRLS. It revokes PUBLIC database privileges/schema creation, grants the app
CONNECT and schema USAGE only, and creates **no product tables/schemas or RLS**.
The app does not own the database/schema and has no blanket table privileges.

Use only `neshane_dev_app` for permitted synthetic development connections, never
the bootstrap identity. Connection readiness checks use TCP app authentication,
not merely pg_isready. This still does not prove role settings, read/write grants,
Tenant Context, pool cleanup or RLS; verify them separately if runtime is authorized.

Existing volumes: the entrypoint skips initialization/scripts. Editing `.env` does
not rotate existing PostgreSQL credentials or create the app role. Health should
fail rather than quietly fall back to admin if the role/password is absent. Stop
and plan explicit task-owned repair or a separately approved disposable reset;
never auto-delete or migrate an existing volume. No migration framework is selected.

## Redis and RabbitMQ trust boundaries

Redis is unauthenticated on its isolated, unpublished dev network. It accepts only
synthetic data; this is not a product cache/session setup or tenant-key policy. AOF
persists synthetic contents. The 256mb dataset limit with noeviction rejects writes
requiring growth when full; 384m container limit leaves some overhead but does not
guarantee no OOM. Persistence buffers and runtime overhead still need observation.

RabbitMQ has one development management-tagged user and `neshane_dev` vhost, with
full configure/read/write **within that dev vhost**. It is not a product service
identity or universal administrator. No product exchanges, queues, retry/DLQ or
Outbox/Inbox are created. Management and AMQP are localhost-only and plaintext.
Default user/vhost settings initialize an empty database; editing env does not
rotate or rewrite existing users/permissions. Readiness diagnostics do not prove
authentication, authorization or delivery semantics.
The container-local hostname `rabbitmq` keeps the node identity stable when its
project container is recreated; it does not allocate a global container name or
authorize a product cluster.

## Experimental SeaweedFS — opt in explicitly

Not present in the base Compose model. Add `compose.seaweedfs.yaml` only for a
separately authorized synthetic experiment. Preserve the original verified digest;
see exact-source/version evidence in `configuration-sources.md`.

The pinned source supports `mini -dir=/data`, AWS_ACCESS_KEY_ID/AWS_SECRET_ACCESS_KEY,
S3_BUCKET and WEED_ADMIN_* credentials. WebDAV/Iceberg/Lance and master telemetry
are disabled. Only S3 is published on localhost. Master, filer, volume, admin and
worker endpoints are not host-published. `/data` persists filer metadata as well as
data. Admin `/health` is not a test of S3 credential enforcement or object durability.
Mini can retain generated keys/options in its volume; no general credential rotation
or secure storage is claimed. OD-017 remains unresolved. Never reuse real S3 keys.

## Observability: deliberately synthetic and incomplete

Collector accepts OTLP metrics/traces, not logs. Inputs must have boolean resource
attribute `neshane.synthetic=true`; this marker is NOT authenticated identity and
does not make real data safe. Metrics additionally allow only `neshane.synthetic.probe`.
Attribute minimization, constant span/service/scope names, cleared status messages
and discarded span events reduce accidental disclosure. No raw debug/log exporter.
This is NOT complete DLP: IDs, links, exemplars or malformed/adversarial payloads
must not contain sensitive values. Do not send production data even with the marker.

Traces go to internal Tempo over plaintext gRPC with bounded queue/retry/timeout.
Prometheus scrapes itself and the Collector exporter only. Grafana has fixed
Prometheus/Tempo datasource UIDs, no anonymous access/signup or automatic plugin
installation/update. No app health catalog, infrastructure exporters, alerts,
dashboard pack or searchable log backend is supplied. There is no production TLS,
IAM or observability architecture acceptance.

Prometheus retention is 1 day/256MB (whichever applies first), Tempo trace-block
retention 24h, and Mailpit 1000 messages/24h. These are synthetic development caps,
not legal/security retention policies or SLAs. Purging is asynchronous and volumes
can still fill. Grafana state persists. Runtime readiness for Collector/Tempo/
SeaweedFS must be probed independently; service_started is not service_healthy.

## Static validation — authorized now

From this `Local-Infra` directory:

```powershell
pwsh -NoProfile -File ./Validate-DevelopmentBaseline.ps1
```

The script never reads `.env`, never contacts a daemon/registry, and invokes only
`docker compose ... config` with isolated synthetic variables. YAML syntax uses the
Compose YAML parser, including extension-only wrappers for mounted YAML files.
It checks both base/experimental models, required/missing variables, images versus
the metadata lock, mounts, ports, network boundaries, governance documentation,
credential placeholders and Git whitespace. Results in ignored `.validation/` are
STATIC ONLY; native config/OTTL compilation, shell execution, health checks and
runtime behavior remain unverified. Registry metadata checks were performed once
over HTTPS during authoring, with no layer downloads.

## Persistent volume lifecycle

| Project-scoped volume | Synthetic contents |
| --- | --- |
| postgres_data | Database and role initialization state |
| redis_data | AOF/cache experiment data |
| rabbitmq_data | Broker users, permissions and development messages |
| mailpit_data | Captured test email database |
| prometheus_data | Time-series WAL and blocks |
| grafana_data | Grafana database, local admin initialization and state |
| tempo_data | Trace WAL and blocks |
| seaweedfs_data | Experimental data, filer metadata, options and generated keys |

Renaming the project selects different volumes; it does not migrate/delete old
volumes. Do not declare external volumes or mount original task/customer volumes.
PostgreSQL/RabbitMQ/Grafana initialization values are not automatic credential rotation.

## Future runtime startup/shutdown — NOT executed or authorized by this task

Only after separate authorization, available trusted pinned images, fresh synthetic
configuration and a project/resource ownership check, from `Local-Infra`:

```powershell
# Base only; --pull never stops rather than downloading missing images.
docker compose --env-file .env -f compose.yaml up -d --pull never
# OR opt into the experiment with explicit additional configuration:
docker compose --env-file .env -f compose.yaml -f compose.seaweedfs.yaml up -d --pull never
```

Use the SAME project name, env file and file set for status/shutdown. Record the
resolved project name privately, without printing secret-bearing expanded config.

```powershell
# Base shutdown keeps persistent volumes:
docker compose --env-file .env -f compose.yaml down
# Experimental shutdown also keeps persistent volumes:
docker compose --env-file .env -f compose.yaml -f compose.seaweedfs.yaml down
```

Do not use `down -v`, global prune or broad volume/network deletion. Safe cleanup
means first stopping only this task's resources and retaining data. Any destructive
disposable-volume reset needs a separate explicit approval, exact project-label/
volume inventory, backup/data-loss check and narrowly named targets. This task
authorizes no such cleanup. Full proposed checks/stop conditions are in
`runtime-validation-plan.md`.
