# V3-LOCAL-INFRA-003 — validation report

Task: `V3-LOCAL-INFRA-003 — Local-Infra Runtime Defect Remediation and Revalidation`.
Workspace `E:\Neshane-CRM-V3-V3-LOCAL-INFRA-001`, branch
`codex/v3-local-infra-001`, baseline `094c966de745285bd5a8d1975312eb06d930d4a8`.

## Baseline and preservation

- 13 of 17 baseline artifacts remain byte-identical; the other 5 are the intended
  remediations (`observability/otel-collector.yaml`, `compose.yaml`,
  `compose.seaweedfs.yaml`, `Validate-DevelopmentBaseline.ps1`, `README.md`).
- All 16 V3-LOCAL-INFRA-002 evidence artifacts remain byte-identical; no historical
  PASS/FAIL/BLOCKED observation was rewritten.
- Pre-existing Docker resources preserved: 13 containers, 5 networks, 8
  `neshane-local_*` volumes and 3 `iam-foundation_*` volumes untouched.
- Original `.env` was never read or reused.

## Confirmed root causes (full analysis in `root-cause-analysis.md`)

1. Collector filter mixed Basic/Advanced OTTL styles.
2. `internal: true` networks suppress Docker Desktop host port publication.
3. AMQP probe negotiated `channel_max = 0`, rejected by RabbitMQ 4.x (max 2047).
4. Preservation comparator flagged a non-deterministic mount-array order.
5. (Secondary) BusyBox `wget` lacks `--max-time`; Tempo `-config.verify` needs a value.

## Remediation results

- Static validation: PASS (`Validate-DevelopmentBaseline.ps1`).
- Collector native `validate`: exit 0 (was 1).
- Runtime revalidation (new project, free ports, synthetic credentials):
  **21 checks, 21 PASS / 0 FAIL**. All nine localhost host ports now reachable;
  Collector starts/health/OTLP accepted; Prometheus ingest; Tempo retrieval;
  Grafana datasource health; full AMQP round-trip + negative tests; Postgres
  regression; Redis unpublished; Mailpit; SeaweedFS health.

## Historical FAIL dispositions

`historical-failure-traceability.json` maps every 002 FAIL/BLOCKED to a disposition:
all `RESOLVED_AND_REVALIDATED` except `LIR002-HARNESS-PULL-INTERRUPTED`, which is
`CONFIRMED_ENVIRONMENT_LIMITATION`. No UNRESOLVED or BLOCKED_BY_EXTERNAL_PREREQUISITE.

## Remaining limitations

- Egress isolation for published dev services is intentionally not provided after
  the networking correction (documented trade-off); segmentation, loopback binds,
  resource limits and no-privileged posture are unchanged.
- Runtime checks use short-lived synthetic observations and process restarts only;
  they do not establish hostile-host isolation, long-horizon retention, complete
  DLP, product IAM/RLS, production readiness or Runtime acceptance.
- SeaweedFS remains EXPERIMENTAL / DEV-ONLY; OD-017 unresolved.

## Cleanup and governance

All task-owned containers, networks and volumes were explicitly removed (no prune).
G-RUNTIME BLOCKED; FE-BE and AUTH/IAM authorization PENDING; offline PROHIBITED;
OD-013/014/015/017 OPEN; GS-01/GS-04 retained. No staging, commit or push.
