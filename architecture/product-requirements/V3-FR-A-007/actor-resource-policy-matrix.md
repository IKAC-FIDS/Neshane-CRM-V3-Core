# Logical actor/resource policy

| Actor | Resource scope | Limit |
|---|---|---|
| Internal User | Own identity/session and authorized memberships | No implicit business permissions |
| Tenant Owner/Administrator | Authorized tenant administration | No cross-tenant or automatic business access |
| Membership Administrator | Authorized memberships and role assignments | No escalation or other Tenant assignment |
| Identity Administrator | Authorized identity/session administration | No Membership or Domain grant |
| Security Administrator | Authorized security policy | No default resource bypass |
| Audit Reviewer | Independently authorized Audit evidence | No general business read |
| Platform Administrator | Infrastructure scope | No implicit Tenant data access |
| Workload Principal | Separate trust scope | Not included in internal human flow |
| Anonymous/external | No selected tenant access | External deferred |

Domain owner enforces resource/action/field policy. All roles are logical proposed responsibilities; exact actor binding and permission IDs OPEN.

