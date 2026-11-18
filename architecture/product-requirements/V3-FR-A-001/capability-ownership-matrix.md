# Capability ownership matrix — V3-FR-A-001

**Exactly fifteen approved FIRST_RELEASE capabilities.** Existing logical owners/authorizers are preserved, not reassigned. All fifteen named accountable Business Owners and operation-owner persons are **UNASSIGNED**. Named deployables are **UNASSIGNED**, topology **OPEN**, not one service per inventory entry. The existing final internal Product Decision Owner/TAO is not automatically nominated as each Business Owner.

| Capability | Original title | Approved logical owner(s) | Ownership decision(s) | Accountable Business Owner |
| --- | --- | --- | --- | --- |
| FR-BJ-001 | Register and Maintain Customer Master | Customer Domain | V3-002B-DEC-002 | UNASSIGNED |
| FR-BJ-002 | Find and Review Customer | Customer Domain | V3-002B-DEC-002 | UNASSIGNED |
| FR-BJ-003 | Manage Opportunity Through the Sales Pipeline | Sales Domain | V3-002B-DEC-006 | UNASSIGNED |
| FR-BJ-004 | Register and Process a Customer Request | Customer Request Domain within the logical Workflow capability | V3-002B-DEC-012 | UNASSIGNED |
| FR-BJ-005 | Plan and Track a Work Task | Work Domain | V3-002B-DEC-035 | UNASSIGNED |
| FR-PF-001 | Establish Trusted Tenant Access | Identity Trust Capability in Platform Core; Tenant Management Capability in Platform Core | V3-002B-DEC-053, V3-002B-DEC-054 | UNASSIGNED |
| FR-PF-002 | Evaluate Feature Eligibility | Independent logical Entitlement capability in Platform Core | V3-002B-DEC-018 | UNASSIGNED |
| FR-PF-003 | Enforce Quota-Controlled Operation | Independent logical Quota capability in Platform Core | V3-002B-DEC-021 | UNASSIGNED |
| FR-PF-004 | Deliver Authorized In-App Notification | Notification Domain | V3-002B-DEC-009 | UNASSIGNED |
| FR-PF-005 | Attach and Retrieve File for an Approved Resource | File/Content Domain for file state; Resource-owning Domain for attachment meaning and relation | V3-002B-DEC-038 | UNASSIGNED |
| FR-PF-006 | Produce an Approved Deterministic Report | Reporting Capability for report resources; Producing Domains retain Business Facts | V3-002B-DEC-028 | UNASSIGNED |
| FR-SO-001 | Record Security, Administrative and Privileged Audit Evidence | Audit Domain for system-wide Audit records; Producing Domains retain Business Facts and Domain-specific Audit | V3-002B-DEC-014 | UNASSIGNED |
| FR-SO-002 | Review Authorized Audit Evidence | Audit Domain for system-wide Audit records; Producing Domains retain Business Facts and Domain-specific Audit | V3-002B-DEC-014 | UNASSIGNED |
| FR-SO-003 | Observe Platform and Service Health | Operational Platform Capability for operational state; source services and logical domains retain their authorities | V3-002B-DEC-050 | UNASSIGNED |
| FR-SO-004 | Execute an Authorized Privileged Operation | Operational Platform Capability for operational state; source services and logical domains retain their authorities | V3-002B-DEC-050 | UNASSIGNED |

## FR-BJ-001 — Register and Maintain Customer Master

**Business domain / boundary:** Customer Domain. Undecided deployment boundary

**Named accountable Business Owner / operation owner / deployable:** UNASSIGNED / UNASSIGNED / UNASSIGNED. Topology OPEN.

**Authoritative data ownership**
- Customer-owned company, person, contact, branch and relationship records; Customer Domain is authoritative and owns writes

**Operation and final resource authorization ownership**
- Customer Domain enforces resource/action authorization; Platform Core supplies validated tenant/membership context

**Decision authority:** existing user/Product Decision Owner/TAO for explicit project decisions; runtime final resource authorization remains in the named owning boundary, with distinct profile authority and local Sovereign scope.

**Cross-domain dependencies**
- Identity/Tenant Context and Customer authorization mandatory
- Customer mutation Audit obligations mandatory for covered successful mutations; exact failure policy OPEN
- Entitlement/Quota/Attachment/Notification integration only where separately required

**Documented responsibility:** Company/person/contact master maintenance; Customer owns branch and relationship facts

**Actor context:** ACT-A001-001, ACT-A001-002, ACT-A001-015, ACT-A001-016, ACT-A001-022, ACT-A001-023, ACT-A001-024, ACT-A001-025 (not granted access)

**Approved ownership decisions:** V3-002B-DEC-002

**Evidence IDs:** EVID-A001-028, EVID-A001-043

**Open ownership/product questions:** PDQ-A001-001, PDQ-A001-002, PDQ-A001-003

**Profiles:** Shared SaaS / Dedicated Managed / Dedicated Sovereign; compatible semantics, independent implementation/security/profile evidence.

## FR-BJ-002 — Find and Review Customer

**Business domain / boundary:** Customer Domain. Undecided deployment boundary

**Named accountable Business Owner / operation owner / deployable:** UNASSIGNED / UNASSIGNED / UNASSIGNED. Topology OPEN.

**Authoritative data ownership**
- Customer-owned company, person, contact, branch and relationship records; Customer Domain is authoritative and owns writes

**Operation and final resource authorization ownership**
- Customer Domain enforces resource/action authorization; Platform Core supplies validated tenant/membership context

**Decision authority:** existing user/Product Decision Owner/TAO for explicit project decisions; runtime final resource authorization remains in the named owning boundary, with distinct profile authority and local Sovereign scope.

**Cross-domain dependencies**
- Identity/Tenant and Customer disclosure authorization mandatory
- Search remains Customer-owned; no selected engine
- Safe explicit Customer disclosure-denial Audit; no universal successful-read event

**Documented responsibility:** Authorized retrieval and business search; disclosure belongs to Customer

**Actor context:** ACT-A001-001, ACT-A001-003, ACT-A001-015, ACT-A001-022, ACT-A001-023, ACT-A001-024, ACT-A001-025 (not granted access)

**Approved ownership decisions:** V3-002B-DEC-002

**Evidence IDs:** EVID-A001-029, EVID-A001-043

**Open ownership/product questions:** PDQ-A001-004, PDQ-A001-005, PDQ-A001-006

**Profiles:** Shared SaaS / Dedicated Managed / Dedicated Sovereign; compatible semantics, independent implementation/security/profile evidence.

## FR-BJ-003 — Manage Opportunity Through the Sales Pipeline

**Business domain / boundary:** Sales Domain. Undecided deployment boundary

**Named accountable Business Owner / operation owner / deployable:** UNASSIGNED / UNASSIGNED / UNASSIGNED. Topology OPEN.

**Authoritative data ownership**
- Sales-owned Opportunity, Pipeline, Stage Transition and Opportunity amount/currency; Sales Domain is authoritative and owns writes

**Operation and final resource authorization ownership**
- Sales Domain makes and enforces final Opportunity resource/action authorization

**Decision authority:** existing user/Product Decision Owner/TAO for explicit project decisions; runtime final resource authorization remains in the named owning boundary, with distinct profile authority and local Sovereign scope.

**Cross-domain dependencies**
- Customer reference by versioned contract/authorized projection; no private SQL
- Identity/Tenant and Sales authorization mandatory
- Product Catalog/Lead Source/Pain Point/Use Case LATER_RELEASE; amount/currency independent

**Documented responsibility:** Opportunity/Pipeline core and Customer contract reference; amount/currency independent of Product Catalog

**Actor context:** ACT-A001-001, ACT-A001-004, ACT-A001-015, ACT-A001-022, ACT-A001-023, ACT-A001-024, ACT-A001-025 (not granted access)

**Approved ownership decisions:** V3-002B-DEC-006

**Evidence IDs:** EVID-A001-030, EVID-A001-044

**Open ownership/product questions:** PDQ-A001-007, PDQ-A001-008, PDQ-A001-009

**Profiles:** Shared SaaS / Dedicated Managed / Dedicated Sovereign; compatible semantics, independent implementation/security/profile evidence.

## FR-BJ-004 — Register and Process a Customer Request

**Business domain / boundary:** Customer Request Domain within the logical Workflow capability. Undecided deployment boundary; no mandatory generic Workflow Engine

**Named accountable Business Owner / operation owner / deployable:** UNASSIGNED / UNASSIGNED / UNASSIGNED. Topology OPEN.

**Authoritative data ownership**
- Request, Lifecycle, Status History, Triage and Assignment; Customer Request Domain is authoritative and owns writes

**Operation and final resource authorization ownership**
- Customer Request Domain makes and enforces final Request resource/action authorization; Assignment grants no authority

**Decision authority:** existing user/Product Decision Owner/TAO for explicit project decisions; runtime final resource authorization remains in the named owning boundary, with distinct profile authority and local Sovereign scope.

**Cross-domain dependencies**
- Customer reference contract; Request authorization independent
- No Portal/generic Workflow Engine prerequisite
- Automatic Task/Opportunity/Document links LATER_RELEASE

**Documented responsibility:** Internal creation, Customer reference, view/tracking, base lifecycle, status history and assignment

**Actor context:** ACT-A001-001, ACT-A001-005, ACT-A001-015, ACT-A001-022, ACT-A001-023, ACT-A001-024, ACT-A001-025 (not granted access)

**Approved ownership decisions:** V3-002B-DEC-012

**Evidence IDs:** EVID-A001-031, EVID-A001-046

**Open ownership/product questions:** PDQ-A001-010, PDQ-A001-011, PDQ-A001-012

**Profiles:** Shared SaaS / Dedicated Managed / Dedicated Sovereign; compatible semantics, independent implementation/security/profile evidence.

## FR-BJ-005 — Plan and Track a Work Task

**Business domain / boundary:** Work Domain. Undecided deployment boundary

**Named accountable Business Owner / operation owner / deployable:** UNASSIGNED / UNASSIGNED / UNASSIGNED. Topology OPEN.

**Authoritative data ownership**
- Work owns Task, Task Lifecycle/Status, Due Date, Assignment Record and cross-domain Link Metadata

**Operation and final resource authorization ownership**
- Work authorizes only Task resources; Assignment/links grant no Membership, Entitlement or authorization to related resources

**Decision authority:** existing user/Product Decision Owner/TAO for explicit project decisions; runtime final resource authorization remains in the named owning boundary, with distinct profile authority and local Sovereign scope.

**Cross-domain dependencies**
- Work authorization and validated Tenant Context
- Manual links preserve related-domain authorization
- Assignment grants no related-resource access; automatic integration deferred

**Documented responsibility:** Create/view/edit, assignment, status, due date and manual contract-based links

**Actor context:** ACT-A001-001, ACT-A001-006, ACT-A001-015, ACT-A001-022, ACT-A001-023, ACT-A001-024, ACT-A001-025 (not granted access)

**Approved ownership decisions:** V3-002B-DEC-035

**Evidence IDs:** EVID-A001-032, EVID-A001-051

**Open ownership/product questions:** PDQ-A001-013, PDQ-A001-014, PDQ-A001-015

**Profiles:** Shared SaaS / Dedicated Managed / Dedicated Sovereign; compatible semantics, independent implementation/security/profile evidence.

## FR-PF-001 — Establish Trusted Tenant Access

**Business domain / boundary:** Identity Trust Capability in Platform Core; Tenant Management Capability in Platform Core. Undecided deployment boundary; Undecided deployment boundary

**Named accountable Business Owner / operation owner / deployable:** UNASSIGNED / UNASSIGNED / UNASSIGNED. Topology OPEN.

**Authoritative data ownership**
- Identity owns Principal Identity, Credential/Authenticator Registration, External Identity Mapping, Authentication State, Session/Refresh/Revocation State and Token-Issuance Metadata; Tenant, Entitlement, Portal and business ownerships remain separate
- Tenant Management owns Tenant, Organization, Tenant Lifecycle, Organization/Tenant Membership, Membership Status, Principal-to-Tenant Association and Membership Role Assignment; Identity, Entitlement and business ownerships remain separate

**Operation and final resource authorization ownership**
- Identity decides only Principal/Session validity; token/session grants no Membership, Entitlement or business authorization; Tenant switching revalidates Membership/Context; Dedicated Sovereign authority is local
- Tenant Management authorizes its own resources and membership administration only; Membership/role grants no Entitlement or business authorization; Dedicated Sovereign authority is local

**Decision authority:** existing user/Product Decision Owner/TAO for explicit project decisions; runtime final resource authorization remains in the named owning boundary, with distinct profile authority and local Sovereign scope.

**Cross-domain dependencies**
- Identity Principal/session validity and Tenant Management Membership are distinct
- Resource-owning Domains retain final operation authority
- Entitlement when applicable never substitutes for Membership/authorization

**Documented responsibility:** Approved Option B: internal authenticated Principal, active Membership, valid/revalidated Tenant Context, destination Membership validation for switching

**Actor context:** ACT-A001-001, ACT-A001-011, ACT-A001-015, ACT-A001-018, ACT-A001-019, ACT-A001-022, ACT-A001-023, ACT-A001-024, ACT-A001-025, ACT-A001-026 (not granted access)

**Approved ownership decisions:** V3-002B-DEC-053, V3-002B-DEC-054

**Evidence IDs:** EVID-A001-033, EVID-A001-054, EVID-A001-055

**Open ownership/product questions:** PDQ-A001-016, PDQ-A001-017, PDQ-A001-018

**Profiles:** Shared SaaS / Dedicated Managed / Dedicated Sovereign; compatible semantics, independent implementation/security/profile evidence.

## FR-PF-002 — Evaluate Feature Eligibility

**Business domain / boundary:** Independent logical Entitlement capability in Platform Core. Undecided deployment boundary

**Named accountable Business Owner / operation owner / deployable:** UNASSIGNED / UNASSIGNED / UNASSIGNED. Topology OPEN.

**Authoritative data ownership**
- Entitlement owns authoritative Feature Assignment, effective Entitlement state and Eligibility evaluation results; Plan/Subscription facts, Billing, Pricing and Quota ownership remain separate

**Operation and final resource authorization ownership**
- Entitlement decides eligibility only; each Resource-owning Domain makes and enforces final Resource/Action Authorization; Dedicated Sovereign authority/evaluation is local

**Decision authority:** existing user/Product Decision Owner/TAO for explicit project decisions; runtime final resource authorization remains in the named owning boundary, with distinct profile authority and local Sovereign scope.

**Cross-domain dependencies**
- Tenant/Organization references remain Tenant Management-owned
- Plan/Subscription source facts owner OPEN; Billing/Pricing not implicitly owned here
- Each capability mapping separately defined; no business permission from eligibility

**Documented responsibility:** Feature Assignment and effective eligibility, traceable to Tenant/Organization and approved Plan/Subscription facts

**Actor context:** ACT-A001-001, ACT-A001-015, ACT-A001-019, ACT-A001-022, ACT-A001-023, ACT-A001-024, ACT-A001-025, ACT-A001-026 (not granted access)

**Approved ownership decisions:** V3-002B-DEC-018

**Evidence IDs:** EVID-A001-034, EVID-A001-048

**Open ownership/product questions:** PDQ-A001-019, PDQ-A001-020, PDQ-A001-021

**Profiles:** Shared SaaS / Dedicated Managed / Dedicated Sovereign; compatible semantics, independent implementation/security/profile evidence.

## FR-PF-003 — Enforce Quota-Controlled Operation

**Business domain / boundary:** Independent logical Quota capability in Platform Core. Undecided deployment boundary

**Named accountable Business Owner / operation owner / deployable:** UNASSIGNED / UNASSIGNED / UNASSIGNED. Topology OPEN.

**Authoritative data ownership**
- Quota owns authoritative Effective Limit, Reservation Ledger, Usage/Consumption State, Reconciliation State and Quota Decision Results; producers retain source Usage Facts

**Operation and final resource authorization ownership**
- Producing Resource-owning Domain makes and enforces final Resource/Action Authorization; Dedicated Sovereign Quota authority/control is local

**Decision authority:** existing user/Product Decision Owner/TAO for explicit project decisions; runtime final resource authorization remains in the named owning boundary, with distinct profile authority and local Sovereign scope.

**Cross-domain dependencies**
- Producing Domain owns operation and source Usage Facts
- Entitlement eligibility distinct from Limit/Reservation/Usage
- Each consuming-capability integration requires approval

**Documented responsibility:** Effective limits, Usage, atomic Reservation/Commit/Release, reconciliation and Reason/Period/Correlation

**Actor context:** ACT-A001-001, ACT-A001-015, ACT-A001-016, ACT-A001-022, ACT-A001-023, ACT-A001-024, ACT-A001-025 (not granted access)

**Approved ownership decisions:** V3-002B-DEC-021

**Evidence IDs:** EVID-A001-035, EVID-A001-049

**Open ownership/product questions:** PDQ-A001-022, PDQ-A001-023, PDQ-A001-024

**Profiles:** Shared SaaS / Dedicated Managed / Dedicated Sovereign; compatible semantics, independent implementation/security/profile evidence.

## FR-PF-004 — Deliver Authorized In-App Notification

**Business domain / boundary:** Notification Domain. Undecided deployment boundary

**Named accountable Business Owner / operation owner / deployable:** UNASSIGNED / UNASSIGNED / UNASSIGNED. Topology OPEN.

**Authoritative data ownership**
- Notification-owned Template, Rule, Lifecycle, Delivery Ledger, Delivery Attempts, Deduplication, Retry State and In-App records; physical persistence design remains undecided

**Operation and final resource authorization ownership**
- Notification authorizes Notification resources and recipient access only; producer retains business-operation authorization

**Decision authority:** existing user/Product Decision Owner/TAO for explicit project decisions; runtime final resource authorization remains in the named owning boundary, with distinct profile authority and local Sovereign scope.

**Cross-domain dependencies**
- Producing Domain owns Business Fact and original operation authorization
- Notification owns recipient/delivery state only
- In-App only; Email/SMS/Push deferred

**Documented responsibility:** Core + In-App: Template, base Rule/lifecycle, Delivery Ledger, deduplication, retry/Audit

**Actor context:** ACT-A001-001, ACT-A001-007, ACT-A001-015, ACT-A001-016, ACT-A001-022, ACT-A001-023, ACT-A001-024, ACT-A001-025 (not granted access)

**Approved ownership decisions:** V3-002B-DEC-009

**Evidence IDs:** EVID-A001-036, EVID-A001-045

**Open ownership/product questions:** PDQ-A001-025, PDQ-A001-026, PDQ-A001-027

**Profiles:** Shared SaaS / Dedicated Managed / Dedicated Sovereign; compatible semantics, independent implementation/security/profile evidence.

## FR-PF-005 — Attach and Retrieve File for an Approved Resource

**Business domain / boundary:** File/Content Domain for file state; Resource-owning Domain for attachment meaning and relation. Undecided deployment boundary

**Named accountable Business Owner / operation owner / deployable:** UNASSIGNED / UNASSIGNED / UNASSIGNED. Topology OPEN.

**Authoritative data ownership**
- File/Content owns File Metadata, Content/Object Lifecycle, Storage Reference, Integrity/Checksum and Validation/Quarantine State; resource owner owns Attachment semantics and relationship to its Business Resource

**Operation and final resource authorization ownership**
- File Domain authorizes the file and Resource-owning Domain authorizes attachment operations and related-resource access; File ID/link grants no authority; Dedicated Sovereign authority is local

**Decision authority:** existing user/Product Decision Owner/TAO for explicit project decisions; runtime final resource authorization remains in the named owning boundary, with distinct profile authority and local Sovereign scope.

**Cross-domain dependencies**
- File Domain owns object/file state; resource Domain owns Attachment relation
- Both authorizations required; resource-by-resource attachment approval
- Provider/scanning/retention OPEN; attachment unlink not automatic object deletion

**Documented responsibility:** Metadata, controlled upload/download, base lifecycle and contract-based attachments

**Actor context:** ACT-A001-001, ACT-A001-008, ACT-A001-015, ACT-A001-022, ACT-A001-023, ACT-A001-024, ACT-A001-025 (not granted access)

**Approved ownership decisions:** V3-002B-DEC-038

**Evidence IDs:** EVID-A001-037, EVID-A001-052

**Open ownership/product questions:** PDQ-A001-028, PDQ-A001-029, PDQ-A001-030

**Profiles:** Shared SaaS / Dedicated Managed / Dedicated Sovereign; compatible semantics, independent implementation/security/profile evidence.

## FR-PF-006 — Produce an Approved Deterministic Report

**Business domain / boundary:** Reporting Capability for report resources; Producing Domains retain Business Facts. Undecided deployment boundary

**Named accountable Business Owner / operation owner / deployable:** UNASSIGNED / UNASSIGNED / UNASSIGNED. Topology OPEN.

**Authoritative data ownership**
- Reporting owns Report Catalog/Definition Metadata, Execution State, Generated Report Artifact/Snapshot and its authorized dedicated Projections; producers own source Business Facts

**Operation and final resource authorization ownership**
- Reporting authorizes its report resources subject to Tenant Isolation and source disclosure constraints; projections cannot bypass source authorization; Dedicated Sovereign authority is local

**Decision authority:** existing user/Product Decision Owner/TAO for explicit project decisions; runtime final resource authorization remains in the named owning boundary, with distinct profile authority and local Sovereign scope.

**Cross-domain dependencies**
- Reporting owns definitions/execution/artifact/projections; producers own facts
- Approved Report Sets, source freshness and disclosure rules required
- No cross-service SQL, advanced/custom builder or mandatory synchronous per-record source checks

**Documented responsibility:** Reporting Core: approved deterministic tenant-scoped Report Sets, execution/artifact and authorized projections

**Actor context:** ACT-A001-001, ACT-A001-009, ACT-A001-015, ACT-A001-016, ACT-A001-022, ACT-A001-023, ACT-A001-024, ACT-A001-025 (not granted access)

**Approved ownership decisions:** V3-002B-DEC-028

**Evidence IDs:** EVID-A001-038, EVID-A001-050

**Open ownership/product questions:** PDQ-A001-031, PDQ-A001-032, PDQ-A001-033

**Profiles:** Shared SaaS / Dedicated Managed / Dedicated Sovereign; compatible semantics, independent implementation/security/profile evidence.

## FR-SO-001 — Record Security, Administrative and Privileged Audit Evidence

**Business domain / boundary:** Audit Domain for system-wide Audit records; Producing Domains retain Business Facts and Domain-specific Audit. Undecided deployment boundary

**Named accountable Business Owner / operation owner / deployable:** UNASSIGNED / UNASSIGNED / UNASSIGNED. Topology OPEN.

**Authoritative data ownership**
- Audit Domain is authoritative for system-wide security, administrative and Privileged records and authorized Audit projections; producers remain authoritative for their Business Facts and Domain-specific Audit

**Operation and final resource authorization ownership**
- Audit Domain makes and enforces final access decisions for its Audit resources; Dedicated Sovereign security and operational authority is local

**Decision authority:** existing user/Product Decision Owner/TAO for explicit project decisions; runtime final resource authorization remains in the named owning boundary, with distinct profile authority and local Sovereign scope.

**Cross-domain dependencies**
- Producing Domain Business Facts/obligations distinct from authoritative Audit ingestion
- Trusted source/Tenant provenance, integrity and scoped disclosure
- No universal Audit catalog/failure/retention policy or executable DURABLE_DEFER approval

**Documented responsibility:** Append-oriented Audit Core, Tenant/Platform separation, Actor/Action/Target/Outcome/Correlation, integrity and base retention policy obligation

**Actor context:** ACT-A001-001, ACT-A001-015, ACT-A001-016, ACT-A001-017, ACT-A001-019, ACT-A001-022, ACT-A001-023, ACT-A001-024, ACT-A001-025, ACT-A001-026 (not granted access)

**Approved ownership decisions:** V3-002B-DEC-014

**Evidence IDs:** EVID-A001-039, EVID-A001-047

**Open ownership/product questions:** PDQ-A001-034, PDQ-A001-035, PDQ-A001-036

**Profiles:** Shared SaaS / Dedicated Managed / Dedicated Sovereign; compatible semantics, independent implementation/security/profile evidence.

## FR-SO-002 — Review Authorized Audit Evidence

**Business domain / boundary:** Audit Domain for system-wide Audit records; Producing Domains retain Business Facts and Domain-specific Audit. Undecided deployment boundary

**Named accountable Business Owner / operation owner / deployable:** UNASSIGNED / UNASSIGNED / UNASSIGNED. Topology OPEN.

**Authoritative data ownership**
- Audit Domain is authoritative for system-wide security, administrative and Privileged records and authorized Audit projections; producers remain authoritative for their Business Facts and Domain-specific Audit

**Operation and final resource authorization ownership**
- Audit Domain makes and enforces final access decisions for its Audit resources; Dedicated Sovereign security and operational authority is local

**Decision authority:** existing user/Product Decision Owner/TAO for explicit project decisions; runtime final resource authorization remains in the named owning boundary, with distinct profile authority and local Sovereign scope.

**Cross-domain dependencies**
- Audit Domain controls its resources, not general operator entitlement
- Sensitive access/lifecycle evidence obligations per existing bounded decisions
- Search/disclosure/purpose policy and audit-of-audit recursion OPEN

**Documented responsibility:** Authorized Audit Core viewing with Tenant/Platform scope and disclosure protection

**Actor context:** ACT-A001-001, ACT-A001-010, ACT-A001-015, ACT-A001-017, ACT-A001-022, ACT-A001-023, ACT-A001-024, ACT-A001-025 (not granted access)

**Approved ownership decisions:** V3-002B-DEC-014

**Evidence IDs:** EVID-A001-040, EVID-A001-047

**Open ownership/product questions:** PDQ-A001-037, PDQ-A001-038, PDQ-A001-039

**Profiles:** Shared SaaS / Dedicated Managed / Dedicated Sovereign; compatible semantics, independent implementation/security/profile evidence.

## FR-SO-003 — Observe Platform and Service Health

**Business domain / boundary:** Operational Platform Capability for operational state; source services and logical domains retain their authorities. Undecided deployment boundary

**Named accountable Business Owner / operation owner / deployable:** UNASSIGNED / UNASSIGNED / UNASSIGNED. Topology OPEN.

**Authoritative data ownership**
- Operational Platform owns Operational Visibility Projections, Health/Readiness Aggregation, Privileged Operation Request/Execution State and approved control state; source services own signals/configuration; domains own Business Facts; Audit/Tenant/Reporting/Notification ownerships remain unchanged

**Operation and final resource authorization ownership**
- Operational Platform authorizes only its resources; destination domain authorizes business effects; privileged actions require limited identity, explicit scope and traceable Audit; Dedicated Sovereign authority is local

**Decision authority:** existing user/Product Decision Owner/TAO for explicit project decisions; runtime final resource authorization remains in the named owning boundary, with distinct profile authority and local Sovereign scope.

**Cross-domain dependencies**
- Each Service owns source signal; Operational Platform authorized aggregation only
- Profile Observability Authority owns minimized telemetry configuration
- Telemetry is not authoritative Audit or Domain authorization; no universal operational UI

**Documented responsibility:** Operational Core health/readiness, scope separation and authorized signal aggregation

**Actor context:** ACT-A001-001, ACT-A001-012, ACT-A001-013, ACT-A001-014, ACT-A001-015, ACT-A001-019, ACT-A001-022, ACT-A001-023, ACT-A001-024, ACT-A001-025, ACT-A001-026 (not granted access)

**Approved ownership decisions:** V3-002B-DEC-050

**Evidence IDs:** EVID-A001-041, EVID-A001-053

**Open ownership/product questions:** PDQ-A001-040, PDQ-A001-041, PDQ-A001-042

**Profiles:** Shared SaaS / Dedicated Managed / Dedicated Sovereign; compatible semantics, independent implementation/security/profile evidence.

## FR-SO-004 — Execute an Authorized Privileged Operation

**Business domain / boundary:** Operational Platform Capability for operational state; source services and logical domains retain their authorities. Undecided deployment boundary

**Named accountable Business Owner / operation owner / deployable:** UNASSIGNED / UNASSIGNED / UNASSIGNED. Topology OPEN.

**Authoritative data ownership**
- Operational Platform owns Operational Visibility Projections, Health/Readiness Aggregation, Privileged Operation Request/Execution State and approved control state; source services own signals/configuration; domains own Business Facts; Audit/Tenant/Reporting/Notification ownerships remain unchanged

**Operation and final resource authorization ownership**
- Operational Platform authorizes only its resources; destination domain authorizes business effects; privileged actions require limited identity, explicit scope and traceable Audit; Dedicated Sovereign authority is local

**Decision authority:** existing user/Product Decision Owner/TAO for explicit project decisions; runtime final resource authorization remains in the named owning boundary, with distinct profile authority and local Sovereign scope.

**Cross-domain dependencies**
- Operational Platform request/execution; destination Domain effect authorization; Audit record ownership
- Profile Operations/Recovery authority for infrastructure only
- No generic Admin or emergency cross-Domain bypass; actual action/approval/recovery model OPEN

**Documented responsibility:** Scoped operational request/execution with limited identity, explicit Tenant/Platform scope, destination authorization and durable Audit

**Actor context:** ACT-A001-001, ACT-A001-012, ACT-A001-013, ACT-A001-014, ACT-A001-015, ACT-A001-019, ACT-A001-022, ACT-A001-023, ACT-A001-024, ACT-A001-025, ACT-A001-026 (not granted access)

**Approved ownership decisions:** V3-002B-DEC-050

**Evidence IDs:** EVID-A001-042, EVID-A001-053

**Open ownership/product questions:** PDQ-A001-043, PDQ-A001-044, PDQ-A001-045

**Profiles:** Shared SaaS / Dedicated Managed / Dedicated Sovereign; compatible semantics, independent implementation/security/profile evidence.
