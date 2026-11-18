# V3-LOCAL-INFRA-001 — proposed runtime validation, NOT authorized or executed

This is a plan, not new approved tasks/IDs, gate reassessment or production use.
Obtain a separate explicit runtime-validation authorization first. No current static
PASS implies any row below passed. Native binary config validation also remains
unexecuted: no images were pulled and no infrastructure executable was run.

## Preconditions

1. Review current static results and the exact baseline/files/images. Stop on an
   unresolved static failure or changed/unverified image/config.
2. Select a unique task-owned project name/host ports and NEW disposable volumes;
   verify that no unrelated resources use them. Do not reuse `neshane-local` or the
   original Local-Infra volumes, `.env`, Backend/Frontend resources or real data.
3. Use linux/amd64 and the pinned images only. Images must already be available
   with verified provenance acceptable to the authorized task. If absent, stop for
   separate download authorization; `up --pull never` is not a pull workaround.
4. Generate different synthetic credentials, protect the NEW ignored env file and
   avoid recording expanded config, environment arrays, keys, connection URLs or
   password-bearing SQL. No production/customer/session data, cloud access or host mounts.

## Proposed sequence and evidence

| Step | Proposed check | Required observation; stop on failure |
| --- | --- | --- |
| Native config validation | Use each pinned binary's documented validation mode where available: Collector `validate --config=...`, Prometheus promtool `check config`, and documented Tempo/Grafana checks | Native syntax/components/OTTL compile for the exact versions; inspect failures without exposing synthetic credential values. Do not replace a failed control with a weaker one. |
| Startup | Base startup command in README, no pull, task-owned project only | Expected containers, CPU/memory/PID limits and network/volume labels; no unintended egress/ports, root privileges or host socket access. |
| PostgreSQL | Inspect role attributes using authorized admin without logging credentials; connect via TCP as app, wrong-password rejection, try harmless forbidden role/schema administration | App login works; NOSUPERUSER/NOCREATEDB/NOCREATEROLE/NOREPLICATION/NOBYPASSRLS and no ownership/create privileges. No product table or RLS proof claimed. |
| Existing-volume behavior | In a newly created disposable test volume only, restart with configuration changes under a separately bounded test plan | No automatic credential rotation/init rerun; health failure for mismatched app password is preserved, no admin fallback. Never mutate an unrelated volume. |
| Redis | Task-owned container PING, inspect configured limits and planned synthetic-only use | No host listener; unauthenticated trust boundary limited to its own network. No tenant/session/cache correctness claim. |
| RabbitMQ | Diagnostics, allowed user/vhost login and denied out-of-scope access; inspect actual tag/permissions | Management tag, not administrator; correct vhost permissions, no product topology. |
| Readiness | All configured checks, plus independent probes of Collector :13133, Tempo :3200/ready and experimental admin :12535/health over their exact isolated networks | Do not invent shell/wget availability in distroless images. Use an already approved/pinned task-owned probe if needed; acquiring a new tool/image needs authorization. service_started is not healthy. |
| Telemetry | Tiny new synthetic metrics/traces with boolean marker; negative samples without marker, wrong metric name and synthetic event/attribute sentinels | Allowed metric/trace arrives, disallowed signals do not; minimization removes sentinel attributes/events/status text. Real data is forbidden even if filters appear to work. Verify no logs/debug payload export. |
| Retention/resources | Observe development retention, volume growth, log rotation, queue retry bounds and cgroup limits | No production retention/SLA inference. Stop on OOM, unbounded growth, stuck retries or silent data loss beyond explicitly disposable policy. |
| Optional SeaweedFS | Only after experiment-specific approval; source-confirmed flags, S3 signed tiny synthetic upload/read, wrong/missing-key rejection and internal health | Admin/master/filer/WebDAV ports are not host-published; only loopback S3. Auth behavior/volume restart proven only for this experiment, not OD-017 closure. |
| Shutdown/preservation | README down command, SAME project/file set, no volume deletion | Only task-created containers/networks stopped; volumes retained; original index/files, Backend and Frontend still match preservation snapshot. |

## Boundaries

Stop on any need for real credentials, production endpoints/data, broader host
privileges, unapproved dependencies, relaxed binds/TLS/security checks, unrelated
resource mutation or scope expansion. No automatic remediation, credential-policy
decision, staging/commit/push or phase progression. Record failures, skipped rows
and exact task-owned resource identities. G-RUNTIME stays BLOCKED; FE-BE/AUTH-IAM
authorization PENDING; OD-013/014/015/017 OPEN; offline PROHIBITED; GS-01/GS-04 retained.
