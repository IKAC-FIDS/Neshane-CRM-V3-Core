# Confirmed decision record

Farzad explicitly confirmed each group in conversation 2026-11-20; no exact issuance time or legal signature asserted. Bounded product direction, not executable security/architecture decision.

| ID | Direction | Source |
|---|---|---|
| T01-D01 | Stable unique Principal ID | DEC-053/054; FR-PF-001 Option B |
| T01-D02 | Separate Principal from Customer | DEC-053/054; FR-PF-001 Option B |
| T01-D03 | Separate Principal from Membership | DEC-053/054; FR-PF-001 Option B |
| T01-D04 | Multiple Tenant memberships | DEC-053/054; FR-PF-001 Option B |
| T01-D05 | Tenant-specific roles | DEC-053/054; FR-PF-001 Option B |
| T01-D06 | No automatic Membership from authentication | DEC-053/054; FR-PF-001 Option B |
| T01-D07 | Identity Trust owns Principal | DEC-053/054; FR-PF-001 Option B |
| T01-D08 | Tenant Management owns Membership | DEC-053/054; FR-PF-001 Option B |
| T01-D09 | Separate human and workload | DEC-053/054; FR-PF-001 Option B |
| T01-D10 | External Principal excluded now | DEC-053/054; FR-PF-001 Option B |
| T01-D11 | Anonymous cannot access Tenant | DEC-053/054; FR-PF-001 Option B |
| T01-D12 | No automatic Platform admin data access | DEC-053/054; FR-PF-001 Option B |
| T01-D13 | Independent business authorization | DEC-053/054; FR-PF-001 Option B |
| T01-D14 | Logical actor responsibilities only | DEC-053/054; FR-PF-001 Option B |
| T01-D15 | Local Sovereign authority | DEC-053/054; FR-PF-001 Option B |
| T02-D01 | Independent Tenant and Principal creation | DEC-053/054; FR-PF-001 |
| T02-D02 | Managed registration | DEC-053/054; FR-PF-001 |
| T02-D03 | Invitation support | DEC-053/054; FR-PF-001 |
| T02-D04 | Reuse verified existing Principal | DEC-053/054; FR-PF-001 |
| T02-D05 | No public self-registration | DEC-053/054; FR-PF-001 |
| T02-D06 | No automatic Membership on login | DEC-053/054; FR-PF-001 |
| T02-D07 | Independent Principal lifecycle | DEC-053/054; FR-PF-001 |
| T02-D08 | Independent Tenant lifecycle | DEC-053/054; FR-PF-001 |
| T02-D09 | Validate identity before activation | DEC-053/054; FR-PF-001 |
| T02-D10 | Authorized initial Tenant administrator | DEC-053/054; FR-PF-001 |
| T02-D11 | No access before prerequisites | DEC-053/054; FR-PF-001 |
| T02-D12 | Identity validates external mapping | DEC-053/054; FR-PF-001 |
| T02-D13 | No cross-Tenant disclosure in invitations | DEC-053/054; FR-PF-001 |
| T02-D14 | Audit administrative operations under policy | DEC-053/054; FR-PF-001 |
| T02-D15 | Entitlement independent | DEC-053/054; FR-PF-001 |
| T02-D16 | Local Sovereign onboarding | DEC-053/054; FR-PF-001 |
| T02-D17 | No IdP or provisioning technology choice | DEC-053/054; FR-PF-001 |
| T03-D01 | Tenant owns Membership | DEC-054; Option B |
| T03-D02 | Independent stable membership ID | DEC-054; Option B |
| T03-D03 | At most one nonterminal membership per Principal/Tenant | DEC-054; Option B |
| T03-D04 | Multiple Tenant memberships | DEC-054; Option B |
| T03-D05 | Independent lifecycle | DEC-054; Option B |
| T03-D06 | Permanent or time-limited membership | DEC-054; Option B |
| T03-D07 | Validate validity interval | DEC-054; Option B |
| T03-D08 | No operational access with inactive membership | DEC-054; Option B |
| T03-D09 | Suspend and resume | DEC-054; Option B |
| T03-D10 | Revoke | DEC-054; Option B |
| T03-D11 | No automatic reactivation after revoke | DEC-054; Option B |
| T03-D12 | Multiple roles per membership | DEC-054; Option B |
| T03-D13 | Tenant-specific roles | DEC-054; Option B |
| T03-D14 | Prevent privilege escalation | DEC-054; Option B |
| T03-D15 | Preserve membership/role history | DEC-054; Option B |
| T03-D16 | Audit under policy | DEC-054; Option B |
| T03-D17 | Concurrency control | DEC-054; Option B |
| T03-D18 | No ordinary physical deletion | DEC-054; Option B |
| T03-D19 | Independent of Entitlement and business authorization | DEC-054; Option B |
| T03-D20 | Sovereign local membership | DEC-054; Option B |
| T03-D21 | No executable grant or mechanism | DEC-054; Option B |
| T04-D01 | Selection after authentication | DEC-053/054; Option B |
| T04-D02 | Only valid memberships listed | DEC-053/054; Option B |
| T04-D03 | Auto-select single eligible Tenant | DEC-053/054; Option B |
| T04-D04 | Manual choice among multiple without valid default | DEC-053/054; Option B |
| T04-D05 | Default Tenant support | DEC-053/054; Option B |
| T04-D06 | Revalidate default | DEC-053/054; Option B |
| T04-D07 | Remember last used Tenant | DEC-053/054; Option B |
| T04-D08 | Tenant switching | DEC-053/054; Option B |
| T04-D09 | Validate Session | DEC-053/054; Option B |
| T04-D10 | Validate destination Membership | DEC-053/054; Option B |
| T04-D11 | Create new Context | DEC-053/054; Option B |
| T04-D12 | Evaluate destination roles | DEC-053/054; Option B |
| T04-D13 | No source privilege transfer | DEC-053/054; Option B |
| T04-D14 | Separate client state/cache | DEC-053/054; Option B |
| T04-D15 | Prevent old requests executing in new Tenant | DEC-053/054; Option B |
| T04-D16 | No existence disclosure | DEC-053/054; Option B |
| T04-D17 | Fail closed invalid destination | DEC-053/054; Option B |
| T04-D18 | Audit under policy | DEC-053/054; Option B |
| T04-D19 | Sovereign local authority | DEC-053/054; Option B |
| T04-D20 | No token/session mechanism choice | DEC-053/054; Option B |
| T05-D01 | Context from authoritative sources | Option B; ADR-V3-003/004/005; DEC-053/054 |
| T05-D02 | Bind valid Principal | Option B; ADR-V3-003/004/005; DEC-053/054 |
| T05-D03 | Bind valid Membership | Option B; ADR-V3-003/004/005; DEC-053/054 |
| T05-D04 | Bind valid Session | Option B; ADR-V3-003/004/005; DEC-053/054 |
| T05-D05 | Single Tenant per Context | Option B; ADR-V3-003/004/005; DEC-053/054 |
| T05-D06 | Client tenant selector untrusted | Option B; ADR-V3-003/004/005; DEC-053/054 |
| T05-D07 | Revalidate at trust boundaries | Option B; ADR-V3-003/004/005; DEC-053/054 |
| T05-D08 | Prevent tampering | Option B; ADR-V3-003/004/005; DEC-053/054 |
| T05-D09 | Immutable request context | Option B; ADR-V3-003/004/005; DEC-053/054 |
| T05-D10 | No unauthorized transfer | Option B; ADR-V3-003/004/005; DEC-053/054 |
| T05-D11 | Validate destination and Cell placement | Option B; ADR-V3-003/004/005; DEC-053/054 |
| T05-D12 | Validate freshness | Option B; ADR-V3-003/004/005; DEC-053/054 |
| T05-D13 | Fail closed invalid Context | Option B; ADR-V3-003/004/005; DEC-053/054 |
| T05-D14 | Independent business authorization | Option B; ADR-V3-003/004/005; DEC-053/054 |
| T05-D15 | Application isolation | Option B; ADR-V3-003/004/005; DEC-053/054 |
| T05-D16 | Shared SaaS PostgreSQL RLS | Option B; ADR-V3-003/004/005; DEC-053/054 |
| T05-D17 | Sovereign local authority | Option B; ADR-V3-003/004/005; DEC-053/054 |
| T05-D18 | No sensitive context logging | Option B; ADR-V3-003/004/005; DEC-053/054 |
| T05-D19 | No offline | Option B; ADR-V3-003/004/005; DEC-053/054 |
| T05-D20 | No transport/token selection | Option B; ADR-V3-003/004/005; DEC-053/054 |
| T06-D01 | Identity owns Session | DEC-053; Option B; OD-010 |
| T06-D02 | Unique independent Session ID | DEC-053; Option B; OD-010 |
| T06-D03 | Bind Principal | DEC-053; Option B; OD-010 |
| T06-D04 | Independent lifecycle | DEC-053; Option B; OD-010 |
| T06-D05 | Multiple concurrent sessions | DEC-053; Option B; OD-010 |
| T06-D06 | Absolute timeout | DEC-053; Option B; OD-010 |
| T06-D07 | Idle timeout | DEC-053; Option B; OD-010 |
| T06-D08 | Controlled renewal | DEC-053; Option B; OD-010 |
| T06-D09 | Logout | DEC-053; Option B; OD-010 |
| T06-D10 | Logout all | DEC-053; Option B; OD-010 |
| T06-D11 | Authorized revocation | DEC-053; Option B; OD-010 |
| T06-D12 | Authorized session inventory | DEC-053; Option B; OD-010 |
| T06-D13 | Prevent hijacking/replay | DEC-053; Option B; OD-010 |
| T06-D14 | Policy reauthentication | DEC-053; Option B; OD-010 |
| T06-D15 | Conditional step-up | DEC-053; Option B; OD-010 |
| T06-D16 | Independent Membership | DEC-053; Option B; OD-010 |
| T06-D17 | Independent business authorization | DEC-053; Option B; OD-010 |
| T06-D18 | Invalidate dependent Context | DEC-053; Option B; OD-010 |
| T06-D19 | Protect sensitive data | DEC-053; Option B; OD-010 |
| T06-D20 | Security Audit under policy | DEC-053; Option B; OD-010 |
| T06-D21 | Sovereign local session | DEC-053; Option B; OD-010 |
| T06-D22 | OD-010 storage/token OPEN | DEC-053; Option B; OD-010 |
| T07-D01 | Principal revocation | DEC-053/054; Option B; ADR-V3-004/005; OD-010/023 |
| T07-D02 | Session revocation | DEC-053/054; Option B; ADR-V3-004/005; OD-010/023 |
| T07-D03 | Membership revocation | DEC-053/054; Option B; ADR-V3-004/005; OD-010/023 |
| T07-D04 | Role changes affect permissions | DEC-053/054; Option B; ADR-V3-004/005; OD-010/023 |
| T07-D05 | Tenant suspension restricts access | DEC-053/054; Option B; ADR-V3-004/005; OD-010/023 |
| T07-D06 | Scope revocation narrowly | DEC-053/054; Option B; ADR-V3-004/005; OD-010/023 |
| T07-D07 | Preserve valid other Tenant access | DEC-053/054; Option B; ADR-V3-004/005; OD-010/023 |
| T07-D08 | Validate security freshness | DEC-053/054; Option B; ADR-V3-004/005; OD-010/023 |
| T07-D09 | Cache not authority | DEC-053/054; Option B; ADR-V3-004/005; OD-010/023 |
| T07-D10 | Unexpired token insufficient | DEC-053/054; Option B; ADR-V3-004/005; OD-010/023 |
| T07-D11 | Revalidate at approved control points | DEC-053/054; Option B; ADR-V3-004/005; OD-010/023 |
| T07-D12 | Prevent revoked Context replay | DEC-053/054; Option B; ADR-V3-004/005; OD-010/023 |
| T07-D13 | Fail closed unknown validity | DEC-053/054; Option B; ADR-V3-004/005; OD-010/023 |
| T07-D14 | Assess in-flight effects | DEC-053/054; Option B; ADR-V3-004/005; OD-010/023 |
| T07-D15 | Audit revocation under policy | DEC-053/054; Option B; ADR-V3-004/005; OD-010/023 |
| T07-D16 | Sovereign local revocation | DEC-053/054; Option B; ADR-V3-004/005; OD-010/023 |
| T07-D17 | No offline access | DEC-053/054; Option B; ADR-V3-004/005; OD-010/023 |
| T07-D18 | Latency/freshness thresholds OPEN | DEC-053/054; Option B; ADR-V3-004/005; OD-010/023 |
| T07-D19 | No invalidation/event mechanism choice | DEC-053/054; Option B; ADR-V3-004/005; OD-010/023 |
| T07-D20 | Token/protocol independence | DEC-053/054; Option B; ADR-V3-004/005; OD-010/023 |
| T08-D01 | Authentication independent | ADR-V3-005; DEC-053/054/018; Option B |
| T08-D02 | Membership independent | ADR-V3-005; DEC-053/054/018; Option B |
| T08-D03 | Entitlement independent | ADR-V3-005; DEC-053/054/018; Option B |
| T08-D04 | Owning Domain final authority | ADR-V3-005; DEC-053/054/018; Option B |
| T08-D05 | Shared Policy Governance | ADR-V3-005; DEC-053/054/018; Option B |
| T08-D06 | Deny by default | ADR-V3-005; DEC-053/054/018; Option B |
| T08-D07 | Least privilege | ADR-V3-005; DEC-053/054/018; Option B |
| T08-D08 | Policy separation of duties | ADR-V3-005; DEC-053/054/018; Option B |
| T08-D09 | Conceptual RBAC | ADR-V3-005; DEC-053/054/018; Option B |
| T08-D10 | Conceptual ABAC | ADR-V3-005; DEC-053/054/018; Option B |
| T08-D11 | Resource-level control | ADR-V3-005; DEC-053/054/018; Option B |
| T08-D12 | Field-level control | ADR-V3-005; DEC-053/054/018; Option B |
| T08-D13 | Independent operation authorization | ADR-V3-005; DEC-053/054/018; Option B |
| T08-D14 | No unlimited administrator access | ADR-V3-005; DEC-053/054/018; Option B |
| T08-D15 | Prevent escalation | ADR-V3-005; DEC-053/054/018; Option B |
| T08-D16 | Client permissions untrusted | ADR-V3-005; DEC-053/054/018; Option B |
| T08-D17 | Gateway not final authority | ADR-V3-005; DEC-053/054/018; Option B |
| T08-D18 | Independent privileged operation controls | ADR-V3-005; DEC-053/054/018; Option B |
| T08-D19 | Security Audit under policy | ADR-V3-005; DEC-053/054/018; Option B |
| T08-D20 | Sovereign local authority | ADR-V3-005; DEC-053/054/018; Option B |
| T08-D21 | No authorization engine chosen | ADR-V3-005; DEC-053/054/018; Option B |
| T08-D22 | No executable IAM grants | ADR-V3-005; DEC-053/054/018; Option B |
| T09-D01 | Fail closed security failures | FR-PF-001; support matrix §5/11; ADR-V3-003/004/005/010/012 |
| T09-D02 | No bypass in outage | FR-PF-001; support matrix §5/11; ADR-V3-003/004/005/010/012 |
| T09-D03 | No invalid Tenant/Cell fallback | FR-PF-001; support matrix §5/11; ADR-V3-003/004/005/010/012 |
| T09-D04 | No invalid/stale security reliance | FR-PF-001; support matrix §5/11; ADR-V3-003/004/005/010/012 |
| T09-D05 | Revalidate after recovery | FR-PF-001; support matrix §5/11; ADR-V3-003/004/005/010/012 |
| T09-D06 | No resurrection of revoked access | FR-PF-001; support matrix §5/11; ADR-V3-003/004/005/010/012 |
| T09-D07 | Preserve valid membership on recovery | FR-PF-001; support matrix §5/11; ADR-V3-003/004/005/010/012 |
| T09-D08 | Preserve Tenant/Cell boundaries | FR-PF-001; support matrix §5/11; ADR-V3-003/004/005/010/012 |
| T09-D09 | Audit obligation survives failure | FR-PF-001; support matrix §5/11; ADR-V3-003/004/005/010/012 |
| T09-D10 | Common security across profiles | FR-PF-001; support matrix §5/11; ADR-V3-003/004/005/010/012 |
| T09-D11 | Shared Application/RLS | FR-PF-001; support matrix §5/11; ADR-V3-003/004/005/010/012 |
| T09-D12 | No implicit dedicated trust | FR-PF-001; support matrix §5/11; ADR-V3-003/004/005/010/012 |
| T09-D13 | Sovereign local authority | FR-PF-001; support matrix §5/11; ADR-V3-003/004/005/010/012 |
| T09-D14 | No offline continuation | FR-PF-001; support matrix §5/11; ADR-V3-003/004/005/010/012 |
| T09-D15 | Positive/negative/recovery scenarios | FR-PF-001; support matrix §5/11; ADR-V3-003/004/005/010/012 |
| T09-D16 | Independent profile evidence | FR-PF-001; support matrix §5/11; ADR-V3-003/004/005/010/012 |
| T09-D17 | No unapproved SLA/RTO/RPO/freshness | FR-PF-001; support matrix §5/11; ADR-V3-003/004/005/010/012 |
| T09-D18 | No unexecuted PASS | FR-PF-001; support matrix §5/11; ADR-V3-003/004/005/010/012 |
| T09-D19 | No Gate change | FR-PF-001; support matrix §5/11; ADR-V3-003/004/005/010/012 |
| T09-D20 | No recovery technology choice | FR-PF-001; support matrix §5/11; ADR-V3-003/004/005/010/012 |
| T10-D01 | Farzad Business Owner | Roadmap A-007 AC-01–05; task-governance.md |
| T10-D02 | Record all decisions | Roadmap A-007 AC-01–05; task-governance.md |
| T10-D03 | Consolidate actor/operation catalogs | Roadmap A-007 AC-01–05; task-governance.md |
| T10-D04 | Trace FR-PF-001 Option B | Roadmap A-007 AC-01–05; task-governance.md |
| T10-D05 | Disposition eight requirement gaps | Roadmap A-007 AC-01–05; task-governance.md |
| T10-D06 | Independent profile cases | Roadmap A-007 AC-01–05; task-governance.md |
| T10-D07 | Preserve OPEN blockers | Roadmap A-007 AC-01–05; task-governance.md |
| T10-D08 | SHA-256 manifest | Roadmap A-007 AC-01–05; task-governance.md |
| T10-D09 | Core registration after separate authorization | Roadmap A-007 AC-01–05; task-governance.md |
| T10-D10 | Separate requirements from architecture/security/runtime acceptance | Roadmap A-007 AC-01–05; task-governance.md |

