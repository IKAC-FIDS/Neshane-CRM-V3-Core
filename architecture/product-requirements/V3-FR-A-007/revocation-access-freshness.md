# Revocation and Access Freshness

Bounded product direction; not executable policy or grant.

Source: DEC-053/054; Option B; ADR-V3-004/005; OD-010/023

Principal suspension/disablement affects all access; session revocation affects dependent contexts; membership only affected Tenant; role removal affects rights; tenant suspension affects operating access; entitlement changes applicable feature. Unknown or stale security state cannot prove validity. Recovery and in-flight revalidation policy and exposure/latency bounds OPEN.

| ID | Direction |
|---|---|
| T07-D01 | Principal revocation |
| T07-D02 | Session revocation |
| T07-D03 | Membership revocation |
| T07-D04 | Role changes affect permissions |
| T07-D05 | Tenant suspension restricts access |
| T07-D06 | Scope revocation narrowly |
| T07-D07 | Preserve valid other Tenant access |
| T07-D08 | Validate security freshness |
| T07-D09 | Cache not authority |
| T07-D10 | Unexpired token insufficient |
| T07-D11 | Revalidate at approved control points |
| T07-D12 | Prevent revoked Context replay |
| T07-D13 | Fail closed unknown validity |
| T07-D14 | Assess in-flight effects |
| T07-D15 | Audit revocation under policy |
| T07-D16 | Sovereign local revocation |
| T07-D17 | No offline access |
| T07-D18 | Latency/freshness thresholds OPEN |
| T07-D19 | No invalidation/event mechanism choice |
| T07-D20 | Token/protocol independence |

