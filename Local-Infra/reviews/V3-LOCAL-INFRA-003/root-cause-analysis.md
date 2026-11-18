# V3-LOCAL-INFRA-003 — root cause analysis

Each finding is traced to authoritative evidence (rabbitmq framing source,
Collector filter processor documentation, deterministic A/B Docker test), not
inference. No historical evidence is modified.

## 1. NATIVE-COLLECTOR FAIL

**Evidence:** contrib 0.164.0 `otelcol validate --config` returned:
`'processors' error reading configuration for "filter/synthetic": configuring
multiple configuration styles is not supported`.

**Root cause:** `filter/synthetic` listed a flat string condition
(`'resource.attributes[...] != true'`, Basic style) alongside an object entry
(`{context: spanevent, conditions: [...]}`, Advanced style) in the same
`trace_conditions` list. The filter processor requires one style per list.

**Remediation:** converted every entry to the Advanced object form while keeping
the same OTTL predicates and the synthetic-only boundary. Verified native
validation exit 0, then runtime start/health/OTLP ingestion.

## 2. HOST-* failures (8 ports)

**Evidence:** `docker inspect ... .NetworkSettings.Ports` showed `{"5432/tcp":[]}`
for task containers on `internal:true` networks, while pre-existing containers on
the default bridge showed a real `127.0.0.1` binding. A controlled A/B test with
the same pinned image reproduced it: internal network => empty binding and host
unreachable; default network => binding present and host reachable.

**Root cause:** Docker Desktop (npipe engine) does not create the host port
binding for containers on `internal: true` bridge networks.

**Remediation:** removed `internal: true` from every network whose service
publishes a host port; kept it only for the unpublished Redis network. Loopback
binds, segmentation, resource limits and no-privileged posture are unchanged.
Container egress isolation for published services is no longer provided (documented).

## 3. RABBIT-AMQP / RABBIT-AMQP-CORRECTED-PROBE FAIL

**Evidence:** RabbitMQ server log verbatim:
`closing AMQP connection ... failed to negotiate connection parameters:
negotiated channel_max = 0 (no limit) is higher than the maximum allowed value (2047)`.
Credentials were separately proven valid (permissions `.*` on `neshane_dev`).

**Root cause:** the hand-rolled probe sent `connection.tune-ok` with
`channel_max = 0` (legacy "unlimited"), which RabbitMQ 4.x rejects. This was a
probe implementation defect, not a broker, credential or vhost defect.

**Remediation:** corrected client negotiates `channel_max = 2047` (and echoes the
server's offered values within limits). A full AMQP 0-9-1 round-trip (connect,
authenticate, open vhost, open channel, declare queue, publish persistent message,
basic.get consume, basic.ack) plus negative tests (invalid password => 403,
invalid vhost => 530) now passes.

## 4. PRESERVATION-DOCKER FAIL

**Evidence:** two long-running containers (`neshane-tempo`, `neshane-prometheus`)
showed a before/after difference only in the ORDER of their `mounts` arrays.

**Root cause:** `docker inspect` returns mounts in a non-deterministic order; the
strict array comparison in the 002 verifier flagged an ordering-only difference.

**Remediation:** deterministic comparator sorts mounts by a stable
(type, name/source, destination) key while preserving full mount attributes,
records raw-vs-sorted equality, and reports added/removed/changed mounts. It
confirms no actual change occurred and demonstrates detection of real changes.

## 5. LIR003-SEAWEED-HEALTH (initial revalidation FAIL)

**Evidence:** empty stdout, `wget: unrecognized option: max-time` (BusyBox
wget usage). Re-check with `-T 5` returned `{"health":"ok"}`.

**Root cause:** harness defect — BusyBox `wget` uses `-T SEC`, not `--max-time`.

**Remediation:** corrected the probe timeout flag; no configuration change.
