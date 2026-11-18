# Customer failure scenarios — V3-FR-A-002

PROPOSED acceptance examples; not executed; not accepted.

| Scenario | Type | Required behavior | Status |
| --- | --- | --- | --- |
| CUS-CREATE with invalid/incomplete data | Validation failure | Reject; no authoritative record; no mandatory Audit event for rejection | PROPOSED |
| CUS-CREATE where Audit obligation cannot be durably recorded | Audit failure | Do not report success; do not commit mutation (DEC-012 p4) | APPROVED boundary, mechanics OPEN |
| CUS-UPDATE concurrent modification | Concurrency | Detect conflict; no silent overwrite (policy OPEN) | PROPOSED |
| Potential duplicate detection | Duplicate | Flag for review; no automatic merge (policy OPEN) | PROPOSED |
| Unauthorized operation | Authorization | Fail closed; Customer Domain denies; disclosure-safe | APPROVED invariant, matrix OPEN |
| Cross-tenant access attempt | Tenant isolation | Fail closed | APPROVED invariant |
| Invalid lifecycle transition | Lifecycle | Reject; no approved transition bypass | PROPOSED |
| Audit ingestion unavailable | Audit outage | Per DEC-013/014; no executable DURABLE_DEFER | OPEN |

Every scenario requires owner-approved examples before acceptance. See PDQ-002-06, PDQ-A001-049.

## Concurrency, race and idempotency (user-confirmed)

| Scenario | Required behavior | Status |
| --- | --- | --- |
| CUS-UPDATE stale record version | Reject without changing data; no auto-merge / last-write-wins | PROPOSED (CM1-PD-014) |
| Same Relationship updated with stale version | Reject stale version | PROPOSED (CM1-PD-038) |
| Concurrent creation of separate overlapping Relationships | Consistent authoritative overlap assessment; re-evaluate if conflict set changed | PROPOSED (CM1-PD-038) |
| Idempotent retry of Relationship create | No unintended additional Relationship record | PROPOSED (CM1-PD-039) |
| Intentional overlap vs accidental duplicate | Distinguished; exception requires reason | PROPOSED (CM1-PD-039) |
| Overlap exception vs Tenant isolation/validation | Exception never bypasses stale/tenant/validation/disclosure | PROPOSED (CM1-PD-040) |
| Mandatory coordinated Audit failure | Do not report successful mutation | APPROVED invariant (CM1-PD-051) |
| Stale provider result vs newer verification state | Stale result never overwrites newer state | PROPOSED (CM1-PD-051) |
