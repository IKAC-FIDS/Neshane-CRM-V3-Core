# Failure and Recovery

Bounded product direction; not executable policy or grant.

Source: FR-PF-001; support matrix §5/11; ADR-V3-003/004/005/010/012

Unavailable identity provider cannot establish new session without valid authentication; expired session requires approved reauthentication; invalid Principal/session/membership, suspended Tenant, mismatched Context, authorization uncertainty, invalid routing or stale state deny affected operation. Entitlement unavailability blocks dependent capability. Network partition cannot authorize offline continuation. Mandatory Audit failure cannot bypass obligation. Revalidate after recovery, no new membership/grants or resurrected revoked state; preserve tenant/cell boundaries.

| ID | Direction |
|---|---|
| T09-D01 | Fail closed security failures |
| T09-D02 | No bypass in outage |
| T09-D03 | No invalid Tenant/Cell fallback |
| T09-D04 | No invalid/stale security reliance |
| T09-D05 | Revalidate after recovery |
| T09-D06 | No resurrection of revoked access |
| T09-D07 | Preserve valid membership on recovery |
| T09-D08 | Preserve Tenant/Cell boundaries |
| T09-D09 | Audit obligation survives failure |
| T09-D10 | Common security across profiles |
| T09-D11 | Shared Application/RLS |
| T09-D12 | No implicit dedicated trust |
| T09-D13 | Sovereign local authority |
| T09-D14 | No offline continuation |
| T09-D15 | Positive/negative/recovery scenarios |
| T09-D16 | Independent profile evidence |
| T09-D17 | No unapproved SLA/RTO/RPO/freshness |
| T09-D18 | No unexecuted PASS |
| T09-D19 | No Gate change |
| T09-D20 | No recovery technology choice |

