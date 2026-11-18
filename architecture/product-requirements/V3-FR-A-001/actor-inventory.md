# Product actor inventory — V3-FR-A-001

**Requirements engineering only; prepared for owner review, not a new approved role or permission catalog.** ACT-A001-* identifies records in this task. No new product RBAC, actor assignment, IAM mechanism or grant is defined. One Principal can appear in several analytical views; these are not independently approved personas or a count of user accounts.

## Classification and source rule

Documented internal authenticated Principal scope is approved; specific business participant labels below are analytical views of existing operations, not approved role names. Tenant administration and profile operations are documented responsibilities with role/action details OPEN. Logical profile authority scopes are not appointed people or actual workloads. Governance authorities do not gain runtime access. External customer and plugin records are context only, not newly approved first-release features. Sources/quotes/lines and byte hashes are in source-traceability.json.

| Actor ID | Category | Record kind | Name | Capability references |
| --- | --- | --- | --- | --- |
| ACT-A001-001 | HUMAN_PRODUCT_USER | DOCUMENTED_APPROVED_ACTOR_CLASS | Internal authenticated Principal | FR-BJ-001, FR-BJ-002, FR-BJ-003, FR-BJ-004, FR-BJ-005, FR-PF-001, FR-PF-002, FR-PF-003, FR-PF-004, FR-PF-005, FR-PF-006, FR-SO-001, FR-SO-002, FR-SO-003, FR-SO-004 |
| ACT-A001-002 | HUMAN_PRODUCT_USER | ANALYTICAL_PARTICIPATION_VIEW_NOT_APPROVED_ROLE | Customer maintenance participant | FR-BJ-001 |
| ACT-A001-003 | HUMAN_PRODUCT_USER | ANALYTICAL_PARTICIPATION_VIEW_NOT_APPROVED_ROLE | Customer find/review participant | FR-BJ-002 |
| ACT-A001-004 | HUMAN_PRODUCT_USER | ANALYTICAL_PARTICIPATION_VIEW_NOT_APPROVED_ROLE | Opportunity/Pipeline participant | FR-BJ-003 |
| ACT-A001-005 | HUMAN_PRODUCT_USER | ANALYTICAL_PARTICIPATION_VIEW_NOT_APPROVED_ROLE | Internal Customer Request participant | FR-BJ-004 |
| ACT-A001-006 | HUMAN_PRODUCT_USER | ANALYTICAL_PARTICIPATION_VIEW_NOT_APPROVED_ROLE | Work Task participant / assignment subject | FR-BJ-005 |
| ACT-A001-007 | HUMAN_PRODUCT_USER | ANALYTICAL_PARTICIPATION_VIEW_NOT_APPROVED_ROLE | In-App Notification recipient concept | FR-PF-004 |
| ACT-A001-008 | HUMAN_PRODUCT_USER | ANALYTICAL_PARTICIPATION_VIEW_NOT_APPROVED_ROLE | File/Attachment operation participant | FR-PF-005 |
| ACT-A001-009 | HUMAN_PRODUCT_USER | ANALYTICAL_PARTICIPATION_VIEW_NOT_APPROVED_ROLE | Deterministic Report consumer concept | FR-PF-006 |
| ACT-A001-010 | HUMAN_PRODUCT_USER | ANALYTICAL_PARTICIPATION_VIEW_NOT_APPROVED_ROLE | Authorized Audit reviewer concept | FR-SO-002 |
| ACT-A001-011 | TENANT_SCOPED_ADMINISTRATOR | DOCUMENTED_RESPONSIBILITY_NOT_APPROVED_ROLE_CATALOG | Tenant administration responsibility (role model unspecified) | FR-PF-001 |
| ACT-A001-012 | PLATFORM_OPERATIONAL_ACTOR | DOCUMENTED_PROFILE_OPERATIONAL_RESPONSIBILITY | Provider operations participant | FR-SO-003, FR-SO-004 |
| ACT-A001-013 | PLATFORM_OPERATIONAL_ACTOR | DOCUMENTED_PROFILE_OPERATIONAL_RESPONSIBILITY | Managed operations/support participant | FR-SO-003, FR-SO-004 |
| ACT-A001-014 | PLATFORM_OPERATIONAL_ACTOR | DOCUMENTED_PROFILE_OPERATIONAL_RESPONSIBILITY | Sovereign-local operations participant | FR-SO-003, FR-SO-004 |
| ACT-A001-015 | SERVICE_AND_WORKLOAD_IDENTITY | DOCUMENTED_DISTINCT_IDENTITY_CLASS | Authenticated service/workload identity | FR-BJ-001, FR-BJ-002, FR-BJ-003, FR-BJ-004, FR-BJ-005, FR-PF-001, FR-PF-002, FR-PF-003, FR-PF-004, FR-PF-005, FR-PF-006, FR-SO-001, FR-SO-002, FR-SO-003, FR-SO-004 |
| ACT-A001-016 | SERVICE_AND_WORKLOAD_IDENTITY | DOCUMENTED_PRODUCER_RESPONSIBILITY | Producing Domain workload | FR-BJ-001, FR-PF-003, FR-PF-004, FR-PF-006, FR-SO-001 |
| ACT-A001-017 | SERVICE_AND_WORKLOAD_IDENTITY | DOCUMENTED_AUDIT_BOUNDARY_RESPONSIBILITY | Audit-owned processing workload | FR-SO-001, FR-SO-002 |
| ACT-A001-018 | EXTERNAL_SYSTEM_ACTOR | DOCUMENTED_TRUST_BOUNDARY_PROVIDER_NOT_SELECTED | Admitted identity issuer / external IdP boundary | FR-PF-001 |
| ACT-A001-019 | EXTERNAL_SYSTEM_ACTOR | DOCUMENTED_CONDITIONAL_CROSS_PLANE_CONTEXT | Central / federation / external support system boundary | FR-PF-001, FR-PF-002, FR-SO-001, FR-SO-003, FR-SO-004 |
| ACT-A001-020 | HUMAN_PRODUCT_USER | DOCUMENTED_DEFERRED_HUMAN_EXTERNAL_PRINCIPAL | External customer / Portal user (deferred) | Context only; no mandatory first-release mapping |
| ACT-A001-021 | SERVICE_AND_WORKLOAD_IDENTITY | DOCUMENTED_ARCHITECTURAL_CONTEXT_NOT_MANDATORY_JOURNEY | Plugin Installation identity (architectural extension context) | Context only; no mandatory first-release mapping |
| ACT-A001-022 | PRODUCT_GOVERNANCE_AUTHORITY | DOCUMENTED_EXISTING_PROJECT_AUTHORITY | Product Decision Owner / TAO (existing unified internal authority) | FR-BJ-001, FR-BJ-002, FR-BJ-003, FR-BJ-004, FR-BJ-005, FR-PF-001, FR-PF-002, FR-PF-003, FR-PF-004, FR-PF-005, FR-PF-006, FR-SO-001, FR-SO-002, FR-SO-003, FR-SO-004 |
| ACT-A001-023 | PRODUCT_GOVERNANCE_AUTHORITY | DOCUMENTED_OWNERSHIP_RESPONSIBILITY_PERSON_UNASSIGNED | Domain/Service Owner contributor role | FR-BJ-001, FR-BJ-002, FR-BJ-003, FR-BJ-004, FR-BJ-005, FR-PF-001, FR-PF-002, FR-PF-003, FR-PF-004, FR-PF-005, FR-PF-006, FR-SO-001, FR-SO-002, FR-SO-003, FR-SO-004 |
| ACT-A001-024 | PRODUCT_GOVERNANCE_AUTHORITY | DOCUMENTED_ADVISORY_ASSESSMENT_ROLE | Specialist / independent technical assessor role | FR-BJ-001, FR-BJ-002, FR-BJ-003, FR-BJ-004, FR-BJ-005, FR-PF-001, FR-PF-002, FR-PF-003, FR-PF-004, FR-PF-005, FR-PF-006, FR-SO-001, FR-SO-002, FR-SO-003, FR-SO-004 |
| ACT-A001-025 | PRODUCT_GOVERNANCE_AUTHORITY | DOCUMENTED_EXISTING_SCOPED_QUALITY_ROLE | Existing scoped interim Quality Authority | FR-BJ-001, FR-BJ-002, FR-BJ-003, FR-BJ-004, FR-BJ-005, FR-PF-001, FR-PF-002, FR-PF-003, FR-PF-004, FR-PF-005, FR-PF-006, FR-SO-001, FR-SO-002, FR-SO-003, FR-SO-004 |
| ACT-A001-026 | PLATFORM_OPERATIONAL_ACTOR | DOCUMENTED_LOGICAL_AUTHORITY_SCOPES_NOT_PRINCIPAL_ASSIGNMENTS | Profile control-plane authority scopes (twelve documented boundaries) | FR-PF-001, FR-PF-002, FR-SO-001, FR-SO-003, FR-SO-004 |

## ACT-A001-001 — Internal authenticated Principal

**Category / status:** HUMAN_PRODUCT_USER / DOCUMENTED_APPROVED_ACTOR_CLASS

**Applicable capabilities:** FR-BJ-001, FR-BJ-002, FR-BJ-003, FR-BJ-004, FR-BJ-005, FR-PF-001, FR-PF-002, FR-PF-003, FR-PF-004, FR-PF-005, FR-PF-006, FR-SO-001, FR-SO-002, FR-SO-003, FR-SO-004. Association documents an interaction/context, never a permission grant.

**Documented responsibilities**
- Participate in protected FIRST_RELEASE journeys only after active Membership, validated Context and separate Domain authorization

**Documented operation concepts — NOT permissions**
- Active Membership validation; valid destination Membership for Tenant switching; access journey, not an approved operation-permission list

**Authorization boundary:** Authenticated Principal or assigned operational responsibility is not permission. Owning Domain authorizes each resource/action; detailed role/action/disclosure matrix remains OPEN.

**Tenant boundary:** Validated/revalidated Tenant Context; Tenant selector untrusted; cross-Tenant access not implied. Shared, Managed and Sovereign preserve logical boundaries; local authority is profile-specific.

**Assignment / approved role:** UNASSIGNED / UNASSIGNED. No person/workload instantiated here.

**Source evidence:** EVID-A001-002, EVID-A001-001, EVID-A001-003

**Unresolved requirements**
- Exact supported internal personas, onboarding, role/action/disclosure and session policies OPEN

**Question register links:** PDQ-A001-001, PDQ-A001-002, PDQ-A001-003, PDQ-A001-004, PDQ-A001-005, PDQ-A001-006, PDQ-A001-007, PDQ-A001-008, PDQ-A001-009, PDQ-A001-010, PDQ-A001-011, PDQ-A001-012, PDQ-A001-013, PDQ-A001-014, PDQ-A001-015, PDQ-A001-016, PDQ-A001-017, PDQ-A001-018, PDQ-A001-019, PDQ-A001-020, PDQ-A001-021, PDQ-A001-022, PDQ-A001-023, PDQ-A001-024, PDQ-A001-025, PDQ-A001-026, PDQ-A001-027, PDQ-A001-028, PDQ-A001-029, PDQ-A001-030, PDQ-A001-031, PDQ-A001-032, PDQ-A001-033, PDQ-A001-034, PDQ-A001-035, PDQ-A001-036, PDQ-A001-037, PDQ-A001-038, PDQ-A001-039, PDQ-A001-040, PDQ-A001-041, PDQ-A001-042, PDQ-A001-043, PDQ-A001-044, PDQ-A001-045, PDQ-A001-046, PDQ-A001-047, PDQ-A001-048, PDQ-A001-049, PDQ-A001-050, PDQ-A001-051, PDQ-A001-052, PDQ-A001-053, PDQ-A001-054

## ACT-A001-002 — Customer maintenance participant

**Category / status:** HUMAN_PRODUCT_USER / ANALYTICAL_PARTICIPATION_VIEW_NOT_APPROVED_ROLE

**Applicable capabilities:** FR-BJ-001. Association documents an interaction/context, never a permission grant.

**Documented responsibilities**
- Maintain authoritative Customer Master through Customer-owned validation and writes

**Documented operation concepts — NOT permissions**
- CUS-CREATE; CUS-VALIDATE; CUS-GET-FOR-UPDATE; CUS-UPDATE are documented Customer operation concepts; no granted permission

**Authorization boundary:** Authenticated Principal or assigned operational responsibility is not permission. Owning Domain authorizes each resource/action; detailed role/action/disclosure matrix remains OPEN.

**Tenant boundary:** Validated/revalidated Tenant Context; Tenant selector untrusted; cross-Tenant access not implied. Shared, Managed and Sovereign preserve logical boundaries; local authority is profile-specific.

**Assignment / approved role:** UNASSIGNED / UNASSIGNED. No person/workload instantiated here.

**Source evidence:** EVID-A001-002, EVID-A001-009, EVID-A001-028, EVID-A001-043, EVID-A001-022, EVID-A001-076, EVID-A001-077, EVID-A001-078, EVID-A001-079, EVID-A001-080

**Unresolved requirements**
- Human persona/role and organization-specific assignment UNASSIGNED; mapping to an actual allowed action is OPEN
- Capability/operation participation is documented; this local label is analytical, not an approved role or permission

**Question register links:** PDQ-A001-001, PDQ-A001-002, PDQ-A001-003, PDQ-A001-049, PDQ-A001-050, PDQ-A001-052, PDQ-A001-053

## ACT-A001-003 — Customer find/review participant

**Category / status:** HUMAN_PRODUCT_USER / ANALYTICAL_PARTICIPATION_VIEW_NOT_APPROVED_ROLE

**Applicable capabilities:** FR-BJ-002. Association documents an interaction/context, never a permission grant.

**Documented responsibilities**
- Find/review Customer within Customer-controlled disclosure boundary

**Documented operation concepts — NOT permissions**
- CUS-SEARCH; CUS-GET; CUS-AUTHORIZE-DISCLOSURE are documented assessment/operation concepts, not permissions

**Authorization boundary:** Authenticated Principal or assigned operational responsibility is not permission. Owning Domain authorizes each resource/action; detailed role/action/disclosure matrix remains OPEN.

**Tenant boundary:** Validated/revalidated Tenant Context; Tenant selector untrusted; cross-Tenant access not implied. Shared, Managed and Sovereign preserve logical boundaries; local authority is profile-specific.

**Assignment / approved role:** UNASSIGNED / UNASSIGNED. No person/workload instantiated here.

**Source evidence:** EVID-A001-002, EVID-A001-009, EVID-A001-029, EVID-A001-043, EVID-A001-081, EVID-A001-082, EVID-A001-083

**Unresolved requirements**
- Human persona/role and organization-specific assignment UNASSIGNED; mapping to an actual allowed action is OPEN
- Capability/operation participation is documented; this local label is analytical, not an approved role or permission

**Question register links:** PDQ-A001-004, PDQ-A001-005, PDQ-A001-006, PDQ-A001-049, PDQ-A001-050, PDQ-A001-052

## ACT-A001-004 — Opportunity/Pipeline participant

**Category / status:** HUMAN_PRODUCT_USER / ANALYTICAL_PARTICIPATION_VIEW_NOT_APPROVED_ROLE

**Applicable capabilities:** FR-BJ-003. Association documents an interaction/context, never a permission grant.

**Documented responsibilities**
- Perform approved Sales journey; Customer reference does not transfer Customer ownership

**Documented operation concepts — NOT permissions**
- Manage Opportunity, Pipeline/Stage transitions and amount/currency; detailed operation catalog OPEN

**Authorization boundary:** Authenticated Principal or assigned operational responsibility is not permission. Owning Domain authorizes each resource/action; detailed role/action/disclosure matrix remains OPEN.

**Tenant boundary:** Validated/revalidated Tenant Context; Tenant selector untrusted; cross-Tenant access not implied. Shared, Managed and Sovereign preserve logical boundaries; local authority is profile-specific.

**Assignment / approved role:** UNASSIGNED / UNASSIGNED. No person/workload instantiated here.

**Source evidence:** EVID-A001-002, EVID-A001-009, EVID-A001-030, EVID-A001-044, EVID-A001-084

**Unresolved requirements**
- Human persona/role and organization-specific assignment UNASSIGNED; mapping to an actual allowed action is OPEN
- Capability/operation participation is documented; this local label is analytical, not an approved role or permission

**Question register links:** PDQ-A001-007, PDQ-A001-008, PDQ-A001-009, PDQ-A001-050, PDQ-A001-052

## ACT-A001-005 — Internal Customer Request participant

**Category / status:** HUMAN_PRODUCT_USER / ANALYTICAL_PARTICIPATION_VIEW_NOT_APPROVED_ROLE

**Applicable capabilities:** FR-BJ-004. Association documents an interaction/context, never a permission grant.

**Documented responsibilities**
- Register/process Request without a Portal or mandatory generic Workflow Engine

**Documented operation concepts — NOT permissions**
- Internal creation, view/tracking, base lifecycle, history, triage and assignment; exact transitions OPEN

**Authorization boundary:** Authenticated Principal or assigned operational responsibility is not permission. Owning Domain authorizes each resource/action; detailed role/action/disclosure matrix remains OPEN.

**Tenant boundary:** Validated/revalidated Tenant Context; Tenant selector untrusted; cross-Tenant access not implied. Shared, Managed and Sovereign preserve logical boundaries; local authority is profile-specific.

**Assignment / approved role:** UNASSIGNED / UNASSIGNED. No person/workload instantiated here.

**Source evidence:** EVID-A001-002, EVID-A001-009, EVID-A001-031, EVID-A001-046, EVID-A001-085

**Unresolved requirements**
- Human persona/role and organization-specific assignment UNASSIGNED; mapping to an actual allowed action is OPEN
- Capability/operation participation is documented; this local label is analytical, not an approved role or permission

**Question register links:** PDQ-A001-010, PDQ-A001-011, PDQ-A001-012, PDQ-A001-050, PDQ-A001-052, PDQ-A001-053

## ACT-A001-006 — Work Task participant / assignment subject

**Category / status:** HUMAN_PRODUCT_USER / ANALYTICAL_PARTICIPATION_VIEW_NOT_APPROVED_ROLE

**Applicable capabilities:** FR-BJ-005. Association documents an interaction/context, never a permission grant.

**Documented responsibilities**
- Plan/track Work Task; assignment/link grants no related-resource authority

**Documented operation concepts — NOT permissions**
- Create/View/Edit, Assignment, Status, Due Date and manual contract links; exact assignee policy OPEN

**Authorization boundary:** Authenticated Principal or assigned operational responsibility is not permission. Owning Domain authorizes each resource/action; detailed role/action/disclosure matrix remains OPEN.

**Tenant boundary:** Validated/revalidated Tenant Context; Tenant selector untrusted; cross-Tenant access not implied. Shared, Managed and Sovereign preserve logical boundaries; local authority is profile-specific.

**Assignment / approved role:** UNASSIGNED / UNASSIGNED. No person/workload instantiated here.

**Source evidence:** EVID-A001-002, EVID-A001-009, EVID-A001-032, EVID-A001-051, EVID-A001-086

**Unresolved requirements**
- Human persona/role and organization-specific assignment UNASSIGNED; mapping to an actual allowed action is OPEN
- Capability/operation participation is documented; this local label is analytical, not an approved role or permission

**Question register links:** PDQ-A001-013, PDQ-A001-014, PDQ-A001-015, PDQ-A001-050, PDQ-A001-052

## ACT-A001-007 — In-App Notification recipient concept

**Category / status:** HUMAN_PRODUCT_USER / ANALYTICAL_PARTICIPATION_VIEW_NOT_APPROVED_ROLE

**Applicable capabilities:** FR-PF-004. Association documents an interaction/context, never a permission grant.

**Documented responsibilities**
- Notification recipient access is distinct from producer Business Fact authorization

**Documented operation concepts — NOT permissions**
- Receive/access an authorized In-App notification; recipient determination/type/read/dismiss details OPEN

**Authorization boundary:** Authenticated Principal or assigned operational responsibility is not permission. Owning Domain authorizes each resource/action; detailed role/action/disclosure matrix remains OPEN.

**Tenant boundary:** Validated/revalidated Tenant Context; Tenant selector untrusted; cross-Tenant access not implied. Shared, Managed and Sovereign preserve logical boundaries; local authority is profile-specific.

**Assignment / approved role:** UNASSIGNED / UNASSIGNED. No person/workload instantiated here.

**Source evidence:** EVID-A001-002, EVID-A001-009, EVID-A001-036, EVID-A001-045, EVID-A001-087

**Unresolved requirements**
- Human persona/role and organization-specific assignment UNASSIGNED; mapping to an actual allowed action is OPEN
- Capability/operation participation is documented; this local label is analytical, not an approved role or permission

**Question register links:** PDQ-A001-025, PDQ-A001-026, PDQ-A001-027, PDQ-A001-050, PDQ-A001-052

## ACT-A001-008 — File/Attachment operation participant

**Category / status:** HUMAN_PRODUCT_USER / ANALYTICAL_PARTICIPATION_VIEW_NOT_APPROVED_ROLE

**Applicable capabilities:** FR-PF-005. Association documents an interaction/context, never a permission grant.

**Documented responsibilities**
- Participate only under separate File and related-resource authorization

**Documented operation concepts — NOT permissions**
- Controlled upload/download and resource attachment; resource-specific matrix OPEN

**Authorization boundary:** Authenticated Principal or assigned operational responsibility is not permission. Owning Domain authorizes each resource/action; detailed role/action/disclosure matrix remains OPEN.

**Tenant boundary:** Validated/revalidated Tenant Context; Tenant selector untrusted; cross-Tenant access not implied. Shared, Managed and Sovereign preserve logical boundaries; local authority is profile-specific.

**Assignment / approved role:** UNASSIGNED / UNASSIGNED. No person/workload instantiated here.

**Source evidence:** EVID-A001-002, EVID-A001-009, EVID-A001-037, EVID-A001-052, EVID-A001-088

**Unresolved requirements**
- Human persona/role and organization-specific assignment UNASSIGNED; mapping to an actual allowed action is OPEN
- Capability/operation participation is documented; this local label is analytical, not an approved role or permission

**Question register links:** PDQ-A001-028, PDQ-A001-029, PDQ-A001-030, PDQ-A001-050, PDQ-A001-052

## ACT-A001-009 — Deterministic Report consumer concept

**Category / status:** HUMAN_PRODUCT_USER / ANALYTICAL_PARTICIPATION_VIEW_NOT_APPROVED_ROLE

**Applicable capabilities:** FR-PF-006. Association documents an interaction/context, never a permission grant.

**Documented responsibilities**
- Report disclosure preserves source data restrictions

**Documented operation concepts — NOT permissions**
- Request/access approved deterministic report; no final Report Set or reader permission inferred

**Authorization boundary:** Authenticated Principal or assigned operational responsibility is not permission. Owning Domain authorizes each resource/action; detailed role/action/disclosure matrix remains OPEN.

**Tenant boundary:** Validated/revalidated Tenant Context; Tenant selector untrusted; cross-Tenant access not implied. Shared, Managed and Sovereign preserve logical boundaries; local authority is profile-specific.

**Assignment / approved role:** UNASSIGNED / UNASSIGNED. No person/workload instantiated here.

**Source evidence:** EVID-A001-002, EVID-A001-009, EVID-A001-038, EVID-A001-050, EVID-A001-089

**Unresolved requirements**
- Human persona/role and organization-specific assignment UNASSIGNED; mapping to an actual allowed action is OPEN
- Capability/operation participation is documented; this local label is analytical, not an approved role or permission

**Question register links:** PDQ-A001-031, PDQ-A001-032, PDQ-A001-033, PDQ-A001-050, PDQ-A001-052, PDQ-A001-054

## ACT-A001-010 — Authorized Audit reviewer concept

**Category / status:** HUMAN_PRODUCT_USER / ANALYTICAL_PARTICIPATION_VIEW_NOT_APPROVED_ROLE

**Applicable capabilities:** FR-SO-002. Association documents an interaction/context, never a permission grant.

**Documented responsibilities**
- Review Audit within Audit Domain authorization; operator title is not blanket Audit access

**Documented operation concepts — NOT permissions**
- Authorized Audit evidence viewing/search; exact viewer/purpose/disclosure operation catalog OPEN

**Authorization boundary:** Authenticated Principal or assigned operational responsibility is not permission. Owning Domain authorizes each resource/action; detailed role/action/disclosure matrix remains OPEN.

**Tenant boundary:** Validated/revalidated Tenant Context; Tenant selector untrusted; cross-Tenant access not implied. Shared, Managed and Sovereign preserve logical boundaries; local authority is profile-specific.

**Assignment / approved role:** UNASSIGNED / UNASSIGNED. No person/workload instantiated here.

**Source evidence:** EVID-A001-002, EVID-A001-009, EVID-A001-040, EVID-A001-047, EVID-A001-024, EVID-A001-090

**Unresolved requirements**
- Human persona/role and organization-specific assignment UNASSIGNED; mapping to an actual allowed action is OPEN
- Capability/operation participation is documented; this local label is analytical, not an approved role or permission

**Question register links:** PDQ-A001-037, PDQ-A001-038, PDQ-A001-039, PDQ-A001-050, PDQ-A001-051, PDQ-A001-052

## ACT-A001-011 — Tenant administration responsibility (role model unspecified)

**Category / status:** TENANT_SCOPED_ADMINISTRATOR / DOCUMENTED_RESPONSIBILITY_NOT_APPROVED_ROLE_CATALOG

**Applicable capabilities:** FR-PF-001. Association documents an interaction/context, never a permission grant.

**Documented responsibilities**
- Customer-side Tenant administration, authorized users and business configuration/data stewardship within approved contracts

**Documented operation concepts — NOT permissions**
- No complete approved Tenant administrator action catalog; Membership administration ownership belongs to Tenant Management, not any automatically entitled user

**Authorization boundary:** Tenant-scoped administration is not Platform administration, Entitlement, Customer data access or a universal administrator. Resource owners decide actions.

**Tenant boundary:** Validated/revalidated Tenant Context; Tenant selector untrusted; cross-Tenant access not implied. Shared, Managed and Sovereign preserve logical boundaries; local authority is profile-specific.

**Assignment / approved role:** UNASSIGNED / UNASSIGNED. No person/workload instantiated here.

**Source evidence:** EVID-A001-006, EVID-A001-008, EVID-A001-055

**Unresolved requirements**
- Who may administer Membership, delegation/revocation and configuration? OPEN
- Tenant administration UI and exact role permissions are not approved by minimum access scope

**Question register links:** PDQ-A001-016, PDQ-A001-017, PDQ-A001-018, PDQ-A001-046, PDQ-A001-047, PDQ-A001-048, PDQ-A001-050, PDQ-A001-052, PDQ-A001-053

## ACT-A001-012 — Provider operations participant

**Category / status:** PLATFORM_OPERATIONAL_ACTOR / DOCUMENTED_PROFILE_OPERATIONAL_RESPONSIBILITY

**Applicable capabilities:** FR-SO-003, FR-SO-004. Association documents an interaction/context, never a permission grant.

**Documented responsibilities**
- Operate only approved infrastructure/visibility/support/recovery within named profile and explicit destination scope

**Documented operation concepts — NOT permissions**
- Authorized visibility and privileged request/execution; exact action/role/emergency catalogs remain OPEN

**Authorization boundary:** No implicit Business Fact ownership, Audit access or customer-data permission; destination Domain authorization and durable Audit required. Global support has no ambient local right.

**Tenant boundary:** Validated/revalidated Tenant Context; Tenant selector untrusted; cross-Tenant access not implied. Shared, Managed and Sovereign preserve logical boundaries; local authority is profile-specific. Profiles: Shared SaaS

**Assignment / approved role:** UNASSIGNED / UNASSIGNED. No person/workload instantiated here.

**Source evidence:** EVID-A001-005, EVID-A001-007, EVID-A001-025, EVID-A001-027, EVID-A001-023

**Unresolved requirements**
- Named operators and role/action/approval/break-glass model UNASSIGNED/OPEN
- Approved operation-specific identity, failure, recovery and revocation conditions missing

**Question register links:** PDQ-A001-040, PDQ-A001-041, PDQ-A001-042, PDQ-A001-043, PDQ-A001-044, PDQ-A001-045, PDQ-A001-048, PDQ-A001-050, PDQ-A001-051, PDQ-A001-052, PDQ-A001-054

## ACT-A001-013 — Managed operations/support participant

**Category / status:** PLATFORM_OPERATIONAL_ACTOR / DOCUMENTED_PROFILE_OPERATIONAL_RESPONSIBILITY

**Applicable capabilities:** FR-SO-003, FR-SO-004. Association documents an interaction/context, never a permission grant.

**Documented responsibilities**
- Operate only approved infrastructure/visibility/support/recovery within named profile and explicit destination scope

**Documented operation concepts — NOT permissions**
- Authorized visibility and privileged request/execution; exact action/role/emergency catalogs remain OPEN

**Authorization boundary:** No implicit Business Fact ownership, Audit access or customer-data permission; destination Domain authorization and durable Audit required. Global support has no ambient local right.

**Tenant boundary:** Validated/revalidated Tenant Context; Tenant selector untrusted; cross-Tenant access not implied. Shared, Managed and Sovereign preserve logical boundaries; local authority is profile-specific. Profiles: Dedicated Managed

**Assignment / approved role:** UNASSIGNED / UNASSIGNED. No person/workload instantiated here.

**Source evidence:** EVID-A001-005, EVID-A001-007, EVID-A001-025, EVID-A001-027, EVID-A001-023

**Unresolved requirements**
- Named operators and role/action/approval/break-glass model UNASSIGNED/OPEN
- Approved operation-specific identity, failure, recovery and revocation conditions missing

**Question register links:** PDQ-A001-040, PDQ-A001-041, PDQ-A001-042, PDQ-A001-043, PDQ-A001-044, PDQ-A001-045, PDQ-A001-048, PDQ-A001-050, PDQ-A001-051, PDQ-A001-052, PDQ-A001-054

## ACT-A001-014 — Sovereign-local operations participant

**Category / status:** PLATFORM_OPERATIONAL_ACTOR / DOCUMENTED_PROFILE_OPERATIONAL_RESPONSIBILITY

**Applicable capabilities:** FR-SO-003, FR-SO-004. Association documents an interaction/context, never a permission grant.

**Documented responsibilities**
- Operate only approved infrastructure/visibility/support/recovery within named profile and explicit destination scope

**Documented operation concepts — NOT permissions**
- Authorized visibility and privileged request/execution; exact action/role/emergency catalogs remain OPEN

**Authorization boundary:** No implicit Business Fact ownership, Audit access or customer-data permission; destination Domain authorization and durable Audit required. Global support has no ambient local right.

**Tenant boundary:** Validated/revalidated Tenant Context; Tenant selector untrusted; cross-Tenant access not implied. Shared, Managed and Sovereign preserve logical boundaries; local authority is profile-specific. Profiles: Dedicated Sovereign

**Assignment / approved role:** UNASSIGNED / UNASSIGNED. No person/workload instantiated here.

**Source evidence:** EVID-A001-005, EVID-A001-007, EVID-A001-025, EVID-A001-027, EVID-A001-023

**Unresolved requirements**
- Named operators and role/action/approval/break-glass model UNASSIGNED/OPEN
- Approved operation-specific identity, failure, recovery and revocation conditions missing

**Question register links:** PDQ-A001-040, PDQ-A001-041, PDQ-A001-042, PDQ-A001-043, PDQ-A001-044, PDQ-A001-045, PDQ-A001-048, PDQ-A001-050, PDQ-A001-051, PDQ-A001-052, PDQ-A001-054

## ACT-A001-015 — Authenticated service/workload identity

**Category / status:** SERVICE_AND_WORKLOAD_IDENTITY / DOCUMENTED_DISTINCT_IDENTITY_CLASS

**Applicable capabilities:** FR-BJ-001, FR-BJ-002, FR-BJ-003, FR-BJ-004, FR-BJ-005, FR-PF-001, FR-PF-002, FR-PF-003, FR-PF-004, FR-PF-005, FR-PF-006, FR-SO-001, FR-SO-002, FR-SO-003, FR-SO-004. Association documents an interaction/context, never a permission grant.

**Documented responsibilities**
- Authenticate at each relevant service trust boundary and act only within owning/consuming contract authority

**Documented operation concepts — NOT permissions**
- Owning use cases and authorized cross-service API/event/job paths; no concrete new workload/service chosen

**Authorization boundary:** Internal network, broker delivery or valid workload credential does not confer tenant/resource access. Audience, scope, provenance, Context and Domain authorization required.

**Tenant boundary:** Validated/revalidated Tenant Context; Tenant selector untrusted; cross-Tenant access not implied. Shared, Managed and Sovereign preserve logical boundaries; local authority is profile-specific.

**Assignment / approved role:** UNASSIGNED / UNASSIGNED. No person/workload instantiated here.

**Source evidence:** EVID-A001-004, EVID-A001-011, EVID-A001-012

**Unresolved requirements**
- Issuance, trust admission, audience/credential/session lifecycle and actual service inventory OPEN; OD-009..012 remain unresolved

**Question register links:** PDQ-A001-001, PDQ-A001-002, PDQ-A001-003, PDQ-A001-004, PDQ-A001-005, PDQ-A001-006, PDQ-A001-007, PDQ-A001-008, PDQ-A001-009, PDQ-A001-010, PDQ-A001-011, PDQ-A001-012, PDQ-A001-013, PDQ-A001-014, PDQ-A001-015, PDQ-A001-016, PDQ-A001-017, PDQ-A001-018, PDQ-A001-019, PDQ-A001-020, PDQ-A001-021, PDQ-A001-022, PDQ-A001-023, PDQ-A001-024, PDQ-A001-025, PDQ-A001-026, PDQ-A001-027, PDQ-A001-028, PDQ-A001-029, PDQ-A001-030, PDQ-A001-031, PDQ-A001-032, PDQ-A001-033, PDQ-A001-034, PDQ-A001-035, PDQ-A001-036, PDQ-A001-037, PDQ-A001-038, PDQ-A001-039, PDQ-A001-040, PDQ-A001-041, PDQ-A001-042, PDQ-A001-043, PDQ-A001-044, PDQ-A001-045, PDQ-A001-046, PDQ-A001-047, PDQ-A001-048, PDQ-A001-049, PDQ-A001-050, PDQ-A001-051, PDQ-A001-052, PDQ-A001-053, PDQ-A001-054

## ACT-A001-016 — Producing Domain workload

**Category / status:** SERVICE_AND_WORKLOAD_IDENTITY / DOCUMENTED_PRODUCER_RESPONSIBILITY

**Applicable capabilities:** FR-BJ-001, FR-PF-003, FR-PF-004, FR-PF-006, FR-SO-001. Association documents an interaction/context, never a permission grant.

**Documented responsibilities**
- Retain owned Business Facts/Usage and coordinate applicable required publication obligations; do not transfer source fact ownership to Audit/Notification/Reporting

**Documented operation concepts — NOT permissions**
- Producer facts, Usage integration, Notification delivery inputs and approved source-report data contracts; only selected integrations apply

**Authorization boundary:** Own fact publication is not downstream authorization or proof of Audit ingestion; no direct consumer private-database access.

**Tenant boundary:** Validated/revalidated Tenant Context; Tenant selector untrusted; cross-Tenant access not implied. Shared, Managed and Sovereign preserve logical boundaries; local authority is profile-specific.

**Assignment / approved role:** UNASSIGNED / UNASSIGNED. No person/workload instantiated here.

**Source evidence:** EVID-A001-047, EVID-A001-045, EVID-A001-049, EVID-A001-050, EVID-A001-026

**Unresolved requirements**
- Exact producer/event/usage/source projections and policies OPEN; no universal mandatory events inferred

**Question register links:** PDQ-A001-001, PDQ-A001-002, PDQ-A001-003, PDQ-A001-022, PDQ-A001-023, PDQ-A001-024, PDQ-A001-025, PDQ-A001-026, PDQ-A001-027, PDQ-A001-031, PDQ-A001-032, PDQ-A001-033, PDQ-A001-034, PDQ-A001-035, PDQ-A001-036, PDQ-A001-049, PDQ-A001-050, PDQ-A001-052, PDQ-A001-053, PDQ-A001-054

## ACT-A001-017 — Audit-owned processing workload

**Category / status:** SERVICE_AND_WORKLOAD_IDENTITY / DOCUMENTED_AUDIT_BOUNDARY_RESPONSIBILITY

**Applicable capabilities:** FR-SO-001, FR-SO-002. Association documents an interaction/context, never a permission grant.

**Documented responsibilities**
- Audit owns authoritative system-wide Audit records and its authorized projections; producers keep original Business Facts

**Documented operation concepts — NOT permissions**
- Authoritative evidence recording/access; exact ingestion confirmation/retry/access contracts OPEN

**Authorization boundary:** Audit ownership permits neither direct producer-database queries nor universal user disclosure. Sensitive access has distinct Audit obligations.

**Tenant boundary:** Validated/revalidated Tenant Context; Tenant selector untrusted; cross-Tenant access not implied. Shared, Managed and Sovereign preserve logical boundaries; local authority is profile-specific.

**Assignment / approved role:** UNASSIGNED / UNASSIGNED. No person/workload instantiated here.

**Source evidence:** EVID-A001-047, EVID-A001-026, EVID-A001-024

**Unresolved requirements**
- Precise ingestion evidence, viewer purpose, correction/retention/legal policy, recursive Audit behavior OPEN

**Question register links:** PDQ-A001-034, PDQ-A001-035, PDQ-A001-036, PDQ-A001-037, PDQ-A001-038, PDQ-A001-039, PDQ-A001-049, PDQ-A001-050, PDQ-A001-051, PDQ-A001-052, PDQ-A001-054

## ACT-A001-018 — Admitted identity issuer / external IdP boundary

**Category / status:** EXTERNAL_SYSTEM_ACTOR / DOCUMENTED_TRUST_BOUNDARY_PROVIDER_NOT_SELECTED

**Applicable capabilities:** FR-PF-001. Association documents an interaction/context, never a permission grant.

**Documented responsibilities**
- Supply credential assertions only within an admitted trust scope; Neshane validates mapping and Principal/session evidence

**Documented operation concepts — NOT permissions**
- Credential assertion validation; no named provider, SSO, protocol or credential transport selected

**Authorization boundary:** An issuer assertion creates no automatic Membership, entitlement, local Sovereign Principal or resource permission. Profile Trust Authority admits issuer; each Domain validates its own boundary.

**Tenant boundary:** Validated/revalidated Tenant Context; Tenant selector untrusted; cross-Tenant access not implied. Shared, Managed and Sovereign preserve logical boundaries; local authority is profile-specific.

**Assignment / approved role:** UNASSIGNED / UNASSIGNED. No person/workload instantiated here.

**Source evidence:** EVID-A001-054, EVID-A001-056, EVID-A001-008

**Unresolved requirements**
- Provider choice, admission/mapping and session/trust lifecycle OPEN; no concrete external integration authorized

**Question register links:** PDQ-A001-016, PDQ-A001-017, PDQ-A001-018, PDQ-A001-046, PDQ-A001-047, PDQ-A001-048, PDQ-A001-050, PDQ-A001-052, PDQ-A001-053

## ACT-A001-019 — Central / federation / external support system boundary

**Category / status:** EXTERNAL_SYSTEM_ACTOR / DOCUMENTED_CONDITIONAL_CROSS_PLANE_CONTEXT

**Applicable capabilities:** FR-PF-001, FR-PF-002, FR-SO-001, FR-SO-003, FR-SO-004. Association documents an interaction/context, never a permission grant.

**Documented responsibilities**
- Provide only locally approved artifacts, coordination, minimized telemetry or support/federation interactions where permitted

**Documented operation concepts — NOT permissions**
- Locally governed proposals, synchronization/support and minimized telemetry; no general central runtime call requirement

**Authorization boundary:** No implicit Sovereign administration; critical local authority must not depend synchronously on Central. Current offline continuation still PROHIBITED.

**Tenant boundary:** Validated/revalidated Tenant Context; Tenant selector untrusted; cross-Tenant access not implied. Shared, Managed and Sovereign preserve logical boundaries; local authority is profile-specific.

**Assignment / approved role:** UNASSIGNED / UNASSIGNED. No person/workload instantiated here.

**Source evidence:** EVID-A001-057, EVID-A001-025, EVID-A001-026

**Unresolved requirements**
- Exact federation/support actor admission, data classes, freshness and Critical Local Operation catalog OPEN

**Question register links:** PDQ-A001-016, PDQ-A001-017, PDQ-A001-018, PDQ-A001-019, PDQ-A001-020, PDQ-A001-021, PDQ-A001-034, PDQ-A001-035, PDQ-A001-036, PDQ-A001-040, PDQ-A001-041, PDQ-A001-042, PDQ-A001-043, PDQ-A001-044, PDQ-A001-045, PDQ-A001-046, PDQ-A001-047, PDQ-A001-048, PDQ-A001-049, PDQ-A001-050, PDQ-A001-051, PDQ-A001-052, PDQ-A001-053, PDQ-A001-054

## ACT-A001-020 — External customer / Portal user (deferred)

**Category / status:** HUMAN_PRODUCT_USER / DOCUMENTED_DEFERRED_HUMAN_EXTERNAL_PRINCIPAL

**Applicable capabilities:** None as a mandatory first-release actor; see contextual exclusions. Association documents an interaction/context, never a permission grant.

**Documented responsibilities**
- No FIRST_RELEASE runtime responsibility approved for an external customer Principal

**Documented operation concepts — NOT permissions**
- Portal submission/sharing is LATER_RELEASE; a Customer Master record is not a login Principal

**Authorization boundary:** Do not add external customers to minimum internal access scope or infer permission from a Customer record/link.

**Tenant boundary:** External-user trust, Membership and resource exposure require separate later scope.

**Assignment / approved role:** UNASSIGNED / UNASSIGNED. No person/workload instantiated here.

**Source evidence:** EVID-A001-008, EVID-A001-058

**Unresolved requirements**
- All external Principal/user journey, trust/session/resource requirements remain later-scope decisions

**Question register links:** PDQ-A001-001, PDQ-A001-002, PDQ-A001-003, PDQ-A001-010, PDQ-A001-011, PDQ-A001-012, PDQ-A001-016, PDQ-A001-017, PDQ-A001-018, PDQ-A001-046, PDQ-A001-047, PDQ-A001-048, PDQ-A001-049, PDQ-A001-050, PDQ-A001-052, PDQ-A001-053

## ACT-A001-021 — Plugin Installation identity (architectural extension context)

**Category / status:** SERVICE_AND_WORKLOAD_IDENTITY / DOCUMENTED_ARCHITECTURAL_CONTEXT_NOT_MANDATORY_JOURNEY

**Applicable capabilities:** None as a mandatory first-release actor; see contextual exclusions. Association documents an interaction/context, never a permission grant.

**Documented responsibilities**
- Distinct Package/Installation/Runtime boundary; only Installation-scoped identity/grants if separately selected

**Documented operation concepts — NOT permissions**
- Extension Gateway events/hooks only within approved extension scope; no extension implementation required by this actor inventory

**Authorization boundary:** Installation/Tenant binding and valid grant do not replace resource-owning Domain authorization; never in-process or direct database authority.

**Tenant boundary:** Validated/revalidated Tenant Context; Tenant selector untrusted; cross-Tenant access not implied. Shared, Managed and Sovereign preserve logical boundaries; local authority is profile-specific.

**Assignment / approved role:** UNASSIGNED / UNASSIGNED. No person/workload instantiated here.

**Source evidence:** EVID-A001-059, EVID-A001-004

**Unresolved requirements**
- Installed plugin actors/scopes and grant/revocation model OPEN; hosted runtime/marketplace not CM-1 prerequisite

**Question register links:** PDQ-A001-053

## ACT-A001-022 — Product Decision Owner / TAO (existing unified internal authority)

**Category / status:** PRODUCT_GOVERNANCE_AUTHORITY / DOCUMENTED_EXISTING_PROJECT_AUTHORITY

**Applicable capabilities:** FR-BJ-001, FR-BJ-002, FR-BJ-003, FR-BJ-004, FR-BJ-005, FR-PF-001, FR-PF-002, FR-PF-003, FR-PF-004, FR-PF-005, FR-PF-006, FR-SO-001, FR-SO-002, FR-SO-003, FR-SO-004. Association documents an interaction/context, never a permission grant.

**Documented responsibilities**
- Final internal product, architecture, security/Gate/risk, task-authorization and release decisions as distinct scopes

**Documented operation concepts — NOT permissions**
- Issue explicit scope/evidence-bound conversation decisions and authorize recording separately; no fabricated signature

**Authorization boundary:** Project decision authority is not a runtime login role or bypass of Domain/Sovereign authority; technical evidence and binding obligations remain mandatory.

**Tenant boundary:** Governance spans profiles but does not grant runtime Tenant access or Central administration.

**Assignment / approved role:** EXISTING_CONVERSATION_ROLE_ATTRIBUTION_ONLY / NOT_A_RUNTIME_ROLE. No person/workload instantiated here.

**Source evidence:** EVID-A001-013, EVID-A001-014, EVID-A001-016

**Unresolved requirements**
- Actual decision issuance timestamps only if provided; no legal identity/signature assertion
- Named per-capability accountable Business Owner not automatically this authority

**Question register links:** PDQ-A001-001, PDQ-A001-002, PDQ-A001-003, PDQ-A001-004, PDQ-A001-005, PDQ-A001-006, PDQ-A001-007, PDQ-A001-008, PDQ-A001-009, PDQ-A001-010, PDQ-A001-011, PDQ-A001-012, PDQ-A001-013, PDQ-A001-014, PDQ-A001-015, PDQ-A001-016, PDQ-A001-017, PDQ-A001-018, PDQ-A001-019, PDQ-A001-020, PDQ-A001-021, PDQ-A001-022, PDQ-A001-023, PDQ-A001-024, PDQ-A001-025, PDQ-A001-026, PDQ-A001-027, PDQ-A001-028, PDQ-A001-029, PDQ-A001-030, PDQ-A001-031, PDQ-A001-032, PDQ-A001-033, PDQ-A001-034, PDQ-A001-035, PDQ-A001-036, PDQ-A001-037, PDQ-A001-038, PDQ-A001-039, PDQ-A001-040, PDQ-A001-041, PDQ-A001-042, PDQ-A001-043, PDQ-A001-044, PDQ-A001-045, PDQ-A001-046, PDQ-A001-047, PDQ-A001-048, PDQ-A001-049, PDQ-A001-050, PDQ-A001-051, PDQ-A001-052, PDQ-A001-053, PDQ-A001-054

## ACT-A001-023 — Domain/Service Owner contributor role

**Category / status:** PRODUCT_GOVERNANCE_AUTHORITY / DOCUMENTED_OWNERSHIP_RESPONSIBILITY_PERSON_UNASSIGNED

**Applicable capabilities:** FR-BJ-001, FR-BJ-002, FR-BJ-003, FR-BJ-004, FR-BJ-005, FR-PF-001, FR-PF-002, FR-PF-003, FR-PF-004, FR-PF-005, FR-PF-006, FR-SO-001, FR-SO-002, FR-SO-003, FR-SO-004. Association documents an interaction/context, never a permission grant.

**Documented responsibilities**
- Supply domain rules, evidence, contract/data ownership and scoped review; preserve final project decision route

**Documented operation concepts — NOT permissions**
- Requirement/contract/persistence and business-effect boundary review, not universal runtime access

**Authorization boundary:** Logical Service/Data ownership is not an appointed person or cross-service database privilege. Final internal approval remains unified owner; destination runtime authorization belongs to owning Domain.

**Tenant boundary:** Validated/revalidated Tenant Context; Tenant selector untrusted; cross-Tenant access not implied. Shared, Managed and Sovereign preserve logical boundaries; local authority is profile-specific.

**Assignment / approved role:** UNASSIGNED / UNASSIGNED. No person/workload instantiated here.

**Source evidence:** EVID-A001-060, EVID-A001-009, EVID-A001-010

**Unresolved requirements**
- Accountable individual/team for every journey UNASSIGNED; no appointment made

**Question register links:** PDQ-A001-001, PDQ-A001-002, PDQ-A001-003, PDQ-A001-004, PDQ-A001-005, PDQ-A001-006, PDQ-A001-007, PDQ-A001-008, PDQ-A001-009, PDQ-A001-010, PDQ-A001-011, PDQ-A001-012, PDQ-A001-013, PDQ-A001-014, PDQ-A001-015, PDQ-A001-016, PDQ-A001-017, PDQ-A001-018, PDQ-A001-019, PDQ-A001-020, PDQ-A001-021, PDQ-A001-022, PDQ-A001-023, PDQ-A001-024, PDQ-A001-025, PDQ-A001-026, PDQ-A001-027, PDQ-A001-028, PDQ-A001-029, PDQ-A001-030, PDQ-A001-031, PDQ-A001-032, PDQ-A001-033, PDQ-A001-034, PDQ-A001-035, PDQ-A001-036, PDQ-A001-037, PDQ-A001-038, PDQ-A001-039, PDQ-A001-040, PDQ-A001-041, PDQ-A001-042, PDQ-A001-043, PDQ-A001-044, PDQ-A001-045, PDQ-A001-046, PDQ-A001-047, PDQ-A001-048, PDQ-A001-049, PDQ-A001-050, PDQ-A001-051, PDQ-A001-052, PDQ-A001-053, PDQ-A001-054

## ACT-A001-024 — Specialist / independent technical assessor role

**Category / status:** PRODUCT_GOVERNANCE_AUTHORITY / DOCUMENTED_ADVISORY_ASSESSMENT_ROLE

**Applicable capabilities:** FR-BJ-001, FR-BJ-002, FR-BJ-003, FR-BJ-004, FR-BJ-005, FR-PF-001, FR-PF-002, FR-PF-003, FR-PF-004, FR-PF-005, FR-PF-006, FR-SO-001, FR-SO-002, FR-SO-003, FR-SO-004. Association documents an interaction/context, never a permission grant.

**Documented responsibilities**
- Provide requested actual technical assessments and findings; independence is evidenced, not asserted by role name

**Documented operation concepts — NOT permissions**
- Assess design/security/quality evidence in authorized scope only

**Authorization boundary:** Advisory to unified final owner unless identified binding external obligation requires independent approval; cannot waive controls or convert failed cases PASS.

**Tenant boundary:** No runtime Tenant or operator rights granted by reviewer status.

**Assignment / approved role:** UNASSIGNED / UNASSIGNED. No person/workload instantiated here.

**Source evidence:** EVID-A001-015, EVID-A001-016

**Unresolved requirements**
- Specific reviewers UNASSIGNED unless independently documented; no specialist sign-off claimed; binding obligations must be evidenced

**Question register links:** PDQ-A001-001, PDQ-A001-002, PDQ-A001-003, PDQ-A001-004, PDQ-A001-005, PDQ-A001-006, PDQ-A001-007, PDQ-A001-008, PDQ-A001-009, PDQ-A001-010, PDQ-A001-011, PDQ-A001-012, PDQ-A001-013, PDQ-A001-014, PDQ-A001-015, PDQ-A001-016, PDQ-A001-017, PDQ-A001-018, PDQ-A001-019, PDQ-A001-020, PDQ-A001-021, PDQ-A001-022, PDQ-A001-023, PDQ-A001-024, PDQ-A001-025, PDQ-A001-026, PDQ-A001-027, PDQ-A001-028, PDQ-A001-029, PDQ-A001-030, PDQ-A001-031, PDQ-A001-032, PDQ-A001-033, PDQ-A001-034, PDQ-A001-035, PDQ-A001-036, PDQ-A001-037, PDQ-A001-038, PDQ-A001-039, PDQ-A001-040, PDQ-A001-041, PDQ-A001-042, PDQ-A001-043, PDQ-A001-044, PDQ-A001-045, PDQ-A001-046, PDQ-A001-047, PDQ-A001-048, PDQ-A001-049, PDQ-A001-050, PDQ-A001-051, PDQ-A001-052, PDQ-A001-053, PDQ-A001-054

## ACT-A001-025 — Existing scoped interim Quality Authority

**Category / status:** PRODUCT_GOVERNANCE_AUTHORITY / DOCUMENTED_EXISTING_SCOPED_QUALITY_ROLE

**Applicable capabilities:** FR-BJ-001, FR-BJ-002, FR-BJ-003, FR-BJ-004, FR-BJ-005, FR-PF-001, FR-PF-002, FR-PF-003, FR-PF-004, FR-PF-005, FR-PF-006, FR-SO-001, FR-SO-002, FR-SO-003, FR-SO-004. Association documents an interaction/context, never a permission grant.

**Documented responsibilities**
- Maintain accepted OD-020 contract-quality policy and evidence/risk duties within existing scope, not a new appointment

**Documented operation concepts — NOT permissions**
- Scoped Quality review of contract risk, evidence and exceptions under accepted rules

**Authorization boundary:** Technical/Quality capacities and final owner decisions remain distinct; no independent Security sign-off, mandatory-control waiver or production execution right.

**Tenant boundary:** No runtime resource rights from Quality role.

**Assignment / approved role:** EXISTING_SCOPED_TAO_ROLE_ONLY / NOT_A_RUNTIME_ROLE. No person/workload instantiated here.

**Source evidence:** EVID-A001-061, EVID-A001-013

**Unresolved requirements**
- No named assessor or completed review fabricated; current task assigns no new quality/security authority

**Question register links:** PDQ-A001-001, PDQ-A001-002, PDQ-A001-003, PDQ-A001-004, PDQ-A001-005, PDQ-A001-006, PDQ-A001-007, PDQ-A001-008, PDQ-A001-009, PDQ-A001-010, PDQ-A001-011, PDQ-A001-012, PDQ-A001-013, PDQ-A001-014, PDQ-A001-015, PDQ-A001-016, PDQ-A001-017, PDQ-A001-018, PDQ-A001-019, PDQ-A001-020, PDQ-A001-021, PDQ-A001-022, PDQ-A001-023, PDQ-A001-024, PDQ-A001-025, PDQ-A001-026, PDQ-A001-027, PDQ-A001-028, PDQ-A001-029, PDQ-A001-030, PDQ-A001-031, PDQ-A001-032, PDQ-A001-033, PDQ-A001-034, PDQ-A001-035, PDQ-A001-036, PDQ-A001-037, PDQ-A001-038, PDQ-A001-039, PDQ-A001-040, PDQ-A001-041, PDQ-A001-042, PDQ-A001-043, PDQ-A001-044, PDQ-A001-045, PDQ-A001-046, PDQ-A001-047, PDQ-A001-048, PDQ-A001-049, PDQ-A001-050, PDQ-A001-051, PDQ-A001-052, PDQ-A001-053, PDQ-A001-054

## ACT-A001-026 — Profile control-plane authority scopes (twelve documented boundaries)

**Category / status:** PLATFORM_OPERATIONAL_ACTOR / DOCUMENTED_LOGICAL_AUTHORITY_SCOPES_NOT_PRINCIPAL_ASSIGNMENTS

**Applicable capabilities:** FR-PF-001, FR-PF-002, FR-SO-001, FR-SO-003, FR-SO-004. Association documents an interaction/context, never a permission grant.

**Documented responsibilities**
- Maintain only the separately owned registry/lifecycle/placement/trust/policy/eligibility/grant/admission/operations/evidence/recovery scopes recorded in V3-020

**Documented operation concepts — NOT permissions**
- Exact twelve source control-plane rows copied as documented authority boundaries, not executable permission list

**Authorization boundary:** Co-operated planes or shared operator do not merge scopes; replicas do not gain write authority; Domain authorization and Sovereign local authority remain distinct.

**Tenant boundary:** Validated/revalidated Tenant Context; Tenant selector untrusted; cross-Tenant access not implied. Shared, Managed and Sovereign preserve logical boundaries; local authority is profile-specific.

**Assignment / approved role:** UNASSIGNED / UNASSIGNED. No person/workload instantiated here.

**Source evidence:** EVID-A001-062, EVID-A001-063, EVID-A001-064, EVID-A001-065, EVID-A001-066, EVID-A001-067, EVID-A001-068, EVID-A001-069, EVID-A001-070, EVID-A001-071, EVID-A001-072, EVID-A001-073

**Unresolved requirements**
- Actual principal/service/person realization and detailed operation/freshness/grant policies UNASSIGNED/OPEN; no runtime/control-plane deployment chosen

**Question register links:** PDQ-A001-016, PDQ-A001-017, PDQ-A001-018, PDQ-A001-019, PDQ-A001-020, PDQ-A001-021, PDQ-A001-034, PDQ-A001-035, PDQ-A001-036, PDQ-A001-040, PDQ-A001-041, PDQ-A001-042, PDQ-A001-043, PDQ-A001-044, PDQ-A001-045, PDQ-A001-046, PDQ-A001-047, PDQ-A001-048, PDQ-A001-049, PDQ-A001-050, PDQ-A001-051, PDQ-A001-052, PDQ-A001-053, PDQ-A001-054

### Existing profile control scopes (source V3-020; no assignment)

| Source row | Boundary | Existing authoritative scopes by profile | Evidence |
| --- | --- | --- | --- |
| 1 | Tenant Registry and stable Tenant ID | Stable-ID/active-registry scope — Shared: **Provider Tenant Registry Authority**; Managed: **Global Managed Tenant Registry Authority**; Sovereign: **Sovereign Tenant Registry Authority** after explicit local import. | EVID-A001-062 |
| 2 | Tenant lifecycle and suspension | Runtime-effective lifecycle scope — Shared: **Provider Tenant Lifecycle Authority**; Managed: **Global Managed Tenant Lifecycle Authority**; Sovereign: **Sovereign Tenant Lifecycle Authority**. Commercial-account scope remains separately owned by **Product Authority** and is not permission. | EVID-A001-063 |
| 3 | Cell Registry and Tenant Placement | Placement scope — Shared: **Provider Placement Authority**; Managed: **Global Managed Placement Authority**; Sovereign: **Sovereign Placement Authority**. | EVID-A001-064 |
| 4 | Trust authorities and cryptographic keys | Trust-admission/key-custody scope — Shared: **Provider Trust Authority**; Managed: **Dedicated Managed Trust Authority**; Sovereign: **Sovereign Trust Authority**. | EVID-A001-065 |
| 5 | Identity and workload trust | Issuer-admission scope — Shared: **Provider Trust Authority**; Managed: **Dedicated Managed Trust Authority**; Sovereign: **Sovereign Trust Authority**. Credential-assertion scope: the single **Admitted Identity Issuer** identified by validated issuer metadata for that credential. | EVID-A001-066 |
| 6 | Platform and local policies | Common-policy-contract scope: **Shared Policy Governance**. Activation scope — Shared: **Shared Policy Activation Authority**; Managed: **Dedicated Managed Policy Activation Authority**; Sovereign: **Sovereign Policy Authority**. Resource-rule scope: each **resource-owning Domain**. | EVID-A001-067 |
| 7 | Product entitlements and offline license verification | Commercial-evidence scope: **Product Entitlement Authority**. Eligibility-activation scope — Shared: **Shared Entitlement Eligibility Authority**; Managed: **Dedicated Managed Entitlement Eligibility Authority**; Sovereign: **Sovereign Entitlement Eligibility Authority**. Permission scope: each **resource-owning Domain**. | EVID-A001-068 |
| 8 | Administrative and user Grants | Platform/admin-grant scope — Shared: **Shared Platform Grant Authority**; Managed: **Dedicated Managed Grant Authority**; Sovereign: **Sovereign Grant Authority**. Resource-grant scope: each **resource-owning Domain**. Plugin Installation-grant scope: the profile's **Plugin Control Plane**. | EVID-A001-069 |
| 9 | Application admission and Client Registration | Admission scope — Shared: **Shared Admission Authority**; Managed: **Dedicated Managed Admission Authority**; Sovereign: **Sovereign Admission Authority**. | EVID-A001-070 |
| 10 | Deployment, operations and support authority | Infrastructure-operation scope — Shared: **Provider Operations Authority**; Managed: **Dedicated Managed Operations Authority**; Sovereign: **Sovereign Operations Authority**. Destination business-operation scope remains with each **resource-owning Domain**. | EVID-A001-071 |
| 11 | Audit evidence and operational telemetry | Business-fact scope: each **producing Domain**. Authoritative Audit-record scope: the profile's **Audit Domain**. Operational-telemetry scope: the profile's **Observability Authority**. | EVID-A001-072 |
| 12 | Recovery and emergency administrative access | Infrastructure-recovery scope — Shared: **Provider Recovery Authority**; Managed: **Dedicated Managed Recovery Authority**; Sovereign: **Sovereign Recovery Authority**. Durable Domain-evidence scope remains with its **owning Domain**; emergency business-action authorization remains with the **destination Domain**. | EVID-A001-073 |
