# V3-LOCAL-INFRA-001 — configuration evidence and boundaries

Reviewed 2026-11-18. Only HTTPS text/metadata was retrieved. No executables or image
layers were downloaded. Full fetched text/registry config metadata is retained in
the task's external local evidence folder, not treated as an external attestation.
`image-references.json` pins the actually resolved registry indexes, not guessed
versions. Major/minor tags were first inspected for PG_VERSION/REDIS_VERSION/
RABBITMQ_VERSION; the resulting exact tags were then independently resolved.

| Dependency | Authoritative source reviewed | Configuration consequence |
| --- | --- | --- |
| PostgreSQL | https://github.com/docker-library/docs/tree/master/postgres ; https://raw.githubusercontent.com/docker-library/postgres/master/docker-entrypoint.sh ; https://www.postgresql.org/docs/17/app-psql.html | Init scripts run only for an empty data directory; bootstrap is privileged. `psql` supports `\getenv`, ON_ERROR_STOP and TCP password authentication. Separate restricted login, no product schema. |
| Redis | https://redis.io/docs/latest/operate/oss_and_stack/management/config/ ; https://redis.io/docs/latest/develop/reference/eviction/ | AOF and 256mb/noeviction are development choices; noeviction refuses memory-growing writes, not container memory control. No host publication; dedicated internal network, no real/session data. |
| RabbitMQ | https://www.rabbitmq.com/docs/monitoring ; https://raw.githubusercontent.com/rabbitmq/rabbitmq-server/v4.2.9/deps/rabbit/docs/rabbitmq.conf.example | Check application running, local alarms and listener connectivity. Development management tag and vhost permissions are not product identities/topology. |
| SeaweedFS 4.50 | https://raw.githubusercontent.com/seaweedfs/seaweedfs/ec8f9793502c59ce3381cc4151bfc0806afd92e8/weed/command/mini.go ; https://raw.githubusercontent.com/seaweedfs/seaweedfs/ec8f9793502c59ce3381cc4151bfc0806afd92e8/weed/s3api/auth_credentials.go ; https://raw.githubusercontent.com/seaweedfs/seaweedfs/ec8f9793502c59ce3381cc4151bfc0806afd92e8/docker/entrypoint.sh | Exact pinned image labels identify this revision. `mini -dir`, bucket env, WEED_ADMIN_* fallback and AWS_ACCESS_KEY_ID/AWS_SECRET_ACCESS_KEY are source-backed. Disable unused WebDAV/Iceberg/Lance and telemetry. Internal admin `/health` is source-backed; host admin publication removed. |
| Mailpit | https://api.github.com/repos/axllent/mailpit/releases/latest ; https://mailpit.axllent.org/docs/configuration/runtime-options/ | Resolve v1.34.0, not latest. Registry image config itself declares `/mailpit readyz`. Bounded message count/age and disabled update check. |
| Collector 0.164.0 | https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.164.0/processor/filterprocessor/README.md ; https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.164.0/processor/transformprocessor/README.md ; https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.164.0/extension/healthcheckextension/README.md | Use current trace_conditions/metric_conditions syntax, explicit propagate errors, synthetic-only signals, attribute minimization, no logs/debug exporter, bounded retries/queue and internal health extension. Not a DLP/security identity system. |
| Prometheus 3.7.3 | https://raw.githubusercontent.com/prometheus/prometheus/v3.7.3/Dockerfile ; https://prometheus.io/docs/prometheus/latest/management_api/ | Busybox-derived image, `/-/ready`; local time/size retention. No admin/lifecycle API enabled. |
| Grafana 13.2.1 | https://raw.githubusercontent.com/grafana/grafana/v13.2.1/Dockerfile ; https://raw.githubusercontent.com/grafana/grafana/v13.2.1/conf/defaults.ini | Image tooling and preinstall/update settings reviewed; `/api/health` readiness, no anonymous/signup, no auto-install plugins or analytics. Admin env is initial setup, not credential rotation. |
| Tempo 3.1.1 | https://raw.githubusercontent.com/grafana/tempo/v3.1.1/example/docker-compose/single-binary/tempo.yaml ; https://raw.githubusercontent.com/grafana/tempo/v3.1.1/cmd/tempo/app/config.go ; https://raw.githubusercontent.com/grafana/tempo/v3.1.1/modules/backendworker/config.go ; https://raw.githubusercontent.com/grafana/tempo/v3.1.1/tempodb/config.go | Single binary/local storage; 3.x retention at backend_worker.compaction.block_retention, not old compactor key. No metrics generator/MCP server enabled by this configuration. Internal `/ready` requires later runtime observation. |

Some initial guessed source paths returned 404 and were replaced with the actual
version-specific source paths above. Current-source documentation and registry
correspondence do not prove native program configuration validation or runtime
compatibility. Those remain explicitly unexecuted in `runtime-validation-plan.md`.

Root authority remains `094c966de745285bd5a8d1975312eb06d930d4a8`:
ADR-007 permits PostgreSQL/RabbitMQ and justified tenant-safe Redis; service ownership
and ordinary runtime identities remain mandatory. This is not a product service
database, migration mechanism, RLS acceptance, production orchestrator or object
storage selection. OD-013/014/015/017 remain OPEN. G-RUNTIME BLOCKED; FE-BE and
AUTH/IAM authorization PENDING; offline continuation PROHIBITED; GS-01/GS-04 retained.
