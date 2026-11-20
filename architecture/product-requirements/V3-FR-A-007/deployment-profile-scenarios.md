# Deployment profile scenarios

| Profile | Authority | Isolation | Evidence |
|---|---|---|---|
| Shared SaaS | Approved Identity/Tenant authority | Application + PostgreSQL RLS | Initial synthetic Shared Cell only; actual paths pending |
| Dedicated Managed | Profile-approved identity and tenant authority | No implicit trust from dedicated infrastructure | Independent evidence pending |
| Dedicated Sovereign | Local final Identity/Tenant/revocation/Audit authority | Local validated context and domain authorization | Independent evidence pending; no offline bypass |

All profiles require valid Principal/session, active Membership, validated Context, destination authorization, applicable entitlement and required audit. No inherited runtime PASS. Local sovereign authority is not offline continuation. Every synthetic example in acceptance-criteria.md is independently applicable subject to approved profile policy; exact operational path and numeric policy OPEN.

