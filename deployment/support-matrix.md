# Neshane CRM V3 — First Release Deployment Support Matrix

## Document control

| Field | Value |
| --- | --- |
| Task | `V3-004 — First Release Support Matrix` |
| Phase / priority | `P00 / P0` |
| Status | `CLOSED — FIRST RELEASE SUPPORT MATRIX DESIGN BASELINE ONLY` |
| Review milestone | `R0` |
| Repository baseline | Root `main` at `9023c935f96df1d6ba0af3bc89979235c3592b02` before this file was created |
| Architecture | `NESHANE-V3-ARCH-P00-002`; ADR-V3-001 through ADR-V3-012 Accepted |
| Governance | `NESHANE-V3-GOV-P00-000A`; Level 1 task rules in `architecture/task-governance.md` |
| Prerequisites | V3-001 architecture baseline approved; V3-003 closed in analytical scope by `CDR-V3-003-2026-1030` |
| Readiness effect | Product-architecture support definition only; no Implementation, Security or Production Readiness evidence |

No repository-local roadmap file defining V3-004 was present at the verified baseline. The explicit authorized `TASK_ID = V3-004` and acceptance boundary supplied for this task are therefore the task definition. This file creates no new Task ID or architecture decision.

## 1. Classification vocabulary

| Classification | Meaning in this document |
| --- | --- |
| `SUPPORTED IN FIRST RELEASE` | Approved target-state commitment for the first supported production release. It does not mean the capability is currently implemented, deployable or operationally ready. |
| `CONDITIONALLY SUPPORTED` | Support is bounded by stated prerequisites, approved policy or profile evidence that is not yet complete. |
| `DEFERRED` | Explicitly outside FIRST_RELEASE and reserved for a later approved release. |
| `NOT SUPPORTED` | Excluded from the current support commitment. |
| `PENDING DECISION` | Support cannot be committed until the referenced Open Decision or named authority resolves it. |

Product commitment, design assumption and evidence status are independent. A profile or capability classified `SUPPORTED IN FIRST RELEASE` remains unavailable for production use until its implementation, security and profile-specific operational evidence passes the applicable later gates.

| Independent status dimension | Current state |
| --- | --- |
| Approved FIRST_RELEASE target scope | Defined by the approved fifteen-entry inventory and the three required deployment profiles |
| Current implementation availability | `NOT VERIFIED` |
| Formal R0 Product authority disposition | `APPROVED — CPO; FIRST_RELEASE TARGET SCOPE` |
| R0 Design Consistency Acceptance by Technical Architecture Owner | `APPROVED — CPO IN DUAL PROJECT ROLE` |
| Production Readiness | `NOT ESTABLISHED` |

## 2. Common obligations for all supported profiles

The following approved invariants apply to Shared SaaS, Dedicated Managed and Dedicated Sovereign without weakening:

1. Tenant identity is stable and does not encode cell, database or physical placement.
2. Tenant Context is established from authenticated and validated provenance; client tenant values are selectors only. Missing, conflicting or invalid context fails closed.
3. The resource-owning Domain makes and enforces final resource/action authorization. Identity, Membership, Entitlement, Assignment, gateway routing or physical dedication is not authorization.
4. Each Service owns its Business Facts, schema, migrations, credentials and transaction boundary. Cross-service SQL, shared ORM entities and private-database access are prohibited.
5. Shared tenant-aware persistence requires application authorization, tenant-scoped constraints, PostgreSQL RLS and ordinary runtime roles that cannot bypass isolation. Dedicated placement does not remove compatible logical Tenant and Domain authorization semantics.
6. Control Plane operational intent does not grant Data Plane Business authority. Privileged operations require limited identity, explicit Tenant/Platform scope, destination-Domain authorization and durable Audit.
7. User, Workload, Operator and Plugin Installation identities remain distinct. User or Workload identity must be authenticated at every Service trust boundary, including validation of the approved issuer/trust source, intended audience, expiry and required claims. Internal network location, broker delivery or Central identity is not trust by itself. The final identity protocol and credential technology remain unresolved.
8. APIs and events are owned, versioned and compatibility-governed. Breaking evolution requires an approved version/coexistence/deprecation path.
9. Release, upgrade, rollback, backup/restore, observability, security operation and recovery require independent evidence for each profile.
10. Numeric SLA, SLO, RTO, RPO, MTD, latency, capacity, throughput, freshness and disconnected-duration targets remain unresolved under `OD-023`.

## 3. Profile support summary

The matrix separates approved architectural authority boundaries from operating-responsibility allocations. The CPO accepts the detailed customer/provider/operator allocation below as the R0 Product support model only. It is not a contract, SLA, implemented operating model or Production Readiness commitment. The Technical Architecture Owner accepts its consistency with the approved architecture only within the bounded R0 scope recorded in section 11.

| Support concern | Shared SaaS | Dedicated Managed | Dedicated Sovereign |
| --- | --- | --- | --- |
| Profile commitment | `SUPPORTED IN FIRST RELEASE` — multi-tenant provider-managed cells | `SUPPORTED IN FIRST RELEASE` — dedicated placement with managed operations | `SUPPORTED IN FIRST RELEASE` — locally authoritative Control Plane and independently operating Data Plane |
| Deployment boundary | Multiple Tenants share managed cell infrastructure; Service/Data ownership remains private by logical boundary | Dedicated placement for the customer; Service/Data ownership and contract boundaries remain unchanged | Customer/Sovereign-local environment; local Control Plane, Data Plane, trust, secrets, Audit and operations are authoritative |
| Operational authority | Authorized provider operations within approved privileged boundaries | Authorized managed operator/provider within the customer-specific dedicated boundary and agreed support model | Sovereign-local authorized operators have final security and operational authority; Central has no implicit administrative right |
| Tenant isolation | Validated Tenant Context, Domain authorization, tenant constraints, PostgreSQL RLS and non-bypass roles are mandatory | Physical dedication plus validated Tenant Context and Domain authorization; physical separation is not an authorization substitute; RLS/integration details remain `OD-014` where applicable | Local Tenant Context and Domain authorization remain mandatory; physical/local custody does not create implicit access; RLS details remain profile/service design evidence |
| Control Plane | Provider-managed Control Plane may manage placement, lifecycle and operational intent | Centrally managed capabilities may manage the dedicated placement under explicit scope | Locally authoritative Control Plane; Central interaction only through locally approved, authenticated and policy-controlled federation |
| Data Plane | Provider-operated cells execute Business APIs/events under Service/Tenant authorization | Dedicated Data Plane executes the same compatible business contracts | Independently operating local Data Plane; critical local operations must not require synchronous Central availability |
| Identity/trust dependency | Approved issuer/trust, audience, lifecycle and Tenant association are required; exact IdP/session/workload mechanisms remain Open | Same logical requirements; dedicated network/location is not identity | Local trust roots, credential lifecycle, validation and revocation authority are required; Central assertion creates no automatic local Principal or access |
| Proposed provider/operator responsibility | Cell/platform operation, authorized deployment, observability, recovery process and incident coordination; no Business Fact ownership | Managed dedicated infrastructure, authorized release/upgrade/recovery and support access; no universal Domain authority | Approved artifacts and support interfaces only under local policy; no unapproved Central operation or data access |
| Proposed customer responsibility | Tenant administration, authorized users, business configuration/data stewardship and incident cooperation within approved contracts | Same, plus agreed dedicated-environment coordination and customer-side dependencies | Local trust/credential custody, authorized operators, local policy, connectivity/federation approval, local recovery and physical/environmental dependencies |
| Online connectivity assumption | Online client/service connectivity is assumed for supported Business Journeys | Connectivity to the dedicated service is assumed; Central-management disconnection behavior is not yet committed | Local client-to-local service connectivity is assumed; Central connectivity is optional for critical local operation but exact disconnected scope is unresolved |
| Client offline operation | `NOT SUPPORTED` — no offline client/data synchronization commitment | `NOT SUPPORTED` — no offline client/data synchronization commitment | `NOT SUPPORTED` unless separately approved; Sovereign-local operation is not an offline-client feature |
| Central disconnection | `PENDING DECISION` for Control Plane failure/degraded behavior; no universal offline claim | `PENDING DECISION`; continued dedicated Data Plane behavior and management limitations require profile design/evidence | `CONDITIONALLY SUPPORTED` for approved critical local operations; operation catalog, duration, capacity, reconciliation and evidence remain pending |
| Full Air Gap | `NOT SUPPORTED` | `NOT SUPPORTED` | `PENDING DECISION` under `OD-001`; not implied by Sovereign |
| Audit obligation | FIRST_RELEASE Audit Core applies; Producing Domains retain Business Facts and Audit owns authoritative Audit records | Same, with dedicated operational evidence | Same under local Audit authority; Central acknowledgement cannot replace required local Audit evidence |
| Upgrade/rollback | Required as a profile-specific operational contract; implementation/evidence not verified | Required independently for dedicated placement; implementation/evidence not verified | Local authorized promotion, upgrade and rollback required; artifact import/custody process remains unresolved |
| Backup/recovery | Required; tested RTO/RPO and restore evidence absent | Required per dedicated environment; objectives/evidence absent | Local backup/restore and recovery authority required; no Central substitution; objectives/evidence absent |
| Support escalation | Provider support → owning Service/Domain → Security/Operations where applicable | Dedicated operations → owning Service/Domain → Security/customer coordination | Local Sovereign Operations first; locally approved provider escalation; Security/Domain authority retained locally |
| Production readiness | `NOT ESTABLISHED` | `NOT ESTABLISHED` | `NOT ESTABLISHED` |

## 4. Profile obligations, dependencies, offline claims and exclusions

### 4.1 Shared SaaS

**Obligations**

- Enforce Tenant Context and owning-Domain authorization before tenant-aware work.
- Apply PostgreSQL RLS, tenant-scoped constraints and non-owner/non-bypass runtime roles to shared tenant-aware tables.
- Prevent cross-Tenant leakage through APIs, events, logs, caches, search/report projections, File access and operational visibility.
- Preserve independent Service ownership, schema/migration ownership and versioned contracts inside shared cells.
- Maintain provider-side privileged-operation scope and durable Audit evidence.

**Dependencies**

- Provider-operated cell lifecycle, placement/routing and compatible Service releases.
- Approved Identity/Tenant foundations and resource-owning Domain authorization.
- Profile-specific observability, incident, backup/restore, upgrade and rollback evidence.

**Offline claim**

Shared SaaS is an online service profile. No offline client workflow, disconnected Tenant replica or guaranteed operation during unavailable provider Control/Data Plane is committed.

**Exclusions**

- Full Air Gap and customer-operated platform authority.
- Direct Tenant database access or bypass roles.
- Numeric availability/recovery commitments before `OD-023`.

### 4.2 Dedicated Managed

**Obligations**

- Preserve all logical Tenant, Service, contract and authorization boundaries despite physical dedication.
- Restrict provider operational access by identity, customer/environment scope, destination authorization and Audit.
- Provide independent dedicated-environment release, upgrade, rollback, backup/restore and observability evidence.
- Prevent dedicated infrastructure from becoming a shared Business authority or shared database boundary.

**Dependencies**

- Centrally managed capabilities with explicit scope and authenticated trust.
- Customer-specific networking, identity integration and operational coordination.
- Runtime orchestration, secrets and recovery choices still governed by `OD-012`, `OD-015` and `OD-023`.

**Offline claim**

Dedicated Managed does not automatically promise continued operation while Central management, provider connectivity or external identity dependencies are unavailable. Any such degraded mode is `PENDING DECISION` and requires explicit failure semantics and evidence.

**Exclusions**

- Sovereign-local final authority.
- Full Air Gap.
- Implicit privileged access based on provider identity or network location.
- Guaranteed failover/recovery without tested profile evidence.

### 4.3 Dedicated Sovereign

**Obligations**

- Maintain locally authoritative trust, secrets, policy, grants, Audit, plugin lifecycle, release/recovery authority and critical business/security operation.
- Reject implicit Central administration and validate every locally accepted Central/federation input for authentication, scope, Tenant provenance and policy approval.
- Ensure critical local operations have no mandatory synchronous Central dependency.
- Preserve both evidence views and provenance during reconnection conflict; no automatic `CENTRAL_WINS`, `LOCAL_WINS` or `LAST_WRITER_WINS` rule is approved.
- Produce local install, upgrade, rollback, backup/restore, observability, security-operation and recovery evidence.

**Dependencies**

- Local identity/trust and credential lifecycle, local authorized operations and local Audit.
- A future approved Critical Local Operation Catalog.
- Profile-specific release/import, capacity, time, licensing, reconciliation and recovery designs.

**Offline claim**

Central-disconnected operation is `CONDITIONALLY SUPPORTED` only for critical local operations that are explicitly approved and whose required local dependencies remain valid. No duration, capacity or universal offline behavior is approved. Loss of required local trust, durability, visibility, integrity or recovery authority fails closed for the affected path.

**Exclusions**

- Full Air Gap without resolution of `OD-001`.
- Central acknowledgement as a substitute for local authority or local evidence.
- Automatic reconnection conflict winner.
- Guaranteed recovery, continuity duration or capacity without tested evidence.

## 5. FIRST_RELEASE capability coverage

The classifications below are product-scope commitments, not implementation evidence. Unless a row says otherwise, the approved logical capability applies across all three supported profiles with compatible business semantics and profile-specific operational evidence.

| Stable ID | Capability / journey | Shared | Dedicated Managed | Dedicated Sovereign | Boundary or condition |
| --- | --- | --- | --- | --- | --- |
| `FR-BJ-001` | Register and Maintain Customer Master | `SUPPORTED IN FIRST RELEASE` | `SUPPORTED IN FIRST RELEASE` | `SUPPORTED IN FIRST RELEASE` | Customer Domain owns Customer Master and authorization |
| `FR-BJ-002` | Find and Review Customer | `SUPPORTED IN FIRST RELEASE` | `SUPPORTED IN FIRST RELEASE` | `SUPPORTED IN FIRST RELEASE` | Business search only; no search engine selection |
| `FR-BJ-003` | Manage Opportunity Through the Sales Pipeline | `SUPPORTED IN FIRST RELEASE` | `SUPPORTED IN FIRST RELEASE` | `SUPPORTED IN FIRST RELEASE` | Sales owns Opportunity/Pipeline/Stage/amount-currency; detailed rules pending |
| `FR-BJ-004` | Register and Process a Customer Request | `SUPPORTED IN FIRST RELEASE` | `SUPPORTED IN FIRST RELEASE` | `SUPPORTED IN FIRST RELEASE` | No Portal or general Workflow Engine dependency |
| `FR-BJ-005` | Plan and Track a Work Task | `SUPPORTED IN FIRST RELEASE` | `SUPPORTED IN FIRST RELEASE` | `SUPPORTED IN FIRST RELEASE` | Manual contract-based links; linked resource authorization remains independent |
| `FR-PF-001` | Establish Trusted Tenant Access | `SUPPORTED IN FIRST RELEASE` | `SUPPORTED IN FIRST RELEASE` | `SUPPORTED IN FIRST RELEASE` | Option B approved: minimum trusted access for internal authenticated Principals, active Membership validation, valid/revalidated Tenant Context, valid destination Membership for Tenant switching and independent owning-Domain authorization; detailed identity/session choices remain pending |
| `FR-PF-002` | Evaluate Feature Eligibility | `SUPPORTED IN FIRST RELEASE` | `SUPPORTED IN FIRST RELEASE` | `SUPPORTED IN FIRST RELEASE` | Eligibility is not Membership or Business Authorization; Sovereign evaluation is local |
| `FR-PF-003` | Enforce Quota-Controlled Operation | `SUPPORTED IN FIRST RELEASE` | `SUPPORTED IN FIRST RELEASE` | `SUPPORTED IN FIRST RELEASE` | Each capability-to-Quota integration needs separate approval |
| `FR-PF-004` | Deliver Authorized In-App Notification | `SUPPORTED IN FIRST RELEASE` | `SUPPORTED IN FIRST RELEASE` | `SUPPORTED IN FIRST RELEASE` | Core + In-App only; Email/SMS/Push deferred |
| `FR-PF-005` | Attach and Retrieve File for an Approved Resource | `SUPPORTED IN FIRST RELEASE` | `SUPPORTED IN FIRST RELEASE` | `SUPPORTED IN FIRST RELEASE` | Dual File/resource authorization; storage/scanning/retention choices pending |
| `FR-PF-006` | Produce an Approved Deterministic Report | `SUPPORTED IN FIRST RELEASE` | `SUPPORTED IN FIRST RELEASE` | `SUPPORTED IN FIRST RELEASE` | Reporting Core only; each Report Set and authorization requires approval |
| `FR-SO-001` | Record Security, Administrative and Privileged Audit Evidence | `SUPPORTED IN FIRST RELEASE` | `SUPPORTED IN FIRST RELEASE` | `SUPPORTED IN FIRST RELEASE` | Audit Core; catalog/retention/integrity mechanics incomplete |
| `FR-SO-002` | Review Authorized Audit Evidence | `SUPPORTED IN FIRST RELEASE` | `SUPPORTED IN FIRST RELEASE` | `SUPPORTED IN FIRST RELEASE` | Audit Domain authorizes Audit resources; disclosure rules incomplete |
| `FR-SO-003` | Observe Platform and Service Health | `SUPPORTED IN FIRST RELEASE` | `SUPPORTED IN FIRST RELEASE` | `SUPPORTED IN FIRST RELEASE` | Operational Core obligation; signal/readiness catalog pending |
| `FR-SO-004` | Execute an Authorized Privileged Operation | `SUPPORTED IN FIRST RELEASE` | `SUPPORTED IN FIRST RELEASE` | `SUPPORTED IN FIRST RELEASE` | Destination Domain authorization and Audit required; no generic Admin authority |

## 6. Deferred and excluded capability scope

| Capability | Classification | Boundary |
| --- | --- | --- |
| Product Catalog, Lead Source, Pain Point and Use Case | `DEFERRED` | LATER_RELEASE requirements and ownership remain separate |
| Email, SMS and Push Notification | `DEFERRED` | Provider, credential, contract and delivery policy decisions required |
| Customer Portal and external customer workspace | `DEFERRED` | External Principal, trust/session and resource-contract decisions required |
| Technical Knowledge and University reference capability | `DEFERRED` | Lifecycle, classification, access, search and retention decisions required |
| AI-generated Insights, Assistant and Business Action Proposals | `DEFERRED` | No autonomous Business Write; future explicit approval/re-authorization model required |
| Advanced Analytics and Custom Report Builder | `DEFERRED` | Reporting Core does not imply these capabilities |
| Meetings, Timesheets, Personal Todos and Advanced Collaboration | `DEFERRED` | Separate requirements and ownership required |
| Public File Sharing, Advanced Versioning, Media Processing and Advanced Generated Artifacts | `DEFERRED` | Separate security, ownership and lifecycle decisions required |
| General Administration UI, Advanced Operational Dashboard, Bulk Import, Email Administration and Advanced Remediation | `DEFERRED` | Operational Core does not create a universal Admin surface |
| Offline client synchronization | `NOT SUPPORTED` | No approved client-side offline data/merge contract |
| Full Air Gap | `PENDING DECISION` | `OD-001`; Dedicated Sovereign does not imply Air Gap |

## 7. Audit and DURABLE_DEFER boundary

Audit Core is a FIRST_RELEASE commitment, but Audit lifecycle, retention, integrity implementation and operation-specific failure semantics require their later approved gates.

DEC-014 applies only to the covered mandatory Audit publication obligations for authoritative `CUS-CREATE` and `CUS-UPDATE` mutations. It preserves five foundational restrictions:

1. valid Customer authorization, authoritative Tenant Context and durable Customer-owned mutation/obligation evidence are prerequisites;
2. obligation creation, durable recording, publication attempts, broker delivery and authoritative Audit ingestion evidence remain distinct;
3. recoverability, trustworthy backlog visibility, reconciliation ownership and escalation are required, and indeterminate evidence suspends deferred eligibility;
4. invalid Tenant, integrity, provenance or recovery evidence cannot qualify and must fail closed for the deferred path;
5. Dedicated Sovereign eligibility relies on locally valid evidence and authority, not Central substitution.

This matrix does not approve executable or unconditional `DURABLE_DEFER`, universal continuation during Audit outage, automatic restoration, numeric backlog/deferral limits or a complete Audit Event Catalog.

## 8. Air Gap boundary

`Dedicated Sovereign` means local final security and operational authority with Central-disconnected capability for approved critical local operations. It does not mean `Full Air Gap`.

Full Air Gap remains `PENDING DECISION` under `OD-001`. A future support commitment must separately decide and validate at least:

- offline release and update distribution, artifact provenance and rollback;
- licensing or entitlement operation without Central dependency;
- local identity, workload credentials, key custody, rotation and revocation;
- trusted time synchronization and behavior under time uncertainty;
- local Audit retention, integrity verification, export and incident handling;
- backup/restore, recovery media and disaster-recovery authority;
- vulnerability/advisory intake and supply-chain response;
- capacity and maximum disconnected duration;
- federation/import/export data classes and reconnection conflict governance.

No Air Gap support commitment, implementation or readiness claim is created by V3-004.

## 9. Open decisions and required milestones

| Decision | Support impact | Existing owner | Required milestone | Current effect |
| --- | --- | --- | --- | --- |
| `OD-001` | Full Air Gap and isolated release/trust flows | Architecture + Sovereign Operations + Security | Before an Air-Gapped commitment | Air Gap remains `PENDING DECISION` |
| `OD-002` | Java toolchain baseline | Backend Architecture | Before Backend build initialization | No compiler/toolchain support baseline selected |
| `OD-003` | Spring Boot stable line | Backend Architecture | Before Backend build initialization | No dependency/runtime line selected |
| `OD-004` | Build system and project layout | Backend Architecture + Developer Experience | Before Backend build initialization | No reproducible Backend build layout selected |
| `OD-007` | Public API/BFF strategy | API Architecture + Backend/Frontend owners | Before first public contract | No public composition boundary committed |
| `OD-008` | API/event versioning and coexistence mechanics | API + Event Architecture | Before first published contract/event | No detailed compatibility mechanism committed |
| `OD-009` | IdP integration | Identity + Security + Product | Before production authentication | Identity foundation required; provider selection pending |
| `OD-010` | Session lifecycle and revocation | Identity + Security | Before production session implementation | Session/refresh/revocation behavior pending |
| `OD-011` | Workload identity | Security + Platform Operations | Before production service-to-service trust | Service trust protocol pending |
| `OD-012` | Secrets and key custody | Security + Operations + Sovereign owner | Before production credential storage/signing | Profile-specific secret/key mechanism pending |
| `OD-013` | PostgreSQL migration tooling | Data Architecture | Before first schema migration | Migration mechanism pending |
| `OD-014` | Java/RLS integration | Data + Security + Backend Architecture | Before first tenant-aware repository | Transaction/context binding mechanism pending |
| `OD-015` | Runtime orchestration and profile deployment | Platform Operations + Architecture | Before deployment implementation | No runtime/orchestrator commitment |
| `OD-017` | Object storage | Data + Operations + Security | Before File/Content capability implementation | File Core scope does not select storage |
| `OD-018` | Search/indexing | Data Architecture + owning Domains | Before search-dependent feature | Customer business search does not select an engine |
| `OD-019` | Durable scheduling/recovery mechanics | Backend Architecture + Operations | Before durable scheduled workflows | No scheduler or recovery technology approved |
| `OD-020` | Contract testing | API/Event Architecture + Quality | Before first released contract | Compatibility evidence mechanism pending |
| `OD-022` | Tenant placement migration | Cell Management + Data + Security | Before tenant placement migration is supported | Migration automation/support remains pending |
| `OD-023` | SLO/RTO/RPO/capacity and measurement | Product + Operations + Security + Service owners | Before Production Architecture Sign-off | No numeric support guarantee |

All `OD-001..023` remain Open; omission from this impact table does not close or deprioritize an Open Decision.

## 10. Support and escalation responsibilities

| Event | First responsible boundary | Required escalation |
| --- | --- | --- |
| Business-operation denial or data correctness | Resource-owning Domain | Domain owner; Security if trust/Tenant/authorization is implicated |
| Tenant isolation or cross-Tenant concern | Owning Service + Security | Tenant Security, Data/Security authority and incident process |
| Identity/session/workload trust failure | Identity/Platform Security | Affected Domain and profile Operations; fail closed |
| Cell placement/routing problem | Cell/Operational Platform | Affected Service owners and customer operations |
| Audit obligation/ingestion discrepancy | Producing Domain + Audit Domain | Messaging/Operations/Security according to evidence state; no fabricated success |
| Shared SaaS platform incident | Provider Operations | Service/Security/Product escalation according to affected scope |
| Dedicated Managed incident | Dedicated Operations | Customer coordination plus affected Service/Security owner |
| Dedicated Sovereign incident | Sovereign-local Operations | Local Security/Domain authority; provider only through locally approved support path |
| Reconnection conflict | Sovereign-local authority + affected evidence owners | Contract/Messaging/Security review; preserve both views and provenance |
| Supply-chain/artifact concern | Release/Supply-chain owner | Profile Operations + Security; stop unauthorized promotion |

No response-time, restoration-time or escalation-time guarantee is approved.

## 11. R0 Product and Design Consistency review requirements

The focused R0 analysis is complete. The CPO Product disposition and the Technical Architecture Owner Design Consistency Acceptance are recorded below. V3-004 is Closed only for the First Release Support Matrix design baseline.

### Product review

**Disposition:** `APPROVED — CPO; FIRST_RELEASE TARGET SCOPE`

**Decision source:** Explicit CPO confirmation in the project conversation; no signature, reviewer account, organizational artifact or approval date is claimed.

The Product disposition approves:

1. Shared SaaS, Dedicated Managed and Dedicated Sovereign as first-release target profiles.
2. All fifteen existing FIRST_RELEASE capability mappings.
3. `FR-PF-001 = OPTION B — MINIMUM TRUSTED TENANT ACCESS`, limited to:
   - internal authenticated Principals;
   - active Membership verification;
   - valid and revalidated Tenant Context;
   - Tenant switching only with valid destination Membership;
   - access to protected FIRST_RELEASE capabilities; and
   - independent Resource-owning Domain authorization for every operation.
4. The customer/provider/managed-operator allocation in section 3 as an R0 Product model, not a contractual commitment.
5. The exclusions in section 6 and the bounded carry-forward in section 9.

The Product disposition does not approve Customer Portal or external customer users; a named IdP, SSO, Passkey or protocol; token/session/refresh technology; Tenant administration UI; unapproved Membership policy details; implicit authorization from Authentication, Membership or Entitlement; numeric SLA or offline guarantees; implementation availability; or Production Readiness.

### Security consistency analysis

The bounded Codex assessment is technical analysis, not Security Authority approval:

| Security concern | Assessment | Basis or carry-forward |
| --- | --- | --- |
| Validated/revalidated Tenant Context and fail-closed denial | `NONBLOCKING` | Represented in sections 2, 3 and the approved `FR-PF-001` boundary |
| Resource-owning Domain authorization | `NONBLOCKING` | Remains independent for every operation; no identity, Membership or Entitlement grants implicit access |
| Tenant isolation and RLS defense in depth | `NONBLOCKING` | Shared profile retains application authorization, tenant constraints, RLS and non-bypass roles |
| User, Workload, Operator and Plugin identity separation | `NONBLOCKING` | Distinct identities and Service-boundary validation are explicit |
| Dedicated Sovereign local final authority | `NONBLOCKING` | No synchronous Central dependency or implicit Central administrative right is introduced |
| DEC-014 five principles | `NONBLOCKING` | Section 7 preserves scope, evidence separation, recovery/visibility, integrity/provenance and Sovereign-local eligibility |
| Full Air Gap | `NONBLOCKING` | Remains a separate pending decision under `OD-001` |
| Executable `DURABLE_DEFER`, runtime assurance and Production approval | `NONBLOCKING` | Explicitly not approved |
| IdP/session/workload/secrets/RLS integration and deployment mechanics | `DEFERRED TO EXISTING OPEN DECISION` | `OD-009..015`; V3-004 makes no technology or runtime claim |
| Technical Architecture Owner Design Consistency Acceptance | `NONBLOCKING — APPROVED` | The CPO, acting in the declared dual project role of Final Technical Architecture Owner, approves the bounded design consistency baseline |
| Specialist and independent Security reviews | `DEFERRED TO EXISTING FUTURE GATES` | `AUTH-IP`, `AUTH-TS`, `AUTH-SS`, `AUTH-SA` and `AUTH-ISR` remain unassigned/not verified and are not satisfied by this route |

No substantive contradiction between the approved Product Scope and the existing security invariants was found. Codex analysis remains supporting evidence only.

### Technical Architecture Owner R0 acceptance

```text
TECHNICAL_ARCHITECTURE_OWNER = CPO (dual role)
DESIGNATION_SCOPE = Neshane V3 project architecture and V3-004 R0 design baseline
DESIGNATION_SOURCE = Explicit project-owner declaration in conversation
REVIEWED_SUPPORT_MATRIX_SHA256 = ad1ab89632003ec129fdf174a9589c69780307967516d2f5d6747369fcfd7611
TECHNICAL_ARCHITECTURE_R0_DISPOSITION = APPROVE — DESIGN CONSISTENCY BASELINE ONLY
```

The Technical Architecture Owner confirms that the reviewed baseline preserves the three target profiles, all fifteen FIRST_RELEASE mappings, `FR-PF-001` Option B, separate Identity/Tenant/Entitlement/resource-owning Domain authorities, validated Tenant Context and fail-closed behavior, Domain-owned authorization, RLS defense in depth, Dedicated Sovereign local final authority, the five DEC-014 principles, `OD-001` as the separate Air Gap decision, and the absence of unsupported SLA or Production commitments.

This approval is a user-declared project-role decision. It does not claim a legal identity, signature, appointment certificate, independent reviewer or corporate credential. It is not Security Sign-off, specialist approval, risk acceptance, implementation verification or Production approval.

### Evidence required before Production Readiness

- profile-specific install, upgrade, rollback, backup/restore and recovery execution evidence;
- implemented identity, Tenant isolation, RLS, authorization and secrets evidence;
- executed security and negative tests;
- supply-chain/artifact integrity and authorized promotion evidence;
- approved numeric objectives and measured results under `OD-023`;
- required Security Sign-off and release authorization.

## 12. Acceptance assessment and current status

| V3-004 acceptance requirement | Result | Evidence |
| --- | --- | --- |
| Every profile states obligations | `MET — DOCUMENTARY` | Sections 3 and 4 |
| Every profile states dependencies | `MET — DOCUMENTARY` | Sections 3 and 4 |
| Every profile states offline claims | `MET — DOCUMENTARY` | Sections 3, 4 and 8 |
| Every profile states exclusions | `MET — DOCUMENTARY` | Sections 4, 6 and 8 |
| FIRST_RELEASE capabilities are mapped | `MET — DOCUMENTARY` | Section 5; V3-003-DEC-002 inventory |
| Open Decisions retain owners/milestones | `MET — DOCUMENTARY` | Section 9; `architecture/open-decisions.md` |
| Focused Product/Security R0 analysis | `COMPLETE — ANALYST REVIEW` | Evidence-supported findings and editorial corrections recorded; this is not Product or Security approval |
| Formal Product R0 authority disposition | `MET — APPROVED BY CPO` | Product review in section 11; explicit project-conversation decision source recorded |
| Bounded security consistency analysis | `MET — ANALYST REVIEW` | No substantive contradiction found; no Security approval implied |
| Technical Architecture Owner R0 Design Consistency Acceptance | `MET — APPROVED IN DECLARED DUAL PROJECT ROLE` | Section 11 records designation, reviewed baseline and bounded disposition |
| Implementation/runtime validation | `NOT_APPLICABLE TO THIS DOCUMENTATION TASK` | No executable deployment exists and repository policy forbids execution |
| Production Readiness | `NOT ESTABLISHED` | ADR-V3-012 separation preserved |

```text
V3-004 = CLOSED — FIRST RELEASE SUPPORT MATRIX DESIGN BASELINE ONLY
OD-001..023 = OPEN
SR-CAND-001..024 = PROPOSED — NOT APPROVED
SECURITY_REVIEW_STATUS = NOT_SIGNED_OFF
IMPLEMENTATION_EVIDENCE_STATUS = NOT_VERIFIED
NEGATIVE_TEST_EXECUTION_STATUS = NOT_EXECUTED
EXECUTABLE_DURABLE_DEFER = NOT APPROVED
PRODUCTION_READINESS = NOT ESTABLISHED
```

## 13. Authoritative references

- `architecture/baseline-v3.md`
- `architecture/decision-register.md`
- `architecture/open-decisions.md`
- `architecture/adr/003-cell-based-hybrid-tenancy.md`
- `architecture/adr/004-sovereign-authority.md`
- `architecture/adr/005-domain-owned-authorization.md`
- `architecture/adr/007-data-messaging-baseline.md`
- `architecture/adr/008-contract-compatibility.md`
- `architecture/adr/010-operational-profiles.md`
- `architecture/adr/012-evidence-based-readiness.md`
- `architecture/standards/security.md`
- `architecture/nfr.md`
- `architecture/threat-assumptions.md`
- `architecture/reviews/V3-003-decision-record.md`
- `architecture/task-governance.md`
