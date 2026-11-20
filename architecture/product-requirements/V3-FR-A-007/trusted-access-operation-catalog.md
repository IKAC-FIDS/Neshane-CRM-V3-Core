# Logical operation catalog

No new executable IDs or grants; names descriptive. All mutations require authorized owner, applicable Audit and concurrency; exact reason/event schemas OPEN.

| Operation family | Actor/owner | Input and prerequisite | Output or failure |
|---|---|---|---|
| Register Principal / link verified existing identity / activate | Authorized Identity Administrator; Identity Trust | Approved identity and mapping | Principal lifecycle; unknown linkage blocks |
| Provision Tenant / initialize administrator | Authorized Tenant provisioning authority; Tenant Management | Approved Tenant and bootstrap policy | Tenant state; missing prerequisite blocks |
| Invite / CreateMembership / ActivateMembership | Authorized Membership Administrator; Tenant Management | Valid Principal/Tenant, invitation policy | Membership; no duplicate nonterminal association |
| Suspend / Resume / RevokeMembership / UpdateMembershipValidity | Membership Administrator | Valid authorized membership/version | Updated state; no automatic revoked reactivation |
| Assign / RemoveMembershipRole | Membership Administrator | Authorized role and valid Tenant scope | Assignment change or deny escalation |
| ListPrincipalMemberships / ListTenantMembers / ValidateMembership | Authorized Principal or administrator | Valid identity and applicable access | Authorized results only |
| Select/SwitchTenant | Internal User | Valid session and destination membership | New validated Context or denial |
| Establish / Validate / RenewSession | Internal User; Identity Trust | Valid approved authentication/session | Valid session or deny |
| Terminate / RevokeSession / RevokeAllPrincipalSessions / ListPrincipalSessions | Principal or separately authorized administrator | Scoped session authority | Authorized outcome, affected context invalidation |
| RequireReauthentication | Identity Trust under approved policy | Protected action/session | Reauthentication requirement; no grant |
| Validate/RevalidateContext | Applicable trust boundary | Validated session, membership, Tenant, placement | Scoped Context or deny |
| AuthorizeResourceOperation | Owning Domain | Valid Context and relevant policy | Allow or deny; no implicit access |

Exact field rules, actor grants, transport/storage and operation-specific failure details remain OPEN.

