# V3-LOCAL-INFRA-003 — remediation report

Only Local-Infra files necessary to correct verified defects were changed.
No 002 evidence, no historical observation, no image reference/digest, no service
definition beyond the two corrections, no product code and no architecture
decision were changed.

## Changed files

| File | Change | Reason |
| --- | --- | --- |
| `observability/otel-collector.yaml` | `filter/synthetic` rewritten to consistent Advanced OTTL object style | Defect 1 |
| `compose.yaml` | removed `internal: true` from postgres/broker/mail/telemetry; kept for redis; added explanatory comment | Defect 2 |
| `compose.seaweedfs.yaml` | removed `internal: true` from experimental | Defect 2 |
| `Validate-DevelopmentBaseline.ps1` | network invariant now "published => non-internal"; excludes reviews/ from baseline scan | Defect 2 consequence |
| `README.md` | networking section now documents segmentation (not egress isolation) and the internal/Redis exception | Defect 2 consequence |

The Collector filter correction preserves `error_mode: propagate`, the
synthetic-only resource-attribute gate, metric-name allowlist, span-event
dropping, attribute minimization, no logs pipeline and bounded retries/queue —
no filtering was removed to obtain startup. The networking correction preserves
loopback-only binds, per-group network segmentation, no privileged/host
networking/Docker-socket, resource limits and restart policy; it removes only the
egress-isolation flag that Docker Desktop cannot combine with host port
publication. No service was bound to 0.0.0.0 and no Docker Desktop/global or
host-firewall setting was changed.

## Static and native validation

- `Validate-DevelopmentBaseline.ps1`: **PASS** (YAML, two Compose models, 21
  template variables, 11 negative variable checks, 9 pinned image references,
  network/port/mount/resource boundaries, credential-placeholder and Git
  whitespace checks).
- Collector native `otelcol validate --config`: **exit 0** (was 1).
- Prometheus `promtool check config`: **exit 0** (unchanged).
- Tempo `-config.verify=true`: **exit 0** (unchanged; 002 harness flag corrected).

## Runtime revalidation (project `v3li003-reval-*`, free ports, synthetic creds)

21 checks, **21 PASS / 0 FAIL**, including: all nine localhost host ports now
reachable; Collector starts and reports internal health; synthetic OTLP metric and
trace accepted, Prometheus ingest (value 7, minimized), Tempo retrieval; Grafana
Prometheus/Tempo datasource health; full AMQP round-trip and negative tests;
PostgreSQL restricted-app regression; Redis still unpublished; Mailpit; SeaweedFS
internal health (`{"health":"ok"}` with corrected BusyBox timeout flag).

Full per-check evidence: `runtime-validation-matrix.json`; deterministic trace:
`historical-failure-traceability.json`; change rationale:
`configuration-change-matrix.json`.

G-RUNTIME remains BLOCKED. FE-BE and AUTH/IAM authorization PENDING. Offline
PROHIBITED. OD-013/014/015/017 OPEN; GS-01/GS-04 retained. This is a development
infrastructure baseline correction, not production readiness.
