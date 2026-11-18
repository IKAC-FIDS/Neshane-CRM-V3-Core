# V3-LOCAL-INFRA-003 — defect register

Task: `V3-LOCAL-INFRA-003 — Local-Infra Runtime Defect Remediation and Revalidation`.
Authority: explicit owner conversation; workspace `E:\Neshane-CRM-V3-V3-LOCAL-INFRA-001`,
branch `codex/v3-local-infra-001`, baseline `094c966de745285bd5a8d1975312eb06d930d4a8`.
No 002 evidence or historical FAIL/BLOCKED observation is modified. No staging,
commit or push. G-RUNTIME BLOCKED; FE-BE/AUTH-IAM authorization PENDING; offline
PROHIBITED; OD-013/014/015/017 OPEN; GS-01/GS-04 retained.

| # | Defect (historical) | Confirmed root cause | Remediation | Disposition |
| --- | --- | --- | --- | --- |
| 1 | LIR002-NATIVE-COLLECTOR (FAIL) | `filter/synthetic` mixed Basic (string) and Advanced (object) condition styles, which the contrib 0.164.0 filter processor rejects. | Rewrote `trace_conditions`/`metric_conditions` to consistent Advanced OTTL object style; synthetic boundary unchanged. | RESOLVED_AND_REVALIDATED |
| 2 | LIR002-HOST-* (8 FAIL) | `internal: true` networks suppress host port publication on Docker Desktop (`NetworkSettings.Ports` empty). A/B test proved it. | Removed `internal: true` from published networks; retained it for the unpublished Redis network; loopback binds kept. | RESOLVED_AND_REVALIDATED |
| 3 | LIR002-RABBIT-AMQP / RABBIT-AMQP-CORRECTED-PROBE (FAIL) | Probe sent `channel_max = 0` in `connection.tune-ok`; RabbitMQ 4.x rejects it (max 2047). Server log verbatim: "negotiated channel_max = 0 (no limit) is higher than the maximum allowed value (2047)". | Corrected AMQP client negotiates `channel_max = 2047`; full round-trip verified. No auth/permission weakening. | RESOLVED_AND_REVALIDATED |
| 4 | LIR002-PRESERVATION-DOCKER (FAIL) | `docker inspect` returned equivalent mounts in a different order between snapshots; strict array comparison flagged it. | Deterministic comparator (stable mount sort) proves order-only difference; also demonstrates detection of real mount changes. | RESOLVED_AND_REVALIDATED |
| 5 | LIR002-NATIVE-TEMPO (FAIL) | Harness invoked `-config.verify` without a value (flag requires an argument). | Corrected invocation `-config.verify=true`; Tempo config valid. | RESOLVED_AND_REVALIDATED |
| 6 | LIR002-HARNESS-PULL-INTERRUPTED (BLOCKED) | Initial shell harness 120s limit exceeded during first pinned-image pull. | Resumed the same pinned pull; not a baseline defect. | CONFIRMED_ENVIRONMENT_LIMITATION |
| 7 | LIR002-PG-EXISTING-VOLUME (FAIL then PASS) | Windows text-stdin CRLF conversion corrupted the password probe. | Binary stdin transport; task config restored. | RESOLVED_AND_REVALIDATED |
| 8 | LIR002-SERVICE-BLOCKED-rabbitmq/mailpit/seaweedfs/observability (BLOCKED) | Initial host-path HTTP connection refused (consequence of defect #2). | Independent internal task-network checks passed for all four groups. | RESOLVED_AND_REVALIDATED |

Not a defect (documented): collector-dependent 002 BLOCKED rows (OTLP-ACCEPT,
TELEMETRY-NEGATIVES, TELEMETRY-LOGS-DISABLED, PROMETHEUS-INGEST, TEMPO-RETRIEVE,
COLLECTOR-HEALTH, READY/BOUNDARY-otel-collector) were direct consequences of
defect #1 and are resolved together with it.
