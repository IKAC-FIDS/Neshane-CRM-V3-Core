# V3-003 decision record and FIRST_RELEASE journey inventory

## Document control

| Field | Recorded value |
| --- | --- |
| Task | `V3-003 — NFR and Threat Assumptions` |
| Architecture baseline | `NESHANE-V3-ARCH-P00-002` |
| Governance baseline | `NESHANE-V3-GOV-P00-000A` |
| Task status | `CLOSED — ANALYTICAL SCOPE ONLY` under `CDR-V3-003-2026-1030`; Security, implementation, runtime and production gates remain independent |
| Decisions recorded | `V3-003-DEC-001 — Business Criticality Assessment Methodology`; `V3-003-DEC-002 — FIRST_RELEASE Journey Inventory Taxonomy and Coverage Baseline`; `V3-003-DEC-003 — Customer Registration and Maintenance Business Criticality`; `V3-003-DEC-004 — Customer Search and Retrieval Business Criticality`; `V3-003-DEC-005 — In-System Pending Customer Submission Business Allowance`; `V3-003-DEC-006 — Logical Threat Inventory and Trust Boundary Baseline` |
| Decision statuses | `APPROVED — OWNER` |
| Approval evidence | Explicit Project Owner instructions to record approval of `V3-003-DEC-001` through `V3-003-DEC-006`; each decision retains its stated partial-coverage, review-status and non-approval boundaries |
| Approval date | Not recorded |
| Independent reviewer signature | Not recorded |
| Independent security review | Pending; not signed off |
| Readiness effect | None; this record supplies no implementation, runtime-security, operational or production-readiness evidence |

This is the authoritative task-local record for V3-003 decisions. It does not alter the architecture revision, the governance baseline, ADR-V3-001 through ADR-V3-012 or the status of any Open Decision.

## V3-003-DEC-001 — Business Criticality Assessment Methodology

**Status:** `APPROVED — OWNER`

### Decision

The Project Owner approves the V3-003 Business Criticality assessment methodology with the following rules:

1. Business Criticality (`BC`), Security Criticality (`SC`), Data Classification (`DC`), Recovery Priority (`RP`) and Availability Requirements are independent assessment dimensions.
2. The primary assessment unit is `Business Journey + Operation + Failure Scenario + Deployment Profile`.
3. `BC-1` through `BC-4` classify business impact caused by disruption:
   - `BC-1 — Mission-Critical`: disruption causes severe or unacceptable consequences to an essential business journey, with no safe and sufficiently timely workaround.
   - `BC-2 — Business-Critical`: disruption materially impairs a core workflow, but controlled recovery, an approved workaround or explicitly approved degraded operation can temporarily contain the consequences.
   - `BC-3 — Operationally Important`: disruption reduces efficiency, visibility, coordination or service quality while core workflows can continue temporarily without violating security or data-integrity requirements.
   - `BC-4 — Low-Criticality / Deferrable`: disruption has limited and tolerable business impact, and recovery may be deferred behind more critical operations.
4. `LATER_RELEASE` does not imply `BC-4`. Release Scope and Business Criticality remain separate.
5. `NOT_ASSESSED`, `CONDITIONAL` and `OUT_OF_CURRENT_RELEASE_SCOPE` are valid non-final classification states.
6. Classification uses documented qualitative evidence and explicit decision boundaries, not arbitrary weighted scores.
7. Domain-level BC is a reporting summary of Operation-level assessments and does not assign one uniform classification to every Operation in the Domain.
8. No BC classification automatically approves or establishes an SLO, RTO, RPO, latency, throughput, capacity, freshness or recovery target.
9. The current candidate Data Classification notation remains `DC-0 — Public`, `DC-1 — Internal`, `DC-2 — Tenant Confidential` and `DC-3 — Restricted`. This notation is preserved only as a candidate model and is not approved by this decision.
10. Data Classification and Data Loss Criticality are separate dimensions. No Data Loss Criticality model is approved by this decision.

### Classification boundaries

- BC describes business impact only. It is not derived from implementation technology, Security Criticality, Data Classification, Recovery Priority or deployment topology.
- Business Impact, Time Sensitivity, business Dependency Impact, safe Workaround Feasibility and business Blast Radius are direct qualitative BC inputs.
- Security compromise impact, data disclosure/loss/corruption, recovery sequencing, recovery complexity and numeric Availability targets remain separate assessments.
- A Domain, service, deployable, database or technology is not a sufficient assessment unit.
- Where business-impact evidence is insufficient, the classification remains `NOT_ASSESSED`; a high Security Criticality or Recovery Priority must not be used to infer BC.
- A `CONDITIONAL` result must name the unresolved contract, Report Set, resource integration, Tenant requirement or other dependency on which classification depends.
- `OUT_OF_CURRENT_RELEASE_SCOPE` records release placement only and makes no statement about future criticality.

### Explicit non-approvals

This decision does not approve:

- any Operation-level or Domain-level BC classification;
- any `SC`, `DC`, Data Loss Criticality or `RP` model or assignment;
- any numeric NFR target;
- any security exception or weakening of an approved security invariant;
- any degraded-mode, queueing, caching, manual-bypass or Audit-failure policy;
- any technology, implementation mechanism, protocol, product or Service Topology;
- closure of any Open Decision; or
- Architecture, Implementation, Runtime Security, Operational or Production Readiness.

### Preserved security and architecture invariants

Tenant Isolation, PostgreSQL RLS where required, validated Tenant Context, Domain-Owned Authorization, Service-Owned Data, Contract Compatibility, Sovereign-Local Authority and Fail-closed behavior when valid authority cannot be established remain mandatory. Business continuity may not bypass these controls.

### Security-sensitive Operation boundary

Session Revocation, Emergency Privileged-Access Revocation, Tenant Suspension, Incident Audit Search, Security Audit Recording, Entitlement Evaluation and Quota Reservation/Consumption remain `NOT_ASSESSED` for BC until sufficient business-impact evidence receives separate Owner approval. Their security importance or proposed Recovery Priority does not establish a BC level.

### Decision effect

This approval authorizes use of the methodology for subsequent V3-003 evidence collection and classification preparation only. Every final classification and every numeric target requires separate evidence and explicit approval.

### Traceability

- Architecture and readiness boundaries: [Architecture baseline](../baseline-v3.md), [ADR-V3-010](../adr/010-operational-profiles.md) and [ADR-V3-012](../adr/012-evidence-based-readiness.md).
- Tenant, authorization and data safeguards: [ADR-V3-003](../adr/003-cell-based-hybrid-tenancy.md), [ADR-V3-005](../adr/005-domain-owned-authorization.md), [ADR-V3-007](../adr/007-data-messaging-baseline.md) and the [Security standard](../standards/security.md).
- Sovereign-local authority: [ADR-V3-004](../adr/004-sovereign-authority.md).
- Contract compatibility: [ADR-V3-008](../adr/008-contract-compatibility.md).
- Numeric NFR targets: [OD-023](../open-decisions.md); it remains Open.
- FIRST_RELEASE scope and logical ownership evidence: [V3-002B Owner Decision Record](../../migration/v2-owner-review.md).
- Approval provenance: explicit Project Owner instruction for `V3-003 — Record Owner Approval of DEC-001`; no approval date, reviewer identity, signature or additional stakeholder sign-off was supplied.

All `OD-001` through `OD-023` remain Open.

## V3-003-DEC-002 — FIRST_RELEASE Journey Inventory Taxonomy and Coverage Baseline

**Status:** `APPROVED — OWNER`

### Approval provenance

| Field | Recorded value |
| --- | --- |
| Decision ID | `V3-003-DEC-002` |
| Decision title | `FIRST_RELEASE Journey Inventory Taxonomy and Coverage Baseline` |
| Approval authority | Project Owner |
| Approval evidence | Explicit Project Owner instruction to record approval of `V3-003-DEC-002`, subject to the mandatory inventory-coverage clarification below |
| Approval date | Not recorded |
| Stakeholder signatures | Not recorded |
| Independent reviewer sign-off | Not recorded |

### Decision scope

This decision approves the FIRST_RELEASE inventory taxonomy, the fifteen stable inventory identifiers, responsibility boundaries, inventory-level coverage and traceability to previously approved FIRST_RELEASE capability scope. It also establishes the known requirements-maturity gaps and the conditions for future refinement.

This decision does not change the Architecture Baseline, Governance Baseline, any ADR, any Open Decision or any previously approved Product Scope or Domain/Data Ownership decision.

### Mandatory coverage clarification

> The inventory provides complete coverage of the currently approved FIRST_RELEASE capability scope at the inventory level. This does not imply completeness or approval of detailed business requirements, operation catalogs, acceptance criteria, or implementation specifications.

This clarification limits the meaning of inventory coverage and does not alter the approved FIRST_RELEASE product scope.

### Inventory taxonomy

- `FR-BJ-* — Business Journeys`: end-to-end journeys that directly pursue an identifiable business objective for a Business Actor.
- `FR-PF-* — Supporting Platform Capabilities`: platform or cross-cutting journeys that support one or more Business Journeys. Their future Business Criticality assessment must be based on actual impact on dependent Business Journeys.
- `FR-SO-* — Security and Operational Journeys`: security or operational journeys with explicit actors, trust boundaries, start/completion conditions and failure scenarios.

The taxonomy does not define a Service, deployable, database or Service Topology.

### Separation of decision dimensions

| Dimension | Meaning in this baseline | Decision status |
| --- | --- | --- |
| Approved Release Scope | Whether the capability is already approved for FIRST_RELEASE | Preserved from existing Owner Decisions |
| Inventory Classification | Whether an entry is `FR-BJ`, `FR-PF` or `FR-SO` | Approved by this decision |
| Requirements Maturity | Completeness of requirements, actors, contracts, state models and evidence | Gaps remain Open |
| Business Criticality Assessment Status | BC status for a Journey or Operation | Every entry and Operation remains `NOT_ASSESSED` |

Incomplete requirements do not automatically alter approved Release Scope.

### Preserved architectural dependencies and boundaries

1. Identity Trust retains ownership of Principal Identity, Credential/Authenticator, Authentication, Session/Refresh/Revocation and Token-Issuance Metadata.
2. Tenant Management retains ownership of Tenant, Organization, Membership, Membership Status and Principal-to-Tenant Association.
3. Entitlement owns Feature Eligibility only and does not replace Membership or Resource/Action Authorization.
4. Each Resource-owning Domain makes and enforces the final authorization decision for its Operations and resources.
5. Authentication, Session, Membership, Entitlement, Assignment, a cross-domain Link or a File ID does not independently grant Business Authorization.
6. Tenant Context must be validated and revalidated at Trust Boundaries. Tenant Isolation and PostgreSQL RLS remain required where applicable.
7. Services retain ownership of their data and private persistence. Direct Cross-Service Database Access remains prohibited.
8. Cross-domain integration uses authorized versioned API/Event Contracts or authorized owned Projections.
9. Dedicated Sovereign retains local authority and has no mandatory synchronous Central dependency for critical business or security Operations.
10. Shared SaaS, Dedicated Managed and Dedicated Sovereign remain applicable assessment profiles.

### Approved inventory baseline

#### Business Journeys — five entries

| Stable ID | Inventory entry | Primary responsibility | Release Scope | Requirements Maturity | BC status |
| --- | --- | --- | --- | --- | --- |
| `FR-BJ-001` | Register and Maintain Customer Master | Customer Domain owns Customer Master and Customer resource/action Authorization | `FIRST_RELEASE — APPROVED` | Customer business rules, duplicate handling, merge, deletion and retention remain incomplete | `NOT_ASSESSED` |
| `FR-BJ-002` | Find and Review Customer | Customer Domain owns Customer retrieval, disclosure and business-search semantics | `FIRST_RELEASE — APPROVED` | Search requirements, result scope, freshness and disclosure fields remain incomplete | `NOT_ASSESSED` |
| `FR-BJ-003` | Manage Opportunity Through the Sales Pipeline | Sales Domain owns Opportunity, Pipeline, Stage Transition and amount/currency | `FIRST_RELEASE — APPROVED` | Stage model, currency rules, concurrency and completion semantics remain incomplete | `NOT_ASSESSED` |
| `FR-BJ-004` | Register and Process a Customer Request | Customer Request Domain owns Request, Lifecycle, Triage, Status History and Assignment | `FIRST_RELEASE — APPROVED` | Request categories, State Machine, escalation and completion semantics remain incomplete | `NOT_ASSESSED` |
| `FR-BJ-005` | Plan and Track a Work Task | Work Domain owns Task, Status, Due Date, Assignment and cross-domain Link Metadata | `FIRST_RELEASE — APPROVED` | Task State Machine, assignment eligibility, overdue rules and completion semantics remain incomplete | `NOT_ASSESSED` |

`CUS-SEARCH` names a business operation for finding Customer records. It approves no Search Engine, indexing design, query technology, cache, API shape or other implementation selection.

#### Supporting Platform Capabilities — six entries

| Stable ID | Inventory entry | Primary responsibility and boundary | Release Scope | Requirements Maturity | BC status |
| --- | --- | --- | --- | --- | --- |
| `FR-PF-001` | Establish Trusted Tenant Access | Composite access journey across Identity Trust and Tenant Management; the Resource-owning Domain remains final Authorizer | Mandatory architectural foundation for protected FIRST_RELEASE journeys; explicit product-capability scope confirmation remains required | IdP, Session/Revocation, Tenant-switch, Membership Policy and supported Principal journeys remain incomplete | `NOT_ASSESSED` |
| `FR-PF-002` | Evaluate Feature Eligibility | Entitlement owns Feature Assignment, effective Entitlement state and Eligibility results; it grants no Business Authorization | `FIRST_RELEASE — APPROVED` | Capability mapping, Plan/Subscription ownership, validity and freshness remain incomplete | `NOT_ASSESSED` |
| `FR-PF-003` | Enforce Quota-Controlled Operation | Quota owns Limit, Reservation/Usage state and decision results; the Producing Domain owns the Business Operation | `FIRST_RELEASE — APPROVED` | Each Capability integration, Limit Model, period/reset and Reservation semantics require independent approval | `NOT_ASSESSED` |
| `FR-PF-004` | Deliver Authorized In-App Notification | Notification owns Notification state and recipient access; the Producing Domain retains its Business Fact | `FIRST_RELEASE Core + In-App — APPROVED` | Notification types, recipient rules, timing and retry bounds remain incomplete | `NOT_ASSESSED` |
| `FR-PF-005` | Attach and Retrieve File for an Approved Resource | File/Content owns File state; the Resource-owning Domain owns Attachment meaning and relation authorization | `FIRST_RELEASE — APPROVED` | Resource Attachment matrix, validation/quarantine, retention and detailed lifecycle remain incomplete | `NOT_ASSESSED` |
| `FR-PF-006` | Produce an Approved Deterministic Report | Reporting owns Report Metadata, Execution State, Artifact and authorized owned Projections; Producing Domains retain source facts | `FIRST_RELEASE Reporting Core — APPROVED` | Final Report Sets, Business Owners, source freshness, disclosure and retention remain incomplete | `NOT_ASSESSED` |

`FR-PF-001` is a composite access journey for end-to-end assessment and traceability only. It does not merge Identity Trust and Tenant Management, create shared authority, require a single Service or database, or transfer Entitlement or Resource/Action Authorization into either capability. The responsibility chain remains explicit:

`Identity validation → Membership/Tenant Context → Entitlement where applicable → Resource-owning Domain Authorization`

Reporting Core remains explicitly within FIRST_RELEASE. Missing Final Report Set definitions are a Requirements Maturity gap, not a Release Scope change. No specific Report Set is approved by this decision.

#### Security and Operational Journeys — four entries

| Stable ID | Inventory entry | Primary responsibility and boundary | Release Scope | Requirements Maturity | BC status |
| --- | --- | --- | --- | --- | --- |
| `FR-SO-001` | Record Security, Administrative and Privileged Audit Evidence | Audit Domain owns system-wide Audit records; the Producing Domain retains its Business Fact | `FIRST_RELEASE Audit Core — APPROVED` | Mandatory event catalog, failure semantics, retention duration and integrity procedures remain incomplete | `NOT_ASSESSED` |
| `FR-SO-002` | Review Authorized Audit Evidence | Audit Domain authorizes access to its Audit resources | `FIRST_RELEASE Audit Core — APPROVED` | Search use cases, incident deadlines, disclosure rules and evidence-completeness requirements remain incomplete | `NOT_ASSESSED` |
| `FR-SO-003` | Observe Platform and Service Health | Operational Platform owns authorized aggregation/projection; each Service owns its source signal | `FIRST_RELEASE Operational Core — APPROVED` | Signal catalog, Health/Readiness semantics and visibility requirements remain incomplete | `NOT_ASSESSED` |
| `FR-SO-004` | Execute an Authorized Privileged Operation | Operational Platform owns request/execution state; the destination Domain authorizes the Operation; Audit owns the Audit record | `FIRST_RELEASE Operational Core — APPROVED` | Privileged Role Model, action catalog, failure handling and recovery semantics remain incomplete | `NOT_ASSESSED` |

### Application of V3-003-DEC-001

The approved methodology in `V3-003-DEC-001` applies to individual Operations across `FR-BJ-*`, `FR-PF-*` and `FR-SO-*` using:

`Business Journey + Operation + Failure Scenario + Deployment Profile`

No category has an inherent higher or lower BC. Supporting Platform Capabilities must be assessed through their actual effect on consuming Business Journeys. Every Journey-level and Operation-level BC assignment remains `NOT_ASSESSED` until separate business-impact evidence and explicit Owner approval exist.

### FIRST_RELEASE coverage

The fifteen entries provide inventory-level coverage for Customer Core, Sales Opportunity/Pipeline Core, Customer Request Core, Work Core, Identity/Tenant architectural foundations, Entitlement Core, Quota Core, Notification Core + In-App, File/Attachment Core, Reporting Core, Audit Core and Operational Core.

Product Catalog, Lead Source, Pain Point, Use Case, Email/SMS/Push, Customer Portal, Technical Knowledge, AI, Advanced Reporting, Meetings, Timesheets, Personal Todos, Public File Sharing, Advanced Versioning, Bulk Import and Advanced Administration remain outside the current FIRST_RELEASE inventory. Their exclusion creates no BC conclusion.

### Known evidence gaps

1. Explicit FIRST_RELEASE product-capability scope confirmation for Identity Trust and Tenant Management, separate from their mandatory foundation role.
2. Business Actor catalog and accountable Business Owner for each Journey.
3. Customer validation, duplicate, merge, deletion and retention rules.
4. Sales Pipeline/Stage State Machine and currency semantics.
5. Customer Request and Task lifecycle definitions.
6. Capability-to-Entitlement and Capability-to-Quota mappings.
7. Notification type and recipient catalog.
8. Mandatory Audit event/action catalog and Audit recording failure policy.
9. Final Reporting Report Sets.
10. Resource-by-resource Attachment requirements.
11. Health/Readiness signal catalog.
12. Privileged Operation catalog and Role Model.
13. Failure Scenario, business-impact and Workaround evidence per Operation and Deployment Profile.
14. Disconnected Sovereign business and security scenarios.
15. Operation-level approval owners.
16. Numeric NFR evidence, which remains open under `OD-023`.

### Explicit non-approvals

This decision does not approve:

- any Operation-level, Journey-level or Domain-level BC classification;
- any `SC`, `DC`, Data Loss Criticality or `RP` classification;
- any SLO, RTO, RPO, latency, throughput, capacity or freshness target;
- any degraded-mode, caching, queueing, manual fallback or failure-handling policy;
- any final Report Set;
- any API/Event Contract;
- any Aggregate, Data Model, Persistence or Migration Design;
- any Search Engine, Index, Object Storage, provider or implementation technology;
- any IdP, Session mechanism, Token design or Service Topology;
- any Architecture, Runtime Security, Implementation, Operational or Production Readiness claim;
- closure of any Open Decision; or
- completion or closure of V3-003.

Approved architecture and security invariants remain unchanged. All `OD-001` through `OD-023` remain Open. V3-003 remains `IN PROGRESS`.

### Conditions for future refinement

1. Stable IDs may be removed, merged or materially redefined only through a later Owner-approved V3-003 decision.
2. Future splits or refinements preserve predecessor/successor traceability.
3. A new inventory entry requires Release Scope and ownership evidence.
4. Adding an Operation approves neither BC nor an API Contract.
5. Every final Report Set requires its own Journey/Operation mapping, Business Owner and Authorization review.
6. Every Entitlement or Quota integration must be traceable to consuming Business Journeys.
7. Every File Attachment integration must identify its Resource owner and dual-authorization boundary.
8. Security/Operational Journeys require explicit actor, scope, authorization and Audit boundaries.
9. Profile-specific refinements may not weaken common business semantics or approved security invariants.
10. Every future BC proposal requires separate business-impact evidence and Owner approval.

### Decision effect

This decision approves the Inventory Taxonomy, the fifteen Stable Inventory IDs, inventory-level FIRST_RELEASE coverage and the recorded responsibility boundaries only. Requirements-maturity gaps remain Open; every Journey and Operation remains `NOT_ASSESSED` for BC; numeric NFRs remain unapproved; V3-003 remains in progress.

**Subsequent status note:** The `NOT_ASSESSED` statement above records the effect of `V3-003-DEC-002` at its approval and is not rewritten by later decisions. `V3-003-DEC-003` and `V3-003-DEC-004`, recorded below, subsequently approve only `CUS-BC-001`, `CUS-BC-002` and `CUS-BC-003`; all other Journey, Operation and Failure-Scenario assessments retain their recorded unresolved status.

### Traceability

- Methodology: `V3-003-DEC-001` in this document.
- FIRST_RELEASE scope and logical ownership: [V3-002B Owner Decision Record](../../migration/v2-owner-review.md).
- Architecture baseline: [Neshane V3 architecture baseline](../baseline-v3.md).
- Tenant and authorization: [ADR-V3-003](../adr/003-cell-based-hybrid-tenancy.md), [ADR-V3-005](../adr/005-domain-owned-authorization.md) and the [Security standard](../standards/security.md).
- Sovereign authority: [ADR-V3-004](../adr/004-sovereign-authority.md).
- Data/messaging and contracts: [ADR-V3-007](../adr/007-data-messaging-baseline.md) and [ADR-V3-008](../adr/008-contract-compatibility.md).
- Profile evidence and readiness separation: [ADR-V3-010](../adr/010-operational-profiles.md) and [ADR-V3-012](../adr/012-evidence-based-readiness.md).
- Numeric NFR targets: [OD-023](../open-decisions.md), which remains Open.
- Approval provenance: explicit Project Owner instruction to record `V3-003-DEC-002`; no approval date, signature, independent reviewer sign-off or additional stakeholder approval was supplied.

## V3-003-DEC-003 — Customer Registration and Maintenance Business Criticality

**Status:** `APPROVED — OWNER`

**Coverage:** Partial Operation-level and Failure-Scenario-level BC coverage

### Approval provenance

| Field | Recorded value |
| --- | --- |
| Approval authority | Project Owner |
| Approval evidence | Explicit Project Owner instruction approving `CUS-BC-001` and authorizing its recording under `V3-003-DEC-003` |
| Approval date | Not recorded |
| Additional Business Owner validation | Not recorded |
| Security or Compliance sign-off | Not recorded |
| Independent reviewer sign-off | Not recorded |
| Methodology | `V3-003-DEC-001 — Business Criticality Assessment Methodology` |
| Inventory entry | `FR-BJ-001 — Register and Maintain Customer Master` |

### Approved assessment — CUS-BC-001

| Field | Approved value |
| --- | --- |
| Assessment ID | `CUS-BC-001` |
| Journey | `FR-BJ-001` |
| Operation | `CUS-CREATE` |
| Failure Scenario | A limited interruption of new Customer creation causes a manageable onboarding backlog; existing Customer records remain available and business Operations involving existing Customers continue |
| Business impact assumptions | Impact is concentrated on delayed new-Customer onboarding; ongoing existing-Customer workflows remain operational; the backlog is manageable and no material disruption of those ongoing workflows is demonstrated |
| Approved classification | `BC-3` |
| Approval status | `APPROVED — OWNER` |

This classification applies only to the assessment unit `FR-BJ-001 + CUS-CREATE + the stated limited-interruption Failure Scenario + the applicable Deployment Profile`. It does not classify every `CUS-CREATE` failure.

### Classification rationale

- Existing-Customer workflows remain operational under the approved scenario.
- The business consequence is delayed onboarding of new Customers.
- The confirmed consequence is a manageable backlog rather than demonstrated material impairment of ongoing core workflows.
- These boundaries support `BC-3` under `V3-003-DEC-001`.

### Deployment Profile limitation

The assessment may be used for Shared SaaS, Dedicated Managed or Dedicated Sovereign only where the stated Failure Scenario and business-impact assumptions are evidenced for that Profile. Equivalent blast radius, workload, contractual effect and interruption tolerance across the three Profiles are not approved. Profile-specific evidence remains outstanding.

### Unassessed Operations and scenarios

| Operation or Failure Scenario | Status | Remaining gap |
| --- | --- | --- |
| `CUS-CREATE — prolonged or materially different interruption` | `NOT_ASSESSED` | May support `BC-2`, but the qualitative boundary and evidence remain unapproved |
| `CUS-VALIDATE` | `NOT_ASSESSED` | Business effects of unavailability, false rejection, invalid acceptance and delayed validation remain unresolved |
| `CUS-GET-FOR-UPDATE` | `NOT_ASSESSED` | Field/use-case business impact is unresolved |
| `CUS-UPDATE` | `NOT_ASSESSED` | Critical field and use-case categories and their consequences are unresolved |

### Boundaries and non-approvals

- No numeric meaning for “limited interruption,” MTD, RTO, RPO, SLO, latency, throughput, freshness or capacity is approved.
- External Customer recording remains prohibited.
- Pending Customer Submission remains `PERMITTED, NOT REQUIRED` under `V3-003-DEC-005`; it is not an available or verified Workaround and does not reduce the approved scenario's impact.
- This decision approves no additional BC, SC, DC, Data Loss Criticality or RP classification.
- No degraded-mode, recovery, Queue, API, Event Contract, persistence, State Machine, Service Topology or implementation mechanism is approved.
- All approved security and architecture invariants remain mandatory.

### Decision effect

`V3-003-DEC-003` is approved only for `CUS-BC-001`. Its partial coverage does not imply that all `FR-BJ-001` Operations or Failure Scenarios have a BC classification.

## V3-003-DEC-004 — Customer Search and Retrieval Business Criticality

**Status:** `APPROVED — OWNER`

**Coverage:** Partial Failure-Scenario-level BC coverage

### Approval provenance

| Field | Recorded value |
| --- | --- |
| Approval authority | Project Owner |
| Approval evidence | Explicit Project Owner instruction approving `CUS-BC-002` and `CUS-BC-003` and authorizing their recording under `V3-003-DEC-004` |
| Approval date | Not recorded |
| Additional Business Owner validation | Not recorded |
| Security or Compliance sign-off | Not recorded |
| Independent reviewer sign-off | Not recorded |
| Methodology | `V3-003-DEC-001 — Business Criticality Assessment Methodology` |
| Inventory entry | `FR-BJ-002 — Find and Review Customer` |

### Approved assessment — CUS-BC-002

| Field | Approved value |
| --- | --- |
| Assessment ID | `CUS-BC-002` |
| Journey | `FR-BJ-002` |
| Operation | `CUS-SEARCH` |
| Failure Scenario | Customer Search is unavailable and prevents essential search-first Sales or Customer Request workflows from proceeding |
| Business impact assumptions | Search is an essential entry point for a significant portion of the affected workflows; those workflows cannot continue through their normal search-first path |
| Approved classification | `BC-2` |
| Approval status | `APPROVED — OWNER` |

The classification applies only to the stated blocked search-first workflow scenario. It does not classify every Search failure. Scenarios in which an authorized actor knows a Customer identifier and valid direct retrieval permits work to continue remain independently assessable and are not automatically `BC-3`.

### Approved assessment — CUS-BC-003

| Field | Approved value |
| --- | --- |
| Assessment ID | `CUS-BC-003` |
| Journey | `FR-BJ-002` |
| Operation | `CUS-GET` |
| Failure Scenario | Current, valid Customer information is unavailable to affected Sales and Customer Request workflows; a limited interruption creates manageable delays, but continued interruption materially impairs those core workflows |
| Business impact assumptions | Current, valid Customer information is a required business dependency and the affected workflows cannot continue without it |
| Approved classification | `BC-2` |
| Approval status | `APPROVED — OWNER` |

The manageable effect of a limited interruption does not by itself downgrade this scenario to `BC-3`; the evidence also does not establish `BC-1`. No quantitative boundary between limited and continued interruption is approved.

### Classification rationale

- `CUS-BC-002`: blocking the essential search-first path materially impairs the specified Sales and Customer Request workflows.
- `CUS-BC-003`: continued loss of current, valid Customer information materially impairs workflows that depend on it.
- Both classifications are tied to their stated business-impact scenarios and do not establish a technology or integration pattern.

### Deployment Profile limitation

Each assessment may be used for Shared SaaS, Dedicated Managed or Dedicated Sovereign only where its stated Failure Scenario and business consequences are evidenced for that Profile. Equivalent blast radius, contractual impact, workload and interruption tolerance across Profiles are not approved. Profile-specific evidence remains outstanding.

### Unassessed Operations and scenarios

| Operation or Failure Scenario | Status | Remaining gap |
| --- | --- | --- |
| `CUS-SEARCH — known identifier and authorized direct retrieval available` | `NOT_ASSESSED` | Actual workflow coverage and residual business impact require separate evidence |
| Other `CUS-SEARCH` failure scenarios | `NOT_ASSESSED` | Scenario-specific impact has not been approved |
| Other `CUS-GET` failure scenarios | `NOT_ASSESSED` | Scenario-specific impact has not been approved |
| `CUS-AUTHORIZE-DISCLOSURE` | `NOT_ASSESSED` | Fail-closed remains mandatory, but BC cannot be inferred from Security Criticality |

### Boundaries and non-approvals

- No Search Engine, index, cache, Projection, API design or mandatory synchronous Customer Service call is approved.
- Any future access mechanism must preserve Customer Domain ownership, validated Tenant Context, Tenant Isolation, Domain-Owned Authorization, Service-Owned Data and Versioned Contracts.
- No numeric MTD, RTO, RPO, SLO, latency, throughput, freshness or capacity target is approved.
- This decision approves no additional BC, SC, DC, Data Loss Criticality or RP classification.
- No degraded-mode, recovery, persistence, State Machine, Service Topology or implementation mechanism is approved.
- Fail-closed behavior and Dedicated Sovereign local authority remain mandatory.

### Decision effect

`V3-003-DEC-004` is approved only for `CUS-BC-002` and `CUS-BC-003`. Its partial coverage does not imply that all `FR-BJ-002` Operations or Failure Scenarios have a BC classification.

## V3-003-DEC-005 — In-System Pending Customer Submission Business Allowance

**Decision Status:** `APPROVED — OWNER`

**Related Task:** `V3-003 — NFR and Threat Assumptions`

**Related Journey:** `FR-BJ-001 — Register and Maintain Customer Master`

**Related Operations:** `CUS-CREATE`, `CUS-VALIDATE`

**Decision Authority:** Project Owner

### Approval provenance and traceability

| Field | Recorded value |
| --- | --- |
| Approval authority | Project Owner |
| Approval evidence | Explicit Project Owner instruction approving `V3-003-DEC-005` and authorizing its repository recording |
| Approval date | Not recorded |
| Stakeholder signatures | Not recorded |
| Independent reviewer sign-off | Not recorded |
| Methodology dependency | `V3-003-DEC-001 — Business Criticality Assessment Methodology` (`APPROVED — OWNER`) |
| Inventory dependency | `V3-003-DEC-002 — FIRST_RELEASE Journey Inventory Taxonomy and Coverage Baseline` (`APPROVED — OWNER`) |
| Customer BIA evidence | Owner-confirmed Customer Core input `INPUT-CUS-006`, interpreted only as a business allowance and not as an implemented or verified workaround |
| Journey and Operations | `FR-BJ-001`; `CUS-CREATE`; `CUS-VALIDATE` |

### 1. Decision

The Project Owner approves the business acceptability of an in-system Pending Customer Submission capability within Neshane CRM V3, subject to the following conditions:

1. Pending Customer Submission inside Neshane is acceptable from a business perspective.
2. Pending Customer Submission is **PERMITTED, NOT REQUIRED** for FIRST_RELEASE.
3. This decision does not change the previously approved FIRST_RELEASE scope.
4. A separate Owner-approved product-scope decision is required before treating Pending Customer Submission as a mandatory deliverable.
5. A Pending Customer Submission must not be treated as a valid or authoritative Customer Master.
6. A Pending Submission must not implicitly establish a valid Customer identity, authoritative Customer Master reference, Tenant Membership, Entitlement, or Business Resource Authorization for consuming business Domains.
7. Sales, Customer Request, Work, and other consuming Domains must not use a Pending Submission as a valid Customer Master.
8. Recording Customer information outside Neshane remains prohibited.
9. Any future implementation must preserve Customer Domain ownership, validated Tenant Context, Tenant Isolation, Domain-Owned Authorization, data integrity, privacy obligations, and relevant security invariants.
10. This business allowance does not establish any runtime availability, validation-failure behavior, or recovery guarantee.

### 2. Business Scope Boundary

This decision confirms that the Pending Submission concept is acceptable from a business perspective.

It does not require the product to deliver this capability in FIRST_RELEASE.

If the capability is selected for implementation, its detailed requirements, lifecycle, ownership, validation behavior, retention, access control, and acceptance criteria must be approved separately.

### 3. Business Impact Analysis Effect

This decision does not establish Pending Customer Submission as an existing, available, or verified business-continuity mechanism.

Therefore:

- This decision itself approves no Business Criticality classification.
- `CUS-BC-001` is now separately `APPROVED — OWNER` under `V3-003-DEC-003` as `BC-3` for the precisely bounded limited-interruption `CUS-CREATE` scenario.
- Materially disruptive `CUS-CREATE` scenarios remain `NOT_ASSESSED` and may support `BC-2` only through separate evidence and approval.
- `CUS-VALIDATE` remains `NOT_ASSESSED`.
- No reduction in business impact may be justified solely by assuming Pending Submission availability.

The current Customer Core assessment boundaries, including later approvals recorded independently of this decision, are:

| Operation and Failure Scenario | Classification | Current Status |
| --- | --- | --- |
| `CUS-CREATE — limited interruption defined by CUS-BC-001` | `BC-3` | `APPROVED — OWNER` under `V3-003-DEC-003` |
| `CUS-CREATE — prolonged or materially different interruption` | Unresolved; may support `BC-2` | `NOT_ASSESSED` |
| `CUS-VALIDATE` | No approved candidate | `NOT_ASSESSED` |
| `CUS-GET-FOR-UPDATE` | Unresolved | `NOT_ASSESSED` |
| `CUS-UPDATE` | Depends on field/use-case impact | `NOT_ASSESSED` |
| `CUS-SEARCH — blocked search-first workflows defined by CUS-BC-002` | `BC-2` | `APPROVED — OWNER` under `V3-003-DEC-004` |
| `CUS-SEARCH — known identifier and authorized direct retrieval available`, and other Search scenarios | Unresolved | `NOT_ASSESSED` |
| `CUS-GET — continued unavailability defined by CUS-BC-003` | `BC-2` | `APPROVED — OWNER` under `V3-003-DEC-004` |
| Other `CUS-GET` scenarios | Unresolved | `NOT_ASSESSED` |
| `CUS-AUTHORIZE-DISCLOSURE` | Unresolved | `NOT_ASSESSED` |

A possible future Pending Submission capability is not an available or verified workaround and must not be used to reduce the assessed impact of Customer Creation failure.

### 4. Explicit Non-Approvals

This decision does not approve:

- Mandatory FIRST_RELEASE delivery of Pending Customer Submission.
- Any BC, SC, DC, Data Loss Criticality, or RP classification.
- Any SLO, RTO, RPO, MTD, latency, capacity, or freshness target.
- Any submission lifecycle or State Machine.
- Any Queue, Background Job, API, Event Contract, Database Schema, Aggregate, persistence design, or Customer/Submission identifier format.
- Any degraded-mode, recovery, reconciliation, or validation-failure policy.
- Any authorization bypass or security exception.
- Any implementation, operational, runtime-security, or production-readiness claim.

### 5. Scope protection

- The approved FIRST_RELEASE inventory and all fifteen stable Inventory identifiers remain unchanged.
- No additional mandatory FIRST_RELEASE capability is introduced.
- Existing Owner-confirmed Customer Core BIA inputs remain unchanged; this record formalizes only the business allowance expressed by `INPUT-CUS-006`.
- `V3-003-DEC-001` and `V3-003-DEC-002` remain `APPROVED — OWNER`.
- At the time `V3-003-DEC-005` was approved, `V3-003-DEC-003` and `V3-003-DEC-004` remained proposals. They are now separately `APPROVED — OWNER` with the partial-coverage boundaries recorded above; `V3-003-DEC-005` itself does not approve their BC classifications.
- All `OD-001` through `OD-023` remain `OPEN`.

### 6. Decision Effect

This decision authorizes consideration of Pending Customer Submission in future product and architecture analysis without creating a mandatory FIRST_RELEASE commitment.

All existing approved architectural and security invariants remain in force.

V3-003 remains IN PROGRESS.

All existing Open Decisions, including OD-001 through OD-023, remain OPEN.

The later Owner approval of `V3-003-DEC-003` and `V3-003-DEC-004` is recorded separately above and does not change the business allowance or non-approval boundaries of this decision.

## V3-003-DEC-006 — Logical Threat Inventory and Trust Boundary Baseline

**Decision Status:** `APPROVED — OWNER`

**Decision Authority:** Project Owner

**Related Task:** `V3-003 — NFR and Threat Assumptions`

**Independent Security Review:** `PENDING — NOT SIGNED OFF`

**Repository Recording:** Completed after identifier and traceability verification; no conflicting Decision or stable inventory identifier was found

### Approval provenance

| Field | Recorded value |
| --- | --- |
| Approval authority | Project Owner |
| Approval evidence | Explicit Project Owner instruction approving `V3-003-DEC-006` and authorizing repository recording after identifier and traceability verification |
| Approval date | Not recorded |
| Security reviewer | Not recorded |
| Independent security sign-off | Pending; not completed |
| Implementation or runtime evidence | Not provided |

### 1. Decision

The Project Owner approves the normalized Logical Threat Inventory and Trust Boundary Baseline for Neshane CRM V3, comprising ratification packages `PR-01` through `PR-06`.

This approval establishes an authoritative logical inventory baseline for architectural threat analysis only. It does not validate every threat assumption, approve an implementation mechanism, constitute independent Security sign-off or verify any security control.

#### PR-01 — Threat Actor Taxonomy

Twelve normalized Threat Actor categories are approved as the logical inventory baseline.

- Historical `TA-P11` is reclassified as a messaging-provenance attack technique, not an independent Threat Actor.
- Historical `TA-P12` is reclassified as a cross-tenant/cross-cell attack objective or capability, not an independent Threat Actor.
- Both historical identifiers remain traceable and must not be reused.
- Individual attacker capabilities, footholds, exposure assumptions and exploitability claims remain subject to independent Security Review.

#### PR-02 — Non-Adversarial Threat Sources

Six logical non-adversarial Threat Source categories are approved: human error; misconfiguration and policy drift; infrastructure and connectivity failure; messaging delivery and consistency failure; stale or inconsistent derived state; and deployment, upgrade or rollback failure.

A failure mode does not imply adversarial intent. Deliberately induced or exploited failures remain separate abuse scenarios.

#### PR-03 — Asset-at-Risk Inventory

Twenty-one logical Assets at Risk are approved as the initial threat-analysis asset inventory. Approval establishes asset identity, logical ownership and traceability only; it approves no security/data/business/recovery classification, storage mechanism, retention policy or implementation detail.

#### PR-04 — Logical Trust Boundary Inventory

Twenty-five normalized Logical Trust Boundaries are approved as the logical baseline for security analysis. The baseline preserves:

1. Independent Identity Trust, Tenant Management and Entitlement authority boundaries.
2. Domain-Owned Authorization as final authority for resource/action decisions.
3. Service-owned persistence, validated Tenant Context and applicable PostgreSQL RLS enforcement without depicting Tenant A to Tenant B as an authorized flow.
4. Independent Plugin Package, Installation, Runtime, Extension Gateway and resource-owning Domain relationships.
5. Messaging producer, broker and consumer trust distinctions.
6. Control Plane and Data Plane authority separation.
7. Dedicated Sovereign local authority without implicit Central authority.
8. Separation of operator identity, operational execution and destination-domain authorization.
9. Separate File/Attachment and Reporting trust relationships.

For File/Attachment, File-owned resource authorization and resource-owner authorization of the Attachment relationship remain distinct. For Reporting, report/artifact authorization and source-data disclosure restrictions remain distinct; synchronous per-record authorization against a producing Domain is not mandated and authorized projections remain permitted.

These are logical trust transitions, not physical network boundaries, deployment topology, protocols, API-call ordering or mandatory synchronous service dependencies.

#### PR-05 — Abuse/Misuse Cases and Negative Security Tests

The normalized analytical structure and traceability of Abuse/Misuse/Failure Cases and candidate Negative Security Tests are approved.

Messaging scenarios distinguish forged or unauthorized provenance, valid duplicate delivery under at-least-once messaging, malicious replay, and delayed or out-of-order delivery. A valid duplicate is not automatically an attack and does not require unconditional rejection. Approved Outbox/Inbox and idempotency invariants remain applicable.

Audit scenarios distinguish omission of an event subject to a future approved mandatory-event catalog, Audit-record tampering, unauthorized Audit disclosure, and sensitive-data leakage through Audit payloads.

This approval creates no mandatory Audit Event Catalog, retention policy, Audit-failure policy, global messaging-order guarantee or technical enforcement mechanism. Every candidate Negative Security Test remains `NOT_EXECUTED`.

#### PR-06 — Security Review Ownership

Role-based review responsibility is approved across Identity, Tenant Management, Data Security, resource-owning Domains, Plugin Platform, Messaging, Operational Platform, Sovereign Operations, Audit and Supply-Chain Security. This creates no individual appointment, team acceptance, completed review or Security sign-off.

### 2. Stable identifier and traceability governance

The conflict check found no existing `V3-003-DEC-006` and no conflicting stable `TA-*`, `TS-*`, `AS-*`, `TB-*`, `AB-*` or `NT-*` inventory identifiers in the authorized V3 documentation scope. The stable catalogs in the normative annexes below are therefore assigned by this record.

Historical `*-P*`, `TB-N*` and `TB-F*` analytical identifiers are predecessor references. They must not be deleted, silently renamed or reused. Later merge, split, addition, removal or semantic change must preserve predecessor/successor traceability and follow applicable architecture governance.

### 3. Independent status dimensions

| Dimension | Status |
| --- | --- |
| `INVENTORY_BASELINE_STATUS` | `APPROVED — OWNER` |
| `THREAT_ASSUMPTION_VALIDATION_STATUS` | `PENDING SECURITY REVIEW` |
| `IMPLEMENTATION_EVIDENCE_STATUS` | `NOT_VERIFIED` |
| `SECURITY_REVIEW_STATUS` | `NOT SIGNED OFF` |
| `NEGATIVE_TEST_EXECUTION_STATUS` | `NOT_EXECUTED` |

Approval of the logical inventory changes no other status dimension.

### 4. Explicit non-approvals

This decision does not approve:

- Threat likelihood, severity, rating or risk acceptance.
- Mitigation implementation or security exceptions.
- `BC`, `SC`, `DC`, Data Loss Criticality or `RP` assignments.
- Numeric SLO, RTO, RPO, MTD, latency, freshness, throughput or capacity targets.
- Identity, session, token, workload-identity or secret-management implementation.
- API contracts, event envelopes, protocols or physical Service Topology.
- Plugin isolation technology or detailed grant implementation.
- Runtime RLS integration or proof of Tenant Isolation.
- Audit retention, mandatory-event catalog or failure-handling policy.
- Privileged-operation workflow or break-glass policy.
- Security test outcomes, runtime enforcement or production-security readiness.
- Closure of an Open Decision.

### 5. Decision effect

The approved stable inventory may be used for subsequent threat analysis, abuse-case refinement, security-requirement preparation and negative-test design. `V3-003-DEC-001` through `V3-003-DEC-005`, the approved Customer BC assessments and FIRST_RELEASE scope remain unchanged. `V3-003` remains `IN PROGRESS`; `OD-001` through `OD-023` remain `OPEN`; independent Security Review, assumption validation and implementation evidence remain outstanding.

### Normative Annex A — Stable Threat Actor catalog

| Stable ID | Logical actor category | Historical predecessor | Validation limitation | Review owner role |
| --- | --- | --- | --- | --- |
| `TA-001` | Unauthenticated External Adversary | `TA-P01` | Entry points and capabilities remain unvalidated | Security + API Architecture |
| `TA-002` | Malicious Authenticated Tenant User | `TA-P02` | Legitimate permission extent remains operation-specific | Resource-owning Domain + Security |
| `TA-003` | Adversary Controlling a Legitimate User Account | `TA-P03` | Compromise method and session capability remain unvalidated | Identity + Security |
| `TA-004` | Malicious Tenant Administrator | `TA-P04` | Tenant-admin Role Model remains unresolved | Tenant Management + Security |
| `TA-005` | Adversary Controlling a Service Identity | `TA-P05` | Workload-identity protocol and scope remain unresolved | Security + Service Owners |
| `TA-006` | Malicious or Compromised Platform Operator | `TA-P06` | Privileged Role/Action catalog remains unresolved | Platform Security |
| `TA-007` | Adversary Controlling an Identity or Token Authority | `TA-P07` | IdP, token and session mechanics remain unresolved | Identity + Security |
| `TA-008` | Malicious Plugin Publisher | `TA-P08` | Package-trust and publisher-verification model remain unresolved | Plugin Security |
| `TA-009` | Adversary Controlling a Plugin Runtime or Host | `TA-P09` | Runtime isolation and hosting capability remain unresolved | Plugin + Operations Security |
| `TA-010` | Malicious or Compromised Integration Client | `TA-P10` | Client identity and contract scope remain unresolved | API + Domain Security |
| `TA-011` | Supply-Chain Adversary | `TA-P13` | Dependency, build and artifact exposure remain unresolved | Supply-Chain Security |
| `TA-012` | Adversary Controlling a Central or Federation Component | `TA-P14` | Federation protocol and Central capability remain unresolved | Sovereign Security |

Historical `TA-P11` maps to messaging-provenance/replay techniques exercised by applicable stable Actors, particularly `TA-005`, `TA-009`, `TA-010` or `TA-012`. Historical `TA-P12` maps to the cross-tenant/cross-cell objective applicable to multiple Actor categories, particularly `TA-002` through `TA-006`, `TA-009` and `TA-010`.

### Normative Annex B — Stable non-adversarial Threat Source catalog

| Stable ID | Threat Source | Historical predecessor |
| --- | --- | --- |
| `TS-001` | Human Error | `TS-P01` |
| `TS-002` | Misconfiguration or Policy Drift | `TS-P02` |
| `TS-003` | Infrastructure or Connectivity Failure | `TS-P03` |
| `TS-004` | Messaging Delivery or Consistency Failure | `TS-P04` |
| `TS-005` | Stale or Inconsistent Derived State | `TS-P05` |
| `TS-006` | Deployment, Upgrade or Rollback Failure | `TS-P06` |

### Normative Annex C — Stable Asset-at-Risk catalog

| Stable ID | Logical asset | Logical owner | Historical predecessor |
| --- | --- | --- | --- |
| `AS-001` | Principal Identities and Authenticators | Identity Trust | `AS-P01` |
| `AS-002` | Sessions, Tokens and Revocation State | Identity Trust | `AS-P02` |
| `AS-003` | Tenant Membership and validated Tenant Context | Tenant Management; Context is derived and propagated evidence | `AS-P03` |
| `AS-004` | Domain Authorization Policies, Inputs and Decisions | Resource-owning Domain; shared governance supplies common contracts only | `AS-P04` |
| `AS-005` | Entitlement State and Eligibility Decisions | Entitlement | `AS-P05` |
| `AS-006` | Quota Limits, Reservation/Usage Ledger and Decisions | Quota | `AS-P06` |
| `AS-007` | Customer Master | Customer Domain | `AS-P07` |
| `AS-008` | Opportunity and Sales State | Sales Domain | `AS-P08` |
| `AS-009` | Customer Request State and History | Customer Request Domain | `AS-P09` |
| `AS-010` | Work Task, Assignment and Link Metadata | Work Domain | `AS-P10` |
| `AS-011` | File Metadata and Content | File/Content Domain; Attachment meaning remains with resource owner | `AS-P11` |
| `AS-012` | Report Definitions, Execution State, Artifacts and Authorized Projections | Reporting Capability; source Business Facts remain with producing Domains | `AS-P12` |
| `AS-013` | Audit Records and Integrity Evidence | Audit Domain | `AS-P13` |
| `AS-014` | Privileged-Operation Request and Execution State | Operational Platform; destination Domain retains business authorization | `AS-P14` |
| `AS-015` | Service Identities and Credentials | Owning Service / Platform trust authority | `AS-P15` |
| `AS-016` | Service-Owned Private Data and Persistence Boundary | Each owning Service | `AS-P16` |
| `AS-017` | Plugin Package, Installation Identity, Grants and Lifecycle | Plugin Platform; Installation is tenant-bound | `AS-P17` |
| `AS-018` | Event Messages, Contract Version and Provenance | Producing Domain owns the Fact and event contract | `AS-P18` |
| `AS-019` | Secrets, Keys and Trust Material | Profile-local authorized custodian; exact tooling unresolved | `AS-P19` |
| `AS-020` | Dedicated Sovereign Local Security and Operational Authority | Sovereign-local Control Plane | `AS-P20` |
| `AS-021` | Build and Release Artifacts plus Provenance Evidence | Service/release owner | `AS-P21` |

No Asset in this catalog has an approved `SC`, `DC`, `BC`, Data Loss Criticality, `RP` or risk rating merely by inclusion.

### Normative Annex D — Stable Logical Trust Boundary catalog

| Stable ID | Source context → receiving context | Receiving enforcement authority | Historical predecessor |
| --- | --- | --- | --- |
| `TB-001` | External Client → Platform Entry | Entry/Identity validation boundary | `TB-P01` → `TB-N01` → `TB-F01` |
| `TB-002` | Platform Entry or API Edge → Resource-owning Domain | Resource-owning Domain | `TB-P02` → `TB-N02` → `TB-F02` |
| `TB-003` | External IdP or Issuer → Identity Trust | Identity Trust | `TB-P03` → `TB-N03` → `TB-F03` |
| `TB-004` | Identity Trust → Consuming Capability | Consumer validates identity/session evidence | `TB-P04` → `TB-N04` → `TB-F04` |
| `TB-005` | Tenant Management → Consuming Capability | Consumer validates Membership and Tenant Context evidence | `TB-P04` → `TB-N05` → `TB-F05` |
| `TB-006` | Entitlement → Resource-owning Domain | Domain treats result only as eligibility | `TB-P04` → `TB-N06` → `TB-F06` |
| `TB-007` | Domain or Service → another Resource-owning Domain | Destination Domain | `TB-P05` → `TB-N07` → `TB-F07` |
| `TB-008` | Service Execution Context → Service-Owned Persistence | Owning Service and persistence controls | `TB-P06/P07` → `TB-N08/N09` → `TB-F08` |
| `TB-009` | Plugin Publisher or Package → Plugin Control Plane | Plugin Control Plane | `TB-P08` → `TB-N10` → `TB-F09` |
| `TB-010` | Tenant/Plugin Administrator → Installation and Grant Management | Plugin Control Plane | `TB-P08` → `TB-N11` → `TB-F10` |
| `TB-011` | Plugin Runtime → Extension Gateway | Extension Gateway | `TB-P09` → `TB-N12` → `TB-F11` |
| `TB-012` | Extension Gateway → Resource-owning Domain | Destination Domain | `TB-P09` → `TB-N13` → `TB-F12` |
| `TB-013` | Producing Domain → Messaging Infrastructure | Producer/messaging publication boundary | `TB-P10` → `TB-N14` → `TB-F13` |
| `TB-014` | Messaging Infrastructure → Consumer | Consumer | `TB-P10` → `TB-N15` → `TB-F14` |
| `TB-015` | Control Plane → Data Plane | Data Plane under scoped operational intent | `TB-P11` → `TB-N16` → `TB-F15` |
| `TB-016` | Central or Federation → Dedicated Sovereign | Sovereign-local authority | `TB-P12` → `TB-N17` → `TB-F16` |
| `TB-017` | Privileged Operator → Operational Platform | Operational Platform | `TB-P13` → `TB-N18` → `TB-F17` |
| `TB-018` | Operational Platform → Destination Domain | Destination Domain | `TB-P13` → `TB-N19` → `TB-F18` |
| `TB-019` | Producing Domain → Audit Capability | Audit Domain | `TB-P14` → `TB-N20` → `TB-F19` |
| `TB-020` | Consumer → File/Content Resource | File/Content Domain | `TB-P15` → `TB-N21` → `TB-F20` |
| `TB-021` | Resource-owning Domain ↔ File/Content Attachment Relationship | Resource owner for relationship; File Domain for File resource | `TB-P15` → `TB-N22` → `TB-F21` |
| `TB-022` | Consumer → Report Definition or Artifact | Reporting Capability | `TB-P15` → `TB-N21` → `TB-F22` |
| `TB-023` | Producing Domain → Reporting Contract or Authorized Projection | Producing Domain at publication; Reporting at consumption | `TB-P15` → `TB-N22` → `TB-F23` |
| `TB-024` | Source or Dependency Inputs → Artifact Production | Build/release owner | `TB-P16` → `TB-N23` → `TB-F24` |
| `TB-025` | Approved Artifact → Runtime/Profile | Profile-local release authority | `TB-P16` → `TB-N24` → `TB-F25` |

`TB-008` includes Shared SaaS enforcement properties—validated transaction Tenant Context, application authorization, tenant-scoped constraints, PostgreSQL RLS and a runtime database role unable to bypass tenant protection—without defining an authorized Tenant A-to-Tenant B flow.

`TB-020` through `TB-023` preserve distinct File/Attachment and Reporting semantics. Reporting may consume versioned contracts or authorized projections and does not require a synchronous per-record call to the producing Domain merely because this boundary exists.

### Normative Annex E — Stable Abuse/Misuse/Failure and Negative-Test catalog

| Case ID | Scenario | Actor or Source | Test ID | Historical predecessor | Test status |
| --- | --- | --- | --- | --- | --- |
| `AB-001` | Forged, expired or invalid user credential/session use | `TA-001` or `TA-003` | `NT-001` | `AB-P01` / `NT-P01` | `NOT_EXECUTED` |
| `AB-002` | Missing, forged or conflicting Tenant Context | Applicable adversarial Actor | `NT-002` | `AB-P02` / `NT-P02` | `NOT_EXECUTED` |
| `AB-003` | Direct resource/action authorization bypass | `TA-002`, `TA-003`, `TA-004` or `TA-010` | `NT-003` | `AB-P03` / `NT-P03` | `NOT_EXECUTED` |
| `AB-004` | Confused deputy or unauthorized service-to-service action | `TA-005` | `NT-004` | `AB-P04` / `NT-P04` | `NOT_EXECUTED` |
| `AB-005` | Use of stale or revoked Membership/Entitlement state | Applicable adversarial Actor or `TS-005` | `NT-005` | `AB-P05` / `NT-P05` | `NOT_EXECUTED` |
| `AB-006` | Unauthorized direct access to another Service's private persistence | `TA-005` or `TA-006` | `NT-006` | `AB-P06` / `NT-P06` | `NOT_EXECUTED` |
| `AB-007` | Cross-tenant data access or RLS/context isolation bypass | Applicable adversarial Actor | `NT-007` | `AB-P07`; historical objective `TA-P12` / `NT-P07` | `NOT_EXECUTED` |
| `AB-008` | Plugin grant, installation or tenant-boundary violation | `TA-008` or `TA-009` | `NT-008` | `AB-P08` / `NT-P08` | `NOT_EXECUTED` |
| `AB-009` | Forged or unauthorized event provenance | `TA-005`, `TA-009`, `TA-010` or `TA-012` | `NT-009` | `AB-P09A`; historical technique `TA-P11` / `NT-P09A` | `NOT_EXECUTED` |
| `AB-010` | Valid duplicate delivery under at-least-once messaging | `TS-004` | `NT-010` | `AB-P09B` / `NT-P09B` | `NOT_EXECUTED` |
| `AB-011` | Malicious event replay | Applicable Actor with event access | `NT-011` | `AB-P09C`; historical technique `TA-P11` / `NT-P09C` | `NOT_EXECUTED` |
| `AB-012` | Delayed or out-of-order event delivery | `TS-004` or attacker-induced failure | `NT-012` | `AB-P09D` / `NT-P09D` | `NOT_EXECUTED` |
| `AB-013` | Privileged operator bypasses destination-domain authorization | `TA-006` | `NT-013` | `AB-P10` / `NT-P10` | `NOT_EXECUTED` |
| `AB-014` | File or Report access outside tenant/resource/disclosure authority | `TA-002`, `TA-003` or `TA-010` | `NT-014` | `AB-P11` / `NT-P11` | `NOT_EXECUTED` |
| `AB-015` | Omission of an event required by a future approved Audit catalog | Applicable Actor or failure source | `NT-015` | `AB-P12A` / `NT-P12A` | `NOT_EXECUTED` |
| `AB-016` | Audit-record tampering | Applicable privileged Actor | `NT-016` | `AB-P12B` / `NT-P12B` | `NOT_EXECUTED` |
| `AB-017` | Unauthorized Audit disclosure | Applicable adversarial Actor | `NT-017` | `AB-P12C` / `NT-P12C` | `NOT_EXECUTED` |
| `AB-018` | Sensitive-data leakage through Audit payload | Applicable Actor or `TS-002` | `NT-018` | `AB-P12D` / `NT-P12D` | `NOT_EXECUTED` |
| `AB-019` | Central or federation component asserts implicit Sovereign authority | `TA-012` | `NT-019` | `AB-P13` / `NT-P13` | `NOT_EXECUTED` |
| `AB-020` | Critical Sovereign operation depends on unavailable Central authority | `TS-003` or attacker-induced outage | `NT-020` | `AB-P14` / `NT-P14` | `NOT_EXECUTED` |
| `AB-021` | Tampered dependency, build input or artifact reaches deployment | `TA-011` | `NT-021` | `AB-P15` / `NT-P15` | `NOT_EXECUTED` |

The `AB-*` prefix in this annex covers adversarial abuse, non-adversarial misuse and failure scenarios for unified traceability; inclusion does not imply malicious intent.

### Normative Annex F — End-to-end traceability and review ownership

| Case | Entry point | Boundary | Primary assets | Approved invariant | Main evidence gap | Security review owner role |
| --- | --- | --- | --- | --- | --- | --- |
| `AB-001` | Client credential/session | `TB-001`, `TB-003`, `TB-004` | `AS-001`, `AS-002` | Validated identity/session; identity alone grants no business permission | IdP/session/revocation model | Identity + Security |
| `AB-002` | Tenant selector/context evidence | `TB-005`, `TB-008` | `AS-003` | Tenant Context comes from validated Membership/provenance and invalid context fails closed | Context format/propagation | Tenant Management + Security |
| `AB-003` | Resource ID or business action | `TB-002`, `TB-007` | `AS-004`, domain Assets | Resource-owning Domain makes final authorization decision | Resource/action policy matrices | Owning Domain + Security |
| `AB-004` | Service-to-service contract | `TB-007` | `AS-004`, `AS-015`, `AS-016` | Authenticated audience-restricted workload plus destination authorization | Workload identity protocol | Service Owners + Security |
| `AB-005` | Membership/eligibility evidence | `TB-005`, `TB-006` | `AS-003`, `AS-005` | Membership, Entitlement and Authorization are independent current decisions | Freshness/revocation semantics | Tenant/Entitlement + Security |
| `AB-006` | Persistence access | `TB-008` | `AS-016` | Service-owned data; no cross-service database access | Roles/network/topology evidence | Data + Service Security |
| `AB-007` | Shared tenant-owned persistence access | `TB-008` | Tenant-owned domain Assets | Application authorization, validated context, RLS and non-bypass role | Runtime RLS integration | Data + Tenant Security |
| `AB-008` | Package/install/runtime request | `TB-009`–`TB-012` | `AS-017`, domain Assets | Installation identity, tenant binding, grants, Gateway and Domain authority | Package trust/grant/isolation model | Plugin + Domain Security |
| `AB-009` | Event publication or delivery | `TB-013`, `TB-014` | `AS-018`, consumer state | Producer-owned Fact, explicit versioned event, validated provenance | Event envelope/provenance design | Messaging + Domain Security |
| `AB-010` | Valid broker redelivery | `TB-014` | `AS-018`, consumer state | At-least-once duplicate tolerance and idempotent effect where mandated | Inbox transaction/effect evidence | Messaging + Consumer Owner |
| `AB-011` | Replayed event | `TB-013`, `TB-014` | `AS-018`, consumer state | Authorization/business constraints and idempotency remain effective | Replay/idempotency semantics | Messaging + Domain Security |
| `AB-012` | Delayed/reordered delivery | `TB-014` | `AS-018`, consumer state | Contract-specific consistency behavior; no global ordering assumption | Ordering/version behavior | Messaging + Consumer Owner |
| `AB-013` | Privileged operation | `TB-017`, `TB-018` | `AS-014`, domain Assets | Limited identity, explicit scope, destination authorization and Audit | Role/action catalog | Platform + Domain Security |
| `AB-014` | File or Report request | `TB-020`–`TB-023` | `AS-011`, `AS-012`, source Assets | File/Report-owned authorization plus attachment/source disclosure boundaries | Attachment/report/projection matrix | File/Reporting + Source Domains |
| `AB-015` | Audit evidence emission | `TB-019` | `AS-013` | Required Audit evidence must be preserved when cataloged | Mandatory-event catalog/failure policy | Audit + Producing Domain Security |
| `AB-016` | Audit storage/access | `TB-019` | `AS-013` | Audit integrity protection | Storage/integrity mechanism | Audit Security |
| `AB-017` | Audit read/search | Audit resource access boundary under `TB-019` | `AS-013` | Audit Domain authorizes Audit resources | Viewer/resource policy | Audit Security |
| `AB-018` | Audit payload | `TB-019` | `AS-013`, source-sensitive data | Sensitive-data minimization and safe Audit context | Data classification/redaction catalog | Audit + Data Security |
| `AB-019` | Central/federation request | `TB-016` | `AS-020`, `AS-019` | Sovereign-local final authority; Central has no implicit administration | Federation protocol | Sovereign Security |
| `AB-020` | Central dependency during outage | `TB-016` | `AS-020` | No mandatory synchronous Central dependency for critical local operations | Disconnected operational evidence | Sovereign Operations + Security |
| `AB-021` | Build/dependency/artifact input | `TB-024`, `TB-025` | `AS-021`, `AS-019` | Reproducible, versioned, integrity-verifiable artifact and profile evidence | Signing/attestation/promotion design | Supply-Chain Security |

### Normative Annex G — Role-based review responsibility

| Review area | Responsible review roles |
| --- | --- |
| Identity, authenticator, token and session assumptions | Identity Architecture + Security |
| Tenant Membership, Tenant Context and cross-tenant threats | Tenant Management + Security |
| RLS and persistence isolation | Data Architecture + Security + owning Service |
| Domain resource/action authorization | Resource-owning Domain + Security |
| Entitlement and Quota assumptions | Platform capability owner + Security |
| Plugin package, installation, grants, runtime and Gateway | Plugin Platform + Security + Operations |
| Events, Outbox/Inbox, replay and delivery failures | Messaging Architecture + producing/consuming Domains + Security |
| File/Attachment and Reporting disclosure boundaries | File/Reporting owners + source/resource-owning Domains + Security |
| Audit integrity and disclosure | Audit owner + Security + producing Domains |
| Privileged operations | Operational Platform + destination Domains + Security |
| Sovereign/Central authority | Sovereign Operations + Security + Architecture |
| Build and release supply chain | Release/Supply-Chain Security + Service owners |

These are role allocations only. They record no named reviewer, team acceptance, completed review or sign-off.

## V3-003-DEC-007 — Priority Abuse Case Analysis and Security Requirement Candidate Baseline

**Decision Status:** `APPROVED — OWNER`

**Decision Authority:** Project Owner

**Related Task:** `V3-003 — NFR and Threat Assumptions`

**Independent Security Review:** `PENDING — NOT SIGNED OFF`

**Normative Content Binding:** Approval applies exclusively to Normative Annexes A through D recorded directly under this decision, including the authorized editorial expansion of abbreviated references into complete stable identifiers. Later modifications are not automatically approved.

### Approval provenance

| Field | Recorded value |
| --- | --- |
| Approval authority | Project Owner |
| Approval evidence | Explicit Project Owner instruction approving `V3-003-DEC-007` and authorizing safe repository recording of the complete Normative Annexes A through D with full stable-identifier normalization |
| Approval date | Not recorded |
| Security reviewer | Not recorded |
| Independent security sign-off | Pending; not completed |
| Implementation or runtime evidence | Not provided |
| Git revision binding | None; repository recording is not represented as an immutable Git revision |

### 1. Decision

The Project Owner approves the bounded analytical baseline defined by Normative Annexes A through D, comprising:

1. The twelve selected Abuse/Misuse Cases identified by their existing stable IDs.
2. Twenty-four Security Requirement Candidates, `SR-CAND-001` through `SR-CAND-024`.
3. Scenario-to-Actor/Source, Trust Boundary, Asset, architectural invariant, Candidate Requirement, Negative Test, evidence gap and review-owner traceability.
4. Unresolved threat assumptions, architecture-decision dependencies and the nine unassessed Abuse Cases retained in the backlog.

Approval applies exclusively to the exact Annex A through D content recorded with this decision in this authoritative decision record.

All Security Requirement Candidates remain `PROPOSED — NOT APPROVED`.

The `RESTATEMENT` category does not grant additional approval to candidate implementation or verification wording. `DERIVED` items require Independent Security Review before becoming mandatory. `POLICY/DESIGN` items require separate explicit policy or architectural approval.

All Negative Security Tests remain `NOT_EXECUTED`.

All runtime implementation controls remain `NOT_VERIFIED`.

Threat Actor capabilities and unresolved attributions remain subject to Independent Security Review.

This decision does not authorize implementation, assign risk ratings, accept risks, approve mitigations or security exceptions, establish numeric NFR targets, or approve any new `BC`, `SC`, `DC`, Data Loss Criticality or `RP` classification.

`V3-003-DEC-006` and all earlier approved decisions remain unchanged.

`V3-003` remains `IN PROGRESS`, and `OD-001` through `OD-023` remain `OPEN`.

The normative baseline preserves complete identifiers and internal referential integrity. This repository recording is not an immutable Git revision and no commit hash is asserted.

### 2. Candidate classification and approval boundary

The approved analytical classification baseline is:

- Thirteen `RESTATEMENT` candidates: `SR-CAND-001`, `SR-CAND-003`, `SR-CAND-005`, `SR-CAND-007`, `SR-CAND-009`, `SR-CAND-011`, `SR-CAND-013`, `SR-CAND-015`, `SR-CAND-017`, `SR-CAND-018`, `SR-CAND-019`, `SR-CAND-021` and `SR-CAND-023`.
- Seven `DERIVED` candidates: `SR-CAND-002`, `SR-CAND-004`, `SR-CAND-006`, `SR-CAND-008`, `SR-CAND-012`, `SR-CAND-016` and `SR-CAND-022`.
- Four `POLICY/DESIGN` candidates: `SR-CAND-010`, `SR-CAND-014`, `SR-CAND-020` and `SR-CAND-024`.

`RESTATEMENT` identifies candidate testable wording derived directly from an approved architectural invariant; the wording, verification detail and implementation interpretation are not thereby approved as a final Security Requirement. `DERIVED` identifies a candidate security property requiring Independent Security Review before it may become mandatory. `POLICY/DESIGN` identifies a new implementation, lifecycle or policy choice requiring a separate explicit approval decision.

### 3. Enforcement-semantics boundary

The Candidate Requirements define security properties without selecting mechanisms:

- Preventing unauthorized event effects does not mandate quarantine.
- Valid duplicate delivery does not mandate unconditional rejection.
- Audit integrity does not define a retention policy.
- File and Reporting authorization does not mandate synchronous per-record calls to source Domains.
- Sovereign-local authority does not approve Full Air-Gap support.
- Tenant Context validation does not select an envelope, token format or database-integration mechanism.

### 4. Independent status dimensions

| Dimension | Status |
| --- | --- |
| `DECISION_STATUS` | `APPROVED — OWNER` |
| `SECURITY_REQUIREMENT_CANDIDATES` | `PROPOSED — NOT APPROVED` |
| `THREAT_ASSUMPTION_VALIDATION_STATUS` | `PENDING SECURITY REVIEW` |
| `SECURITY_REVIEW_STATUS` | `NOT_SIGNED_OFF` |
| `IMPLEMENTATION_EVIDENCE_STATUS` | `NOT_VERIFIED` |
| `NEGATIVE_TEST_EXECUTION_STATUS` | `NOT_EXECUTED` |

### 5. Explicit non-approvals

This decision does not approve:

- Any final or mandatory Security Requirement.
- Threat Actor capability validation or resolution of an unresolved Actor attribution.
- Independent Security sign-off.
- Threat likelihood, severity, rating or risk acceptance.
- Mitigation implementation or security exceptions.
- `BC`, `SC`, `DC`, Data Loss Criticality or `RP` classifications.
- Numeric SLO, RTO, RPO, MTD, latency, freshness, throughput or capacity targets.
- API contracts, event envelopes, protocols, cryptographic mechanisms or implementation technologies.
- Identity, session, workload-identity, Tenant Context or secret-management implementation.
- Runtime RLS integration or proof of Tenant Isolation.
- Plugin sandbox, package-trust or grant technology.
- Messaging rejection, quarantine, replay-window, ordering, retry or reconciliation policy.
- Audit Event Catalog, integrity mechanism, retention or failure policy.
- Privileged-operation, role, action or break-glass implementation.
- File, Attachment, Reporting or Projection implementation design.
- Full Air-Gap support.
- Executed security tests, verified runtime controls, Implementation Readiness, Security Readiness or Production Readiness.
- Closure of an Open Decision.

### 6. Decision effect

The exact Normative Annexes A through D below may serve as the controlled analytical baseline for Independent Security Review, detailed Security Requirement refinement, candidate Negative Security Test design and preparation of later explicit decisions. Approval creates no implementation authorization and closes no Open Decision.

### Normative Annex A — Priority Abuse Case Register

The following twelve entries are normative for the approved analytical baseline. Unresolved Actor attribution, attack feasibility, capability assumptions and implementation evidence remain unresolved where stated.

| Case | Actor or Source | Initial foothold, entry point and logical progression | Trust Boundaries and Assets | Expected consequence and approved invariant | Negative Test, evidence gaps and review owner |
| --- | --- | --- | --- | --- | --- |
| `AB-001` — Forged, expired or invalid user credential/session use | `TA-001` or `TA-003` | A forged, expired or revoked credential/session enters through the client credential/session entry point. If validation is incomplete at the External Client, External IdP or consuming-capability transitions, invalid identity/session evidence may reach a protected operation. | `TB-001`, `TB-003`, `TB-004`; `AS-001`, `AS-002` | Impersonation or continued access after revocation. Identity/session evidence must be validated, and identity alone grants no business permission. | `NT-001`; IdP, session and revocation model unresolved; Identity Architecture + Security. |
| `AB-002` — Missing, forged or conflicting Tenant Context | Actor attribution remains unresolved; Normative Annex E of `V3-003-DEC-006` records an applicable adversarial Actor without assigning a stable Actor ID. | Tenant selector or context evidence is missing, forged or conflicts with validated evidence. An invalid Context is created or propagated to domain or persistence work without validated Membership or trusted workload provenance. | `TB-005`, `TB-008`; `AS-003` | Cross-tenant access or incorrect tenant attribution. Tenant Context must derive from validated Membership or provenance, and missing, conflicting or invalid Context must fail closed. | `NT-002`; Context format, propagation and transaction binding unresolved; Tenant Management + Security. |
| `AB-003` — Direct resource/action authorization bypass | `TA-002`, `TA-003`, `TA-004` or `TA-010` | A resource identifier or business action passes an Entry/Gateway or calling service, but the resource-owning Domain does not independently authorize the object and action. | `TB-002`, `TB-007`; `AS-004` and the affected Domain Asset | Unauthorized viewing or modification of a Business Resource. The resource-owning Domain makes and enforces the final authorization decision. | `NT-003`; resource/action policy matrices unresolved; Resource-owning Domain + Security. |
| `AB-007` — Cross-tenant data access or RLS/context isolation bypass | Actor attribution remains unresolved; historical `TA-P12` is a cross-tenant/cross-cell objective, not a stable Actor. | Shared tenant-owned persistence is accessed with missing, stale or incorrect Tenant Context, incomplete application authorization, ineffective RLS, or a runtime role capable of bypassing tenant protection. | `TB-008`; `AS-016` and affected tenant-owned Domain Assets | Cross-tenant disclosure, mutation or deletion. Validated transaction Tenant Context, application authorization, tenant-scoped constraints, PostgreSQL RLS and a non-bypass runtime role are required. | `NT-007`; runtime RLS integration, role and connection-context evidence unresolved; Data Architecture + Tenant Security + owning Service. |
| `AB-008` — Plugin grant, installation or tenant-boundary violation | `TA-008` or `TA-009` | A package, installation or runtime request with invalid publisher/package trust, Installation identity, tenant binding or grant crosses the Plugin Control Plane, Extension Gateway or destination-Domain boundaries. | `TB-009`, `TB-010`, `TB-011`, `TB-012`; `AS-017` and affected Domain Assets | Cross-installation, cross-tenant or unauthorized Domain action. Plugin Package, Installation and Runtime are distinct; Installation identity, tenant binding, grants, Gateway enforcement and final Domain authority remain required. | `NT-008`; package trust, grant, revocation and runtime-isolation model unresolved; Plugin Platform + Domain Security + Operations. |
| `AB-009` — Forged or unauthorized event provenance | `TA-005`, `TA-009`, `TA-010` or `TA-012` | An event with an unauthorized producer, tenant scope, contract version or provenance is published or delivered and is accepted by a Consumer as authority for a business effect. | `TB-013`, `TB-014`; `AS-018` and affected consumer state | Unauthorized state transition or corrupted projection. The producing Domain owns the Fact and event contract; provenance must be validated and the Consumer remains responsible for its effect. | `NT-009`; event envelope, producer provenance and broker/consumer authorization unresolved; Messaging Architecture + producing/consuming Domains + Security. |
| `AB-011` — Malicious event replay | Stable Actor attribution remains unresolved; the scenario assumes an applicable Actor with access to a previously valid event or delivery path. | A valid prior event is deliberately replayed and a Consumer applies a sensitive business effect again without effective current constraints or idempotency. | `TB-013`, `TB-014`; `AS-018` and affected consumer state | Duplicate business effect or state corruption. Authorization and business constraints remain effective, and idempotent processing applies where mandated; valid duplicates are not automatically attacks and are not required to be unconditionally rejected. | `NT-011`; idempotency key, replay, transaction-boundary and reconciliation semantics unresolved; Messaging Architecture + consuming Domain + Security. |
| `AB-013` — Privileged operator bypasses destination-domain authorization | `TA-006` | A privileged operation travels from an Operator through the Operational Platform to a destination Domain, but platform privilege or operational execution is treated as a replacement for destination-Domain authorization. | `TB-017`, `TB-018`; `AS-014` and affected Domain Assets | Unauthorized privileged mutation or cross-tenant action. A limited identity, explicit Tenant/Platform scope, destination-Domain authorization and traceable Audit are required. | `NT-013`; privileged Role/Action Catalog, approval flow and break-glass model unresolved; Operational Platform + destination Domains + Security. |
| `AB-014` — File or Report access outside tenant/resource/disclosure authority | `TA-002`, `TA-003` or `TA-010` | A File ID, Attachment Link, Report ID or projection access is treated as sufficient authority, or File/Reporting authorization is evaluated without the applicable resource relationship or source-data disclosure restriction. | `TB-020`, `TB-021`, `TB-022`, `TB-023`; `AS-011`, `AS-012` and affected source Assets | Unauthorized disclosure. File-resource authorization and resource-owner authorization of the Attachment relationship remain distinct; Reporting authorization must preserve source disclosure restrictions. Authorized projections remain permitted and no synchronous per-record source call is mandated. | `NT-014`; Attachment, Report Set and projection authorization matrices unresolved; File/Reporting owners + source/resource-owning Domains + Security. |
| `AB-016` — Audit-record tampering | Stable Actor attribution remains unresolved; the scenario assumes an applicable privileged Actor. | A privileged Actor reaches Audit storage or access paths and modifies, deletes or substitutes an Audit record or integrity evidence. | `TB-019`; `AS-013` | Loss of Audit integrity, accountability or reliable incident reconstruction. Audit integrity protection is required, but no retention or maintenance mechanism is selected. | `NT-016`; storage, integrity, authorized-maintenance and recovery mechanisms unresolved; Audit owner + Security. |
| `AB-019` — Central or federation component asserts implicit Sovereign authority | `TA-012` | A Central/federation request or assertion is accepted as local authority without locally approved scope and causes a change to trust, policy, grants, secrets or operations. | `TB-016`; `AS-019`, `AS-020` | Loss of Sovereign-local authority. Central has no implicit local administration; federation is locally approved, authenticated and policy controlled. | `NT-019`; federation protocol, trust anchors, local consent and command scope unresolved; Sovereign Operations + Security + Architecture. |
| `AB-020` — Critical Sovereign operation depends on unavailable Central authority | `TS-003` or an attacker-induced outage; any adversarial Actor attribution remains unresolved. | A critical local operation requires a synchronous Central dependency for authorization or completion and becomes unavailable when Central connectivity or authority is absent. | `TB-016`; `AS-020` | Loss of local business, security or operational continuity. Critical Sovereign operations must not depend on synchronous Central availability; this does not establish Full Air-Gap support. | `NT-020`; Critical Local Operation Catalog, disconnected-duration and recovery/reconciliation evidence unresolved; Sovereign Operations + Security. |

### Normative Annex B — Security Requirement Candidate Register

Every entry in this annex has `Requirement Approval Status = PROPOSED — NOT APPROVED`. The category records analytical provenance and review obligations; it does not make a Candidate mandatory.

| Candidate | Category | Exact candidate requirement statement | Source invariant and traceability | Expected security property and candidate verification method | Missing evidence and security-review responsibility | Requirement Approval Status |
| --- | --- | --- | --- | --- | --- | --- |
| `SR-CAND-001` | `RESTATEMENT` | Every receiving boundary must reject forged, expired, revoked or otherwise invalid identity/session evidence. Valid evidence establishes a Principal only and does not create Business Authorization. | `AB-001`; `TB-001`, `TB-003`, `TB-004`; `AS-001`, `AS-002`; validated identity/session and separation from authorization. | Identity authenticity and freshness; candidate `NT-001` scenarios using invalid credential/session evidence. | IdP, session and revocation model; Identity Architecture + Security. | `PROPOSED — NOT APPROVED` |
| `SR-CAND-002` | `DERIVED` | Each Consumer must validate the identity/session evidence required at its own trust boundary and must not treat internal network location or an upstream authentication result alone as authority. | `AB-001`; `TB-004`; `AS-001`, `AS-002`; authentication at every service trust boundary. | Boundary authentication; candidate direct-consumer negative scenarios. | Evidence propagation and audience rules; Identity Architecture + Security. | `PROPOSED — NOT APPROVED` |
| `SR-CAND-003` | `RESTATEMENT` | Tenant Context must be established only from validated Membership or trusted workload provenance. Missing, forged, conflicting or invalid Context must fail closed before domain or persistence work. | `AB-002`; `TB-005`, `TB-008`; `AS-003`; approved Tenant Context invariant. | Tenant isolation and fail-closed behavior; candidate `NT-002`. | Tenant Context contract; Tenant Management + Security. | `PROPOSED — NOT APPROVED` |
| `SR-CAND-004` | `DERIVED` | Tenant Context used for persistence must belong to the same validated operation and transaction; Context remaining from another operation or reused connection must not be usable. | `AB-002`; `TB-008`; `AS-003`, `AS-016`; validated transaction-local Tenant Context. | Context integrity; candidate connection-reuse and transaction-boundary negative scenarios. | RLS and connection-context integration; Data Architecture + Tenant Security. | `PROPOSED — NOT APPROVED` |
| `SR-CAND-005` | `RESTATEMENT` | The resource-owning Domain must independently authorize every resource/action. A Gateway, UI, IdP or calling-service decision is not sufficient. | `AB-003`; `TB-002`, `TB-007`; `AS-004` and affected Domain Asset; Domain-owned authorization. | Final Domain authority; candidate `NT-003` direct-service denial matrix. | Resource/action policy matrices; Resource-owning Domain + Security. | `PROPOSED — NOT APPROVED` |
| `SR-CAND-006` | `DERIVED` | A request for an existing resource outside the caller's authority must not disclose resource data or permission-sensitive detail. | `AB-003`; `TB-002`, `TB-007`; `AS-004` and affected Domain Asset; data minimization and Domain authorization. | Confidential denial; candidate unauthorized-object response matrix. | Safe error and disclosure policy; Resource-owning Domain + Security. | `PROPOSED — NOT APPROVED` |
| `SR-CAND-007` | `RESTATEMENT` | Tenant-owned reads and writes must apply application authorization and applicable PostgreSQL RLS, and the ordinary runtime role must not be capable of bypassing tenant protection. | `AB-007`; `TB-008`; `AS-016` and affected tenant-owned Domain Assets; ADR-V3-003 and ADR-V3-007. | Defense-in-depth tenant isolation; candidate `NT-007` using the actual runtime role in later authorized validation. | RLS schema, role and integration evidence; Data Architecture + Tenant Security + owning Service. | `PROPOSED — NOT APPROVED` |
| `SR-CAND-008` | `DERIVED` | Missing or invalid transaction Tenant Context must not result in an unscoped query, a default tenant or fallback access. | `AB-007`; `TB-008`; `AS-016` and affected tenant-owned Domain Assets; fail-closed invariant. | Fail-closed persistence isolation; candidate missing/invalid-context persistence scenarios. | Context failure and connection lifecycle semantics; Data Architecture + Tenant Security. | `PROPOSED — NOT APPROVED` |
| `SR-CAND-009` | `RESTATEMENT` | A Plugin action may be evaluated only with a valid Installation identity, tenant binding and applicable grant, and the destination Domain must make the final resource/action authorization decision. | `AB-008`; `TB-009`, `TB-010`, `TB-011`, `TB-012`; `AS-017` and affected Domain Assets; ADR-V3-006. | Plugin and tenant authorization; candidate `NT-008`. | Installation identity and grant model; Plugin Platform + Domain Security. | `PROPOSED — NOT APPROVED` |
| `SR-CAND-010` | `POLICY/DESIGN` | The semantics of a grant change or revocation must explicitly define when continued use of that grant is no longer authorized. | `AB-008`; `TB-010`, `TB-011`, `TB-012`; `AS-017`; Plugin grant/lifecycle requirement. | Grant revocation and freshness; candidate revocation-transition scenarios. | Propagation, caching, offline and failure policy; Plugin Platform + Security + Operations. | `PROPOSED — NOT APPROVED` |
| `SR-CAND-011` | `RESTATEMENT` | A Consumer must not accept a producer, tenant scope, contract version or event provenance as trusted without validation. | `AB-009`; `TB-013`, `TB-014`; `AS-018`; producer-owned Fact and explicit versioned event. | Event-provenance authenticity; candidate `NT-009`. | Event envelope and provenance design; Messaging Architecture + producing/consuming Domains + Security. | `PROPOSED — NOT APPROVED` |
| `SR-CAND-012` | `DERIVED` | An event from an unauthorized producer or scope must not create an unauthorized business effect. This Candidate does not select rejection, dead-lettering, quarantine or another handling mechanism. | `AB-009`; `TB-014`; `AS-018` and affected consumer state; validated provenance and Consumer-owned effect. | Effect authorization; candidate unauthorized-producer/scope scenarios. | Failure-handling policy; Messaging Architecture + consuming Domain + Security. | `PROPOSED — NOT APPROVED` |
| `SR-CAND-013` | `RESTATEMENT` | A duplicate or replay must not create a prohibited duplicate business effect, and current authorization and business constraints must remain effective. This Candidate does not require unconditional rejection of a valid duplicate. | `AB-011`; `TB-013`, `TB-014`; `AS-018` and affected consumer state; Inbox/idempotency invariant. | Idempotent effect; candidate `NT-011`. | Business idempotency and transaction semantics; Messaging Architecture + consuming Domain + Security. | `PROPOSED — NOT APPROVED` |
| `SR-CAND-014` | `POLICY/DESIGN` | Idempotency key, replay-recognition scope or window, and response and reconciliation behavior must be approved for each applicable contract. | `AB-011`; `TB-014`; `AS-018`; messaging consistency requirements. | Replay and idempotency policy; candidate crash-boundary and replay scenarios. | Approved replay/idempotency model; Messaging Architecture + producing/consuming Domains + Security. | `PROPOSED — NOT APPROVED` |
| `SR-CAND-015` | `RESTATEMENT` | A Privileged Operation must have a limited identity, explicit Tenant/Platform scope, destination-Domain authorization and traceable Audit. | `AB-013`; `TB-017`, `TB-018`; `AS-014` and affected Domain Assets; approved operational invariant. | Privilege separation and accountability; candidate `NT-013`. | Privileged Role/Action Catalog; Operational Platform + destination Domains + Security. | `PROPOSED — NOT APPROVED` |
| `SR-CAND-016` | `DERIVED` | Platform or Operator privilege must not replace destination-Domain resource/action authorization. | `AB-013`; `TB-018`; affected Domain Assets; ADR-V3-005 and Operational Platform boundary. | No universal authorization; candidate direct-destination denial scenarios. | Privileged-operation workflow; Operational Platform + destination Domains + Security. | `PROPOSED — NOT APPROVED` |
| `SR-CAND-017` | `RESTATEMENT` | A File ID or Attachment Link does not create access. File-resource authorization and authorization of the Attachment relationship by the resource owner must both be preserved. | `AB-014`; `TB-020`, `TB-021`; `AS-011` and affected source Assets; File/Attachment boundary invariant. | File and resource confidentiality; candidate `NT-014` File/Attachment matrix. | Multi-link and deletion semantics; File/Content + resource-owning Domain + Security. | `PROPOSED — NOT APPROVED` |
| `SR-CAND-018` | `RESTATEMENT` | A Report or authorized Projection must not bypass Tenant Isolation, Report authorization or source-data disclosure restrictions. This Candidate does not mandate a synchronous per-record call to a source Domain. | `AB-014`; `TB-022`, `TB-023`; `AS-012` and affected source Assets; Reporting boundary invariant. | Reporting confidentiality; candidate Report/Projection authorization matrix. | Report Set and Projection policy; Reporting + source Domains + Security. | `PROPOSED — NOT APPROVED` |
| `SR-CAND-019` | `RESTATEMENT` | Unauthorized alteration or deletion of an Audit record or its integrity evidence must be prevented or detectable. This Candidate does not define a retention duration. | `AB-016`; `TB-019`; `AS-013`; Audit integrity invariant. | Audit integrity and tamper evidence; candidate `NT-016`. | Storage and integrity mechanism; Audit owner + Security. | `PROPOSED — NOT APPROVED` |
| `SR-CAND-020` | `POLICY/DESIGN` | Correction, authorized maintenance, retention, archival and recovery semantics for Audit records must be defined in a separate approved decision. | `AB-016`; `TB-019`; `AS-013`; Audit lifecycle concerns. | Audit lifecycle policy; candidate lifecycle and failure scenarios. | Mandatory Event Catalog, retention and failure policy; Audit owner + Security + Operations. | `PROPOSED — NOT APPROVED` |
| `SR-CAND-021` | `RESTATEMENT` | A Central or Federation identity creates no implicit Sovereign administration; a local effect requires Sovereign-local authority. | `AB-019`; `TB-016`; `AS-019`, `AS-020`; ADR-V3-004. | Local sovereignty; candidate `NT-019`. | Federation protocol; Sovereign Operations + Security + Architecture. | `PROPOSED — NOT APPROVED` |
| `SR-CAND-022` | `DERIVED` | A Central assertion that is invalid, locally unapproved or outside local scope must fail closed without an unauthorized change to local authority state. | `AB-019`; `TB-016`; `AS-019`, `AS-020`; Sovereign-local final authority. | Authority integrity; candidate negative federation matrix. | Local approval and scope semantics; Sovereign Operations + Security + Architecture. | `PROPOSED — NOT APPROVED` |
| `SR-CAND-023` | `RESTATEMENT` | Critical Sovereign business, security and operational actions must not depend on synchronous Central availability for authorization or completion. This Candidate does not establish Full Air-Gap support. | `AB-020`; `TB-016`; `AS-020`; ADR-V3-004. | Local operational continuity; candidate `NT-020` disconnected scenarios. | Critical Local Operation Catalog; Sovereign Operations + Security. | `PROPOSED — NOT APPROVED` |
| `SR-CAND-024` | `POLICY/DESIGN` | Disconnected operation, permissible local behavior, reconnect and reconciliation semantics must be approved for each applicable operation and data class. | `AB-020`; `TB-016`; `AS-020`; Sovereign disconnection and recovery concerns. | Disconnection and recovery policy; candidate outage/reconnect scenarios. | Duration, conflict and reconciliation policy; Sovereign Operations + Security + affected Domain owners. | `PROPOSED — NOT APPROVED` |

### Normative Annex C — Cross-Reference and Verification Matrix

This matrix is normative traceability for the analytical baseline. Candidate verification methods do not constitute executed or passed tests.

| Abuse Case | Actor or Source | Entry Point | Trust Boundaries | Assets | Approved invariant | Candidate Requirements | Negative Test | Main evidence gap | Security Review Owner |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `AB-001` | `TA-001`, `TA-003` | Client credential/session | `TB-001`, `TB-003`, `TB-004` | `AS-001`, `AS-002` | Validated identity/session; identity alone grants no business permission | `SR-CAND-001`, `SR-CAND-002` | `NT-001` | IdP/session/revocation model | Identity Architecture + Security |
| `AB-002` | Applicable adversarial Actor; stable Actor attribution unresolved | Tenant selector/context evidence | `TB-005`, `TB-008` | `AS-003` | Tenant Context derives from validated Membership/provenance and invalid Context fails closed | `SR-CAND-003`, `SR-CAND-004` | `NT-002` | Context format, propagation and transaction binding | Tenant Management + Security |
| `AB-003` | `TA-002`, `TA-003`, `TA-004`, `TA-010` | Resource identifier or business action | `TB-002`, `TB-007` | `AS-004` and affected Domain Asset | Resource-owning Domain makes the final authorization decision | `SR-CAND-005`, `SR-CAND-006` | `NT-003` | Resource/action policy matrices | Resource-owning Domain + Security |
| `AB-007` | Applicable adversarial Actor; stable Actor attribution unresolved; historical `TA-P12` is an objective | Shared tenant-owned persistence access | `TB-008` | `AS-016` and affected tenant-owned Domain Assets | Application authorization, validated Context, tenant constraints, RLS and non-bypass role | `SR-CAND-007`, `SR-CAND-008` | `NT-007` | Runtime RLS and connection-context integration | Data Architecture + Tenant Security + owning Service |
| `AB-008` | `TA-008`, `TA-009` | Package, installation or runtime request | `TB-009`, `TB-010`, `TB-011`, `TB-012` | `AS-017` and affected Domain Assets | Installation identity, tenant binding, grants, Gateway and final Domain authority | `SR-CAND-009`, `SR-CAND-010` | `NT-008` | Package trust, grant, revocation and isolation model | Plugin Platform + Domain Security + Operations |
| `AB-009` | `TA-005`, `TA-009`, `TA-010`, `TA-012` | Event publication or delivery | `TB-013`, `TB-014` | `AS-018` and affected consumer state | Producer-owned Fact, explicit versioned event and validated provenance | `SR-CAND-011`, `SR-CAND-012` | `NT-009` | Event envelope and provenance design | Messaging Architecture + producing/consuming Domains + Security |
| `AB-011` | Applicable Actor with event access; stable Actor attribution unresolved | Replayed event | `TB-013`, `TB-014` | `AS-018` and affected consumer state | Authorization, business constraints and applicable idempotency remain effective | `SR-CAND-013`, `SR-CAND-014` | `NT-011` | Replay, idempotency and transaction semantics | Messaging Architecture + consuming Domain + Security |
| `AB-013` | `TA-006` | Privileged operation | `TB-017`, `TB-018` | `AS-014` and affected Domain Assets | Limited identity, explicit scope, destination authorization and Audit | `SR-CAND-015`, `SR-CAND-016` | `NT-013` | Privileged Role/Action Catalog | Operational Platform + destination Domains + Security |
| `AB-014` | `TA-002`, `TA-003`, `TA-010` | File or Report request | `TB-020`, `TB-021`, `TB-022`, `TB-023` | `AS-011`, `AS-012` and affected source Assets | File/Report authorization plus Attachment/source-disclosure boundaries | `SR-CAND-017`, `SR-CAND-018` | `NT-014` | Attachment, Report Set and Projection authorization matrices | File/Reporting owners + source/resource-owning Domains + Security |
| `AB-016` | Applicable privileged Actor; stable Actor attribution unresolved | Audit storage or access | `TB-019` | `AS-013` | Audit integrity protection | `SR-CAND-019`, `SR-CAND-020` | `NT-016` | Storage, integrity and authorized-maintenance mechanism | Audit owner + Security |
| `AB-019` | `TA-012` | Central or Federation request | `TB-016` | `AS-019`, `AS-020` | Sovereign-local final authority; Central has no implicit administration | `SR-CAND-021`, `SR-CAND-022` | `NT-019` | Federation, trust and local-approval model | Sovereign Operations + Security + Architecture |
| `AB-020` | `TS-003` or attacker-induced outage; adversarial Actor attribution unresolved | Central dependency during outage | `TB-016` | `AS-020` | No synchronous Central dependency for critical local operations | `SR-CAND-023`, `SR-CAND-024` | `NT-020` | Critical Local Operation Catalog and disconnected evidence | Sovereign Operations + Security |

### Normative Annex D — Open Assumptions, Decision Dependencies and Backlog Register

#### D.1 Unresolved Actor attribution

| Abuse Case | Unresolved attribution |
| --- | --- |
| `AB-002` | `V3-003-DEC-006` identifies an applicable adversarial Actor but does not assign a stable Actor ID. |
| `AB-007` | No single stable Actor is assigned; historical `TA-P12` is a cross-tenant/cross-cell objective, not an Actor. |
| `AB-011` | The Actor is an applicable Actor with event access; no stable Actor assignment has been approved. |
| `AB-016` | The Actor is an applicable privileged Actor; no stable Actor assignment has been approved. |
| `AB-020` | `TS-003` is defined, but any Actor responsible for an attacker-induced outage remains unresolved. |

#### D.2 Open threat and implementation assumptions

- Identity provider, token/session lifecycle and revocation propagation.
- Tenant Context representation, provenance, propagation and transaction binding.
- Domain resource/action authorization matrices and disclosure-safe denial behavior.
- Runtime RLS integration, role ownership, non-bypass evidence and pooled-connection Context handling.
- Plugin publisher/package trust, Installation identity, grants, revocation and runtime isolation.
- Event envelope, producer provenance, consumer authorization, replay and idempotency design.
- Privileged Role/Action Catalog, approval flow, emergency revocation and break-glass behavior.
- File/Attachment and Reporting/Projection disclosure matrices.
- Audit integrity, authorized maintenance, Event Catalog, retention and failure policy.
- Sovereign federation, local approval, Critical Local Operation Catalog and disconnected operation evidence.
- Deployment-profile-specific implementation and validation evidence.
- Scenario-level business impact remains unassessed unless separately approved BIA evidence applies to the affected operation and failure scenario.

#### D.3 Architecture-decision dependencies

| Area | Open dependencies |
| --- | --- |
| Identity, session and workload identity | `OD-009`, `OD-010`, `OD-011`, `OD-012` |
| RLS and persistence integration | `OD-013`, `OD-014` |
| Plugin contracts and runtime | `OD-008`, `OD-016`, `OD-021` |
| Messaging, scheduling and contract verification | `OD-008`, `OD-019`, `OD-020` |
| File and Reporting, depending on the applicable use case | `OD-007`, `OD-008`, `OD-017`, `OD-018`, `OD-020` |
| Sovereign operation | `OD-001`, `OD-011`, `OD-012`, `OD-015`, `OD-023` |
| Privileged operations and Audit | Separate explicit decisions remain required for the Privileged Role/Action Catalog, Audit Event Catalog, integrity mechanism, retention and failure semantics. |

#### D.4 Unassessed Abuse Case backlog

The following nine Abuse Cases remain unassessed backlog items. Exclusion from the bounded set does not assign low likelihood, low severity, accepted risk or reduced architectural significance.

| Backlog area | Abuse Cases | Deferred analytical scope |
| --- | --- | --- |
| Workload identity, freshness and persistence access | `AB-004`, `AB-005`, `AB-006` | Confused deputy/workload identity, stale Membership/Entitlement state and unauthorized private-persistence access. |
| Messaging reliability and consistency | `AB-010`, `AB-012` | Valid duplicate delivery and delayed/out-of-order delivery. |
| Audit completeness and disclosure | `AB-015`, `AB-017`, `AB-018` | Mandatory-event omission, unauthorized Audit disclosure and sensitive-data leakage through Audit payload. |
| Build and release supply chain | `AB-021` | Tampered dependency, build input or artifact reaching deployment. |

#### D.5 Security Review responsibilities

| Review area | Responsible review roles |
| --- | --- |
| Identity, authenticator, token and session assumptions | Identity Architecture + Security |
| Tenant Membership, Tenant Context and cross-tenant threats | Tenant Management + Security |
| RLS and persistence isolation | Data Architecture + Security + owning Service |
| Domain resource/action authorization | Resource-owning Domain + Security |
| Plugin package, installation, grants, runtime and Gateway | Plugin Platform + Security + Operations |
| Events, provenance, replay and delivery behavior | Messaging Architecture + producing/consuming Domains + Security |
| File/Attachment and Reporting disclosure boundaries | File/Reporting owners + source/resource-owning Domains + Security |
| Audit integrity and disclosure | Audit owner + Security + producing Domains |
| Privileged operations | Operational Platform + destination Domains + Security |
| Sovereign/Central authority and disconnection | Sovereign Operations + Security + Architecture |

These are role allocations only. They record no individual appointment, team acceptance, completed review or sign-off.

#### D.6 Normative and unresolved boundaries

- The selected scenario set, Scenario Register, Candidate Register, Cross-Reference Matrix, backlog membership and recorded status dimensions are normative for this approved analytical baseline.
- Actor-attribution gaps, evidence gaps and Open Decision dependencies are normative records of unresolved status; their inclusion does not resolve them.
- Attack feasibility, likelihood, severity, risk rating, business impact and implementation effectiveness remain unassessed or unverified unless separately approved.
- Candidate verification methods are specifications for future evidence preparation only and do not constitute executed or passed tests.

## V3-003-DEC-008 — Hybrid Plugin Grant Authorization: Foundational Principles

**Decision Status:** `APPROVED — OWNER`

**Decision Authority:** Project Owner

**Related Task:** `V3-003 — NFR and Threat Assumptions`

**Related Candidate:** `SR-CAND-010 — PROPOSED — NOT APPROVED`

**Independent Security Review:** `PENDING — NOT SIGNED OFF`

### Approval provenance

| Field | Recorded value |
| --- | --- |
| Approval authority | Project Owner |
| Approval evidence | Explicit Project Owner instruction approving the four foundational principles of the Hybrid / Operation-Sensitive Plugin Grant Authorization model and authorizing their repository recording |
| Approval date | Not recorded |
| Security reviewer | Not recorded |
| Independent security sign-off | Pending; not completed |
| Implementation or runtime evidence | Not provided |

### 1. Decision scope

The Project Owner approves only the following four foundational architectural principles for the Hybrid / Operation-Sensitive Plugin Grant Authorization model:

1. Operation-sensitive classification based on authority, data, business-state impact and reversibility.
2. Valid Grant Evidence bound to the authorized Grant Authority, Plugin Installation, Tenant and Deployment Profile.
3. Separation of Logical Revocation Effectiveness from distributed Enforcement Confirmation, without allowing ineffective Grants to confer new authorization.
4. Dedicated Sovereign final local authority, with no implicit Central or Federation administration.

No detailed policy or implementation mechanism is approved by this decision.

### 2. Principle 1 — Operation-sensitive classification

Operations are classified conceptually based on authority impact, confidentiality, integrity, business-state changes and reversibility.

This principle does not approve `OC-0` through `OC-4` as a normative taxonomy.

### 3. Principle 2 — Valid Grant Evidence

Grant Evidence is accepted only when valid for the relevant authorized Grant Authority, Plugin Installation, Tenant, scope and Deployment Profile.

Extension Gateway enforcement and Domain-Owned final resource/action authorization remain required and independent.

This principle does not prescribe online validation, caching, token types or synchronous Control Plane calls.

### 4. Principle 3 — Revocation effectiveness and enforcement confirmation

Logical Revocation Effectiveness is distinct from distributed Enforcement Confirmation.

An ineffective or revoked Grant must not establish new authorization.

This principle does not claim immediate global revocation enforcement and does not define numeric freshness, propagation or cutoff targets.

### 5. Principle 4 — Dedicated Sovereign authority

Dedicated Sovereign retains final local authority.

Central state and Federation assertions cannot create implicit local administration.

This principle does not select reconnection, reconciliation, disconnected-operation or Full Air-Gap policy.

### 6. Relationship to approved architecture

The four principles preserve the existing separation of Plugin Package, Plugin Installation and Plugin Runtime Instance; Installation-scoped identity, Tenant binding and grants; Extension Gateway enforcement; and final authorization by the resource-owning Domain. They do not change ADR-V3-004, ADR-V3-005, ADR-V3-006, `V3-003-DEC-006` or `V3-003-DEC-007`.

### 7. Explicit non-approvals

This decision does not approve:

- `SR-CAND-010` as a final Security Requirement.
- Any other `SR-CAND-001` through `SR-CAND-024` as a final Security Requirement.
- Plugin operation taxonomy `OC-0` through `OC-4`.
- Grant state-machine implementation.
- Issuance or revocation administrator roles.
- Emergency revocation procedures.
- In-flight operation cutoff.
- Freshness intervals, TTLs or revocation deadlines.
- Token, cache, API, event, broker or persistence mechanisms.
- Membership or Entitlement coupling.
- Sovereign reconnection, reconciliation or disconnected-operation policy.
- Full Air-Gap support.
- Runtime controls or implementation evidence.
- Negative Security Test results.
- Risk likelihood, severity, rating or acceptance.
- Security exceptions or mitigation implementation.
- Implementation, Security or Production Readiness.
- Closure of an Open Decision.

### 8. Independent status dimensions

| Dimension | Status |
| --- | --- |
| `DECISION_STATUS` | `APPROVED — OWNER` |
| `SECURITY_REQUIREMENT_CANDIDATES` | `PROPOSED — NOT APPROVED` |
| `THREAT_ASSUMPTION_VALIDATION_STATUS` | `PENDING SECURITY REVIEW` |
| `SECURITY_REVIEW_STATUS` | `NOT_SIGNED_OFF` |
| `IMPLEMENTATION_EVIDENCE_STATUS` | `NOT_VERIFIED` |
| `NEGATIVE_TEST_EXECUTION_STATUS` | `NOT_EXECUTED` |

### 9. Decision effect

These four principles may constrain later Plugin Grant policy preparation and operation-sensitive authorization analysis. They do not select detailed policy, authorize implementation, resolve the evidence gaps recorded for `AB-008` and `NT-008`, approve `SR-CAND-010`, or close any Open Decision.

`V3-003` remains `IN PROGRESS`. `OD-001` through `OD-023` remain `OPEN`. `V3-003-DEC-001` through `V3-003-DEC-007` and their normative annexes remain unchanged.

## V3-003-DEC-009 — Event Replay and Idempotency: Foundational Architectural Principles

**Decision Status:** `APPROVED — OWNER`

**Decision Authority:** Project Owner

**Related Task:** `V3-003 — NFR and Threat Assumptions`

**Related Candidate:** `SR-CAND-014 — PROPOSED — NOT APPROVED`

**Independent Security Review:** `NOT_SIGNED_OFF`

### Approval provenance

| Field | Recorded value |
| --- | --- |
| Approval authority | Project Owner |
| Approval evidence | Explicit Project Owner instruction approving the eight bounded foundational architectural principles for Event Replay and Idempotency and authorizing their repository recording |
| Approval date | Not recorded |
| Security reviewer | Not recorded |
| Independent security sign-off | Pending; not completed |
| Implementation or runtime evidence | Not provided |

### 1. Decision scope

The Project Owner approves only the following eight foundational architectural principles for Event Replay and Idempotency:

1. Distinct Messaging Scenarios.
2. Layered, Contract-Specific Idempotency.
3. Consumer-Owned Validation and Effects.
4. Durable Consistency.
5. External Effects.
6. Contract-Specific Ordering.
7. Retry and Re-drive Security.
8. Sovereign Local Authority.

This is an actual Owner approval of these eight bounded architectural principles, not approval of detailed messaging policies or Security Requirements. In particular, `SR-CAND-014` remains `PROPOSED — NOT APPROVED`.

### 2. Principle 1 — Distinct Messaging Scenarios

The following scenarios remain distinct:

- Valid duplicate delivery.
- Malicious replay.
- Forged or unauthorized provenance.
- Delayed or out-of-order delivery.

Valid broker redelivery is not inherently malicious. The stable analytical traceability remains `AB-009` / `NT-009` for forged or unauthorized event provenance, `AB-010` / `NT-010` for valid duplicate delivery, `AB-011` / `NT-011` for malicious replay, and `AB-012` / `NT-012` for delayed or out-of-order delivery.

### 3. Principle 2 — Layered, Contract-Specific Idempotency

Message identity, Consumer processing identity, business-operation identity, state-transition identity and external-effect identity are distinct concerns and must be handled according to the applicable contract and operation.

This principle does not select a universal idempotency key and does not assert end-to-end exactly-once execution. At-least-once delivery and possible duplicate delivery remain part of the approved architecture baseline.

### 4. Principle 3 — Consumer-Owned Validation and Effects

The Producer owns the Business Fact and its versioned Event Contract. The Consumer owns validation of the received event and the business effects it applies.

The Consumer must preserve applicable Tenant Context validation, producer and event provenance validation, contract compatibility, and final Domain authorization for protected business resources. Producer publication or upstream acceptance does not replace Consumer responsibility or Domain-Owned Authorization.

### 5. Principle 4 — Durable Consistency

Where applicable, durable Consumer processing evidence and owned-database business effects must have a defined consistency boundary that prevents an acknowledged delivery from silently losing or duplicating the protected effect.

This is a bounded, applicability-aware requirement. It does not create a universal distributed-transaction requirement. Where local atomicity is not applicable, separate consistency, failure, recovery and reconciliation semantics must be defined for the applicable operation.

### 6. Principle 5 — External Effects

Inbox/Outbox processing alone does not prove exactly-once external effects. Operation-appropriate handling of external effects must be defined separately.

This principle does not select provider idempotency, compensation, outcome-ledger or reconciliation mechanisms and does not assume an external provider supplies exactly-once behavior.

### 7. Principle 6 — Contract-Specific Ordering

Delayed or out-of-order behavior must be specified for each applicable contract, aggregate or operation.

This principle does not establish a global ordering guarantee, event-age rejection policy or replay window.

### 8. Principle 7 — Retry and Re-drive Security

Authorization, validated Tenant Context, producer provenance, contract compatibility and applicable consistency constraints remain effective across retry, recovery, dead-letter processing and administrative re-drive.

Retry or re-drive must not become a path around the Consumer's validation or the resource-owning Domain's final authorization. This principle does not approve retry policies, terminal-failure semantics or administrative workflows.

### 9. Principle 8 — Sovereign Local Authority

Dedicated Sovereign retains final local authority for messaging, recovery and re-drive.

No implicit Central administration or mandatory synchronous Central dependency is created for critical local operations. This principle does not approve Full Air-Gap support or a disconnected-operation, reconnection or reconciliation implementation.

### 10. Relationship to approved architecture and analytical baselines

These principles preserve RabbitMQ as the asynchronous messaging baseline; transactional Outbox; durable Inbox or equivalent idempotency processing evidence; at-least-once delivery; acknowledgement after durable processing; no end-to-end exactly-once claim; no global ordering guarantee; Producer-owned Business Facts and Event Contracts; Consumer-owned validation and effects; Service-owned persistence; versioned contract compatibility; Tenant provenance validation; Domain-Owned Authorization; and Dedicated Sovereign local final authority.

They do not change ADR-V3-004, ADR-V3-005, ADR-V3-007, ADR-V3-008, `V3-003-DEC-006`, `V3-003-DEC-007` or `V3-003-DEC-008`. The normative identities and distinctions of `AB-009` through `AB-012`, `NT-009` through `NT-012`, and `SR-CAND-011` through `SR-CAND-014` remain unchanged.

### 11. Explicit non-approvals

This decision does not approve:

- `SR-CAND-014` or any other `SR-CAND-001` through `SR-CAND-024` as a final Security Requirement.
- A universal idempotency key.
- Replay window or replay eligibility policy.
- Inbox/Outbox schemas or distributed-transaction technology.
- Retry counts, timeout, backoff or retention.
- DLQ/re-drive mechanisms or terminal-failure semantics.
- Global event-ordering guarantees.
- External-provider idempotency assumptions.
- Compensation or reconciliation implementations.
- API or Event Contract envelope technologies.
- Audit retention, catalog or failure policy.
- Numeric NFRs.
- Risk ratings, risk acceptance or security exceptions.
- Executed tests.
- Verified runtime controls.
- Implementation, Security or Production Readiness.
- Closure of an Open Decision.

### 12. Independent status dimensions

| Dimension | Status |
| --- | --- |
| `DECISION_STATUS` | `APPROVED — OWNER` |
| `SECURITY_REQUIREMENT_CANDIDATES` | `PROPOSED — NOT APPROVED` |
| `THREAT_ASSUMPTION_VALIDATION_STATUS` | `PENDING SECURITY REVIEW` |
| `SECURITY_REVIEW_STATUS` | `NOT_SIGNED_OFF` |
| `IMPLEMENTATION_EVIDENCE_STATUS` | `NOT_VERIFIED` |
| `NEGATIVE_TEST_EXECUTION_STATUS` | `NOT_EXECUTED` |

### 13. Decision effect

These eight principles may constrain later contract-specific replay, idempotency, ordering, retry, re-drive, recovery and external-effect policy preparation. They do not approve `SR-CAND-014`, select an implementation mechanism, establish runtime correctness or close any Open Decision.

`V3-003` remains `IN PROGRESS`. `OD-001` through `OD-023` remain `OPEN`. `V3-003-DEC-001` through `V3-003-DEC-008`, the DEC-006 normative inventories and the DEC-007 Normative Annexes A through D remain unchanged.

## V3-003-DEC-010 — Audit Lifecycle, Integrity and Governance: Foundational Architectural Principles

**Decision Status:** APPROVED — OWNER  
**Decision Authority:** Project Owner  
**Related Task:** V3-003 — NFR and Threat Assumptions  
**Related Baselines:** V3-003-DEC-006, V3-003-DEC-007, V3-003-DEC-008, V3-003-DEC-009  
**Related Candidates:** SR-CAND-019, SR-CAND-020 — PROPOSED — NOT APPROVED  
**Independent Security Review:** NOT_SIGNED_OFF  
**Repository Recording:** PENDING VERIFICATION

### 1. Decision Scope

The Project Owner approves ten bounded foundational architectural principles governing Audit ownership, lifecycle, integrity, authorization, evidence handling and Sovereign authority.

This approval establishes architectural and governance obligations only. It does not approve implementation mechanisms, mandatory event definitions, retention durations, legal interpretations or operation-specific Audit failure policies.

### 2. Approved Foundational Principles

#### Principle 1 — Audit Domain Ownership

The Audit Domain remains the authoritative owner of platform-wide Audit records and their authorized projections.

Producing Domains retain ownership of their Business Facts, Domain-specific Audit semantics and the authorization of originating business operations.

Audit ownership does not permit direct access to another Domain's private database or override that Domain's authorization boundary.

#### Principle 2 — Explicit Mandatory Event Catalog Governance

The Mandatory Audit Event Catalog shall have explicit governance ownership and accountable contributors.

The Audit Domain shall coordinate the global catalog, while Producing Domains remain accountable for the meaning and coverage of their respective event categories.

Security, Compliance and other relevant authorities shall participate where their responsibilities apply.

This principle does not approve the catalog's contents, final event classifications or mandatory event completeness criteria.

#### Principle 3 — Append-Oriented Evidence and Traceable Correction

Original Audit evidence shall not be silently overwritten or modified without traceability.

Corrections, supplements and authorized maintenance shall preserve an auditable relationship to the original record and the responsible action.

Business Fact corrections remain under the authority of the Producing Domain.

This principle does not prohibit separately authorized legal deletion, privacy-compliant redaction, lifecycle maintenance or integrity recovery. Their specific conditions and mechanisms require independent policy decisions.

#### Principle 4 — No Implicit Administrator or Operator Authority

Administrator, Operator, Infrastructure Administrator or Platform privileges do not automatically confer authority to read, alter, suppress or delete authoritative Audit evidence.

All such actions remain subject to the applicable Audit Domain authorization and approved governance controls.

#### Principle 5 — Scope-Aware Audit Authorization

Access to Audit resources shall be governed by validated Tenant or Platform context, resource and action authorization, and an applicable authorized purpose.

Platform-scoped evidence shall not automatically become visible to Tenant-scoped identities.

Cross-tenant or privileged investigation access requires explicit authorization and accountability.

This principle does not approve a final Audit role, permission, purpose or emergency-access catalog.

#### Principle 6 — Minimal and Sensitive-Data-Aware Audit Payloads

Audit payloads shall be limited to information necessary for their authorized security, administrative, investigative or accountability purpose.

Sensitive information shall be subject to explicit field governance and appropriate protection.

Secrets, credentials, authentication tokens and unnecessary Business Facts shall not be incorporated into Audit evidence merely for convenience.

This principle establishes data-minimization obligations but does not approve a final field allowlist, redaction mechanism, sensitivity classification or payload schema.

#### Principle 7 — Category-Specific Audit Failure Semantics

Audit ingestion, persistence or evidence-availability failures shall be evaluated according to the relevant event category, originating operation, business impact, reversibility and applicable security or legal obligations.

No universal fail-open or fail-closed policy for all CRM business operations is approved.

Mandatory Audit evidence shall not be silently discarded.

The operation-specific choices among blocking, durable deferral, controlled degraded operation or recovery remain open and require separate decisions.

This principle does not authorize continuation of any operation where an already applicable approved security control requires denial.

#### Principle 8 — Evidence-Grounded Retention Governance

Audit retention, archival, legal hold and permitted deletion shall be governed by explicit policies that account for applicable event categories, jurisdictions, Deployment Profiles, contractual obligations and legally valid preservation or deletion requirements.

No universal retention duration, legal-hold mechanism, deletion permission or jurisdictional rule is approved.

Where requirements conflict, the resolution must be supported by applicable Legal/Compliance authority and an approved policy hierarchy.

#### Principle 9 — Dedicated Sovereign Local Audit Authority

In Dedicated Sovereign deployments, final authority over Audit custody, authorized access, retention execution, maintenance, recovery and locally governed disclosure remains Sovereign-local.

Central or Federation-originated identities, requests or assertions shall not create implicit local administrative or Audit access authority.

Any permitted federation, export or reconciliation shall remain subject to locally approved governance.

This principle does not approve Full Air-Gap, export mechanisms, federation protocols or disconnected reconciliation policies.

#### Principle 10 — Integrity and Recovery Verification Obligations

Audit integrity and recovery shall be subject to explicit verification objectives and profile-appropriate evidence.

The ability to detect or prevent unauthorized alteration, identify relevant completeness gaps, and establish the integrity of restored evidence shall be assessed within the applicable approved requirements and threat assumptions.

Verification evidence shall be independently distinguishable from architectural intent or implementation claims.

This principle does not establish a cryptographic mechanism, verification cadence, numeric recovery target, completed control verification or Independent Security Review sign-off.

### 3. Preserved Architecture Invariants

This decision preserves:

- Audit Core in FIRST_RELEASE.
- Append-oriented authoritative Audit records.
- Audit Domain ownership and Producing Domain boundaries.
- Domain-Owned Authorization.
- Tenant Context validation and Tenant Isolation.
- Separation of Tenant-scoped and Platform-scoped Audit evidence.
- Service-owned persistence.
- Relevant producer-owned and versioned contracts.
- Security-sensitive Audit lifecycle accountability.
- Sensitive-data protection.
- Dedicated Sovereign local authority.
- Evidence-based readiness and independent security validation.

### 4. Explicit Non-Approvals

This decision does not approve:

1. SR-CAND-019, SR-CAND-020 or any other final Security Requirement.
2. Mandatory Audit Event Catalog contents or event classifications.
3. Numeric retention, archival, deletion, verification or recovery periods.
4. Legal Hold, privacy deletion or lawful-erasure procedures.
5. A final retention policy hierarchy or jurisdiction-specific interpretation.
6. Audit ingestion failure actions for particular business operations.
7. Universal fail-open or fail-closed business-operation behavior.
8. Cryptographic integrity technology, key custody or storage mechanisms.
9. Audit Event/API schemas, persistence design or runtime topology.
10. Correction, supplementation, maintenance or recovery implementation workflows.
11. Audit viewer, administrator, investigation or break-glass role catalogs.
12. Archival, export, federation or reconciliation mechanisms.
13. Final sensitive-field allowlists or redaction implementation.
14. Numeric NFRs, including RTO, RPO or SLO.
15. Risk ratings, risk acceptance or security exceptions.
16. Completed Negative Tests, verified controls, Security Review sign-off or Production Readiness.

### 5. Governance and Status Preservation

The following remain unchanged:

- `V3-003 = IN PROGRESS`
- `OD-001..OD-023 = OPEN`
- `SR-CAND-001..024 = PROPOSED — NOT APPROVED`
- `THREAT_ASSUMPTION_VALIDATION_STATUS = PENDING SECURITY REVIEW`
- `SECURITY_REVIEW_STATUS = NOT_SIGNED_OFF`
- `IMPLEMENTATION_EVIDENCE_STATUS = NOT_VERIFIED`
- `NEGATIVE_TEST_EXECUTION_STATUS = NOT_EXECUTED`

Previously approved V3-003 decisions, normative annexes, ADRs, Customer Core Business Criticality decisions and architecture standards remain unchanged.

### 6. Decision Effect

These ten principles form the Owner-approved foundational baseline for subsequent Audit Event Catalog, Failure Semantics, Integrity, Retention, Maintenance, Legal Hold, Permitted Deletion and Recovery policy development.

Approval does not close any Open Decision, finalize any Security Requirement or establish implementation readiness.

The normative scope of this decision is restricted to these ten principles and their explicit non-approvals.

Repository recording shall be verified separately. No immutable Git revision may be claimed until the content has been committed.

## V3-003-DEC-011 — Mandatory Audit Coverage and Durable Evidence: Foundational Principles

**Decision Status:** APPROVED — OWNER  
**Decision Authority:** Project Owner  
**Related Task:** V3-003 — NFR and Threat Assumptions  
**Related Decisions:** V3-003-DEC-006, V3-003-DEC-007, V3-003-DEC-009, V3-003-DEC-010  
**Related Candidates:** SR-CAND-019, SR-CAND-020 — PROPOSED — NOT APPROVED  
**Independent Security Review:** NOT_SIGNED_OFF  
**Repository Recording:** PENDING VERIFICATION

### 1. Decision Scope

The Project Owner approves three bounded foundational principles governing mandatory Audit coverage for supported privileged operations, sensitive Audit access and lifecycle actions, and the durable recording of mandatory Audit publication obligations.

This decision establishes limited architectural obligations. It does not approve a complete Mandatory Audit Event Catalog, operation-specific Audit failure policies, implementation mechanisms or final Security Requirements.

### 2. Approved Principles

#### Principle 1 — Mandatory Audit Evidence for Supported Privileged Operations

Every supported FIRST_RELEASE privileged operation within the approved `FR-SO-004` scope shall produce mandatory Audit evidence for its execution request and material execution outcome.

Applicable outcomes include successful execution, authorization denial and execution failure.

The evidence shall preserve sufficient validated actor, Tenant/Platform scope, action, target, outcome and correlation context to support authorized accountability and investigation, subject to approved sensitive-data protection requirements.

Operator, Platform or infrastructure privileges do not replace authorization by the resource-owning Domain.

This principle does not approve a privileged-action catalog, administrator-role model, emergency-access workflow, event schema or detailed failure-handling policy.

It does not imply that every attempted privileged action will successfully produce evidence under all failure conditions; such conditions require explicit detection, recovery and operation-specific failure policies.

#### Principle 2 — Mandatory Evidence for Sensitive Audit Access and Audit Lifecycle Actions

Sensitive access to authoritative Audit records, including applicable authorized access, authorization denial and material access failure, shall be subject to mandatory Audit evidence obligations.

Supported operations that affect authoritative Audit evidence, integrity or lifecycle — including applicable correction, supplementation, maintenance, recovery and retention actions — shall themselves produce traceable Audit evidence of their initiation and material outcome.

These obligations shall preserve Audit Domain-owned authorization, explicit Tenant/Platform scope, validated purpose where applicable, and the prohibition of implicit Administrator or Operator authority.

The exact catalog of sensitive Audit operations, the point at which evidence is considered durably recorded, and the handling of audit-of-audit recursion remain subject to later policy and design decisions.

This principle does not create unrestricted Audit access, approve legal deletion or redaction procedures, or require a separate event for every internal read, query, processing step or implementation detail.

#### Principle 3 — Durable Publication Obligation for Mandatory Audit Events

For a cataloged mandatory Audit event arising from a service-owned durable business or security-state mutation, successful operation completion shall require a consistently recorded durable Audit publication obligation coordinated with the corresponding originating effect.

Where the originating effect and Audit obligation are within the same service-owned transactional resource, they shall preserve an appropriate atomic consistency boundary.

Where this is not applicable, an independently approved equivalent consistency, recovery and reconciliation guarantee is required.

The originating service shall not treat successful publication, an Outbox record or broker acknowledgement as proof that the Audit Domain has durably ingested the Audit record.

Downstream Audit unavailability may be handled through durable deferral only where the relevant operation-specific policy permits it, silent loss is prevented, and recovery and reconciliation obligations are established.

This principle does not mandate cross-service distributed transactions, a universal Outbox implementation, synchronous Audit ingestion, a particular acknowledgement protocol or a universal `BLOCK` / `DURABLE_DEFER` policy.

The separate Audit failure semantics of read-only or disclosure operations remain unresolved.

### 3. Relationship to Existing Architecture

This decision preserves:

- Audit Core within FIRST_RELEASE.
- Audit Domain ownership of authoritative system-wide Audit evidence.
- Producing Domain ownership of Business Facts and originating operations.
- Domain-Owned Authorization.
- Validated Tenant Context and Tenant Isolation.
- Separation of Tenant-scoped and Platform-scoped Audit evidence.
- Service-owned persistence and transaction boundaries.
- At-least-once messaging and idempotent processing.
- Transactional Outbox and durable Inbox where applicable.
- Append-oriented, integrity-protected Audit evidence.
- Sensitive-data minimization.
- Dedicated Sovereign local final authority.

### 4. Explicit Non-Approvals

This decision does not approve:

1. The complete Mandatory Audit Event Catalog.
2. All `AEC-CAND-001..026` entries as mandatory requirements.
3. Final mandatory event classifications for Identity, MFA, Plugin, Customer, Sales, Request, Work, File or Reporting operations.
4. FIRST_RELEASE product scope for unconfirmed Identity, MFA or Plugin operations.
5. Privileged-action, Audit-viewer, Administrator or break-glass role catalogs.
6. Universal Audit coverage of every business mutation or read.
7. Exact Audit Event/API schemas, payload formats or Event Contracts.
8. Any universal `BLOCK`, `DURABLE_DEFER`, `CONTROLLED_DEGRADED` or `REJECT_OR_ESCALATE` policy.
9. Operation-specific Audit failure semantics.
10. Detailed Outbox, Inbox, broker, acknowledgement or recovery mechanisms.
11. Audit-of-Audit recursion handling.
12. Retention duration, Legal Hold, lawful deletion or redaction procedures.
13. Cryptographic integrity, archival or storage technologies.
14. Numeric NFRs, including RTO, RPO and SLO.
15. Risk ratings, risk acceptance or security exceptions.
16. Final approval of SR-CAND-019, SR-CAND-020 or any other Security Requirement.
17. Executed Negative Tests or verified implementation controls.
18. Independent Security Review sign-off or Production Readiness.

### 5. Governance Preservation

The following statuses remain unchanged:

- `V3-003 = IN PROGRESS`
- `OD-001..OD-023 = OPEN`
- `SR-CAND-001..024 = PROPOSED — NOT APPROVED`
- `THREAT_ASSUMPTION_VALIDATION_STATUS = PENDING SECURITY REVIEW`
- `SECURITY_REVIEW_STATUS = NOT_SIGNED_OFF`
- `IMPLEMENTATION_EVIDENCE_STATUS = NOT_VERIFIED`
- `NEGATIVE_TEST_EXECUTION_STATUS = NOT_EXECUTED`

Previously approved V3-003 decisions, normative annexes, architectural ADRs, FIRST_RELEASE inventory decisions and approved Customer Core Business Criticality assessments remain unchanged.

### 6. Decision Effect

These three principles become the Owner-approved foundational basis for subsequent Privileged Operation Audit Catalog, Audit Access/Lifecycle Event Catalog and operation-specific Durable Audit Obligation design.

They do not finalize the full Audit Catalog or determine Audit failure behavior for individual operations.

Repository recording and Git versioning must be verified separately.

## V3-003-DEC-012 — Customer Core Mandatory Audit and Failure Boundaries

**Decision Status:** APPROVED — OWNER  
**Decision Authority:** Project Owner  
**Related Task:** V3-003 — NFR and Threat Assumptions  
**Related Decisions:** V3-003-DEC-003, V3-003-DEC-004, V3-003-DEC-006, V3-003-DEC-007, V3-003-DEC-009, V3-003-DEC-010, V3-003-DEC-011  
**Related Candidates:** AEC-CAND-013, AEC-CAND-014, AEC-CAND-015, AEC-CAND-016 — ANALYTICAL, NON-NORMATIVE REFERENCES  
**Related Security Requirement Candidates:** SR-CAND-019, SR-CAND-020 — PROPOSED — NOT APPROVED  
**Independent Security Review:** NOT_SIGNED_OFF  
**Repository Recording:** PENDING VERIFICATION

### 1. Decision Scope

The Project Owner approves four bounded principles governing Mandatory Audit obligations and failure boundaries for selected FIRST_RELEASE Customer Core operations.

The decision applies to:

- CUS-CREATE — successful durable Customer Master creation.
- CUS-UPDATE — successful durable authoritative Customer Master changes.
- CUS-GET, CUS-GET-FOR-UPDATE and CUS-SEARCH — explicit Customer Domain authorization denials.
- Audit publication obligations associated with the approved mandatory Customer mutation events.

This approval does not establish a complete Customer Audit Event Catalog, a universal Audit failure policy or a final implementation design.

### 2. Approved Principles

#### Principle 1 — Mandatory Customer Creation Audit

Every CUS-CREATE operation that successfully and durably creates an authoritative Customer Master shall incur a Mandatory Audit publication obligation.

The originating Customer Domain shall coordinate the durable Customer creation effect and the corresponding Audit publication obligation within an appropriate service-owned consistency boundary.

The operation shall not be reported as successfully completed if that mandatory durable publication obligation has not been consistently recorded.

Audit evidence shall identify the relevant validated Actor, Tenant, operation, safe Customer reference, outcome and correlation context, subject to data-minimization requirements.

This principle does not approve separate mandatory Audit events for validation rejection, authorization denial, incomplete submissions or unsuccessful creation attempts.

#### Principle 2 — Mandatory Customer Update Audit

Every CUS-UPDATE operation that successfully and durably changes the authoritative Customer Master shall incur a Mandatory Audit publication obligation.

This obligation applies to authoritative durable changes generally and is not restricted to a future sensitive-field list.

The Customer Domain shall coordinate the durable mutation and its Audit publication obligation within an appropriate service-owned consistency boundary.

Conceptual evidence shall preserve the validated Actor, Tenant, Customer reference, action, successful outcome, correlation and a relevant change-category reference.

The decision does not require recording full Customer snapshots or automatically capturing old/new sensitive field values.

Field classification, exact change categories, bulk and partial-success semantics, correction workflows and payload schema remain unresolved.

#### Principle 3 — Mandatory Evidence for Explicit Customer Disclosure Denial

An explicit authorization denial issued by the Customer Domain for CUS-GET, CUS-GET-FOR-UPDATE or CUS-SEARCH shall incur a Mandatory Audit evidence obligation.

The obligation shall preserve applicable Actor, validated Tenant scope, action, safe target or query category, denial outcome and correlation information, without disclosing Customer existence, protected resource details, sensitive search criteria or permission-sensitive information.

The following shall not automatically be classified as Customer Domain authorization denials under this principle:

- A search returning zero results.
- Internal result filtering or suppression of unauthorized records.
- Validation failures unrelated to authorization denial.
- A denial issued before the request reaches the Customer Domain, including invalid Tenant Context rejected at an upstream enforcement boundary.

For denials originating upstream, the producing and auditing responsibility remains with the actual applicable enforcement boundary, subject to separately approved Audit policies.

This principle approves the Audit obligation and its disclosure-safe objective, not the concrete logging mechanism, persistence timing, retry policy, failure recovery or Security Review acceptance criteria.

An Audit failure shall never convert a denied Customer operation into an allowed operation.

#### Principle 4 — Customer Mutation Audit Failure Boundary

For CUS-CREATE and CUS-UPDATE operations covered by Principles 1 and 2, the originating Customer Domain shall not report successful durable mutation unless the corresponding Mandatory Audit publication obligation has been consistently and durably recorded.

Where the mutation and publication obligation share an applicable service-owned transactional resource, they shall preserve atomic consistency.

If the durable publication obligation cannot be established, the originating operation must not commit and report a successful authoritative mutation as though the Audit obligation had been satisfied.

When downstream Audit ingestion or storage is unavailable after the obligation has been durably established, any continuation or durable deferral remains subject to an explicitly approved operation-specific failure policy, recovery and reconciliation obligations, and prevention of silent evidence loss.

The existence of an Outbox record, successful broker publication or broker acknowledgement does not constitute proof of durable Audit Domain ingestion.

This principle does not establish universal BLOCK, DURABLE_DEFER, CONTROLLED_DEGRADED or REJECT_OR_ESCALATE behavior.

Read-only Customer disclosure failure semantics remain separately unresolved.

### 3. Architecture and Ownership Preservation

This decision preserves:

- Customer Domain ownership of authoritative Customer Master data and originating business mutations.
- Audit Domain ownership of authoritative system-wide Audit records.
- Domain-Owned Authorization for Customer resources and actions.
- Validated Tenant Context and Tenant Isolation.
- Service-owned persistence and transactional boundaries.
- Transactional Outbox and idempotent consumer processing where applicable.
- At-least-once messaging without end-to-end exactly-once guarantees.
- Separation of durable Audit publication obligation from downstream durable Audit ingestion.
- Append-oriented, integrity-protected Audit evidence.
- Safe-denial semantics and sensitive-data minimization.
- Dedicated Sovereign local final authority.

### 4. Business Criticality Preservation

Existing Customer Business Criticality decisions retain their exact scope:

- CUS-BC-001 — BC-3, limited approved Customer Create scenario.
- CUS-BC-002 — BC-2, limited search-first blocking scenario.
- CUS-BC-003 — BC-2, limited outdated Customer data scenario.

No approved Business Criticality is generalized to all Customer Create, Get or Search behavior.

CUS-UPDATE, CUS-VALIDATE, CUS-GET-FOR-UPDATE and other unassessed operations remain NOT_ASSESSED where applicable.

No new BC, SC, DC, RP, Risk Rating or numeric recovery target is established.

### 5. Explicit Non-Approvals

This decision does not approve:

1. The complete Mandatory Audit Event Catalog or final disposition of all AEC-CAND entries.
2. AEC-CAND-016 as generally Mandatory for successful Customer retrieval or search.
3. A separately mandatory event for every CUS-VALIDATE execution.
4. Universal Audit coverage for every Customer read, query, result row or field disclosure.
5. Mandatory denial/failure Audit outcomes for CUS-CREATE or CUS-UPDATE.
6. Mandatory events for incomplete Customer submissions or unsuccessful mutations.
7. A final Audit Event/API schema or payload format.
8. Customer field allowlists, change-category taxonomies or storage of old/new sensitive values.
9. Bulk, partial-success, correction, merge or deletion behavior.
10. A universal Audit failure-handling policy.
11. Automatic eligibility for DURABLE_DEFER whenever an Outbox obligation exists.
12. Read-only Customer disclosure failure semantics.
13. Specific Outbox, Inbox, broker, acknowledgement, retry, replay or reconciliation mechanisms.
14. Cross-service database transactions or end-to-end exactly-once delivery guarantees.
15. Retention periods, Legal Hold, deletion, redaction or cryptographic integrity mechanisms.
16. Numeric NFRs, including SLO, RTO, RPO, latency and capacity.
17. New Business Criticality, Security Criticality, Data Classification, Recovery Priority or Risk Rating assignments.
18. Final approval of SR-CAND-019, SR-CAND-020 or any other Security Requirement.
19. Executed Negative Tests, verified implementation controls or Independent Security Review sign-off.
20. Production Readiness or authorization to implement an unapproved detailed Audit policy.

### 6. Governance Preservation

The following statuses remain unchanged:

- V3-003 = IN PROGRESS.
- OD-001 through OD-023 = OPEN.
- SR-CAND-001 through SR-CAND-024 = PROPOSED — NOT APPROVED.
- THREAT_ASSUMPTION_VALIDATION_STATUS = PENDING SECURITY REVIEW.
- SECURITY_REVIEW_STATUS = NOT_SIGNED_OFF.
- IMPLEMENTATION_EVIDENCE_STATUS = NOT_VERIFIED.
- NEGATIVE_TEST_EXECUTION_STATUS = NOT_EXECUTED.

All earlier Owner-approved V3-003 decisions, normative annexes, architectural ADRs and standards remain unchanged.

### 7. Decision Effect

These four principles establish the bounded Owner-approved Customer Core Audit obligations for successful authoritative Customer creation, successful authoritative Customer updates and explicit Customer Domain disclosure denials.

They also establish the consistency boundary for the mandatory publication obligations associated with approved Customer mutations.

This decision does not finalize Customer read/disclosure Audit policies, approve downstream Audit failure handling, or complete V3-003.

Repository recording and Git versioning must be verified independently.

## V3-003-DEC-013 — Customer Core Durable Deferred Audit: Conditional Policy Direction

**Decision Status:** APPROVED — OWNER  
**Decision Authority:** Project Owner  
**Approval Scope:** Conditional Policy Direction Only  
**Related Decisions:** V3-003-DEC-009, V3-003-DEC-010, V3-003-DEC-011, V3-003-DEC-012  
**Affected Operations:** CUS-CREATE, CUS-UPDATE  
**Related Security Candidates:** SR-CAND-019, SR-CAND-020 — PROPOSED — NOT APPROVED  
**Independent Security Review:** NOT_SIGNED_OFF  
**Repository Recording:** PENDING VERIFICATION

### 1. Decision

The Project Owner selects **Durable Deferred Audit** as the preferred conditional policy direction for successful authoritative Customer Core mutations.

This direction applies only to CUS-CREATE and CUS-UPDATE operations covered by V3-003-DEC-012.

The decision does not authorize unconditional deferred Audit delivery, finalize operation-specific failure policies, or establish runtime readiness.

### 2. Approved Direction

#### Principle 1 — Durable Audit Obligation Before Successful Mutation

A successful authoritative CUS-CREATE or CUS-UPDATE mutation shall require a durable Audit publication obligation consistently coordinated with the originating business effect.

If that obligation cannot be established within the applicable approved consistency boundary, the operation must not commit and report a successful authoritative mutation as though its mandatory Audit obligation were satisfied.

#### Principle 2 — No Mandatory Synchronous Audit Ingestion Dependency

Subject to an approved operation-specific failure policy and validated safeguards, Customer mutation completion may be independent of synchronous durable ingestion by the Audit Domain.

The preferred direction is to allow asynchronous delivery of an already durable Audit obligation.

This principle does not establish that an Outbox record, broker acknowledgement, or publication attempt proves durable Audit ingestion.

#### Principle 3 — Controlled Deferred Delivery Eligibility

Deferred Audit delivery may be permitted only when the applicable future policy establishes sufficient evidence and guarantees for:

- Durable and recoverable publication obligations.
- Identification of pending, failed, and unresolved obligations.
- Retry and reconciliation without prohibited duplicate effects.
- Explicit operational ownership and escalation.
- Tenant isolation, event provenance, and integrity protection.
- Profile-appropriate recovery and Sovereign-local authority.

These are policy prerequisites requiring subsequent design, evidence, and validation. Their implementation is not considered verified by this decision.

#### Principle 4 — Explicit Handling of Indeterminate or Unrecoverable Conditions

The future operation-specific policy must define the circumstances under which deferred delivery remains permissible and the circumstances requiring rejection, suspension, escalation, or other controlled handling.

Unknown obligation validity, unavailable recovery evidence, or unresolved integrity concerns shall not automatically authorize continued operation.

No numerical backlog threshold, freshness interval, timeout, retry limit, or availability target is established.

#### Principle 5 — Dedicated Sovereign Locality

For Dedicated Sovereign deployments, mandatory Audit publication obligations, deferred-delivery governance, recovery, and reconciliation must preserve Sovereign-local final authority.

Central Audit ingestion or Central availability shall not become a mandatory synchronous dependency for critical locally authoritative operations.

### 3. Approval Boundary

The Project Owner approves the architectural and policy direction, not its final operational eligibility.

Before Durable Deferred Audit can be adopted as an executable operation-specific policy, the following remain required:

1. Customer Domain Owner confirmation of transaction and business-effect boundaries.
2. Audit Domain Owner definition of durable-ingestion evidence and reconciliation responsibilities.
3. Operations evidence for backlog detection, recovery, and escalation.
4. Security validation of integrity, provenance, Tenant isolation, and failure paths.
5. Dedicated Sovereign Operations confirmation of local continuity.
6. Explicit approval of operation-specific acceptance and failure conditions.

### 4. Explicit Non-Approvals

This decision does not approve:

1. Unconditional DURABLE_DEFER.
2. A universal Audit failure policy.
3. A specific Outbox, Inbox, broker, storage, API, or reconciliation mechanism.
4. An automatic right to continue operations during arbitrary Audit failures.
5. Numeric backlog, retry, retention, timeout, RTO, RPO, or SLO targets.
6. Customer read-only disclosure Audit failure semantics.
7. Final Audit Event Catalog contents beyond existing approved obligations.
8. Bulk, partial-success, compensation, or correction workflows.
9. Final SR-CAND-019 or SR-CAND-020 approval.
10. Executed Negative Tests, verified runtime controls, or Security Review sign-off.
11. Risk acceptance or Production Readiness.

### 5. Governance Preservation

The following statuses remain unchanged:

- V3-003 = IN PROGRESS.
- OD-001 through OD-023 = OPEN.
- SR-CAND-001 through SR-CAND-024 = PROPOSED — NOT APPROVED.
- THREAT_ASSUMPTION_VALIDATION_STATUS = PENDING SECURITY REVIEW.
- SECURITY_REVIEW_STATUS = NOT_SIGNED_OFF.
- IMPLEMENTATION_EVIDENCE_STATUS = NOT_VERIFIED.
- NEGATIVE_TEST_EXECUTION_STATUS = NOT_EXECUTED.

Previously approved decisions and Customer Business Criticality assessments retain their exact scopes.

### 6. Decision Effect

This decision establishes Durable Deferred Audit as the Owner-selected conditional direction for the subsequent design and approval of CUS-CREATE and CUS-UPDATE Audit failure policies.

It does not complete those policies or authorize implementation of unverified deferred-delivery behavior.

## V3-003-DEC-014 — Customer Core Durable Deferred Audit: Eligibility and Safety Gates

**Decision Status:** APPROVED — OWNER  
**Decision Authority:** Project Owner  
**Approval Scope:** Foundational Eligibility and Safety Gates Only  
**Related Task:** V3-003 — NFR and Threat Assumptions  
**Related Decisions:** V3-003-DEC-009, V3-003-DEC-010, V3-003-DEC-011, V3-003-DEC-012, V3-003-DEC-013  
**Affected Operations:** CUS-CREATE, CUS-UPDATE  
**Related Security Candidates:** SR-CAND-019, SR-CAND-020 — PROPOSED — NOT APPROVED  
**Independent Security Review:** NOT_SIGNED_OFF  
**Repository Recording:** PENDING VERIFICATION

### 1. Decision Scope

The Project Owner approves five foundational eligibility and safety principles for the conditional Durable Deferred Audit direction previously selected under V3-003-DEC-013.

These principles apply exclusively to the mandatory Audit publication obligations associated with successful authoritative CUS-CREATE and CUS-UPDATE mutations covered by V3-003-DEC-012.

The decision establishes minimum architectural conditions for future operation-specific deferred-delivery policies.

It does not approve an executable DURABLE_DEFER policy, unconditional continuation during Audit outages, or implementation readiness.

### 2. Approved Principles

#### Principle 1 — Durable Deferred Audit Eligibility Gate

CUS-CREATE or CUS-UPDATE may be considered eligible for successful completion without synchronous Audit Domain ingestion only when:

- Customer Domain Authorization has been successfully validated.
- Tenant Context is valid and authoritative.
- The authoritative Customer mutation and its mandatory Audit publication obligation have been consistently and durably recorded within the applicable Customer-owned consistency boundary.

An obligation existing only in memory, a partially committed mutation, or an unverified publication record does not satisfy this eligibility condition.

This principle does not itself authorize deferred execution. All additional recovery, observability, integrity and operation-specific policy requirements must also be satisfied.

#### Principle 2 — Evidence-State Separation

Evidence of obligation creation, durable obligation recording, publication attempts, broker delivery and authoritative Audit Domain ingestion shall remain conceptually distinct.

Only valid evidence of an appropriately coordinated, durably recorded publication obligation may establish the foundational durability prerequisite for deferred eligibility.

The following shall not independently prove this prerequisite or establish authoritative Audit ingestion:

- An in-memory or merely created obligation.
- An attempted publication.
- A broker acknowledgement without valid proof of the underlying durable obligation.
- A delivery status unsupported by the required evidence.

Authoritative Audit ingestion confirmation requires evidence from the Audit Domain according to a separately established ingestion and acknowledgement contract.

No final obligation state machine, acknowledgement protocol or message contract is approved.

#### Principle 3 — Recoverability and Observability Gate

Continued use of a future approved deferred Audit path shall require demonstrable:

- Recoverability of outstanding publication obligations.
- Identification of pending, failed and unresolved obligations.
- Valid visibility into relevant backlog and recovery status.
- Explicit ownership of monitoring, recovery and escalation.
- Ability to reconcile publication obligations against authoritative Audit ingestion evidence without prohibited duplicate effects.

If backlog observability or recovery status becomes indeterminate or cannot be trusted, eligibility for the deferred Audit path shall be suspended until valid conditions are restored.

Suspending deferred eligibility does not automatically suspend all Customer operations.

Any alternative execution path must independently satisfy the approved mandatory Audit obligations and its own applicable operation-specific authorization, consistency and failure policies.

This principle does not approve unlimited backlog growth, indefinite deferred delivery, a particular monitoring implementation or numeric operational thresholds.

#### Principle 4 — Integrity, Provenance and Recovery Safety Gate

An Audit publication obligation shall not qualify for deferred delivery when its provenance, authoritative Tenant scope, integrity or required recovery evidence is invalid, inconsistent or indeterminate.

Such conditions shall suspend eligibility for the deferred Audit path and initiate escalation through the applicable authorized operational or security process.

Invalid or cross-tenant obligation evidence shall not be accepted or reconciled as authoritative evidence for another Tenant.

This suspension applies to the deferred-delivery pathway, not automatically to every Customer operation or to already committed mutations.

Previously committed effects remain subject to separately approved reconciliation, incident response, correction and recovery policies.

This principle does not establish automatic rollback of already committed Customer mutations or authorize an unapproved emergency bypass.

#### Principle 5 — Dedicated Sovereign Local Eligibility Gate

For Dedicated Sovereign deployments, Central disconnection alone shall not invalidate legitimate locally authoritative Customer operations.

Deferred Audit eligibility must remain grounded in locally valid:

- Durable publication obligations.
- Backlog and recovery visibility.
- Integrity and provenance evidence.
- Authorized operational control.
- Recovery and reconciliation authority.

Loss or invalidity of required local durability, visibility, integrity evidence or recovery authority shall suspend local deferred Audit eligibility until the applicable requirements are restored.

Central availability, Central acknowledgement or Central recovery authority shall not be substituted for the required Sovereign-local evidence or final authority.

Suspension of deferred eligibility does not automatically prohibit every locally authorized Customer operation where an independently valid alternative execution path exists.

This principle does not approve Full Air-Gap support, specific disconnected-operation durations, local infrastructure technologies or numeric recovery targets.

### 3. Decision Boundaries

The five approved principles establish qualitative architectural gates for evaluating future deferred Audit delivery.

They do not demonstrate that these gates are currently implemented or satisfied.

Before an operation-specific DURABLE_DEFER policy may become executable, the following remain necessary:

1. Customer Domain design evidence for transaction and durable-obligation boundaries.
2. Audit Domain design evidence for authoritative durable ingestion confirmation.
3. Obligation identity, lifecycle, ownership and provenance contracts.
4. Operations evidence for backlog visibility, recovery, reconciliation and escalation.
5. Security validation of integrity, authorization, Tenant isolation and failure conditions.
6. Dedicated Sovereign Operations validation of local control and recovery.
7. Explicit approval of operation-specific failure conditions and acceptance criteria.

No implementation readiness or security acceptance is inferred from Owner approval of these foundational principles.

### 4. Explicit Non-Approvals

This decision does not approve:

1. An executable or unconditional DURABLE_DEFER policy.
2. A universal Audit failure-handling policy.
3. Automatic suspension of all Customer operations whenever deferred eligibility is lost.
4. An unapproved alternative execution path or emergency bypass.
5. A final Audit Obligation State Machine.
6. Exact Outbox, Inbox, broker, storage, monitoring, API or acknowledgement technologies.
7. Specific event schemas, publication contracts or reconciliation algorithms.
8. Numeric backlog capacity, retry limits, timeouts or acceptable deferral durations.
9. Numeric SLO, RTO, RPO, latency, availability or recovery objectives.
10. Automatic rollback or compensation for previously committed mutations.
11. A complete Mandatory Audit Event Catalog.
12. Customer read-only disclosure Audit failure semantics.
13. Bulk, partial-success, Customer merge, deletion or correction workflows.
14. Full Air-Gap support or Central-dependent Sovereign recovery.
15. New Business Criticality, Security Criticality, Data Classification, Recovery Priority or Risk Rating assignments.
16. Final approval of SR-CAND-019, SR-CAND-020 or other Security Requirement candidates.
17. Executed Negative Tests or verified implementation controls.
18. Independent Security Review sign-off, risk acceptance or Production Readiness.

### 5. Architecture Preservation

This decision preserves:

- Customer Domain ownership of Customer Master and originating mutations.
- Audit Domain ownership of authoritative Audit evidence.
- Domain-Owned Authorization and validated Tenant Context.
- Service-owned persistence and transactional boundaries.
- At-least-once delivery and idempotent consumer effects.
- No cross-service database transaction requirement.
- No end-to-end exactly-once delivery guarantee.
- Separation of producer obligation durability and Audit Domain ingestion.
- Sensitive-data minimization and Tenant Isolation.
- Dedicated Sovereign local final authority.

Existing Customer Business Criticality assessments retain their exact approved scope:

- CUS-BC-001 — BC-3, limited Customer Create scenario.
- CUS-BC-002 — BC-2, limited Customer Search scenario.
- CUS-BC-003 — BC-2, limited Customer Get scenario.

All other unassessed Customer scenarios remain NOT_ASSESSED where applicable.

### 6. Governance Preservation

The following statuses remain unchanged:

- V3-003 = IN PROGRESS.
- OD-001 through OD-023 = OPEN.
- SR-CAND-001 through SR-CAND-024 = PROPOSED — NOT APPROVED.
- THREAT_ASSUMPTION_VALIDATION_STATUS = PENDING SECURITY REVIEW.
- SECURITY_REVIEW_STATUS = NOT_SIGNED_OFF.
- IMPLEMENTATION_EVIDENCE_STATUS = NOT_VERIFIED.
- NEGATIVE_TEST_EXECUTION_STATUS = NOT_EXECUTED.

All previous V3-003 decisions, normative annexes, architectural ADRs and standards remain unchanged.

### 7. Decision Effect

This decision establishes the Owner-approved foundational eligibility and safety gates governing the conditional Durable Deferred Audit direction for CUS-CREATE and CUS-UPDATE.

The next authorized work is evidence-based design of the Customer/Audit consistency and ingestion contracts, followed by operational recovery and security validation planning.

No executable deferred Audit policy or runtime control is approved by this decision.

Repository recording and Git versioning require separate verification.

## V3-003 Analytical Closure — CDR-V3-003-2026-1030

**Closure status:** `CLOSED — ANALYTICAL SCOPE ONLY`

**Approval level:** `LEVEL 1 — DEVELOPMENT / DOCUMENTATION TASK`

**Decision authority:** `CPO`

**Decision source:** explicit CPO direction under `TASK_ID = V3-003`

**Repository baseline reviewed:** `c146a9b1771df575353059f27c64ca6e1a0f25d7` on branch `main`; working tree clean before this closure registration

**Closure contract:** the twelve criteria `V3-003-AC-P-01..12` defined by `architecture/reviews/V3-003-analytical-closure-contract-proposal.md` are accepted for this analytical closure

**Evidence record:** `architecture/reviews/V3-003-analytical-closure-evidence-matrix.md` plus the current closure reconciliation in that file

### Closure decision

The CPO accepts the V3-003 analytical deliverables and closes the task only in its Analytical / Documentation scope. The CPO also accepts the bounded carry-forward of every unresolved item to its existing owner, milestone and future gate.

Under `architecture/task-governance.md`, the heightened corporate certificate, delegation-matrix and organizational-signature requirements introduced by the V3-003 closure-preparation documents are not applicable to this Level 1 closure. They were not mandated by an independently authoritative corporate policy, contract or external requirement found in the repository. This decision does not represent those historical corporate-evidence assertions as verified.

`V3-003-AC-P-01..12` are satisfied for Analytical Closure. In particular, `V3-003-AC-P-12` is satisfied by the explicit CPO task direction, this authoritative repository acknowledgment, the accepted scope and criteria, and the traceable Git change. The source documents and their pre-closure hashes are recorded in the Evidence Matrix; no immutable post-change commit is claimed before the user commits these changes.

### Carry-forward and non-approvals

The following statuses remain independent and unchanged:

```text
OD-001..023 = OPEN
SR-CAND-001..024 = PROPOSED — NOT APPROVED
SPECIALIST_DISPOSITIONS = 36 PENDING; 0 AUTHENTICATED
SECURITY_REVIEW_STATUS = NOT_SIGNED_OFF
IMPLEMENTATION_EVIDENCE_STATUS = NOT_VERIFIED
NEGATIVE_TEST_EXECUTION_STATUS = NOT_EXECUTED
EXECUTABLE_DURABLE_DEFER = NOT APPROVED
ELIGIBILITY_POLICY_AUTHORITY = NOT_YET_ASSIGNED
ELIGIBILITY_POLICY_AUTHORITY_ASSIGNMENT = DEFERRED
PRODUCTION_READINESS = NOT ESTABLISHED
```

`OD-023` remains Open and due before Production Architecture Sign-off. DEC-014 and its five approved foundational eligibility and safety principles remain unchanged. This closure approves no architecture alternative, Security Requirement, specialist disposition, implementation control, executed test, risk acceptance, deployment or production release.
