# Neshane CRM V3 — V2 owner disposition, product scope and domain ownership review

## 1. Review scope and baseline

| Field | Value |
| --- | --- |
| Task | V3-002B — Owner Disposition, Product Capability Scope & Domain Ownership Review |
| Parent | V3-002 — Legacy V2 Inventory and Salvage |
| Architecture | `NESHANE-V3-ARCH-P00-002` |
| Governance | `NESHANE-V3-GOV-P00-000A` |
| Inventory baseline | 46 Asset IDs: RETAIN 13, REWRITE 19, RETIRE 3, NEEDS_REVIEW 11 — all originally Proposed |
| Historical source | `E:\nodejs\iam-crm-backend` at `9b918ba8972812c129c8b073e1ac4991023ccbbb` (read-only evidence) |
| Review date | 2026-10-23 |
| Current outcome | **Owner Disposition Review Complete — All 46 Assets Have Final Dispositions** |

This review records three independent decision dimensions: legacy disposition, V3 product capability scope, and logical domain/data ownership. A decision in one dimension does not approve either of the other two. It does not authorize copying V2 source, selecting an Open Decision alternative, creating a deployable service, or claiming implementation or production readiness.

ADR-V3-001 through ADR-V3-012 remain authoritative. OD-001 through OD-023 remain Open. Independent architecture reviewer sign-off is not recorded by this review.

## 2. Decision methodology

- `RETAIN` preserves approved semantics, contracts, tests or knowledge; it does not authorize source copying.
- `REWRITE` preserves required behavior through an architecture-compliant new implementation.
- `RETIRE` excludes the legacy asset/behavior, subject to historical retention needs.
- `NEEDS_REVIEW` preserves uncertainty where requirements, ownership or evidence are insufficient.
- Capability scope uses `FIRST_RELEASE`, `LATER_RELEASE`, `OUT_OF_SCOPE` or `UNDECIDED`.
- Ownership decisions identify authoritative data, writes and final resource/action authorization without inferring deployment topology.
- Only an explicit project-owner answer changes a Pending item to Approved or Conditionally Approved.

Review groups are Platform Foundation; Identity; Tenant/Organization/Administration; Customer/CRM; Sales; Notification; Customer Requests/Workflow; Audit/Entitlement/Quota; Linka; AI/Reporting; Work/Content/Portal/Knowledge; and legacy Governance/CI/Test/Documentation. These are review groupings, not service boundaries.

## 3. Complete 46-asset disposition decision matrix

The original evidence, detailed rationale and follow-up remain authoritative in [the inventory](v2-inventory.md#6-complete-asset-inventory-and-proposed-dispositions). This matrix preserves proposal provenance and records owner disposition decisions separately.

| Asset ID | Review group | Evidence basis | Original proposal | Final owner disposition | Decision ID | Approval status | Rationale / follow-up | ADR / OD |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| V2-AST-001 | Platform Foundation | Direct V2 source | REWRITE | **REWRITE** | V3-002B-DEC-056 | **Approved** | Rewrite reproducible build, dependency locking, gates and independent service build/version/artifact boundaries; do not inherit the V2 stack or configuration | ADR-001, ADR-011; OD-002–004, OD-020 |
| V2-AST-002 | API boundary | Direct V2 source | NEEDS_REVIEW | **RETAIN** | V3-002B-DEC-083 | **Approved** | Read-only historical API-composition/discovery evidence; no GraphQL/BFF technology or pattern is approved and composition remains subject to independent decisions | ADR-008, ADR-009; OD-007–008 |
| V2-AST-003 | API security | Direct V2 source | RETAIN | **RETAIN** | V3-002B-DEC-058 | **Approved** | Read-only security/performance evidence; historical GraphQL implementation and thresholds are not inherited | ADR-008, ADR-012; OD-007, OD-020 |
| V2-AST-004 | Identity/Foundation | Direct V2 source | REWRITE | **REWRITE** | V3-002B-DEC-055 | **Approved** | Rewrite workload identity/context validation and negative cases; historical HMAC/shared-secret fixture is prohibited | ADR-003, ADR-005; OD-009–012 |
| V2-AST-005 | Tenant/Organization | Direct V2 source | REWRITE | **REWRITE** | V3-002B-DEC-055 | **Approved** | Rewrite Tenant/Organization/Membership behavior under DEC-054; historical framework/layout/topology is not inherited | ADR-001, ADR-002, ADR-005, ADR-011 |
| V2-AST-006 | Test fixture | Direct V2 source | RETIRE | **RETIRE** | V3-002B-DEC-059 | **Approved** | Do not recreate TenantProbe; preserve valid isolation/fail-closed scenarios only as historical test evidence | ADR-003, ADR-012 |
| V2-AST-007 | Contracts | Direct V2 source | RETAIN | **RETAIN** | V3-002B-DEC-060 | **Approved** | Read-only contract evidence; historical types/shapes create no V3 contract or trusted Tenant Context | ADR-007, ADR-008; OD-008, OD-020 |
| V2-AST-008 | Configuration/Security | Direct V2 source | REWRITE | **REWRITE** | V3-002B-DEC-055 | **Approved** | Rewrite fail-closed/startup/secret-trust configuration semantics; historical Zod/crypto/HMAC helpers are not selected | ADR-005, ADR-010; OD-009–012 |
| V2-AST-009 | Observability | Direct V2 source | RETAIN | **RETAIN** | V3-002B-DEC-061 | **Approved** | Read-only observability/security evidence; historical tooling, fields, configuration and implementation are not inherited | ADR-010, ADR-012; OD-023 |
| V2-AST-010 | Tenant test support | Direct V2 source | RETAIN | **RETAIN** | V3-002B-DEC-062 | **Approved** | Read-only test-support evidence; historical code, identifiers and fixture structure are not inherited | ADR-003, ADR-007, ADR-012 |
| V2-AST-011 | Persistence model | Direct V2 source | REWRITE | **REWRITE** | V3-002B-DEC-063 | **Approved** | Rewrite only valid Outbox/Inbox/processed-event behavior under service ownership; TenantProbe and historical schema details are excluded | ADR-002, ADR-003, ADR-007; OD-013–014 |
| V2-AST-012 | RLS evidence | Direct V2 source | RETAIN | **RETAIN** | V3-002B-DEC-064 | **Approved** | Read-only RLS/isolation evidence; historical SQL, policies, settings, grants and tables are not inherited | ADR-003, ADR-007, ADR-012; OD-013–014 |
| V2-AST-013 | Database identities | Direct V2 source | REWRITE | **REWRITE** | V3-002B-DEC-065 | **Approved** | Rewrite least-privilege identity separation per Service; historical initialization, roles, credentials and grants are excluded | ADR-007, ADR-010; OD-012–015 |
| V2-AST-014 | Cache | Direct V2 source | NEEDS_REVIEW | **RETAIN** | V3-002B-DEC-084 | **Approved** | Read-only historical Cache/security evidence; no Cache technology or pattern is approved and future use requires an independently approved owned use case | ADR-003, ADR-007, ADR-012 |
| V2-AST-015 | Messaging producer | Direct V2 source | REWRITE | **REWRITE** | V3-002B-DEC-067 | **Approved** | Rewrite valid atomic Outbox/publication-confirm behavior; direct source port and historical delivery design are excluded | ADR-007, ADR-008, ADR-012; OD-008, OD-019–020 |
| V2-AST-016 | Messaging consumer | Direct V2 source | REWRITE | **REWRITE** | V3-002B-DEC-068 | **Approved** | Rewrite valid durable Inbox, ACK-after-effect, bounded retry and DLQ behavior; historical source/topology is excluded | ADR-007, ADR-008; OD-008, OD-019–020 |
| V2-AST-017 | Security tests | Direct V2 test source | RETAIN | **RETAIN** | V3-002B-DEC-069 | **Approved** | Read-only security test evidence; historical framework, fixtures and cryptographic mechanisms are not inherited | ADR-005, ADR-012 |
| V2-AST-018 | Foundation tests | Direct V2 test source; unexecuted | RETAIN | **RETAIN** | V3-002B-DEC-070 | **Approved** | Read-only scenario catalog; historical results and test stack create no V3 runtime/security evidence or tooling decision | ADR-003, ADR-005, ADR-007–008, ADR-012; OD-020 |
| V2-AST-019 | Deployment fixture | Direct V2 source | REWRITE | **REWRITE** | V3-002B-DEC-071 | **Approved** | Rewrite only independent service artifact/deployment and profile-verification requirements; historical topology/tooling is excluded | ADR-001, ADR-010–012; OD-012, OD-015, OD-023 |
| V2-AST-020 | Governance CI | Direct V2 source | RETAIN | **RETAIN** | V3-002B-DEC-072 | **Approved** | Read-only CI/governance evidence; historical workflow, tools, steps and ordering are not inherited | ADR-012; OD-020 |
| V2-AST-021 | Main CI | Direct V2 source | REWRITE | **REWRITE** | V3-002B-DEC-073 | **Approved** | Rewrite independent repository/service CI and traceable gate evidence; historical provider/toolchain/workflow is excluded | ADR-001, ADR-010, ADR-012; OD-020 |
| V2-AST-022 | Governance manifest | Direct V2 source | NEEDS_REVIEW | **RETAIN** | V3-002B-DEC-085 | **Approved** | Read-only historical governance discovery/provenance; V2 declarations, tools and rules create no V3 authority or Passed Gate | ADR-002, ADR-011–012 |
| V2-AST-023 | Boundary tests | Direct V2 source | RETAIN | **RETAIN** | V3-002B-DEC-075 | **Approved** | Read-only boundary/adversarial evidence; historical checker/tooling proves no V3 source or runtime enforcement | ADR-001–002, ADR-011–012; OD-004, OD-020 |
| V2-AST-024 | Bootstrap tooling | Direct V2 source | RETIRE | **RETIRE** | V3-002B-DEC-076 | **Approved** | V2-stage-specific tooling is not transferred or rewritten; findings remain in inventory/review records | ADR-012 |
| V2-AST-025 | Architecture documents | Direct V2 documents | NEEDS_REVIEW | **RETAIN** | V3-002B-DEC-086 | **Approved** | Read-only historical architecture/governance provenance and secondary evidence; retention approves no content and Concept Reconciliation remains independent | All ADRs; relevant ODs |
| V2-AST-026 | V2 ADRs | Direct V2 documents | NEEDS_REVIEW | **RETAIN** | V3-002B-DEC-087 | **Approved** | Read-only historical decision provenance; final Asset disposition does not transfer historical approval or complete Concept Reconciliation | ADR-001–012; OD-002–020 |
| V2-AST-027 | Engineering documents | Direct V2 documents | NEEDS_REVIEW | **RETAIN** | V3-002B-DEC-088 | **Approved** | Read-only historical engineering/quality evidence; historical stack, gates, roadmap, priorities and Passed Status create no V3 authority or readiness evidence | ADR-012; OD-020, OD-023 |
| V2-AST-028 | V2 agent skills | Direct V2 documents | RETIRE | **RETIRE** | V3-002B-DEC-080 | **Approved** | Historical V2/NestJS skills are not transferred, installed, executed or directly rewritten and create no V3 authority | Governance baseline |
| V2-AST-029 | Skill-audit evidence | Direct V2 documents | RETAIN | **RETAIN** | V3-002B-DEC-081 | **Approved** | Read-only historical audit provenance; historical pass/coverage/validation status creates no V3 evidence | ADR-012 |
| V2-AST-030 | Historical index | Historical record of 106/106 hash matches | RETAIN | **RETAIN** | V3-002B-DEC-082 | **Approved** | Read-only bounded evidence index; hash identity proves neither completeness, semantics, security nor readiness | ADR-012 |
| V2-AST-031 | Identity/SSO/Passkeys | Verified pinned source; runtime unverified | REWRITE | **REWRITE** | V3-002B-DEC-055 | **Approved** | Rewrite valid Identity/session/tenant-switch/passkey/SSO behavior under DEC-053/054 and future requirements; historical mechanisms/providers/topology are not approved | ADR-004–005, ADR-012; OD-009–012 |
| V2-AST-032 | Notification | Verified pinned source; runtime unverified | REWRITE | **REWRITE** | V3-002B-DEC-010 | **Approved** | Composite Asset Group: rewrite only within approved release scope; direct V2 source transfer prohibited; Delivery Audit remains internal to Notification; physical/design details pending | ADR-002, ADR-007–008, ADR-011–012 |
| V2-AST-033 | Linka | Partial source; provider unverified | NEEDS_REVIEW | **REWRITE** | V3-002B-DEC-026 | **Approved** | Rewrite valid behavior only for the approved LATER_RELEASE scope; no direct V2 source transfer, historical Provider adoption, implementation start or FIRST_RELEASE inclusion is authorized | ADR-001–ADR-003, ADR-005, ADR-008, ADR-010–012; OD-020 |
| V2-AST-034 | AI/Reporting | Verified pinned source; product/runtime unverified | NEEDS_REVIEW | **REWRITE** | V3-002B-DEC-033 | **Approved** | Composite Asset Group reconciles independent Reporting and AI rewrites for historical traceability only; Reporting remains FIRST_RELEASE and AI remains LATER_RELEASE | ADR-001–005, ADR-008, ADR-010–012 |
| V2-AST-035 | Requests/Audit/Quota/Entitlement | Verified pinned source; runtime unverified | NEEDS_REVIEW | **REWRITE** | V3-002B-DEC-023 | **Approved** | Composite Asset Group classification reconciles four approved component rewrites for historical traceability only; no domain merge, shared database, single service or direct source port is authorized | ADR-002, ADR-003, ADR-005, ADR-007–008, ADR-010–012 |
| V2-AST-036 | Capability map | Verified 838-file tree | NEEDS_REVIEW | **RETAIN** | V3-002B-DEC-052 | **Approved** | Read-only Historical Capability/Traceability Map only; no product scope, domain, topology or implementation authority; source port and folder-to-service inference are prohibited | ADR-002, ADR-006, ADR-009, ADR-011; OD-017–019 |
| V2-AST-037 | Customer/CRM | Verified pinned source | REWRITE | **REWRITE** | V3-002B-DEC-003 | **Approved** | Preserve validated business behavior through a new V3 implementation; direct V2 source transfer is prohibited; Aggregate/API/Migration/Topology remain separate | ADR-001–003, ADR-005, ADR-008, ADR-011 |
| V2-AST-038 | Sales | Verified pinned source | REWRITE | **REWRITE** | V3-002B-DEC-007 | **Approved** | Composite Asset Group: rewrite each valid behavior only in its approved release scope; direct V2 source transfer prohibited; auxiliary ownership and detailed designs pending | ADR-001–003, ADR-005, ADR-008, ADR-011 |
| V2-AST-039 | Work/Collaboration | Verified pinned source | REWRITE | **REWRITE** | V3-002B-DEC-036 | **Approved** | Composite Asset Group rewrite follows approved release scope; auxiliary capabilities require independent requirements/ownership approval; direct source port and architectural merging are prohibited | ADR-001–003, ADR-005, ADR-008, ADR-011–012 |
| V2-AST-040 | Content/File | Verified pinned source; storage runtime unverified | REWRITE | **REWRITE** | V3-002B-DEC-039 | **Approved** | Composite Asset Group rewrite follows DEC-037/038 release scope and split ownership; direct source port and architectural merging are prohibited; advanced capabilities require independent requirements/ownership approval | ADR-001–003, ADR-005, ADR-008, ADR-010–012; OD-017 |
| V2-AST-041 | Technical Knowledge | Verified source presence; runtime unverified | NEEDS_REVIEW | **REWRITE** | V3-002B-DEC-042 | **Approved** | Composite Asset Group rewrite is limited to LATER_RELEASE and preserves File/resource ownership; direct source port and architectural merging are prohibited; OD-018 remains Open | ADR-002, ADR-008; OD-018 |
| V2-AST-042 | Customer Portal | Verified pinned source; runtime unverified | REWRITE | **REWRITE** | V3-002B-DEC-045 | **Approved** | Composite Asset Group rewrite is limited to LATER_RELEASE and preserves Portal/Identity/Tenant/Customer/resource boundaries; direct source port and architectural merging are prohibited | ADR-004–005, ADR-008–009 |
| V2-AST-043 | Historical schema/migrations | Verified corpus; unexecuted | REWRITE | **REWRITE** | V3-002B-DEC-046 | **Approved** | Read-only discovery evidence only; V3 schemas/migrations must be independently designed per domain; direct execution/replay/import/port is prohibited | ADR-001–003, ADR-007, ADR-011–012; OD-013–014 |
| V2-AST-044 | Historical test corpus | Verified source; unexecuted | RETAIN | **RETAIN** | V3-002B-DEC-047 | **Approved** | Read-only historical test evidence only; scenarios require V3 review; direct/one-to-one test port, legacy framework adoption and historical-result validation are prohibited | ADR-003, ADR-005, ADR-007–008, ADR-012 |
| V2-AST-045 | Historical contracts/docs | Verified static artifacts | RETAIN | **RETAIN** | V3-002B-DEC-048 | **Approved** | Read-only historical contract/documentation evidence only; no V2 API shape, compatibility, code generation or source/specification port is approved | ADR-008, ADR-012; OD-007–008, OD-020 |
| V2-AST-046 | Administration/Reporting/Operations | Verified pinned source; runtime unverified | REWRITE | **REWRITE** | V3-002B-DEC-051 | **Approved** | Composite Asset Group rewrite follows approved Reporting and Operational release scope; deferred capabilities require independent requirements/ownership/authorization; direct source port and architectural merging are prohibited | ADR-001–003, ADR-005, ADR-008, ADR-010–012 |

## 4. Capability scope matrix

| Capability | Scope status | Decision | Approval | Notes |
| --- | --- | --- | --- | --- |
| Customer/CRM core | FIRST_RELEASE | V3-002B-DEC-001 | Approved | Company/person/contact master capability; does not include Linka, Sales, Portal, AI or Workflow automatically |
| Sales — Opportunity/Pipeline core | FIRST_RELEASE | V3-002B-DEC-004 | Approved | Contractual relationship with Customer Domain; auxiliary Sales capabilities are not included automatically |
| Product Catalog | LATER_RELEASE | V3-002B-DEC-005 | Approved | FIRST_RELEASE Opportunity amount/currency must not require Product Catalog |
| Lead Source | LATER_RELEASE | V3-002B-DEC-005 | Approved | Excluded from FIRST_RELEASE scope |
| Pain Point | LATER_RELEASE | V3-002B-DEC-005 | Approved | Excluded from FIRST_RELEASE scope |
| Use Case | LATER_RELEASE | V3-002B-DEC-005 | Approved | Excluded from FIRST_RELEASE scope |
| Notification Core + In-App | FIRST_RELEASE | V3-002B-DEC-008 | Approved | Template, base rules, lifecycle, Delivery Ledger, deduplication, retry/audit and In-App notification |
| Notification Email | LATER_RELEASE | V3-002B-DEC-008 | Approved | External provider/channel details require later requirements approval |
| Notification SMS | LATER_RELEASE | V3-002B-DEC-008 | Approved | External provider/channel details require later requirements approval |
| Notification Push | LATER_RELEASE | V3-002B-DEC-008 | Approved | External provider/channel details require later requirements approval |
| Customer Requests core | FIRST_RELEASE | V3-002B-DEC-011 | Approved | Internal creation, Customer contract reference, view/tracking, base lifecycle, status history and base assignment |
| Customer Request Portal Submission | LATER_RELEASE | V3-002B-DEC-011 | Approved | Core must not require Portal |
| Customer Request customer sharing | LATER_RELEASE | V3-002B-DEC-011 | Approved | Membership-aware sharing requires later requirements |
| Customer Request workflow automation | LATER_RELEASE | V3-002B-DEC-011 | Approved | Core must not require a Workflow Engine |
| Automatic Task/Opportunity/Technical Document links | LATER_RELEASE | V3-002B-DEC-011 | Approved | Cross-domain automation/contracts require later requirements |
| Audit Core | FIRST_RELEASE | V3-002B-DEC-013 | Approved | Append-oriented security, administrative and privileged events; Tenant/Platform separation; Actor/Action/Target/Outcome/Correlation; authorized viewing; integrity controls; base Retention Policy |
| Audit Export, Archive Automation and advanced UI/Reporting | LATER_RELEASE | V3-002B-DEC-013 | Approved | Deferral must not weaken required protection, retention or recovery in FIRST_RELEASE |
| Entitlement Core | FIRST_RELEASE | V3-002B-DEC-017 | Approved | Traceable capability eligibility for Tenant/Organization using approved Feature Assignment and Plan/Subscription; independent from membership and resource/action authorization |
| Quota Core | FIRST_RELEASE | V3-002B-DEC-020 | Approved | Effective limits, Usage, atomic Reservation/Commit/Release, Reconciliation and traceable Reason/Period/Correlation; each capability integration requires separate requirements approval |
| Linka/external registry | LATER_RELEASE | V3-002B-DEC-024 | Approved | Customer Core must operate without an external provider; later entry requires provider contract, provenance, retention, resilience, validation and authorized approval before Customer Master change |
| Reporting Core | FIRST_RELEASE | V3-002B-DEC-027 | Approved | Deterministic tenant-scoped reports required by approved FIRST_RELEASE capabilities; each Report Set requires separate requirements and authorization |
| Advanced Analytics and Custom Report Builder | LATER_RELEASE | V3-002B-DEC-027 | Approved | Deferred without expanding FIRST_RELEASE Report Sets |
| AI-generated Insights, Assistant and Business Action Proposals | LATER_RELEASE | V3-002B-DEC-030 | Approved | Staged entry; FIRST_RELEASE is model/provider-independent; business writes require explicit approval and execution-time re-authorization; autonomous writes prohibited |
| Work Core — Task | FIRST_RELEASE | V3-002B-DEC-034 | Approved | Create/View/Edit, Assignment, Status, Due Date and manual contract-based links; Assignment grants no authority |
| Meetings, Timesheets, Personal Todos, Advanced Team Collaboration, Workflow Automation and automatic cross-domain integration | LATER_RELEASE | V3-002B-DEC-034 | Approved | Deferred capabilities cannot become mandatory FIRST_RELEASE dependencies |
| File/Attachment Core | FIRST_RELEASE | V3-002B-DEC-037 | Approved | Metadata, controlled upload/download, base lifecycle and contract-based attachments; each resource attachment needs independent requirements/authorization |
| Public Sharing, Advanced Versioning, Media Processing and Advanced Generated Artifacts | LATER_RELEASE | V3-002B-DEC-037 | Approved | Deferred features cannot become mandatory FIRST_RELEASE dependencies |
| Customer Portal — customer-facing access, external users, authentication/session, account workspace and submission/sharing | LATER_RELEASE | V3-002B-DEC-043 | Approved | No FIRST_RELEASE dependency; every exposed resource/action requires owner-domain requirements, contract and authorization |
| Technical Knowledge — Document/Article, Basic Classification, contract-based links and University Reference Data | LATER_RELEASE | V3-002B-DEC-040 | Approved | No FIRST_RELEASE dependency; independent of File Core; implementation requires separately approved requirements and design |
| Operational Core — health/readiness, scope separation, authorized visibility, privileged-operation audit and independently approved minimum controls | FIRST_RELEASE architecture/operations obligation | V3-002B-DEC-049 | Approved | Does not create a Business Domain, General Administration UI or universal Admin Superuser |
| General Administration UI, Advanced Operational Dashboard, Bulk Import, Email Administration and Automation/Advanced Remediation | LATER_RELEASE | V3-002B-DEC-049 | Approved | Reporting and Notification/Email Delivery remain governed independently |
| Platform security, tenancy and operations | Required architecture obligation | DEC-003–DEC-005, DEC-010 | Previously approved architecture | Not an optional product-scope choice; all three production profiles remain required |

## 5. Logical domain and data ownership matrix

All entries below remain proposals until separately approved. “Business Service” is not fixed unless an approved decision supports it; logical ownership does not automatically require a separate initial deployable.

| Capability / aggregate | Proposed logical owner | Proposed Business Service | Authoritative data / writes | Read and integration boundary | Tenant and authorization owner | Approval |
| --- | --- | --- | --- | --- | --- | --- |
| Customer company/person/contact master | **Customer Domain** | Undecided deployment boundary | Customer-owned company, person, contact, branch and relationship records; Customer Domain is authoritative and owns writes | Versioned Customer API/events; authorized projections | Customer Domain enforces resource/action authorization; Platform Core supplies validated tenant/membership context | **Approved — V3-002B-DEC-002** |
| Identity/principal/session | **Identity Trust Capability in Platform Core** | Undecided deployment boundary | Identity owns Principal Identity, Credential/Authenticator Registration, External Identity Mapping, Authentication State, Session/Refresh/Revocation State and Token-Issuance Metadata; Tenant, Entitlement, Portal and business ownerships remain separate | Versioned identity contracts; provider assertions require validation and approved mapping; no direct business-data ownership | Identity decides only Principal/Session validity; token/session grants no Membership, Entitlement or business authorization; Tenant switching revalidates Membership/Context; Dedicated Sovereign authority is local | **Approved — V3-002B-DEC-053** |
| Tenant/Organization/Membership | **Tenant Management Capability in Platform Core** | Undecided deployment boundary | Tenant Management owns Tenant, Organization, Tenant Lifecycle, Organization/Tenant Membership, Membership Status, Principal-to-Tenant Association and Membership Role Assignment; Identity, Entitlement and business ownerships remain separate | Versioned tenant/membership contracts; Tenant Context derives from valid Principal plus active Membership and is revalidated at trust boundaries | Tenant Management authorizes its own resources and membership administration only; Membership/role grants no Entitlement or business authorization; Dedicated Sovereign authority is local | **Approved — V3-002B-DEC-054** |
| Sales opportunity/pipeline | **Sales Domain** | Undecided deployment boundary | Sales-owned Opportunity, Pipeline, Stage Transition and Opportunity amount/currency; Sales Domain is authoritative and owns writes | Customer references only by identifier and versioned API/event or authorized projection; Sales-owned API/events for consumers | Sales Domain makes and enforces final Opportunity resource/action authorization | **Approved — V3-002B-DEC-006** |
| Notification templates/delivery | **Notification Domain** | Undecided deployment boundary | Notification-owned Template, Rule, Lifecycle, Delivery Ledger, Delivery Attempts, Deduplication, Retry State and In-App records; physical persistence design remains undecided | Producing Domain retains Business Fact; integration uses versioned contracts with tenant provenance | Notification authorizes Notification resources and recipient access only; producer retains business-operation authorization | **Approved — V3-002B-DEC-009** |
| Customer Request workflow | **Customer Request Domain within the logical Workflow capability** | Undecided deployment boundary; no mandatory generic Workflow Engine | Request, Lifecycle, Status History, Triage and Assignment; Customer Request Domain is authoritative and owns writes | Customer reference only by identifier and versioned contracts; later Task/Opportunity/Technical Document integration by owned contracts | Customer Request Domain makes and enforces final Request resource/action authorization; Assignment grants no authority | **Approved — V3-002B-DEC-012** |
| Audit | **Audit Domain for system-wide Audit records; Producing Domains retain Business Facts and Domain-specific Audit** | Undecided deployment boundary | Audit Domain is authoritative for system-wide security, administrative and Privileged records and authorized Audit projections; producers remain authoritative for their Business Facts and Domain-specific Audit | Versioned contracts only; Audit Domain has no direct access to private domain databases | Audit Domain makes and enforces final access decisions for its Audit resources; Dedicated Sovereign security and operational authority is local | **Approved — V3-002B-DEC-014** |
| Entitlement | **Independent logical Entitlement capability in Platform Core** | Undecided deployment boundary | Entitlement owns authoritative Feature Assignment, effective Entitlement state and Eligibility evaluation results; Plan/Subscription facts, Billing, Pricing and Quota ownership remain separate | Versioned policy/evaluation contracts; Tenant Management retains Tenant/Organization and Membership | Entitlement decides eligibility only; each Resource-owning Domain makes and enforces final Resource/Action Authorization; Dedicated Sovereign authority/evaluation is local | **Approved — V3-002B-DEC-018** |
| Quota | **Independent logical Quota capability in Platform Core** | Undecided deployment boundary | Quota owns authoritative Effective Limit, Reservation Ledger, Usage/Consumption State, Reconciliation State and Quota Decision Results; producers retain source Usage Facts | Versioned policy/usage contracts; Entitlement remains owner of Eligibility; no shared database access | Producing Resource-owning Domain makes and enforces final Resource/Action Authorization; Dedicated Sovereign Quota authority/control is local | **Approved — V3-002B-DEC-021** |
| Linka/provider records | **Linka/External Registry Integration before acceptance; Customer Domain after acceptance** | Undecided deployment boundary | Linka owns Provider Interaction, Lookup Request/Response, Provider Snapshot, Provenance, Validation State and Reviewed Candidate/Draft before acceptance; Customer owns acceptance/rejection and Customer Master | Explicit reviewed handoff only; no Provider/Adapter direct write or database access to Customer Master | Customer Domain makes and enforces final acceptance and Customer resource/action authorization | **Approved — V3-002B-DEC-025** |
| Reporting | **Reporting Capability for report resources; Producing Domains retain Business Facts** | Undecided deployment boundary | Reporting owns Report Catalog/Definition Metadata, Execution State, Generated Report Artifact/Snapshot and its authorized dedicated Projections; producers own source Business Facts | Versioned source contracts and approved projections only; Operational Platform is infrastructure operator, not semantic owner | Reporting authorizes its report resources subject to Tenant Isolation and source disclosure constraints; projections cannot bypass source authorization; Dedicated Sovereign authority is local | **Approved — V3-002B-DEC-028** |
| AI proposals/actions | **AI Orchestration Capability for AI state; Resource-owning Domain for Business Facts and writes** | Undecided deployment boundary | AI owns Interaction/Execution State, Generated Insight, Proposal, Approval Reference and Replay/Idempotency State; target domain owns Business Fact, Validation and executed write | Versioned contracts only; no direct cross-service database access; Model Provider owns no authoritative Business Fact | AI authorizes only its resources; Approval Reference grants no execution right; target domain re-authorizes every write; Dedicated Sovereign authority is local | **Approved — V3-002B-DEC-031** |
| Work Core / Task | **Work Domain** | Undecided deployment boundary | Work owns Task, Task Lifecycle/Status, Due Date, Assignment Record and cross-domain Link Metadata | Related Customer, Opportunity and Customer Request resources remain owned by their domains; valid contracts only; no direct database access or foreign Business Fact writes | Work authorizes only Task resources; Assignment/links grant no Membership, Entitlement or authorization to related resources | **Approved — V3-002B-DEC-035** |
| Files/content | **File/Content Domain for file state; Resource-owning Domain for attachment meaning and relation** | Undecided deployment boundary | File/Content owns File Metadata, Content/Object Lifecycle, Storage Reference, Integrity/Checksum and Validation/Quarantine State; resource owner owns Attachment semantics and relationship to its Business Resource | Versioned authorized contracts only; no direct cross-service database access; attachment deletion does not by itself delete the File Object | File Domain authorizes the file and Resource-owning Domain authorizes attachment operations and related-resource access; File ID/link grants no authority; Dedicated Sovereign authority is local | **Approved — V3-002B-DEC-038** |
| Technical Knowledge | **Technical Knowledge Domain** | Undecided deployment boundary | Knowledge owns Technical Document/Article, Knowledge Lifecycle, Classification Assignment, University Reference Data and Knowledge-side Link Metadata; File Domain retains File Object/Storage Reference/File State; resource domains retain Business Facts | Versioned authorized contracts only; Search Index is a rebuildable non-authoritative Projection; no direct cross-service database access | Knowledge authorizes only knowledge resources; related-resource access remains owner-authorized; links grant no Membership, Entitlement or Authorization; Dedicated Sovereign authority is local | **Approved — V3-002B-DEC-041** |
| Customer Portal | **Customer Portal Domain for Portal state; Identity, Tenant, Customer and resource domains retain their authorities** | Undecided deployment boundary | Portal owns Portal Account Linkage, Customer-facing Workspace State, Portal Preferences, Invitation/Onboarding State and Portal-specific Access/Interaction State; Identity owns principal/credential/session state; Tenant and Customer ownerships remain unchanged | Versioned authorized contracts only; no direct cross-service database access; External Principal and trust models remain Pending | Portal authorizes only Portal-owned resources; Portal state grants no Membership, Entitlement or business-resource authority; Resource-owning Domain authorizes every business operation; Dedicated Sovereign authority is local | **Approved — V3-002B-DEC-044** |
| Administration / Operational Core | **Operational Platform Capability for operational state; source services and logical domains retain their authorities** | Undecided deployment boundary | Operational Platform owns Operational Visibility Projections, Health/Readiness Aggregation, Privileged Operation Request/Execution State and approved control state; source services own signals/configuration; domains own Business Facts; Audit/Tenant/Reporting/Notification ownerships remain unchanged | Versioned authorized contracts only; no direct cross-service database access; deferred Bulk Import, Email Administration and advanced capability ownerships remain Pending | Operational Platform authorizes only its resources; destination domain authorizes business effects; privileged actions require limited identity, explicit scope and traceable Audit; Dedicated Sovereign authority is local | **Approved — V3-002B-DEC-050** |

## 6. Owner-approved decisions and evidence

### V3-002B-DEC-001 — Customer/CRM product scope

| Field | Recorded value |
| --- | --- |
| Exact question | In which V3 release scope should the core Customer/CRM capability be placed? |
| Selected option | **A — FIRST_RELEASE** |
| Owner rationale | Not provided |
| Affected Asset IDs | Primary: V2-AST-037; dependent but not automatically approved: V2-AST-033, V2-AST-038, V2-AST-039, V2-AST-042 |
| Capability impact | Company/person/contact master capability is required in the initial production release |
| Disposition impact | None; V2-AST-037 remains proposed REWRITE pending a separate disposition decision |
| Domain ownership impact | None; ownership remains Pending |
| ADR / OD impact | Consistent with ADR-V3-002, ADR-V3-003, ADR-V3-005, ADR-V3-008 and ADR-V3-011; closes no OD |
| Approval status | Approved by project owner |
| Approval evidence | Explicit owner response `A` in the V3-002B review conversation |
| Date | 2026-10-23 |

### V3-002B-DEC-002 — Customer/CRM logical domain and data ownership

| Field | Recorded value |
| --- | --- |
| Exact question | Which logical domain owns authoritative Customer company, person, contact, branch and relationship data? |
| Selected option | **A — Customer Domain owns authoritative Customer data** |
| Owner condition | This decision determines logical domain/data ownership only; it does not approve disposition or Service Topology |
| Owner rationale | Not otherwise provided |
| Affected Asset IDs | Primary: V2-AST-037; consuming/dependent capabilities: V2-AST-033, V2-AST-038, V2-AST-039, V2-AST-042, V2-AST-046 |
| Authoritative data/write impact | Customer Domain is source of truth and exclusive writer for Customer company/person/contact/branch/relationship records |
| Read/integration impact | Other domains use Customer-owned versioned APIs/events or explicitly owned projections; no shared ORM or cross-service SQL |
| Authorization impact | Customer Domain makes and enforces final Customer resource/action authorization decisions; Platform Core identity/membership/entitlement does not replace it |
| Disposition impact | None; V2-AST-037 remains proposed REWRITE pending a separate disposition decision |
| Service topology impact | None; deployable boundary and co-deployment remain undecided |
| ADR / OD impact | Applies ADR-V3-002, ADR-V3-005, ADR-V3-008 and ADR-V3-011; closes no OD |
| Approval status | Approved by project owner with the stated limitation |
| Approval evidence | Explicit owner response in the V3-002B review conversation: `A — Customer Domain ... فقط مالکیت منطقی دامنه و داده ...` |
| Date | 2026-10-23 |

### V3-002B-DEC-003 — V2-AST-037 Customer/CRM legacy disposition

| Field | Recorded value |
| --- | --- |
| Exact question | What is the final legacy disposition of V2-AST-037? |
| Selected option | **A — REWRITE** |
| Owner condition | Preserve valid Customer/CRM business behaviors and rewrite them under approved V3 architecture; direct V2 source transfer is prohibited. This approval applies only to V2-AST-037 disposition and creates no Aggregate Design, API, Migration or Service Topology decision. |
| Affected Asset IDs | V2-AST-037 only |
| Capability impact | None beyond the separately approved FIRST_RELEASE scope |
| Domain ownership impact | None beyond the separately approved Customer Domain ownership |
| Implementation impact | Future implementation must be new V3 work and may use approved semantics/evidence only; no source-copy authorization |
| ADR / OD impact | Conforms to ADR-V3-001, ADR-V3-002, ADR-V3-005, ADR-V3-008 and ADR-V3-011; closes no OD |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `A — REWRITE` with prohibition of direct V2 source transfer in the V3-002B review conversation |
| Date | 2026-10-23 |

### V3-002B-DEC-004 — Sales core product scope

| Field | Recorded value |
| --- | --- |
| Exact question | In which V3 release scope should the base Sales capability be placed? |
| Selected option | **A — FIRST_RELEASE** |
| Owner condition | First-release Sales includes Opportunity, Pipeline and a contractual relationship with Customer Domain. Product Catalog, Lead Source, Pain Point and Use Case scope must be decided separately. This decision does not approve disposition, data ownership, Aggregate Design, API, Migration or Service Topology. |
| Affected Asset IDs | Primary: V2-AST-038; Customer dependency: V2-AST-037 |
| Capability impact | Opportunity/Pipeline core is required in the initial production release |
| Disposition impact | None; V2-AST-038 remains proposed REWRITE pending a separate disposition decision |
| Domain ownership impact | None; Sales data ownership remains Pending |
| ADR / OD impact | Consistent with ADR-V3-002, ADR-V3-003, ADR-V3-005, ADR-V3-008 and ADR-V3-011; closes no OD |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `A — FIRST_RELEASE` with the stated included and excluded decision dimensions in the V3-002B review conversation |
| Date | 2026-10-23 |

### V3-002B-DEC-005 — Sales auxiliary capability scope

| Field | Recorded value |
| --- | --- |
| Exact question | What release scope applies to Product Catalog, Lead Source, Pain Point and Use Case? |
| Selected option | **D — Custom Scope Matrix** |
| Approved scope matrix | Product Catalog: LATER_RELEASE; Lead Source: LATER_RELEASE; Pain Point: LATER_RELEASE; Use Case: LATER_RELEASE |
| FIRST_RELEASE condition | Opportunity amount and currency must be recordable without a mandatory Product Catalog dependency |
| Explicitly deferred design | Line Item design, Pricing rules and Currency rules require separate review |
| Affected Asset IDs | V2-AST-038 |
| Disposition impact | None; V2-AST-038 remains proposed REWRITE |
| Domain ownership impact | None; Sales and auxiliary data ownership remain Pending |
| Other excluded impact | No API, Aggregate Design, Migration or Service Topology decision is created |
| Evidence basis | Historical Opportunity line items permit a nullable `productId` and require direct `unitPrice` when no product is selected (`src/opportunities/dto/create-opportunity-line-item.dto.ts:9`; `src/opportunities/opportunity-line-items.service.ts:84-100`) |
| ADR / OD impact | Consistent with ADR-V3-002, ADR-V3-008 and ADR-V3-011; closes no OD |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `D — Custom Scope Matrix` with the four LATER_RELEASE classifications and FIRST_RELEASE amount/currency condition |
| Date | 2026-10-23 |

### V3-002B-DEC-006 — Sales core logical domain and data ownership

| Field | Recorded value |
| --- | --- |
| Exact question | Which logical domain owns authoritative Opportunity, Pipeline, Stage Transition and Opportunity amount/currency data? |
| Selected option | **A — Sales Domain** |
| Owner condition | Customer Domain remains owner of Customer master. Sales may relate to Customer only by identifier and versioned API/event or authorized projection. Sales Domain makes the final Opportunity resource/action authorization decision. |
| Affected Asset IDs | Primary: V2-AST-038; contractual dependency: V2-AST-037 |
| Authoritative data/write impact | Sales Domain is source of truth and exclusive writer for Opportunity, Pipeline, Stage Transition and Opportunity amount/currency |
| Read/integration impact | No shared ORM, cross-service SQL or direct Customer writes; integrations use owned versioned contracts/projections |
| Explicit exclusions | Product Catalog ownership, Pricing, Aggregate Design, API design, Migration, Disposition and Service Topology remain undecided |
| ADR / OD impact | Applies ADR-V3-002, ADR-V3-005, ADR-V3-008 and ADR-V3-011; closes no OD |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `A — Sales Domain` with authoritative data, contract and authorization boundaries in the V3-002B review conversation |
| Date | 2026-10-23 |

### V3-002B-DEC-007 — V2-AST-038 Sales composite legacy disposition

| Field | Recorded value |
| --- | --- |
| Exact question | What is the final legacy disposition of the composite V2-AST-038 Sales asset group? |
| Selected option | **A — REWRITE with approved Release Scope** |
| FIRST_RELEASE portion | Opportunity, Pipeline, Stage Transition and Opportunity amount/currency |
| LATER_RELEASE portion | Product Catalog, Lead Source, Pain Point and Use Case; rewrite is conditional on requirements approval for the applicable later release |
| Owner condition | Keep V2-AST-038 as one composite Asset Group with different scopes. Direct V2 source transfer is prohibited. |
| Explicit exclusions | Auxiliary capability ownership, Line Item, Pricing, Currency Rules, Aggregate Design, API, Migration and Service Topology remain Pending |
| Affected Asset IDs | V2-AST-038 only |
| Capability impact | No scope change; preserves V3-002B-DEC-004 and V3-002B-DEC-005 |
| Domain ownership impact | No change; preserves Sales core ownership from V3-002B-DEC-006 and leaves auxiliary ownership Pending |
| ADR / OD impact | Conforms to ADR-V3-001, ADR-V3-002, ADR-V3-005, ADR-V3-008 and ADR-V3-011; closes no OD |
| Approval status | Approved by project owner with the stated scope conditions |
| Approval evidence | Explicit owner approval `A — REWRITE با رعایت Release Scope` and composite-asset conditions in the V3-002B review conversation |
| Date | 2026-10-23 |

### V3-002B-DEC-008 — Notification product scope

| Field | Recorded value |
| --- | --- |
| Exact question | What Notification capability and channel scope belongs in the first V3 release? |
| Selected option | **A — FIRST_RELEASE Core + In-App** |
| FIRST_RELEASE portion | Template, base rules, notification lifecycle, Delivery Ledger, deduplication, retry/audit and In-App Notification |
| LATER_RELEASE portion | Email, SMS and Push channels |
| Carry-forward requirements | Channel extensibility, Tenant Isolation, idempotency and operational independence across Shared SaaS, Dedicated Managed and Dedicated Sovereign |
| Affected Asset IDs | V2-AST-032 |
| Disposition impact | None; V2-AST-032 remains proposed REWRITE |
| Domain ownership impact | None; Notification data ownership remains Pending |
| Explicit exclusions | API/Event Contracts, Scheduling, Provider Selection and Service Topology remain undecided |
| ADR / OD impact | Applies ADR-V3-002, ADR-V3-003, ADR-V3-007, ADR-V3-008, ADR-V3-010 and ADR-V3-011; OD-008, OD-012, OD-015, OD-019, OD-020 and OD-023 remain Open |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `A — FIRST_RELEASE Core + In-App` with channel scope and cross-profile requirements in the V3-002B review conversation |
| Date | 2026-10-23 |

### V3-002B-DEC-009 — Notification logical domain and data ownership

| Field | Recorded value |
| --- | --- |
| Exact question | Which logical domain owns authoritative Template, Rule, Notification Lifecycle, Delivery Ledger/Attempts, Deduplication, Retry State and In-App Notification data? |
| Selected option | **A — Notification Domain** |
| Authoritative data/write impact | Notification Domain owns the listed Notification records and their lifecycle; physical persistence design remains Pending |
| Producing-domain boundary | Producing Domain retains ownership of the Business Fact and authorization of its Customer/Sales/other business operation |
| Authorization impact | Notification Domain authorizes Notification resources and recipient access; it cannot authorize Customer or Sales operations |
| Audit boundary | Notification Delivery Audit is distinct from system-wide Audit; no universal audit ownership is implied |
| Mandatory safeguards | Tenant Isolation and recipient access control |
| Affected Asset IDs | Primary: V2-AST-032; system-wide Audit is separate and subsequently governed by V3-002B-DEC-013 and V3-002B-DEC-014 |
| Explicit exclusions | Provider Credential ownership, API/Event Contracts, Scheduling, Aggregate Design, physical Persistence design and Service Topology remain Pending |
| ADR / OD impact | Applies ADR-V3-002, ADR-V3-003, ADR-V3-005, ADR-V3-007, ADR-V3-008 and ADR-V3-011; closes no OD |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `A — Notification Domain` with producing-domain, audit, tenant and recipient-access boundaries in the V3-002B review conversation |
| Date | 2026-10-23 |

### V3-002B-DEC-010 — V2-AST-032 Notification composite legacy disposition

| Field | Recorded value |
| --- | --- |
| Exact question | What is the final legacy disposition of V2-AST-032? |
| Selected option | **A — REWRITE with approved Release Scope** |
| FIRST_RELEASE portion | Notification Core, base Template/Rule, Lifecycle, Delivery Ledger, Deduplication, Retry/Audit and In-App Notification |
| LATER_RELEASE portion | Email, SMS and Push; rewrite is conditional on requirements approval for the applicable later release |
| Owner condition | Direct V2 source transfer is prohibited. Delivery Audit remains an internal Notification concern and is not system-wide Audit. |
| Explicit exclusions | Provider Credentials, API/Event Contracts, Scheduling, Aggregate/Persistence Design and Service Topology remain Pending |
| Affected Asset IDs | V2-AST-032 only |
| Capability impact | No scope change; preserves V3-002B-DEC-008 |
| Domain ownership impact | No change; preserves V3-002B-DEC-009 |
| ADR / OD impact | Conforms to ADR-V3-001–ADR-V3-003, ADR-V3-005, ADR-V3-007, ADR-V3-008 and ADR-V3-010–ADR-V3-012; closes no OD |
| Approval status | Approved by project owner with the stated scope conditions |
| Approval evidence | Explicit owner approval `A — REWRITE با رعایت Release Scope برای V2-AST-032` and stated exclusions in the V3-002B review conversation |
| Date | 2026-10-23 |

### V3-002B-DEC-011 — Customer Requests product scope

| Field | Recorded value |
| --- | --- |
| Exact question | What Customer Requests capability belongs in the first V3 release? |
| Selected option | **C — Minimal FIRST_RELEASE** |
| FIRST_RELEASE portion | Internal Request creation, contractual Customer reference, view/tracking, base lifecycle, Status History and base Assignment |
| LATER_RELEASE portion | Portal Submission, Customer Sharing, Workflow Automation and automatic links/creation for Task, Opportunity and Technical Document |
| Security condition | Assignment is work responsibility only and never substitutes for Tenant Membership or resource/action Authorization |
| Dependency condition | Customer Requests core must not require Portal or a Workflow Engine |
| Affected Asset IDs | Customer Requests portion of V2-AST-035; dependent later capabilities include V2-AST-037, V2-AST-038, V2-AST-039, V2-AST-041 and V2-AST-042 |
| Disposition impact | None; mixed V2-AST-035 remains NEEDS_REVIEW pending separate reconciliation |
| Domain ownership impact | None; Customer Request ownership remains Pending |
| Explicit exclusions | State Machine Design, API Contracts, Migration and Service Topology remain Pending |
| ADR / OD impact | Applies ADR-V3-002, ADR-V3-003, ADR-V3-005, ADR-V3-008 and ADR-V3-011; OD-007–OD-008 and OD-019–OD-020 remain Open |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `C — FIRST_RELEASE حداقلی` with included/deferred workflows and authorization/dependency conditions |
| Date | 2026-10-23 |

### V3-002B-DEC-012 — Customer Requests logical domain and data ownership

| Field | Recorded value |
| --- | --- |
| Exact question | Which logical domain owns authoritative Request, Lifecycle, Status History, Triage and base Assignment data? |
| Selected option | **A — Customer Request Domain within the logical Workflow capability** |
| Authoritative data/write impact | Customer Request Domain owns Request, Lifecycle, Status History, Triage and Assignment and is their source of truth |
| Customer boundary | Customer Domain remains owner of Customer master; Customer references use identifiers and versioned contracts only |
| Authorization impact | Customer Request Domain makes and enforces final Request resource/action authorization; Assignment creates no security authority |
| FIRST_RELEASE dependency condition | No dependency on a generic Workflow Engine |
| Affected Asset IDs | Customer Requests portion of V2-AST-035; contractual dependencies include V2-AST-037 and later V2-AST-039/V2-AST-041 integrations |
| Explicit exclusions | Workflow Engine selection, Task/Opportunity ownership, Aggregate Design, API/Event Contracts, Migration and Service Topology remain Pending |
| ADR / OD impact | Applies ADR-V3-002, ADR-V3-005, ADR-V3-008 and ADR-V3-011; OD-007–OD-008 and OD-019–OD-020 remain Open |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `A — Customer Request Domain در محدوده منطقی Workflow` with authoritative-data, contract, authorization and engine-independence conditions |
| Date | 2026-10-23 |

### V3-002B-DEC-013 — System-wide Audit product scope

| Field | Recorded value |
| --- | --- |
| Exact question | What system-wide Audit capability belongs in the first V3 release? |
| Selected option | **A — FIRST_RELEASE Audit Core** |
| FIRST_RELEASE portion | Append-oriented security, administrative and privileged events; Tenant/Platform separation; Actor/Action/Target/Outcome/Correlation; authorized viewing; integrity controls; base Retention Policy |
| LATER_RELEASE portion | Export, Archive Automation and advanced UI/Reporting |
| Non-deferrable condition | LATER_RELEASE classification must not weaken the protection, retention or recovery required for Audit in FIRST_RELEASE |
| Producer boundary | Each Producing Domain remains owner of its Business Fact; Audit Core has no direct access to private domain databases |
| Operational-profile condition | Audit authority in Dedicated Sovereign is local to that environment |
| Affected Asset IDs | Audit portion of V2-AST-035 |
| Disposition impact | None; mixed V2-AST-035 remains NEEDS_REVIEW pending component dispositions and reconciliation |
| Domain ownership impact | None; final Audit logical/data ownership remains Pending |
| Explicit exclusions | Event Schema, Retention Duration, Archive Storage, API, Persistence and Service Topology remain Pending |
| ADR / OD impact | Applies ADR-V3-002–ADR-V3-005, ADR-V3-007–ADR-V3-008 and ADR-V3-010–ADR-V3-012; closes no OD |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `A — FIRST_RELEASE Audit Core` with included/deferred scope, producer boundary and Sovereign-local authority conditions |
| Date | 2026-10-23 |

### V3-002B-DEC-014 — Audit logical domain and data ownership

| Field | Recorded value |
| --- | --- |
| Exact question | Which logical domain owns authoritative system-wide security, administrative and Privileged Audit records and authorized Audit projections? |
| Selected option | **A — Audit Domain** |
| Authoritative data/write impact | Audit Domain owns system-wide security, administrative and Privileged Audit records and authorized Audit projections and is authoritative for them |
| Producer boundary | Each Producing Domain remains owner of its Business Fact and Domain-specific Audit |
| Integration boundary | Audit Domain uses explicit versioned contracts and has no direct access to private databases of other domains |
| Authorization impact | Audit Domain makes and enforces final access decisions for its own Audit resources |
| Operational Platform impact | Operational Platform may operate Audit infrastructure but is not the semantic owner of Audit data or producer Business Facts |
| Operational-profile condition | Final security and operational authority for Audit in Dedicated Sovereign is local to that environment |
| Affected Asset IDs | Audit portion of V2-AST-035 |
| Disposition impact | None; mixed V2-AST-035 remains NEEDS_REVIEW pending component dispositions and reconciliation |
| Explicit exclusions | Event Schema, Retention Duration, Archive Storage, API, Persistence, Migration and Service Topology remain Pending |
| ADR / OD impact | Applies ADR-V3-001–ADR-V3-005, ADR-V3-007–ADR-V3-008 and ADR-V3-010–ADR-V3-012; closes no OD |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `A — Audit Domain` with producer ownership, authorization, database-isolation, operator and Sovereign-local authority conditions |
| Date | 2026-10-23 |

### V3-002B-DEC-015 — Audit component disposition within V2-AST-035

| Field | Recorded value |
| --- | --- |
| Exact question | What is the disposition of the Audit component within composite Asset Group V2-AST-035? |
| Selected option | **A — REWRITE** |
| Disposition impact | Valid Audit behavior and requirements are to be rewritten for the approved V3 architecture; direct V2 source transfer is prohibited |
| Binding scope | The rewrite must preserve the product scope approved by V3-002B-DEC-013 and logical/data ownership approved by V3-002B-DEC-014 |
| Required invariants | Append-oriented records, integrity controls, Tenant Isolation, authorization, sensitive-data protection and Sovereign-local authority |
| Composite-asset impact | This is a component disposition only; overall V2-AST-035 remains NEEDS_REVIEW while other components remain unresolved |
| Explicit exclusions | Event Schema, Retention Duration, Archive Storage, API, Persistence, Migration and Service Topology remain Pending |
| ADR / OD impact | Conforms to ADR-V3-001–ADR-V3-005, ADR-V3-007–ADR-V3-008 and ADR-V3-010–ADR-V3-012; closes no OD |
| Approval status | Approved by project owner for the Audit component only |
| Approval evidence | Explicit owner response `A — REWRITE برای بخش Audit از V2-AST-035` with preserved invariants, source-transfer prohibition and composite-status limitation |
| Date | 2026-10-23 |

### V3-002B-DEC-016 — Customer Requests component disposition within V2-AST-035

| Field | Recorded value |
| --- | --- |
| Exact question | What is the disposition of the Customer Requests component within composite Asset Group V2-AST-035? |
| Selected option | **A — REWRITE** |
| FIRST_RELEASE rewrite scope | Internal Request creation, Lifecycle, Status History, Triage, Assignment and contractual Customer relationship, consistent with V3-002B-DEC-011 and V3-002B-DEC-012 |
| LATER_RELEASE boundary | Portal Submission, Customer Sharing, Workflow Automation and automatic links to other domains remain conditional on approved requirements for that release |
| Disposition impact | Valid Customer Requests behavior and requirements are to be rewritten for the approved V3 architecture; direct V2 source transfer is prohibited |
| Ownership and authorization | Customer Request Domain remains authoritative for its data and the final Resource/Action Authorization owner |
| Dependency condition | FIRST_RELEASE must not depend on Portal or a generic Workflow Engine |
| Composite-asset impact | This is a component disposition only; overall V2-AST-035 remains NEEDS_REVIEW until Entitlement and Quota are resolved |
| Explicit exclusions | State Machine Design, API/Event Contracts, Persistence, Migration and Service Topology remain Pending |
| ADR / OD impact | Conforms to ADR-V3-001–ADR-V3-003, ADR-V3-005, ADR-V3-008 and ADR-V3-010–ADR-V3-012; closes no OD |
| Approval status | Approved by project owner for the Customer Requests component only |
| Approval evidence | Explicit owner response `A — REWRITE برای بخش Customer Requests از V2-AST-035` with release-scope, ownership, authorization, dependency and source-transfer conditions |
| Date | 2026-10-23 |

### V3-002B-DEC-017 — Entitlement product scope

| Field | Recorded value |
| --- | --- |
| Exact question | What Entitlement capability belongs in the first V3 release? |
| Selected option | **A — FIRST_RELEASE Entitlement Core** |
| FIRST_RELEASE portion | Evaluate Tenant/Organization capability eligibility from approved Feature Assignment and Plan/Subscription, with traceable result, reason and validity time |
| Authorization boundary | Entitlement is independent from Tenant Membership and Resource/Action Authorization and does not authorize operations on business resources |
| Operational-profile condition | Dedicated Sovereign must support Entitlement evaluation without a mandatory dependency on a central service |
| Affected Asset IDs | Entitlement portion of V2-AST-035 |
| Disposition impact | None; Entitlement component disposition and overall V2-AST-035 remain Pending/NEEDS_REVIEW |
| Domain ownership impact | None; Entitlement logical/data ownership remains Pending |
| Explicit exclusions | Billing, Pricing, Quota, Policy Model, API, Persistence, Migration and Service Topology remain Pending |
| ADR / OD impact | Applies ADR-V3-003–ADR-V3-005, ADR-V3-010–ADR-V3-012; closes no OD |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `A — FIRST_RELEASE Entitlement Core` with traceability, authorization-separation and Sovereign-local evaluation conditions |
| Date | 2026-10-23 |

### V3-002B-DEC-018 — Entitlement logical domain and data ownership

| Field | Recorded value |
| --- | --- |
| Exact question | Which logical capability owns authoritative Feature Assignment, effective Entitlement state and Eligibility evaluation results? |
| Selected option | **A — Independent logical Entitlement capability in Platform Core** |
| Authoritative data/write impact | Entitlement owns Feature Assignment, effective Entitlement state and Eligibility evaluation results and is authoritative for them |
| Tenant boundary | Tenant Management remains owner of Tenant/Organization and Membership |
| Commercial boundary | Ownership of Plan/Subscription facts, Billing, Pricing and Quota remains separately Pending |
| Authorization impact | Entitlement determines eligibility only; every Resource-owning Domain makes and enforces final Resource/Action Authorization |
| Operational-profile condition | Dedicated Sovereign Entitlement authority and evaluation are local and have no mandatory central-service dependency |
| Affected Asset IDs | Entitlement portion of V2-AST-035 |
| Disposition impact | None; Entitlement component disposition and overall V2-AST-035 remain Pending/NEEDS_REVIEW |
| Explicit exclusions | Policy Model, API, Persistence, Migration and Service Topology remain Pending |
| ADR / OD impact | Applies ADR-V3-001–ADR-V3-005 and ADR-V3-010–ADR-V3-012; closes no OD |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `A — Entitlement به‌عنوان قابلیت منطقی مستقل در Platform Core` with tenant, commercial, authorization and Sovereign-local boundaries |
| Date | 2026-10-23 |

### V3-002B-DEC-019 — Entitlement component disposition within V2-AST-035

| Field | Recorded value |
| --- | --- |
| Exact question | What is the disposition of the Entitlement component within composite Asset Group V2-AST-035? |
| Selected option | **A — REWRITE** |
| Disposition impact | Valid Entitlement behavior is to be rewritten for the approved V3 architecture; direct V2 source transfer is prohibited |
| Binding behavior | Preserve Feature Assignment, effective Entitlement state, Eligibility Evaluation, Decision Reason and Validity behavior consistent with V3-002B-DEC-017 and V3-002B-DEC-018 |
| Security and authority boundary | Entitlement remains independent from Membership and Resource/Action Authorization; Dedicated Sovereign authority and evaluation remain local |
| Composite-asset impact | This is a component disposition only; overall V2-AST-035 remains NEEDS_REVIEW until Quota decisions and final reconciliation are complete |
| Explicit exclusions | Policy Model, Plan/Subscription ownership, Billing, Pricing, Quota, API, Persistence, Migration and Service Topology remain Pending |
| ADR / OD impact | Conforms to ADR-V3-001–ADR-V3-005 and ADR-V3-010–ADR-V3-012; closes no OD |
| Approval status | Approved by project owner for the Entitlement component only |
| Approval evidence | Explicit owner response `A — REWRITE برای بخش Entitlement از V2-AST-035` with binding behavior, authorization-separation, Sovereign-local and source-transfer conditions |
| Date | 2026-10-23 |

### V3-002B-DEC-020 — Quota product scope

| Field | Recorded value |
| --- | --- |
| Exact question | What Quota capability belongs in the first V3 release? |
| Selected option | **A — FIRST_RELEASE Quota Core** |
| FIRST_RELEASE portion | Resolve effective Limit for Tenant/Organization and Capability; record Usage; perform atomic Reservation/Commit/Release; reconcile consumption; return traceable Reason, Period and Correlation results |
| Authorization boundary | Quota is independent from Entitlement, Membership and Resource/Action Authorization and does not grant a business-resource operation |
| Capability-onboarding condition | Connecting any Capability to Quota requires independent approval of that Capability's requirements |
| Operational-profile condition | Dedicated Sovereign consumption evaluation and control are local and have no mandatory central-service dependency |
| Affected Asset IDs | Quota portion of V2-AST-035 |
| Disposition impact | None; Quota component disposition and overall V2-AST-035 remain Pending/NEEDS_REVIEW |
| Domain ownership impact | None; Quota logical/data ownership remains Pending |
| Explicit exclusions | Policy/Limit Model, Reset/Scheduling, API, Persistence, Migration and Service Topology remain Pending |
| ADR / OD impact | Applies ADR-V3-003–ADR-V3-005, ADR-V3-010–ADR-V3-012; closes no OD |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `A — FIRST_RELEASE Quota Core` with atomic lifecycle, traceability, authorization-separation, capability-onboarding and Sovereign-local conditions |
| Date | 2026-10-23 |

### V3-002B-DEC-021 — Quota logical domain and data ownership

| Field | Recorded value |
| --- | --- |
| Exact question | Which logical capability owns authoritative Effective Limit, reservation, consumption, reconciliation and Quota decision data? |
| Selected option | **A — Independent logical Quota capability in Platform Core** |
| Authoritative data/write impact | Quota owns Effective Limit, Reservation Ledger, Usage/Consumption State, Reconciliation State and Quota Decision Results and is authoritative for them |
| Producer boundary | Producing Domain retains its Business Operation and source Usage Fact |
| Entitlement boundary | Entitlement remains owner of Eligibility; Quota ownership does not merge the two capabilities |
| Authorization impact | Each Resource-owning Producing Domain makes and enforces final Resource/Action Authorization |
| Future design requirements | Idempotency, Concurrency Safety, Reservation Lifecycle and Reconciliation must be addressed by later approved design |
| Operational-profile condition | Dedicated Sovereign Quota authority and consumption control are local |
| Affected Asset IDs | Quota portion of V2-AST-035 |
| Disposition impact | None; Quota component disposition and overall V2-AST-035 remain Pending/NEEDS_REVIEW |
| Explicit exclusions | Policy/Limit Model, Plan/Subscription Ownership, Reset/Scheduling, API, Persistence, Migration and Service Topology remain Pending |
| ADR / OD impact | Applies ADR-V3-001–ADR-V3-005, ADR-V3-007–ADR-V3-008 and ADR-V3-010–ADR-V3-012; closes no OD |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `A — Quota به‌عنوان قابلیت منطقی مستقل در Platform Core` with producer, Entitlement, authorization, future-design and Sovereign-local boundaries |
| Date | 2026-10-23 |

### V3-002B-DEC-022 — Quota component disposition within V2-AST-035

| Field | Recorded value |
| --- | --- |
| Exact question | What is the disposition of the Quota component within composite Asset Group V2-AST-035? |
| Selected option | **A — REWRITE** |
| Disposition impact | Valid Quota behavior is to be rewritten for the approved V3 architecture; direct V2 source transfer is prohibited |
| Binding behavior | Preserve Effective Limit, Usage/Consumption, atomic Reservation/Commit/Release, Reconciliation and traceable Decision Results consistent with V3-002B-DEC-020 and V3-002B-DEC-021 |
| Required invariants | Idempotency, Concurrency Safety, Reservation Lifecycle, Tenant Isolation and Sovereign-local Authority |
| Authorization boundary | Quota remains independent from Entitlement, Membership and Resource/Action Authorization |
| Composite-asset impact | This is a component disposition only; overall V2-AST-035 remains NEEDS_REVIEW pending independent disposition reconciliation |
| Explicit exclusions | Policy/Limit Model, Plan/Subscription Ownership, Reset/Scheduling, API, Persistence, Migration and Service Topology remain Pending |
| ADR / OD impact | Conforms to ADR-V3-001–ADR-V3-005, ADR-V3-007–ADR-V3-008 and ADR-V3-010–ADR-V3-012; closes no OD |
| Approval status | Approved by project owner for the Quota component only |
| Approval evidence | Explicit owner response `A — REWRITE برای بخش Quota از V2-AST-035` with binding behavior, invariant, authorization-separation, source-transfer and reconciliation conditions |
| Date | 2026-10-23 |

### V3-002B-DEC-023 — Final disposition reconciliation for V2-AST-035

| Field | Recorded value |
| --- | --- |
| Exact question | What is the final whole-asset disposition of composite Asset Group V2-AST-035 after the four component reviews? |
| Selected option | **A — REWRITE as a Composite Asset Group** |
| Final disposition impact | V2-AST-035 changes from NEEDS_REVIEW to REWRITE, reconciling the separately approved Customer Requests, Audit, Entitlement and Quota component dispositions |
| Historical-traceability rule | Composite grouping is retained only to preserve historical provenance and does not establish a V3 architectural boundary |
| Preserved decisions | Release Scope, logical Domain/Data Ownership, Authorization boundaries and security requirements from V3-002B-DEC-011 through V3-002B-DEC-022 remain unchanged |
| Prohibited inferences | No Domain Merge, Shared Database, Single Microservice or direct V2 source port is authorized |
| Explicit exclusions | Policy/Design, API/Event Contracts, Persistence, Migration, Service Topology and all other recorded open decisions remain Pending |
| ADR / OD impact | Conforms to ADR-V3-001–ADR-V3-005, ADR-V3-007–ADR-V3-008 and ADR-V3-010–ADR-V3-012; closes no OD |
| Approval status | Approved by project owner as the final disposition for V2-AST-035 |
| Approval evidence | Explicit owner response `A — Disposition نهایی V2-AST-035 ... REWRITE` with traceability-only, boundary-preservation and prohibited-inference conditions |
| Date | 2026-10-23 |

### V3-002B-DEC-024 — Linka / External Registry product scope

| Field | Recorded value |
| --- | --- |
| Exact question | In which release does Linka / External Registry belong? |
| Selected option | **A — LATER_RELEASE** |
| FIRST_RELEASE boundary | Customer Core must support internal Customer creation, editing and search without a mandatory external Provider dependency |
| LATER_RELEASE entry conditions | Approved Provider Contract, Provenance, Retention, Resilience, Validation and authorized approval before any Customer Master change |
| Customer boundary | Customer Domain remains the source of truth; no external lookup result may directly mutate Customer Master |
| Operational-profile condition | Dedicated Sovereign base Customer operations must not depend on an external Provider |
| Affected Asset IDs | V2-AST-033; Customer relationship with V2-AST-037 remains contract-bound |
| Disposition impact | None; V2-AST-033 remains NEEDS_REVIEW |
| Domain ownership impact | None; Linka/provider logical and data ownership remains Pending |
| Explicit exclusions | Provider Selection, Contracts, API, Persistence, Migration and Service Topology remain Pending |
| ADR / OD impact | Applies ADR-V3-002, ADR-V3-003, ADR-V3-005, ADR-V3-008 and ADR-V3-010–ADR-V3-012; OD-020 remains Open |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `A — LATER_RELEASE برای Linka و External Registry` with Customer independence, provider-entry, approval and Sovereign conditions |
| Date | 2026-10-23 |

### V3-002B-DEC-025 — Linka / External Registry logical and data ownership

| Field | Recorded value |
| --- | --- |
| Exact question | Which logical capability owns Linka provider-interaction and pre-acceptance candidate data, and who owns the accepted Customer record? |
| Selected option | **A — Split ownership** |
| Linka authoritative data | Linka/External Registry Integration owns Provider Interaction, Lookup Request/Response, Provider Snapshot, Provenance, Validation State and Reviewed Candidate/Draft before acceptance |
| Customer authoritative data | Customer Domain owns acceptance/rejection decisions and the resulting Customer Master |
| Authorization impact | Customer Domain makes and enforces final Resource/Action Authorization for acceptance and Customer Master changes |
| Database boundary | No Provider or Adapter may write directly to Customer Master or access the Customer Domain's private database |
| Data-protection condition | Provider Snapshot is subject to future approved Retention, Security and Data Protection requirements |
| Affected Asset IDs | V2-AST-033; accepted Customer data remains within V2-AST-037 ownership boundaries |
| Disposition impact | None; V2-AST-033 remains NEEDS_REVIEW |
| Explicit exclusions | Provider Selection, Contracts, Retention Duration, API, Persistence, Migration and Service Topology remain Pending |
| ADR / OD impact | Applies ADR-V3-001–ADR-V3-003, ADR-V3-005, ADR-V3-008 and ADR-V3-010–ADR-V3-012; OD-020 remains Open |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `A — مالکیت تفکیک‌شده` with pre-/post-acceptance ownership, authorization, private-database and data-protection conditions |
| Date | 2026-10-23 |

### V3-002B-DEC-026 — V2-AST-033 disposition

| Field | Recorded value |
| --- | --- |
| Exact question | What is the disposition of historical Linka / External Registry asset V2-AST-033? |
| Selected option | **A — REWRITE within LATER_RELEASE** |
| Disposition impact | Valid Lookup, Provider Snapshot, Provenance, Validation and Reviewed Candidate/Draft behavior may be rewritten under the approved V3 architecture and V3-002B-DEC-024–025; direct V2 source transfer is prohibited |
| Release boundary | The decision does not require historical Provider adoption, implementation start or FIRST_RELEASE inclusion |
| Entry conditions | Implementation requires approved release requirements, Provider Contract, Retention, Security, Data Protection and Resilience requirements |
| Customer boundary | Customer Domain remains final authority for acceptance/rejection and applying Customer Master changes |
| Explicit exclusions | Provider Selection, Contracts, Retention Duration, API, Persistence, Migration and Service Topology remain Pending |
| ADR / OD impact | Conforms to ADR-V3-001–ADR-V3-003, ADR-V3-005, ADR-V3-008 and ADR-V3-010–ADR-V3-012; OD-020 remains Open |
| Approval status | Approved by project owner with LATER_RELEASE and entry-condition limitations |
| Approval evidence | Explicit owner response `A — Disposition دارایی V2-AST-033 برابر REWRITE با رعایت LATER_RELEASE` with source-transfer, implementation, provider and Customer-authority conditions |
| Date | 2026-10-23 |

### V3-002B-DEC-027 — Reporting product scope

| Field | Recorded value |
| --- | --- |
| Exact question | What deterministic Reporting capability belongs in the first V3 release, independently from AI? |
| Selected option | **A — FIRST_RELEASE Reporting Core** |
| FIRST_RELEASE portion | Deterministic, tenant-scoped reports required by approved FIRST_RELEASE capabilities, with base filters and authorized viewing |
| Report-set condition | Every Report Set requires independently approved requirements and Authorization rules |
| Data-access boundary | Reporting data must come only through versioned API/Event Contracts or authorized Projections; cross-service database access is prohibited |
| LATER_RELEASE portion | Advanced Analytics and Custom Report Builder |
| AI boundary | AI-generated Insights remain subject to an independent AI decision |
| Affected Asset IDs | Reporting portions of V2-AST-034 and V2-AST-046 |
| Disposition impact | None; V2-AST-034 and V2-AST-046 dispositions remain Pending |
| Domain ownership impact | None; Reporting logical/data ownership remains Pending |
| Explicit exclusions | Final Report Sets, API, Persistence, Migration and Service Topology remain Pending |
| ADR / OD impact | Applies ADR-V3-001–ADR-V3-003, ADR-V3-005, ADR-V3-008 and ADR-V3-010–ADR-V3-012; closes no OD |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `A — FIRST_RELEASE Reporting Core` with report-set approval, authorization, contract/projection and cross-database restrictions |
| Date | 2026-10-23 |

### V3-002B-DEC-028 — Reporting logical domain and data ownership

| Field | Recorded value |
| --- | --- |
| Exact question | Which logical capability owns report definitions, execution state, generated report resources and dedicated reporting projections? |
| Selected option | **A — Split Reporting ownership** |
| Reporting authoritative data | Reporting Capability owns Report Catalog/Definition Metadata, Execution State, Generated Report Artifact/Snapshot and its authorized dedicated Projections |
| Producer boundary | Producing Domain retains its Business Fact and contracts governing publication/disclosure of source data |
| Authorization impact | Reporting makes and enforces final Resource/Action Authorization for its report resources, subject to Tenant Isolation and source-data disclosure constraints |
| Projection boundary | Projections cannot create an Authorization bypass and may be populated only through approved contracts |
| Operational Platform impact | Operational Platform is infrastructure operator only and does not become semantic owner of Reporting data or source Business Facts |
| Operational-profile condition | Final Reporting authority in Dedicated Sovereign is local |
| Affected Asset IDs | Reporting portions of V2-AST-034 and V2-AST-046 |
| Disposition impact | None; V2-AST-034 and V2-AST-046 dispositions remain Pending |
| Explicit exclusions | Final Report Sets, API/Event Contracts, Projection Design, Retention, Persistence, Migration and Service Topology remain Pending |
| ADR / OD impact | Applies ADR-V3-001–ADR-V3-003, ADR-V3-005, ADR-V3-008 and ADR-V3-010–ADR-V3-012; closes no OD |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `A — مالکیت تفکیک‌شده Reporting` with producer, authorization, projection, operator and Sovereign-local boundaries |
| Date | 2026-10-23 |

### V3-002B-DEC-029 — Reporting component dispositions in V2-AST-034 and V2-AST-046

| Field | Recorded value |
| --- | --- |
| Exact question | What is the disposition of the Reporting components within composite assets V2-AST-034 and V2-AST-046? |
| Selected option | **A — REWRITE both Reporting components** |
| Disposition impact | Valid Deterministic Reporting, Basic Filters, Execution State and Report Artifact/Snapshot behavior is to be rewritten under V3-002B-DEC-027–028; direct V2 source port is prohibited |
| Data-access boundary | Reporting may use only approved API/Event Contracts or authorized Projections; cross-service database access is prohibited |
| Required invariants | Tenant Isolation, Reporting resource/action Authorization and source disclosure restrictions |
| Report-set condition | Every Report Set requires independently approved Requirements and Authorization rules |
| Composite-asset impact | V2-AST-034 remains Pending for AI decisions; V2-AST-046 remains Pending for Administration/Operations decisions and separate whole-asset reconciliation |
| Explicit exclusions | Final Report Sets, API/Event Contracts, Projection Design, Retention, Persistence, Migration and Service Topology remain Pending |
| ADR / OD impact | Conforms to ADR-V3-001–ADR-V3-003, ADR-V3-005, ADR-V3-008 and ADR-V3-010–ADR-V3-012; closes no OD |
| Approval status | Approved by project owner for the Reporting components only |
| Approval evidence | Explicit owner response `A — REWRITE برای اجزای Reporting در V2-AST-034 و V2-AST-046` with source-port, data-access, isolation, authorization and report-set conditions |
| Date | 2026-10-23 |

### V3-002B-DEC-030 — AI product scope

| Field | Recorded value |
| --- | --- |
| Exact question | In which release and under what product boundary do AI-generated Insights, Assistant and Business Action Proposals belong? |
| Selected option | **A — LATER_RELEASE with staged entry** |
| LATER_RELEASE portion | AI-generated Insights, Assistant and Business Action Proposals |
| FIRST_RELEASE boundary | FIRST_RELEASE must be independent from any AI Model or Provider |
| Data-access condition | AI may access only data allowed by validated Tenant Context and current User Authorization |
| Business-write condition | Every Business Write requires explicit user approval and execution-time re-authorization by the Resource-owning Domain; autonomous Business Write is prohibited |
| Required future invariants | Replay Protection, Idempotency and Data Sovereignty |
| Affected Asset IDs | AI portion of V2-AST-034 |
| Disposition impact | None; AI component and overall V2-AST-034 dispositions remain Pending |
| Domain ownership impact | None; AI logical/data ownership remains Pending |
| Explicit exclusions | Model/Provider Selection, RAG, Prompt/Data Retention, Approval/Replay Model, API, Persistence, Migration and Service Topology remain Pending |
| ADR / OD impact | Applies ADR-V3-002–ADR-V3-005, ADR-V3-008 and ADR-V3-010–ADR-V3-012; closes no OD |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `A — LATER_RELEASE با ورود مرحله‌ای AI` with access, approval, re-authorization, autonomous-write, replay, idempotency and sovereignty conditions |
| Date | 2026-10-23 |

### V3-002B-DEC-031 — AI logical domain and data ownership

| Field | Recorded value |
| --- | --- |
| Exact question | Which logical capability owns AI interaction/proposal lifecycle state, and who owns resulting Business Facts and writes? |
| Selected option | **A — Split AI ownership** |
| AI authoritative data | AI Orchestration Capability owns AI Interaction/Execution State, Generated Insight, Proposal, Approval Reference and Replay/Idempotency State |
| Target-domain boundary | Resource-owning Domain retains Business Fact ownership and performs final Authorization, Validation and Business Write execution |
| Approval boundary | Approval Reference is evidence only and grants no execution authority; every write requires explicit user approval and execution-time re-authorization in the target domain |
| Integration boundary | Direct cross-service database access and autonomous Business Write are prohibited; integration uses explicit contracts |
| Provider boundary | Model Provider does not own authoritative Business Facts |
| AI authorization | AI Orchestration authorizes only its own resources and cannot authorize target-domain operations |
| Operational-profile condition | Required security and operational authority in Dedicated Sovereign is local |
| Affected Asset IDs | AI portion of V2-AST-034 |
| Disposition impact | None; AI component and overall V2-AST-034 dispositions remain Pending |
| Explicit exclusions | Model/Provider Selection, RAG, Prompt/Data Retention, Approval/Replay Model, API, Persistence, Migration and Service Topology remain Pending |
| ADR / OD impact | Applies ADR-V3-001–ADR-V3-005, ADR-V3-008 and ADR-V3-010–ADR-V3-012; closes no OD |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `A — مالکیت تفکیک‌شده AI` with AI-state, target-domain, approval, database, provider, authorization and Sovereign-local boundaries |
| Date | 2026-10-23 |

### V3-002B-DEC-032 — AI component disposition within V2-AST-034

| Field | Recorded value |
| --- | --- |
| Exact question | What is the disposition of the AI component within composite Asset Group V2-AST-034? |
| Selected option | **A — REWRITE within LATER_RELEASE** |
| Disposition impact | Valid Permission-aware Access, Generated Insight, Proposal, Explicit Approval Reference and Confirmed-action Handoff behavior may be rewritten under V3-002B-DEC-030–031; direct V2 source port is prohibited |
| AI authority boundary | AI Orchestration owns only its resources/state and has no Business Write authority |
| Write-execution condition | Every write requires explicit user approval and execution-time re-authorization by the Resource-owning Domain |
| Prohibited behavior | Autonomous Business Write and direct cross-service database access are prohibited |
| Release boundary | This decision does not authorize FIRST_RELEASE inclusion or implementation start |
| Composite-asset impact | Both Reporting and AI component dispositions are approved; overall V2-AST-034 remains NEEDS_REVIEW pending independent reconciliation |
| Explicit exclusions | Model/Provider Selection, RAG, Prompt/Data Retention, Approval/Replay Model, API, Persistence, Migration and Service Topology remain Pending |
| ADR / OD impact | Conforms to ADR-V3-001–ADR-V3-005, ADR-V3-008 and ADR-V3-010–ADR-V3-012; closes no OD |
| Approval status | Approved by project owner for the AI component only |
| Approval evidence | Explicit owner response `A — Disposition بخش AI از V2-AST-034 برابر REWRITE با رعایت LATER_RELEASE` with behavior, authority, write, prohibited-access, release and source-port conditions |
| Date | 2026-10-23 |

### V3-002B-DEC-033 — Final disposition reconciliation for V2-AST-034

| Field | Recorded value |
| --- | --- |
| Exact question | What is the final whole-asset disposition of composite Asset Group V2-AST-034 after the Reporting and AI component reviews? |
| Selected option | **A — REWRITE as a Composite Asset Group** |
| Final disposition impact | V2-AST-034 changes from NEEDS_REVIEW to REWRITE, reconciling Reporting decisions V3-002B-DEC-027–029 and AI decisions V3-002B-DEC-030–032 |
| Release boundary | Reporting Core remains FIRST_RELEASE; AI remains LATER_RELEASE |
| Preserved boundaries | Independent Domain/Data Ownership, Authorization, Tenant Isolation and security requirements for Reporting and AI remain unchanged |
| Historical-traceability rule | Composite grouping is retained only for provenance and does not establish a V3 architectural boundary |
| Prohibited inferences | No Domain Merge, Shared Database, Single Service, cross-service database access, direct V2 source port, implementation start or AI inclusion in FIRST_RELEASE is authorized |
| Explicit exclusions | Final Report Sets, Model/Provider Selection, RAG, Prompt/Data Retention, Approval/Replay Model, API/Event Contracts, Projection Design, Persistence, Migration, Service Topology and all other open decisions remain Pending |
| ADR / OD impact | Conforms to ADR-V3-001–ADR-V3-005, ADR-V3-008 and ADR-V3-010–ADR-V3-012; closes no OD |
| Approval status | Approved by project owner as the final disposition for V2-AST-034 |
| Approval evidence | Explicit owner response `A — Disposition نهایی V2-AST-034 ... REWRITE` with release, independence, traceability and prohibited-inference conditions |
| Date | 2026-10-23 |

### V3-002B-DEC-034 — Work / Collaboration product scope

| Field | Recorded value |
| --- | --- |
| Exact question | What Work / Collaboration capability belongs in the first V3 release? |
| Selected option | **A — FIRST_RELEASE Work Core** |
| FIRST_RELEASE portion | Base Task Create, View, Edit, Assignment, Status, Due Date and manual contract-based links to Customer, Opportunity and Customer Request |
| LATER_RELEASE portion | Meetings, Timesheets, Personal Todos, Advanced Team Collaboration, Workflow Automation and automatic cross-domain integration |
| Assignment boundary | Assignment creates no Tenant Membership, Entitlement or Resource/Action Authorization |
| Related-resource boundary | Access to linked resources remains subject to independent authorization by each Resource-owning Domain |
| Cross-domain boundary | Links use authorized contracts only and do not transfer Business Fact ownership |
| Affected Asset IDs | V2-AST-039; contractual references to V2-AST-035, V2-AST-037 and V2-AST-038 |
| Disposition impact | None; V2-AST-039 disposition remains Pending |
| Domain ownership impact | None; Work logical/data ownership remains Pending |
| Explicit exclusions | Task State Machine, API/Event Contracts, Persistence, Migration and Service Topology remain Pending |
| ADR / OD impact | Applies ADR-V3-001–ADR-V3-003, ADR-V3-005, ADR-V3-008 and ADR-V3-011–ADR-V3-012; closes no OD |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `A — FIRST_RELEASE Work Core` with included/deferred scope, assignment, authorization, contract and Business Fact conditions |
| Date | 2026-10-23 |

### V3-002B-DEC-035 — Work Core logical domain and data ownership

| Field | Recorded value |
| --- | --- |
| Exact question | Which logical domain owns authoritative Task, lifecycle/status, due date, assignment and cross-domain link metadata? |
| Selected option | **A — Work Domain** |
| Authoritative data/write impact | Work Domain owns Task, Task Lifecycle/Status, Due Date, Assignment Record and cross-domain Link Metadata and is authoritative for them |
| Related-domain boundary | Customer, Sales and Customer Request Domains retain their resources and Business Facts |
| Authorization impact | Work Domain authorizes only Task resources; Assignment and Link Metadata grant no Membership, Entitlement or authorization to related resources |
| Integration boundary | Cross-domain links require valid contracts, Tenant Isolation and authorization by the related Resource-owning Domain; direct cross-service database access and foreign Business Fact changes are prohibited |
| Auxiliary-capability boundary | Ownership of Meetings, Timesheets, Personal Todos and Advanced Collaboration remains Pending |
| Affected Asset IDs | Work Core portion of V2-AST-039; contractual references to V2-AST-035, V2-AST-037 and V2-AST-038 |
| Disposition impact | None; V2-AST-039 disposition remains Pending |
| Explicit exclusions | Task State Machine, API/Event Contracts, Persistence, Migration and Service Topology remain Pending |
| ADR / OD impact | Applies ADR-V3-001–ADR-V3-003, ADR-V3-005, ADR-V3-008 and ADR-V3-011–ADR-V3-012; closes no OD |
| Approval status | Approved by project owner for Work Core only |
| Approval evidence | Explicit owner response `A — Work Domain` with authoritative Task data, related-domain, authorization, contract, tenant and database boundaries |
| Date | 2026-10-23 |

### V3-002B-DEC-036 — V2-AST-039 disposition

| Field | Recorded value |
| --- | --- |
| Exact question | What is the disposition of historical composite Work / Collaboration asset V2-AST-039? |
| Selected option | **A — REWRITE as a Composite Asset Group within approved Release Scope** |
| FIRST_RELEASE rewrite | Task Core, Lifecycle/Status, Assignment, Due Date and manual contract-based links consistent with V3-002B-DEC-034–035 |
| Conditional LATER_RELEASE rewrite | Meetings, Timesheets, Personal Todos and Advanced Collaboration only after independent Requirements and Domain/Data Ownership approval |
| Separately gated capabilities | Workflow Automation and automatic cross-domain integration require independent approval |
| Source rule | Direct V2 source port is prohibited |
| Authorization boundary | Work Domain authorizes only Task resources; Assignment or Link grants no Membership, Entitlement or related-resource Authorization |
| Historical-traceability rule | Composite grouping is provenance-only and authorizes no Domain Merge, Shared Database or Single Service |
| Explicit exclusions | Task State Machine, API/Event Contracts, Persistence, Migration, Service Topology and all open auxiliary-capability decisions remain Pending |
| ADR / OD impact | Conforms to ADR-V3-001–ADR-V3-003, ADR-V3-005, ADR-V3-008 and ADR-V3-011–ADR-V3-012; closes no OD |
| Approval status | Approved by project owner with release-scope and component-gate limitations |
| Approval evidence | Explicit owner response `A — Disposition دارایی V2-AST-039 ... REWRITE با رعایت Release Scope` with source, authorization, traceability and auxiliary-gate conditions |
| Date | 2026-10-23 |

### V3-002B-DEC-037 — Content / File product scope

| Field | Recorded value |
| --- | --- |
| Exact question | What Content / File capability belongs in the first V3 release? |
| Selected option | **A — FIRST_RELEASE File/Attachment Core** |
| FIRST_RELEASE portion | File Metadata, controlled Upload/Download, Basic File Lifecycle and contract-based Attachment to approved FIRST_RELEASE resources |
| Attachment-onboarding condition | Every Domain/Resource Attachment requires independently approved Requirements and Authorization |
| Authorization boundary | File ID and Attachment Link grant no access authority |
| Required invariants | Tenant Isolation, Access Control, Upload Validation and base security requirements |
| LATER_RELEASE portion | Public Sharing, Advanced Versioning, Media Processing and Advanced Generated Artifacts |
| Operational-profile condition | Shared SaaS, Dedicated Managed and Dedicated Sovereign must be deployable without mandatory dependency on an external Storage Provider |
| Affected Asset IDs | V2-AST-040; potential generated-artifact relationship with V2-AST-034/V2-AST-046 remains contract-bound |
| Disposition impact | None; V2-AST-040 disposition remains Pending |
| Domain ownership impact | None; Content/File logical/data ownership remains Pending |
| Explicit exclusions | Storage Provider, Object Storage Strategy, Malware Scanning Design, Retention, API, Persistence, Migration and Service Topology remain Pending |
| ADR / OD impact | Applies ADR-V3-001–ADR-V3-003, ADR-V3-005, ADR-V3-008 and ADR-V3-010–ADR-V3-012; OD-017 remains Open |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `A — FIRST_RELEASE File/Attachment Core` with attachment, authority, isolation, validation, deferred-feature and all-profile conditions |
| Date | 2026-10-23 |

### V3-002B-DEC-038 — File / Attachment logical and data ownership

| Field | Recorded value |
| --- | --- |
| Exact question | Which logical domain is authoritative for File state and for the meaning of an Attachment to a Business Resource? |
| Selected option | **A — Split File/Attachment ownership** |
| File/Content ownership | File/Content Domain is authoritative for File Metadata, Content/Object Lifecycle, Storage Reference, Integrity/Checksum and Validation/Quarantine State |
| Resource-domain ownership | Each Resource-owning Domain owns the meaning of an Attachment and its relationship to the Business Resource, and authorizes creation/removal of that relationship |
| Access rule | File access requires File Domain authorization and valid authorization for the related resource; neither a File ID nor an Attachment Link grants authority |
| Multiple-link invariant | Multiple attachments or references to one file cannot create unauthorized access through a differently authorized resource |
| Lifecycle separation | Removing an Attachment does not necessarily delete the File Object; detailed reference, deletion and lifecycle policies remain Pending |
| Integration boundary | Direct Cross-Service Database Access is prohibited; integration must use authorized versioned contracts |
| Operational-profile condition | Security and operational authority for Dedicated Sovereign remains local |
| Affected Asset IDs | V2-AST-040; Advanced Generated Artifacts ownership remains separately Pending |
| Disposition impact | None; V2-AST-040 disposition remains Pending |
| Explicit exclusions | Advanced Generated Artifacts Ownership, Storage Provider/Strategy, Malware Scanning Design, Retention, API, Persistence, Migration and Service Topology remain Pending |
| ADR / OD impact | Applies ADR-V3-001–ADR-V3-003, ADR-V3-005, ADR-V3-008 and ADR-V3-010–ADR-V3-012; OD-017 remains Open |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `A — مالکیت تفکیک‌شده File/Attachment` with authority, multiple-link, lifecycle, database-boundary and sovereign-local conditions |
| Date | 2026-10-23 |

### V3-002B-DEC-039 — V2-AST-040 disposition

| Field | Recorded value |
| --- | --- |
| Exact question | What is the final disposition of the composite historical Content/File asset group V2-AST-040? |
| Selected option | **A — REWRITE with approved Release Scope** |
| FIRST_RELEASE rewrite scope | File Metadata, Controlled Upload/Download, Basic File Lifecycle and Contract-based Attachment according to V3-002B-DEC-037/038 |
| Per-resource gate | Every connection to a Business Resource requires independently approved requirements and authorization from the Resource-owning Domain |
| LATER_RELEASE rewrite scope | Public Sharing, Advanced Versioning, Media Processing and Advanced Generated Artifacts, only after independent approval of their requirements and ownership |
| Source rule | Direct V2 Source Port is prohibited; only validated behavior and requirements may inform a new V3 implementation |
| Authorization and lifecycle invariants | File ID, Attachment Link and multiple references grant no authority; removing an Attachment does not necessarily delete the File Object |
| Composite limitation | Historical grouping does not approve Domain Merge, Shared Database, Single Service or Direct Cross-Service Database Access |
| Explicit exclusions | Storage Provider/Strategy, Malware Scanning Design, Retention, API/Event Contracts, Persistence, Migration, Service Topology and Advanced Generated Artifacts Ownership remain Pending |
| Readiness limitation | This decision approves neither implementation nor production readiness |
| Affected Asset IDs | V2-AST-040 |
| ADR / OD impact | Applies ADR-V3-001–ADR-V3-003, ADR-V3-005, ADR-V3-008 and ADR-V3-010–ADR-V3-012; OD-017 remains Open |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `A — Disposition دارایی V2-AST-040 ... REWRITE با رعایت Release Scope` with source, authorization, lifecycle, composite-boundary and readiness limitations |
| Date | 2026-10-23 |

### V3-002B-DEC-040 — Technical Knowledge product scope

| Field | Recorded value |
| --- | --- |
| Exact question | When does Technical Knowledge enter V3 product scope? |
| Selected option | **A — LATER_RELEASE** |
| LATER_RELEASE scope | Technical Document/Article, Basic Classification, contract-based links to Customer, Opportunity and Customer Request, and University Reference Data |
| FIRST_RELEASE independence | No FIRST_RELEASE capability may require Technical Knowledge, University Registry or a Search Engine |
| File boundary | Technical Knowledge is independent of the File/Attachment Core approved by V3-002B-DEC-037; its deferral cannot restrict File Core |
| Cross-domain invariant | Links require valid contracts, Tenant Isolation and independent authorization, and do not transfer ownership of any Business Fact |
| Implementation gate | Independent approval of Requirements, Lifecycle, Classification, Search/Indexing, Access Control and Retention |
| Affected Asset IDs | V2-AST-041; potential links to V2-AST-037–040 remain contract-bound |
| Disposition impact | None; V2-AST-041 disposition remains Pending |
| Domain ownership impact | None; Technical Knowledge logical/data ownership remains Pending |
| Explicit exclusions | Domain/Data Ownership, API/Event Contracts, Persistence, Migration and Service Topology remain Pending; implementation is not authorized |
| ADR / OD impact | Applies ADR-V3-001–ADR-V3-003, ADR-V3-005, ADR-V3-008 and ADR-V3-010–ADR-V3-012; OD-018 remains Open |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `A — Technical Knowledge ... در LATER_RELEASE` with FIRST_RELEASE-independence, File-boundary, contract, authorization and implementation-gate conditions |
| Date | 2026-10-23 |

### V3-002B-DEC-041 — Technical Knowledge logical and data ownership

| Field | Recorded value |
| --- | --- |
| Exact question | Which logical domain is authoritative for Technical Knowledge data and its links? |
| Selected option | **A — Technical Knowledge Domain ownership with retained source-domain authority** |
| Knowledge ownership | Technical Knowledge Domain is authoritative for Technical Document/Article, Knowledge Lifecycle, Classification Assignment, University Reference Data and Knowledge-side Link Metadata |
| File boundary | File/Content Domain remains owner of File Object, Storage Reference and File State |
| Business-resource boundary | Customer, Sales and Customer Request domains remain owners of their Business Resources and Business Facts |
| Authorization boundary | Technical Knowledge authorizes only its knowledge resources; access to a related business resource requires authorization from its Resource-owning Domain |
| Link invariant | A Knowledge Link grants no Membership, Entitlement or Authorization |
| Search boundary | Search Index is a rebuildable, non-authoritative Projection and cannot bypass Tenant Isolation, Authorization or source disclosure restrictions |
| Integration boundary | Direct Cross-Service Database Access is prohibited; integration must use authorized versioned contracts |
| Operational-profile condition | Security and operational authority for Dedicated Sovereign remains local |
| Disposition impact | None; V2-AST-041 disposition remains Pending |
| Explicit exclusions | Lifecycle/Classification Design, Search/Indexing, Retention, API/Event Contracts, Persistence, Migration and Service Topology remain Pending |
| ADR / OD impact | Applies ADR-V3-001–ADR-V3-003, ADR-V3-005, ADR-V3-008 and ADR-V3-010–ADR-V3-012; OD-018 remains Open |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `A — Technical Knowledge Domain مالک منطقی و authoritative` with file, resource, authorization, link, search, database-boundary and sovereign-local conditions |
| Date | 2026-10-23 |

### V3-002B-DEC-042 — V2-AST-041 disposition

| Field | Recorded value |
| --- | --- |
| Exact question | What is the final disposition of the composite historical Technical Knowledge asset group V2-AST-041? |
| Selected option | **A — REWRITE with LATER_RELEASE scope** |
| Rewrite scope | Valid Technical Document/Article, Basic Classification, University Reference Data and Contract-based Link behavior according to V3-002B-DEC-040/041 |
| Release constraint | Technical Knowledge cannot become a FIRST_RELEASE dependency or restrict the approved File/Attachment Core |
| Source rule | Direct V2 Source Port is prohibited; only validated behavior and requirements may inform a future V3 implementation |
| Preserved ownership | File/Content Domain retains File Object and File State; Customer, Sales and Customer Request domains retain their Business Resources |
| Search invariant | Search Index is only a rebuildable, non-authoritative Projection |
| Link invariant | Cross-domain Links grant no Membership, Entitlement or Authorization |
| Composite limitation | Historical grouping does not approve Domain Merge, Shared Database, Single Service or Direct Cross-Service Database Access |
| Explicit exclusions | Lifecycle/Classification Design, Search/Indexing, Access Control Design, Retention, API/Event Contracts, Persistence, Migration and Service Topology remain Pending |
| Readiness limitation | This decision approves neither implementation nor production readiness |
| Affected Asset IDs | V2-AST-041 |
| ADR / OD impact | Applies ADR-V3-001–ADR-V3-003, ADR-V3-005, ADR-V3-008 and ADR-V3-010–ADR-V3-012; OD-018 remains Open |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `A — Disposition دارایی V2-AST-041 ... REWRITE با رعایت LATER_RELEASE` with source, dependency, ownership, search, link, composite-boundary and readiness limitations |
| Date | 2026-10-23 |

### V3-002B-DEC-043 — Customer Portal product scope

| Field | Recorded value |
| --- | --- |
| Exact question | When does Customer Portal enter V3 product scope? |
| Selected option | **A — LATER_RELEASE** |
| LATER_RELEASE scope | Customer-facing Access, External Customer Users, Portal Authentication/Session, Customer Account Workspace and Customer Submission/Sharing |
| FIRST_RELEASE independence | No FIRST_RELEASE capability may require Portal, Portal Identity or Customer-facing Workspace |
| Exposure gate | Every Portal-exposed Resource/Action requires independently approved requirements, a valid contract and authorization by its Resource-owning Domain |
| Business-fact boundary | Portal owns no Business Fact of Customer, Customer Request, Sales, Work, File/Content or Technical Knowledge domains |
| Authentication limitation | Portal Authentication alone creates no Tenant Membership, Entitlement or Resource Authorization |
| Independent decisions | External Principal Model, Customer/Tenant Relationship and Trust Boundary require separate approval |
| Integration boundary | Direct Cross-Service Database Access is prohibited; integration must use authorized versioned contracts |
| Operational-profile condition | Sovereign-local security and operational authority is preserved |
| Affected Asset IDs | V2-AST-042; portal-facing portions of V2-AST-035 and links to other domain assets remain independently gated |
| Disposition impact | None; V2-AST-042 disposition remains Pending |
| Domain ownership impact | None; Portal logical/data ownership remains Pending |
| Explicit exclusions | Principal/Identity Model, Session/Trust Model, Domain/Data Ownership, API/Event Contracts, Persistence, Migration and Service Topology remain Pending |
| ADR / OD impact | Applies ADR-V3-001–ADR-V3-005 and ADR-V3-008–ADR-V3-012; relevant identity/session/frontend Open Decisions remain Open |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `A — Customer Portal ... در LATER_RELEASE` with FIRST_RELEASE-independence, exposure, authentication, trust, database-boundary and sovereign-local conditions |
| Date | 2026-10-23 |

### V3-002B-DEC-044 — Customer Portal logical and data ownership

| Field | Recorded value |
| --- | --- |
| Exact question | Which logical domains are authoritative for Customer Portal state and its adjacent identity, tenant, customer and business resources? |
| Selected option | **A — Split Customer Portal ownership** |
| Portal ownership | Customer Portal Domain is authoritative for Portal Account Linkage, Customer-facing Workspace State, Portal Preferences, Invitation/Onboarding State and Portal-specific Access/Interaction State |
| Identity boundary | Identity Capability remains authoritative for Principal Identity, Credential/Authenticator and Authentication/Session State |
| Tenant/customer boundary | Tenant Management retains Tenant/Organization/Membership; Customer Domain retains Customer Master |
| Business-resource boundary | Each Resource-owning Domain retains its Business Fact and final Resource/Action Authorization |
| Portal authorization | Portal authorizes only Portal-owned resources; access to Business Resources requires valid contracts and authorization by their owning domains |
| Authority limitation | Portal Account, Invitation, Session and Workspace State grant no Membership, Entitlement or business-resource authority |
| Independent decisions | External Principal Model, Customer/Tenant Relationship, Invitation Trust and Session/Trust Model remain Pending |
| Integration boundary | Direct Cross-Service Database Access is prohibited; integration must use authorized versioned contracts |
| Operational-profile condition | Security and operational authority for Dedicated Sovereign remains local |
| Disposition impact | None; V2-AST-042 disposition remains Pending |
| Explicit exclusions | API/Event Contracts, Persistence, Migration and Service Topology are not approved |
| ADR / OD impact | Applies ADR-V3-001–ADR-V3-005 and ADR-V3-008–ADR-V3-012; relevant identity/session/frontend Open Decisions remain Open |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `A — مالکیت تفکیک‌شده Customer Portal` with identity, tenant, customer, resource-authorization, trust, database-boundary and sovereign-local conditions |
| Date | 2026-10-23 |

### V3-002B-DEC-045 — V2-AST-042 disposition

| Field | Recorded value |
| --- | --- |
| Exact question | What is the final disposition of the composite historical Customer Portal asset group V2-AST-042? |
| Selected option | **A — REWRITE with LATER_RELEASE scope** |
| Rewrite scope | Valid Customer-facing Access, Portal Account Linkage, External Customer Users, Portal Authentication/Session, Account Workspace, Invitation/Onboarding and Customer Submission/Sharing behavior according to V3-002B-DEC-043/044 |
| Release constraint | FIRST_RELEASE cannot depend on Customer Portal |
| Source rule | Direct V2 Source Port is prohibited; only validated behavior and requirements may inform a future V3 implementation |
| Authority limitation | Portal Account, Invitation, Session and Workspace State grant no Membership, Entitlement or Business Resource Authorization |
| Business-operation rule | Every Business Operation uses a valid contract and is authorized by the Resource-owning Domain |
| Preserved ownership | Identity retains Principal/Credential/Authentication/Session State; Tenant Management retains Membership; Customer retains Customer Master; Portal retains Portal-specific State |
| Composite limitation | Historical grouping does not approve Domain Merge, Shared Database, Single Service or Direct Cross-Service Database Access |
| Explicit exclusions | External Principal Model, Customer/Tenant Relationship, Invitation Trust, Session/Trust Model, API/Event Contracts, Persistence, Migration and Service Topology remain Pending |
| Readiness limitation | This decision approves neither implementation nor production readiness |
| Affected Asset IDs | V2-AST-042 |
| ADR / OD impact | Applies ADR-V3-001–ADR-V3-005 and ADR-V3-008–ADR-V3-012; relevant identity/session/frontend Open Decisions remain Open |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `A — Disposition دارایی V2-AST-042 ... REWRITE با رعایت LATER_RELEASE` with source, dependency, authority, ownership, composite-boundary and readiness limitations |
| Date | 2026-10-23 |

### V3-002B-DEC-046 — V2-AST-043 disposition

| Field | Recorded value |
| --- | --- |
| Exact question | What is the final disposition of the historical V2 schema, SQL migration and database-tool corpus V2-AST-043? |
| Selected option | **A — REWRITE** |
| Historical-use rule | Prisma Schema, 97 SQL Migrations and V2 database tools are Historical Discovery Evidence and read-only references for entities, relationships, constraints and data evolution only |
| V3 design rule | V3 schemas and migrations must be designed independently according to approved Domain/Data Ownership, service-owned persistence, Tenant Isolation and binding ADRs |
| Prohibited reuse | Direct execution, replay, import or port of V2 schemas/migrations into V3 is prohibited |
| Authority limitation | The shared historical schema creates no architectural authority or data ownership in V3 |
| Domain migration gate | Every domain requires an independently approved Migration Plan, Mapping, Validation, Rollback/Cutover approach |
| Explicit exclusions | Actual Data Migration, Physical Schema, RLS Policy, Tooling, Cutover Strategy, Data Cleansing, Persistence Design and Service Topology are not approved |
| Readiness limitation | This decision approves neither implementation nor production readiness |
| Affected Asset IDs | V2-AST-043 |
| ADR / OD impact | Applies ADR-V3-001–ADR-V3-003, ADR-V3-007 and ADR-V3-011–ADR-V3-012; OD-013 and OD-014 remain Open |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `A — Disposition دارایی V2-AST-043 برابر REWRITE` with read-only-evidence, independent-schema, prohibited-reuse, per-domain migration and readiness limitations |
| Date | 2026-10-23 |

### V3-002B-DEC-047 — V2-AST-044 disposition

| Field | Recorded value |
| --- | --- |
| Exact question | What is the final disposition of the historical V2 test corpus V2-AST-044? |
| Selected option | **A — RETAIN as read-only Historical Test Evidence** |
| Retained evidence | Business Behavior Scenarios, Failure Knowledge, Tenant/Security Boundary Cases, Protocol Expectations and Regression Knowledge |
| Adoption gate | Evidence may inform Acceptance Criteria and Test Design only after review against binding ADRs, approved Release Scope, Domain Ownership and V3 Requirements |
| Prohibited reuse | Direct Test Source Port, Jest/NestJS/Prisma adoption, V2-test execution in V3, one-to-one test rewriting and claims that historical results are valid are prohibited |
| V3 test rule | V3 tests must be independently designed for approved Domain Boundaries, Contracts, technologies and Deployment Profiles |
| Evidence-quality rule | Incomplete or contradictory evidence must be identified and cannot automatically become a Requirement |
| Explicit exclusions | Test Strategy, Coverage Targets, Framework/Tooling, Test Environment, CI Integration, Runtime Correctness, Security Validation and Production Readiness remain Pending |
| Affected Asset IDs | V2-AST-044 |
| ADR / OD impact | Applies ADR-V3-003, ADR-V3-005, ADR-V3-007–ADR-V3-008 and ADR-V3-012; closes no Open Decision |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `A — Disposition دارایی V2-AST-044 برابر RETAIN` with read-only-evidence, review-gate, prohibited-reuse, independent-test and evidence-quality conditions |
| Date | 2026-10-23 |

### V3-002B-DEC-048 — V2-AST-045 disposition

| Field | Recorded value |
| --- | --- |
| Exact question | What is the final disposition of the historical V2 contract and documentation corpus V2-AST-045? |
| Selected option | **A — RETAIN as read-only Historical Contract/Documentation Evidence** |
| Retained evidence | OpenAPI, DTOs, Controller Surfaces and V2 design/operational documents, solely for Vocabulary, Consumer Expectations, Candidate Workflows, Error Cases and Compatibility Risks |
| Authority limitation | No historical API Shape, DTO, Endpoint, Authentication/Authorization Behavior or Backward Compatibility is approved for V3 |
| Prohibited reuse | Direct Source/Specification Port, code generation from V2 contracts and publication of those artifacts as V3 contracts are prohibited |
| V3 contract gate | Every V3 contract requires independently approved Requirements, Domain Ownership, Versioning, Tenant Context, Authorization, Error Model, Consumer Review and Approval |
| Evidence-quality rule | Incomplete or contradictory evidence must be explicitly identified |
| Explicit exclusions | API/Event Contracts, Compatibility Policy, Versioning Strategy, Deprecation Policy, Tooling, Implementation and Production Readiness remain Pending |
| Affected Asset IDs | V2-AST-045 |
| ADR / OD impact | Applies ADR-V3-008 and ADR-V3-012; OD-007, OD-008 and OD-020 remain Open |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `A — Disposition دارایی V2-AST-045 برابر RETAIN` with read-only-evidence, authority, prohibited-port, independent-contract and evidence-quality conditions |
| Date | 2026-10-23 |

### V3-002B-DEC-049 — Administration / Operations scope

| Field | Recorded value |
| --- | --- |
| Exact question | What Administration/Operations scope is required in FIRST_RELEASE and what remains deferred? |
| Selected option | **A — Split scope** |
| FIRST_RELEASE obligation | Essential Operational Core: Health/Readiness Visibility, Tenant/Platform Scope Separation, Authorized Operational Visibility, Privileged Operation Audit and independently approved minimum operational controls |
| Nature of obligation | Architecture/Operations obligation only; it creates no new Business Domain, General Administration UI or universal Admin Superuser |
| LATER_RELEASE portion | General Administration UI, Advanced Operational Dashboard, Bulk Import, Email Administration and Automation/Advanced Remediation |
| Preserved boundaries | Reporting remains governed by V3-002B-DEC-027–029; Notification/Email Delivery remains governed by V3-002B-DEC-008–010 |
| Authorization invariant | No Admin Surface or Privileged Operation may bypass Domain-owned Authorization, Tenant Isolation or Audit |
| Operational-profile condition | Security and operational authority for Dedicated Sovereign remains local |
| Affected Asset IDs | Administration/Operations portions of composite V2-AST-046 |
| Disposition impact | None; final V2-AST-046 disposition remains Pending |
| Domain ownership impact | None; Administration/Operations logical/data ownership remains Pending |
| Explicit exclusions | Privileged Role Model, Import Semantics, Operational Action Catalog, API/Event Contracts, Observability Stack, Persistence, Migration and Service Topology remain Pending |
| Readiness limitation | This decision does not establish production readiness |
| ADR / OD impact | Applies ADR-V3-001–ADR-V3-005, ADR-V3-008 and ADR-V3-010–ADR-V3-012; closes no Open Decision |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `A — محدوده تفکیک‌شده Administration/Operations` with obligation, deferral, boundary, authorization, sovereign-local and readiness conditions |
| Date | 2026-10-23 |

### V3-002B-DEC-050 — Administration / Operations logical and data ownership

| Field | Recorded value |
| --- | --- |
| Exact question | Which logical capability is authoritative for Operational Core state, and which existing authorities remain separate? |
| Selected option | **A — Split Administration/Operations ownership** |
| Operational Platform ownership | Operational Visibility Projection, Health/Readiness Aggregation, Privileged Operation Request/Execution State and state of independently approved operational controls |
| Authority limitation | Operational Platform owns no Business Fact and has no universal Authorization authority |
| Source-service boundary | Each Service/Domain retains ownership of its source Health Signal, Configuration and Business Fact |
| Destination-domain boundary | Resource-owning Domain makes the final authorization decision for operations affecting its business resources |
| Preserved authorities | Audit owns Privileged Operation Audit Records; Tenant Management owns Tenant/Organization/Membership; Reporting owns Report Resources; Notification owns Delivery/Email State |
| Admin-surface limitation | Admin UI and Operational Platform grant no implicit access to domain resources |
| Privileged-operation invariant | Valid limited identity, explicit Tenant/Platform scope, destination-domain Authorization and traceable Audit are required |
| Integration boundary | Direct Cross-Service Database Access is prohibited; integration must use authorized versioned contracts |
| Operational-profile condition | Security and operational authority for Dedicated Sovereign remains local |
| Deferred ownership | Bulk Import Staging/Job, Email Administration Policy and Advanced Administration/Remediation ownership remain Pending |
| Disposition impact | None; Administration/Operations component dispositions in V2-AST-046 remain Pending |
| Explicit exclusions | Privileged Role Model, Operational Action Catalog, API/Event Contracts, Observability Stack, Persistence, Migration and Service Topology are not approved |
| ADR / OD impact | Applies ADR-V3-001–ADR-V3-005, ADR-V3-008 and ADR-V3-010–ADR-V3-012; closes no Open Decision |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `A — مالکیت تفکیک‌شده Administration/Operations` with source-service, destination-domain, preserved-authority, privileged-operation, database-boundary and sovereign-local conditions |
| Date | 2026-10-23 |

### V3-002B-DEC-051 — V2-AST-046 final disposition reconciliation

| Field | Recorded value |
| --- | --- |
| Exact question | What is the final reconciled disposition of composite V2-AST-046 after its Reporting and Administration/Operations decisions? |
| Selected option | **A — REWRITE with approved Release Scope** |
| FIRST_RELEASE rewrite scope | Reporting Core according to V3-002B-DEC-027–029 and Operational Core according to V3-002B-DEC-049/050 |
| Operational nature | Operational Core is an Architecture/Operations obligation and creates no new Business Domain |
| LATER_RELEASE rewrite scope | General Administration UI, Advanced Operational Dashboard, Bulk Import, Email Administration and Automation/Advanced Remediation, only after independent Requirements, Ownership and Authorization approval |
| Source rule | Direct V2 Source Port is prohibited |
| Preserved boundaries | Reporting and Notification/Email Delivery retain independent boundaries; Operational Platform owns no Business Fact or universal Authorization |
| Privileged-operation invariant | Every Privileged Operation requires valid identity, explicit Tenant/Platform scope, destination-domain authorization and Audit |
| Admin-surface invariant | No Admin Surface may bypass Tenant Isolation or Domain-owned Authorization |
| Composite limitation | Historical grouping does not approve Domain Merge, Shared Database, Single Service, Admin Superuser or Direct Cross-Service Database Access |
| Explicit exclusions | Bulk Import Staging/Job Ownership, Email Administration Policy Ownership, Advanced Administration/Remediation Ownership, Privileged Role Model, Operational Action Catalog, API/Event Contracts, Observability Stack, Persistence, Migration and Service Topology remain Pending |
| Readiness limitation | This decision approves neither implementation nor production readiness |
| Affected Asset IDs | V2-AST-046 |
| ADR / OD impact | Applies ADR-V3-001–ADR-V3-005, ADR-V3-008 and ADR-V3-010–ADR-V3-012; closes no Open Decision |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `A — Disposition نهایی V2-AST-046 ... REWRITE با رعایت Release Scope` with component, source, boundary, privileged-operation, composite and readiness limitations |
| Date | 2026-10-23 |

### V3-002B-DEC-052 — V2-AST-036 disposition

| Field | Recorded value |
| --- | --- |
| Exact question | What is the final disposition of the historical V2 capability map V2-AST-036? |
| Selected option | **A — RETAIN as read-only Historical Capability/Traceability Map** |
| Retained evidence | Folders, modules and observed capabilities in the pinned 838-file V2 repository, solely for Discovery, Coverage Tracking, Evidence Mapping and Traceability |
| Authority limitation | The map approves no Product Scope, Domain Boundary, Aggregate, Microservice, Service Topology or Implementation Priority for V3 |
| Evidence interpretation | V2 module presence does not place a capability in V3; absence of historical evidence does not prove absence of a Requirement |
| Traceability requirement | Relationships between Historical Assets and approved V3 capabilities must remain explicit; incomplete, overlapping or contradictory evidence must be identified |
| Prohibited inference | Direct V2 Source Port and automatic conversion of V2 folders/modules into V3 services are prohibited |
| Decision preservation | Approved Product Scope and Domain/Data Ownership remain unchanged |
| Readiness limitation | This decision approves neither implementation nor production readiness |
| Affected Asset IDs | V2-AST-036 |
| ADR / OD impact | Applies ADR-V3-002, ADR-V3-006, ADR-V3-009 and ADR-V3-011; OD-017–OD-019 remain Open |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `A — Disposition دارایی V2-AST-036 برابر RETAIN` with read-only-map, authority, evidence-interpretation, traceability, prohibited-inference and readiness limitations |
| Date | 2026-10-23 |

### V3-002B-DEC-053 — Identity Trust logical and data ownership

| Field | Recorded value |
| --- | --- |
| Exact question | Which logical capability is authoritative for Principal Identity, credentials, authentication and session state? |
| Selected option | **A — Identity Trust Capability in Platform Core** |
| Identity ownership | Principal Identity, Credential/Authenticator Registration, External Identity Mapping, Authentication State, Session/Refresh/Revocation State and Token-Issuance Metadata |
| Preserved authorities | Tenant Management owns Tenant/Organization/Membership and Tenant Association; Entitlement owns Feature Eligibility; Resource-owning Domains own Business Facts and Resource/Action Authorization |
| Authority limitation | Identity determines only Principal and Session validity; Authentication, Token and Session grant no Membership, Entitlement or Business Authorization |
| Tenant-switch invariant | Tenant Switching requires valid Membership and re-evaluation of Tenant Context |
| Provider invariant | External Provider Assertion creates no internal Principal or Access without validation and approved Identity Mapping |
| Portal boundary | Portal Account Linkage remains owned by Customer Portal Domain according to V3-002B-DEC-044 |
| Operational-profile condition | Final Identity, Session and Revocation authority for Dedicated Sovereign remains local |
| Affected Asset IDs | V2-AST-004, V2-AST-008 and V2-AST-031 |
| Disposition impact | None; dispositions of V2-AST-004, V2-AST-008 and V2-AST-031 remain Pending |
| Explicit exclusions | IdP Selection, External Principal Model, Token Claims, Session/Refresh Model, Passkey Challenge Lifecycle, Tenant-switch Protocol, API/Event Contracts, Persistence, Migration and Service Topology remain Pending |
| Readiness limitation | This decision does not approve implementation readiness |
| ADR / OD impact | Applies ADR-V3-003–ADR-V3-005 and ADR-V3-012; OD-009–OD-012 remain Open |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `A — Identity Trust Capability ... مالک authoritative` with preserved-authority, validity-only, tenant-switch, provider-mapping, Portal and sovereign-local conditions |
| Date | 2026-10-23 |

### V3-002B-DEC-054 — Tenant Management logical and data ownership

| Field | Recorded value |
| --- | --- |
| Exact question | Which logical capability is authoritative for Tenant, Organization and Membership data? |
| Selected option | **A — Tenant Management Capability in Platform Core** |
| Tenant ownership | Tenant, Organization, Tenant Lifecycle, Organization/Tenant Membership, Membership Status, Principal-to-Tenant Association and Membership Role Assignment |
| Preserved authorities | Identity Trust owns Principal Identity and Authentication/Session Validity; Entitlement owns Feature Eligibility; Resource-owning Domains own Business Facts and Resource/Action Authorization |
| Authority limitation | Membership and Membership Role Assignment grant no Entitlement or Business Authorization |
| Tenant-context invariant | Tenant Context is constructed only from a valid Principal and active Membership and is revalidated at Trust Boundaries |
| Tenant-switch invariant | Tenant Switching requires valid destination Membership and creation of a new Context |
| Privileged-operation invariant | Cross-tenant and Platform-privileged Operations require limited identity, explicit scope, Authorization and Audit |
| Operational-profile condition | Final Tenant/Membership authority for Dedicated Sovereign remains local |
| Affected Asset IDs | Primary: V2-AST-005; contextual dependencies: V2-AST-004, V2-AST-010 and V2-AST-031 |
| Disposition impact | None; dispositions of related assets remain Pending |
| Explicit exclusions | Plan/Subscription Ownership, Membership Role/Policy Model, Invitation Model, Tenant Lifecycle State Machine, Placement/Cell Assignment, API/Event Contracts, Persistence, Migration and Service Topology remain Pending |
| Readiness limitation | This decision does not approve implementation readiness |
| ADR / OD impact | Applies ADR-V3-001–ADR-V3-005 and ADR-V3-010–ADR-V3-012; relevant OD-009–OD-015 and OD-023 remain Open |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `A — Tenant Management Capability ... مالک authoritative` with preserved-authority, membership limitation, context, switching, privileged-operation and sovereign-local conditions |
| Date | 2026-10-23 |

### V3-002B-DEC-055 — Identity / Tenant Foundation asset dispositions

| Field | Recorded value |
| --- | --- |
| Exact question | What are the final dispositions of V2-AST-004, V2-AST-005, V2-AST-008 and V2-AST-031 after Identity Trust and Tenant Management ownership approval? |
| Selected option | **A — REWRITE all four assets** |
| V2-AST-004 mapping | Rewrite Workload Identity, Tenant Context Validation and Signature/Expiry/Replay failure behavior; do not transfer the historical HMAC fixture or shared-secret mechanism |
| V2-AST-005 mapping | Rewrite Tenant/Organization/Membership according to DEC-054; do not inherit NestJS/Prisma/Redis/RabbitMQ layout or historical topology |
| V2-AST-008 mapping | Rewrite Fail-closed Configuration, Startup Validation and Secret/Trust Configuration semantics; Zod, Node Crypto and HMAC helpers are not V3 requirements |
| V2-AST-031 mapping | Rewrite valid Identity, Authentication, Session/Refresh/Revocation, Tenant Switching, Passkey and SSO behavior only under DEC-053/054 and independently approved future Requirements |
| Source rule | Direct V2 Source Port and one-to-one rewriting are prohibited |
| Technology limitation | No historical JWT/HMAC algorithm, Passkey mechanism, OIDC/SAML provider, Session/Cache design or Service Topology is approved |
| Security separation | Authentication, Membership, Entitlement and Resource Authorization remain independent; Dedicated Sovereign Identity/Tenant authority remains local |
| Explicit exclusions | IdP Selection, Workload Identity Protocol, Token Claims/Algorithms, Session/Refresh Model, Passkey Challenge Lifecycle, Tenant-switch Protocol, Membership Policy, API/Event Contracts, Persistence, Migration and Service Topology remain Pending |
| Readiness limitation | This decision approves neither implementation, runtime security nor production readiness |
| Affected Asset IDs | V2-AST-004, V2-AST-005, V2-AST-008 and V2-AST-031 |
| ADR / OD impact | Applies ADR-V3-001–ADR-V3-005 and ADR-V3-010–ADR-V3-012; OD-009–OD-012 remain Open |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `A — Disposition هر چهار دارایی ... برابر REWRITE` with per-asset mappings, prohibited mechanisms, security separation and readiness limitations |
| Date | 2026-10-23 |

### V3-002B-DEC-056 — Build and toolchain asset disposition

| Field | Recorded value |
| --- | --- |
| Exact question | What is the final disposition of V2-AST-001, the historical monorepo build/toolchain asset? |
| Selected option | **A — REWRITE** |
| Required rewrite | Reproduce deterministic builds, dependency locking, ordered Quality/Security Gates and independent Build, Version and Artifact ownership for every Service according to V3 architecture |
| Source and technology rule | Direct V2 Configuration Port is prohibited; Node, pnpm, Turbo, TypeScript, Jest and ESLint are not mandated for V3 |
| Boundary condition | Every Business Service retains an independent build, test, version and artifact boundary; this decision does not create a shared release unit |
| Explicit exclusions | Java/Build Tool, Repository Structure, CI, Versioning, Dependency Policy, Generated Code and Artifact Registry remain Pending |
| Readiness limitation | This decision approves neither implementation, build execution nor production readiness |
| Affected Asset ID | V2-AST-001 |
| ADR / OD impact | Applies ADR-V3-001, ADR-V3-011 and ADR-V3-012; OD-002–OD-004 and OD-020 remain Open |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `DEC-056: A — REWRITE` with build-boundary requirements, prohibited stack inheritance and preserved Open Decisions |
| Date | 2026-10-23 |

### V3-002B-DEC-057 — Historical GraphQL BFF disposition

| Field | Recorded value |
| --- | --- |
| Exact question | What is the final disposition of V2-AST-002, the historical GraphQL BFF and dependency-health composition asset? |
| Selected option | **A — NEEDS_REVIEW** |
| Evidence status | The historical GraphQL BFF is retained only as read-only Discovery Evidence |
| Technology limitation | GraphQL, Apollo, NestJS and the BFF pattern are not approved for V3 |
| Deferred decision | Query Composition must be reconsidered only after Public API Strategy, Client/API Boundary and Consumer Contracts are approved |
| Operational separation | Dependency Health Aggregation is independent of a BFF decision and must be handled under the approved Operational Core obligations |
| Ownership and access boundary | Any future BFF cannot own Business Facts or final Resource/Action Authorization and cannot use Direct Database Access |
| Explicit exclusions | Public API/BFF strategy, client composition, contracts and topology remain Pending |
| Readiness limitation | This decision approves neither implementation nor production readiness |
| Affected Asset ID | V2-AST-002 |
| ADR / OD impact | Applies ADR-V3-008, ADR-V3-009 and ADR-V3-012; OD-007 and OD-008 remain Open |
| Approval status | Owner-approved intentional deferral at this stage; final disposition was later recorded by V3-002B-DEC-083 |
| Approval evidence | Explicit owner response `DEC-057: A — NEEDS_REVIEW` with read-only evidence, technology non-selection, operational separation and boundary conditions |
| Date | 2026-10-23 |

### V3-002B-DEC-058 — Historical GraphQL query-complexity evidence disposition

| Field | Recorded value |
| --- | --- |
| Exact question | What is the final disposition of V2-AST-003, the historical GraphQL depth/complexity limiting behavior? |
| Selected option | **A — RETAIN** |
| Retention purpose | Preserve only read-only Historical Security/Performance Evidence |
| Source and technology rule | GraphQL AST code, historical depth/complexity thresholds and configuration are neither transferred nor approved |
| Conditional future use | If a technology with Composable Queries is selected, Complexity Budget, Resource Consumption Protection, Policy and Acceptance Criteria must be designed independently |
| Non-selection rule | If GraphQL is not selected, this asset creates no historical implementation obligation |
| Cross-cutting condition | General Resource Exhaustion controls remain an independent security and operational concern |
| Explicit exclusions | API technology, query limits, policy, tooling and acceptance criteria remain Pending |
| Readiness limitation | This decision approves neither implementation, runtime protection nor production readiness |
| Affected Asset ID | V2-AST-003 |
| ADR / OD impact | Applies ADR-V3-008 and ADR-V3-012; OD-007 and OD-020 remain Open |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `DEC-058: A — RETAIN` with read-only scope, technology non-selection and independent future-control requirements |
| Date | 2026-10-23 |

### V3-002B-DEC-059 — Synthetic TenantProbe fixture disposition

| Field | Recorded value |
| --- | --- |
| Exact question | What is the final disposition of V2-AST-006, the synthetic TenantProbe fixture? |
| Selected option | **A — RETIRE** |
| Retirement scope | TenantProbe must not become a V3 Product Capability, Domain Model, API, Persistence model or Service |
| Evidence preservation | Tenant Isolation, Missing/Invalid Context, Cross-tenant Denial and Fail-closed behavior remain read-only Historical Test Evidence for independent V3 Acceptance/Security Test Design |
| Source rule | Historical source remains read-only; retirement does not delete the legacy evidence |
| Explicit exclusions | No Test Framework, Domain Ownership, Contract, Schema or Service Topology is approved |
| Readiness limitation | This decision approves neither implementation nor production readiness |
| Affected Asset ID | V2-AST-006 |
| ADR / OD impact | Applies ADR-V3-003 and ADR-V3-012; no Open Decision is closed |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `DEC-059: A — RETIRE` with non-product treatment, preserved test scenarios and readiness limitations |
| Date | 2026-10-23 |

### V3-002B-DEC-060 — Historical contract/envelope evidence disposition

| Field | Recorded value |
| --- | --- |
| Exact question | What is the final disposition of V2-AST-007, the historical TypeScript contracts and Event Envelope asset? |
| Selected option | **A — RETAIN** |
| Retention purpose | Preserve only read-only Historical Contract Evidence |
| Candidate semantics | Ownership, Version, Tenant Provenance and Correlation may inform independent V3 contract design |
| Non-authoritative artifacts | TypeScript Types, TestPrincipal, TenantProbe DTO and the Historical Event Shape are not approved V3 contracts |
| Source rule | Direct Source/Contract Port and Code Generation from V2 are prohibited |
| Independent contract gate | Every V3 contract requires an explicit Owner, Versioning, Tenant Context, Authorization, Error/Delivery Semantics and Consumer Approval |
| Trust limitation | Tenant Provenance carried by an Event must not cause automatic trust of its Tenant Context; trust-boundary validation remains mandatory |
| Readiness limitation | This decision approves neither a contract implementation nor runtime/production readiness |
| Affected Asset ID | V2-AST-007 |
| ADR / OD impact | Applies ADR-V3-007, ADR-V3-008 and ADR-V3-012; OD-008 and OD-020 remain Open |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `DEC-060: A — RETAIN` with read-only scope, prohibited artifacts/porting and Tenant Provenance trust limitation |
| Date | 2026-10-23 |

### V3-002B-DEC-061 — Historical observability/security evidence disposition

| Field | Recorded value |
| --- | --- |
| Exact question | What is the final disposition of V2-AST-009, the historical logging redaction and trace-propagation package? |
| Selected option | **A — RETAIN** |
| Retention purpose | Preserve only read-only Historical Observability/Security Evidence |
| Candidate semantics | Sensitive-data Redaction and Correlation/Trace Propagation may inform independent V3 design |
| Non-authoritative artifacts | Pino, historical OpenTelemetry API, Field Names, Configuration and Implementation are neither approved nor transferred |
| Independent design gate | Sensitive-data Classification, Trace Trust, Tenant Context, Sampling, Cardinality, Retention, Export/Storage and evidence for Shared SaaS, Dedicated Managed and Dedicated Sovereign must be designed independently |
| Disclosure rule | Logs and traces must not expose Credentials, Tokens, Sensitive Business Facts or Cross-tenant Data |
| Authority boundary | Operational Core owns no Business Fact or universal Authorization; Dedicated Sovereign operational authority remains local |
| Readiness limitation | This decision approves no implementation, runtime correctness, security validation or production readiness |
| Affected Asset ID | V2-AST-009 |
| ADR / OD impact | Applies ADR-V3-010 and ADR-V3-012; OD-023 remains Open |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `DEC-061: A — RETAIN` with non-selection of historical tooling, disclosure controls, profile-specific evidence and sovereign-local authority |
| Date | 2026-10-23 |

### V3-002B-DEC-062 — Historical multi-tenant test-support disposition

| Field | Recorded value |
| --- | --- |
| Exact question | What is the final disposition of V2-AST-010, the historical two-tenant fixture support? |
| Selected option | **A — RETAIN** |
| Retention purpose | Preserve only read-only Historical Test-support Evidence |
| Candidate scenarios | At least two tenants, Positive/Negative Isolation Tests, Cross-tenant Denial and Missing/Invalid Context Validation may inform independent V3 Test Design |
| Source rule | TypeScript code, historical identifiers and Fixture Structure are not transferred |
| Test-data rule | Test data must be synthetic, isolated and contain no real sensitive data |
| Evidence limitation | Two tenants are a minimum baseline scenario, not complete proof of Tenant Isolation |
| Explicit exclusions | Test Framework, Fixture API, Data Provisioning, Cleanup Strategy and Test Environment remain Pending |
| Readiness limitation | This decision approves no test execution, runtime correctness or security validation |
| Affected Asset ID | V2-AST-010 |
| ADR / OD impact | Applies ADR-V3-003, ADR-V3-007 and ADR-V3-012; no Open Decision is closed |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `DEC-062: A — RETAIN` with scenario, test-data, non-transfer and evidence limitations |
| Date | 2026-10-23 |

### V3-002B-DEC-063 — Historical messaging-persistence model disposition

| Field | Recorded value |
| --- | --- |
| Exact question | What is the final disposition of V2-AST-011, the historical Prisma persistence models? |
| Selected option | **A — REWRITE** |
| Approved rewrite scope | Rewrite only valid Transactional Outbox, Idempotent Inbox and Processed-event Persistence behavior according to approved V3 ADRs |
| Excluded component | TenantProbe is retired under DEC-059 and must not be rewritten |
| Source rule | Prisma Schema, historical Table Shape, Index, Naming and Migration are not transferred |
| Ownership boundary | Every Service owns its Schema, Migration, Database Role and Transaction Boundary; Shared Schema and Cross-service Database Access are prohibited |
| Delivery invariants | Outbox preserves the owning Service transaction boundary; Inbox prevents duplicate message processing from producing duplicate effects |
| Explicit exclusions | Physical Schema, RLS Policy/Integration, Idempotency Key Design, Retention/Cleanup, Indexing, Reconciliation, Migration/Cutover and Persistence Tooling remain Pending |
| Readiness limitation | This decision approves neither implementation nor production readiness |
| Affected Asset ID | V2-AST-011 |
| ADR / OD impact | Applies ADR-V3-002, ADR-V3-003, ADR-V3-007 and ADR-V3-012; OD-013 and OD-014 remain Open |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `DEC-063: A — REWRITE` with component exclusion, service-owned persistence boundaries and pending physical design |
| Date | 2026-10-23 |

### V3-002B-DEC-064 — Historical RLS and tenant-isolation evidence disposition

| Field | Recorded value |
| --- | --- |
| Exact question | What is the final disposition of V2-AST-012, the historical foundation migration and RLS evidence? |
| Selected option | **A — RETAIN** |
| Retention purpose | Preserve only read-only Historical Tenant-isolation/RLS Evidence |
| Candidate controls | RLS for Tenant-owned Data in Shared SaaS, separate Read/Write Policies, Runtime Role without `BYPASSRLS`, and Non-bypass/Cross-tenant Denial tests may inform independent V3 design and validation |
| Source rule | Historical SQL, Policy Names, `current_setting` keys, Grants and Table Structures are neither transferred nor executed |
| Service obligation | Every Service independently designs its RLS/Tenant Context integration and must later prove it with a real connection, a Runtime Role without `BYPASSRLS`, and Missing/Invalid Context scenarios |
| Deferred design | Table Ownership, `FORCE ROW LEVEL SECURITY`, Connection Pool behavior and transaction-local Context remain future design/validation concerns |
| Explicit exclusions | Physical RLS integration, migration mechanism and validation evidence remain Pending |
| Readiness limitation | This decision approves neither Runtime Isolation nor Security Validation |
| Affected Asset ID | V2-AST-012 |
| ADR / OD impact | Applies ADR-V3-003, ADR-V3-007 and ADR-V3-012; OD-013 and OD-014 remain Open |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `DEC-064: A — RETAIN` with non-transfer rule, per-Service proof obligations and deferred RLS design concerns |
| Date | 2026-10-23 |

### V3-002B-DEC-065 — Database identity separation disposition

| Field | Recorded value |
| --- | --- |
| Exact question | What is the final disposition of V2-AST-013, the historical PostgreSQL role/bootstrap asset? |
| Selected option | **A — REWRITE** |
| Approved rewrite scope | Rewrite separation of Migration, Runtime and, where justified, Dispatcher/Worker Database Identities under Service-owned Persistence and Least Privilege |
| Source rule | Historical `init.sql`, Role Names, Passwords, Ownership and Public-schema Grants are not transferred |
| Runtime constraints | Runtime Role must not own Tables, must not have `BYPASSRLS`, and must receive only required privileges |
| Ownership boundary | Every Service has independent Roles and Credentials |
| Profile condition | Secret Provisioning, Rotation and Revocation must be designed independently for each Deployment Profile; Dedicated Sovereign authority remains local |
| Explicit exclusions | Secret Manager, Role/Grant Matrix, Bootstrap, Dispatcher Identity, Rotation and Privileged Access remain Pending |
| Readiness limitation | This decision approves no implementation, runtime security or production readiness |
| Affected Asset ID | V2-AST-013 |
| ADR / OD impact | Applies ADR-V3-007, ADR-V3-010 and ADR-V3-012; OD-012–OD-015 remain Open |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `DEC-065: A — REWRITE` with identity separation, least-privilege/RLS restrictions and profile-local secrets authority |
| Date | 2026-10-23 |

### V3-002B-DEC-066 — Historical cache behavior disposition

| Field | Recorded value |
| --- | --- |
| Exact question | What is the final disposition of V2-AST-014, the historical Redis cache behavior? |
| Selected option | **A — NEEDS_REVIEW** |
| Evidence status | Preserve only read-only Historical Discovery Evidence; Redis, Cache-aside and a general Cache capability are not approved for V3 |
| Approval gate | Cache may be reconsidered only for a specific Use Case with an owning Service and independently approved Requirements and Failure Policy |
| Candidate behavior only | Tenant/Permission/Version-scoped Keys, Invalidation Generation and Degraded Miss are candidates, not approved designs |
| Authority limitation | Cache is never authoritative for Business Facts, Membership, Entitlement or Authorization |
| Security failure rule | Cache failure must not fail open or permit use of expired/revoked authorization state |
| Explicit exclusions | Source of Truth, Freshness, TTL, Invalidation, Revocation Semantics, Sensitive-data Handling, Failure Policy and Deployment-profile behavior remain Pending |
| Fixture limitation | Retired TenantProbe creates no Cache requirement |
| Readiness limitation | This decision approves neither implementation nor runtime/security/production readiness |
| Affected Asset ID | V2-AST-014 |
| ADR / OD impact | Applies ADR-V3-003, ADR-V3-007 and ADR-V3-012; no Open Decision is closed |
| Approval status | Owner-approved intentional deferral at this stage; final disposition was later recorded by V3-002B-DEC-084 |
| Approval evidence | Explicit owner response `DEC-066: A — NEEDS_REVIEW` with use-case gate, non-authoritative cache boundaries and fail-closed/revocation conditions |
| Date | 2026-10-23 |

### V3-002B-DEC-067 — Transactional Outbox publisher disposition

| Field | Recorded value |
| --- | --- |
| Exact question | What is the final disposition of V2-AST-015, the historical Outbox publisher and dispatcher? |
| Selected option | **A — REWRITE** |
| Approved rewrite scope | Rewrite Atomic Transactional Outbox in the owning Service transaction, Broker Publisher Confirm, Mandatory Routing and Publication State recording only after valid confirmation |
| Confirmation limitation | Publisher Confirm is not Consumer Processing Success; an Unroutable Message must not be marked Published |
| Delivery semantics | At-least-once Delivery is accepted; end-to-end Exactly-once is not claimed |
| Consumer obligation | Consumer Idempotency and Service-owned Inbox/Processed-event State are mandatory |
| Source rule | Direct V2 Source Port is prohibited |
| Deferred design | Polling/Leasing, Concurrency, Ordering, Retry/Backoff, Dead-letter, Re-drive, Reconciliation, Idempotency Design, Event Contract Lifecycle and RabbitMQ Topology/Configuration remain Pending |
| Ownership and trust | An Event contains only Producing Service-owned Facts; Tenant Provenance is not trusted without valid boundary validation |
| Readiness limitation | This decision approves no implementation, runtime correctness or production readiness |
| Affected Asset ID | V2-AST-015 |
| ADR / OD impact | Applies ADR-V3-007, ADR-V3-008 and ADR-V3-012; OD-008, OD-019 and OD-020 remain Open |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `DEC-067: A — REWRITE` with transaction, confirmation, routing, delivery, idempotency, ownership and trust limitations |
| Date | 2026-10-23 |

### V3-002B-DEC-068 — Messaging consumer and durable Inbox disposition

| Field | Recorded value |
| --- | --- |
| Exact question | What is the final disposition of V2-AST-016, the historical Consumer, Inbox, retry and DLQ behavior? |
| Selected option | **A — REWRITE** |
| Approved rewrite scope | Rewrite Durable Inbox/Deduplication, ACK only after durable effect, Bounded Retry and controlled transfer of failed messages to DLQ according to approved V3 ADRs |
| Delivery and failure model | Consumer must tolerate At-least-once delivery, Duplicates, Reordering and Crash Boundaries |
| Transaction/idempotency condition | Business Effect and Inbox/Processed-event State must use a valid coordinated Transaction Boundary and Idempotency design |
| Trust condition | Tenant Provenance and Workload Context require validation before use |
| Source rule | Direct V2 Source Port is prohibited |
| Explicit exclusions | Retry Budget, Backoff, Error Classification, Inbox Transaction Boundary, DLQ/Queue Naming, Retention, Re-drive, Reconciliation, Ordering and Contract Versioning remain Pending |
| Readiness limitation | This decision approves neither runtime correctness nor production readiness |
| Affected Asset ID | V2-AST-016 |
| ADR / OD impact | Applies ADR-V3-007, ADR-V3-008 and ADR-V3-012; OD-008, OD-019 and OD-020 remain Open |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `DEC-068: A — REWRITE` with delivery, ACK, transaction/idempotency, context-validation and pending-design limitations |
| Date | 2026-10-23 |

### V3-002B-DEC-069 — Historical configuration/trust negative-test disposition

| Field | Recorded value |
| --- | --- |
| Exact question | What is the final disposition of V2-AST-017, the historical configuration and trust negative tests? |
| Selected option | **A — RETAIN** |
| Retention purpose | Preserve only read-only Historical Security Test Evidence |
| Candidate scenarios | Production Fixture Rejection, Signature Forgery/Expiry and other valid Failure Cases may inform independent V3 Test Design |
| Source and mechanism rule | Jest code, Fixture Values, Signature Format, Algorithm and historical Shared-secret Mechanism are neither transferred nor approved |
| Future coverage condition | Tests under the approved Identity/Workload Protocol must independently cover Missing/Invalid Context, Issuer/Audience where applicable, Expiry, Replay and Fail-closed Configuration |
| Explicit exclusions | Test Framework and Cryptographic/Identity Design remain Pending |
| Readiness limitation | This decision records no test execution and proves neither runtime security nor correctness |
| Affected Asset ID | V2-AST-017 |
| ADR / OD impact | Applies ADR-V3-005 and ADR-V3-012; relevant OD-009–OD-012 remain Open |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `DEC-069: A — RETAIN` with read-only scope, mechanism non-selection and future negative-test coverage |
| Date | 2026-10-23 |

### V3-002B-DEC-070 — Historical foundation regression-scenario catalog disposition

| Field | Recorded value |
| --- | --- |
| Exact question | What is the final disposition of V2-AST-018, the historical foundation integration-test catalog? |
| Selected option | **A — RETAIN** |
| Retention purpose | Preserve only a read-only Historical Regression Scenario Catalog |
| Selective-use gate | RLS, Tenant Isolation, Cache, BFF, Messaging Failure and Recovery scenarios may enter V3 Test Design only after alignment with approved ADRs, technologies, Requirements and Release Scope and mapping to a specific Requirement/Risk |
| Evidence limitation | Historical Passed Results create no Runtime or Security Evidence |
| Source/tooling rule | Direct Test Source Port and mandates for Testcontainers, Jest, NestJS, Redis or historical Docker Topology are prohibited |
| Conditional scenarios | BFF and Cache scenarios remain conditional on their independent approval |
| Explicit exclusions | Test Strategy, Tooling and Environment remain Pending |
| Readiness limitation | This decision approves no test execution, runtime correctness, security validation or production readiness |
| Affected Asset ID | V2-AST-018 |
| ADR / OD impact | Applies ADR-V3-003, ADR-V3-005, ADR-V3-007, ADR-V3-008 and ADR-V3-012; OD-020 remains Open |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `DEC-070: A — RETAIN` with selective scenario use, requirement/risk mapping, non-porting and evidence limitations |
| Date | 2026-10-23 |

### V3-002B-DEC-071 — Historical deployment fixture disposition

| Field | Recorded value |
| --- | --- |
| Exact question | What is the final disposition of V2-AST-019, the historical Dockerfile and Docker Compose deployment fixture? |
| Selected option | **A — REWRITE** |
| Approved rewrite scope | Rewrite only independent Build, Version, Artifact and Deployment requirements for every Service, explicit Dependency/Readiness Contracts, and verifiable deployment across Shared SaaS, Dedicated Managed and Dedicated Sovereign |
| Source and topology rule | Single Workspace Image, Node/pnpm Build, Compose Topology, Port Mapping, Volume Layout and historical Credentials are not transferred |
| Technology limitation | Docker/Container Runtime and Orchestrator are not selected by this decision |
| Co-deployment boundary | Co-deployment must not erode independent Build, Version or Artifact boundaries |
| Profile condition | Deployment, Secrets, Upgrade/Rollback, Recovery and Observability require independent design and validation for every Profile; Dedicated Sovereign authority remains local |
| Explicit exclusions | Orchestration, Secret Tooling, Image Registry, Network/Storage Layout and SLO/RTO/RPO remain Pending |
| Readiness limitation | This decision approves no implementation, runtime correctness or production readiness |
| Affected Asset ID | V2-AST-019 |
| ADR / OD impact | Applies ADR-V3-001, ADR-V3-010, ADR-V3-011 and ADR-V3-012; OD-012, OD-015 and OD-023 remain Open |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `DEC-071: A — REWRITE` with independent-service boundaries, technology non-selection, profile evidence and sovereign-local authority |
| Date | 2026-10-23 |

### V3-002B-DEC-072 — Historical governance CI evidence disposition

| Field | Recorded value |
| --- | --- |
| Exact question | What is the final disposition of V2-AST-020, the historical governance CI workflow? |
| Selected option | **A — RETAIN** |
| Retention purpose | Preserve only read-only Historical CI/Governance Evidence |
| Candidate controls | Least-privilege Workflow Permissions, non-persistent Credentials, Supply-chain Pinning and Governance/Boundary/Test/Build Gates may inform independent V3 CI design |
| Source/tooling rule | GitHub Actions workflow, pnpm, Python scripts, Steps and historical ordering are neither transferred nor approved |
| Gate requirements | Every Gate requires explicit Scope, Evidence, Failure Criteria and failure effect |
| Evidence limitation | Historical CI creates no execution evidence for V3 |
| Explicit exclusions | CI Provider, Pinning Policy, Artifact Signing/Attestation and Branch Protection remain Pending |
| Readiness limitation | This decision approves no pipeline execution, security validation or production readiness |
| Affected Asset ID | V2-AST-020 |
| ADR / OD impact | Applies ADR-V3-012; OD-020 remains Open |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `DEC-072: A — RETAIN` with least-privilege/pinning candidate controls, non-transfer rule and evidence limitations |
| Date | 2026-10-23 |

### V3-002B-DEC-073 — Independent repository/service CI disposition

| Field | Recorded value |
| --- | --- |
| Exact question | What is the final disposition of V2-AST-021, the historical foundation CI workflow? |
| Selected option | **A — REWRITE** |
| Approved rewrite scope | Rewrite Independent CI for every Repository/Service, Service-owned Build/Test/Security Gates and traceable Evidence/Artifacts according to V3 architecture |
| Source/tooling rule | GitHub Actions, pnpm, Docker prerequisite, Python scripts, Floating Action Tags and historical Workflow Shape are neither transferred nor approved |
| Independence boundary | CI for one Repository cannot require the Build or Release of another independent Repository/Service |
| Shared-control condition | Shared Governance Controls and Contract Compatibility Checks may be considered only while preserving independent Build, Version, Artifact and Release boundaries |
| Supply-chain condition | Dependencies/Actions require immutable pinning under a future approved Policy; Credentials must be least-privilege and short-lived |
| Explicit exclusions | CI Provider, Trigger/Branch Policy, Runner Isolation, Cache, Signing/Attestation, Secret Integration and Release Promotion remain Pending |
| Readiness limitation | This decision approves no pipeline execution, security validation or production readiness |
| Affected Asset ID | V2-AST-021 |
| ADR / OD impact | Applies ADR-V3-001, ADR-V3-010 and ADR-V3-012; OD-020 remains Open |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `DEC-073: A — REWRITE` with CI independence, shared-control boundary, immutable pinning and short-lived credential conditions |
| Date | 2026-10-23 |

### V3-002B-DEC-074 — Historical governance manifest/validator disposition

| Field | Recorded value |
| --- | --- |
| Exact question | What is the final disposition of V2-AST-022, the historical governance manifest, validator and tests? |
| Selected option | **A — NEEDS_REVIEW** |
| Evidence status | Preserve only read-only Historical Governance Discovery Evidence |
| Review rule | V2 Contexts, Skills, Gates, Statuses and Invariants require item-by-item comparison with the V3 Governance Baseline and approved ADRs; none transfer automatically |
| Non-authoritative artifacts | `manifest.json`, Python Validator, Test Code and historical Document-integrity Rules are not approved V3 policy or tooling |
| Approval gate | Every candidate Invariant requires explicit Authority, Scope, Failure Semantics and Approval |
| Existing authority | Governance Controls already approved for V3 remain valid and are not changed by this disposition |
| Explicit exclusions | Governance Schema, Validator Tooling, Enforcement Location and CI Integration remain Pending |
| Readiness limitation | No new Gate is treated as Passed and no implementation/runtime readiness is approved |
| Affected Asset ID | V2-AST-022 |
| ADR / OD impact | Applies ADR-V3-002, ADR-V3-011 and ADR-V3-012; no Open Decision is closed |
| Approval status | Owner-approved intentional deferral at this stage; final disposition was later recorded by V3-002B-DEC-085 |
| Approval evidence | Explicit owner response `DEC-074: A — NEEDS_REVIEW` with item-level comparison, non-authority, existing-governance preservation and no-passed-gate conditions |
| Date | 2026-10-23 |

### V3-002B-DEC-075 — Historical architecture-boundary checker disposition

| Field | Recorded value |
| --- | --- |
| Exact question | What is the final disposition of V2-AST-023, the historical boundary policy/checker and adversarial fixtures? |
| Selected option | **A — RETAIN** |
| Retention purpose | Preserve only read-only Historical Boundary-policy/Adversarial-test Evidence |
| Candidate scenarios | Cross-service Implementation Import, BFF/Service Private Database Access, Dynamic Import and Re-export Bypass may inform independent V3 Boundary Enforcement design |
| Source/tooling rule | Node, Dependency Cruiser, Rule Configuration and Fixture Code are not transferred |
| V3 alignment condition | Future enforcement must support Java/Build Graph and independent Repositories and distinguish Shared Versioned Contracts from Shared Business Implementation |
| Coverage limitation | A Dependency Graph alone cannot disprove Cross-service Database Access or Runtime boundary violations |
| Explicit exclusions | Tooling, Rule Schema, Generated-code Handling, CI Integration and Failure Policy remain Pending |
| Readiness limitation | The historical checker proves neither V3 Boundary Enforcement nor Security Validation |
| Affected Asset ID | V2-AST-023 |
| ADR / OD impact | Applies ADR-V3-001, ADR-V3-002, ADR-V3-011 and ADR-V3-012; OD-004 and OD-020 remain Open |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `DEC-075: A — RETAIN` with adversarial scenarios, V3 graph/repository alignment and static/runtime coverage limitations |
| Date | 2026-10-23 |

### V3-002B-DEC-076 — V2-stage bootstrap/report tooling disposition

| Field | Recorded value |
| --- | --- |
| Exact question | What is the final disposition of V2-AST-024, the historical bootstrap, deferred-report and typecheck-bootstrap tooling? |
| Selected option | **A — RETIRE** |
| Retirement scope | Bootstrap Scripts, Deferred-report Tooling and Typecheck Bootstrap are specific to V2 and must not be transferred or rewritten for V3 |
| Evidence preservation | Valid findings remain recorded only in the Inventory and Owner Review Record |
| Source handling | Historical Source remains read-only; no physical deletion is performed |
| Authority limitation | The asset creates no Product Capability, Governance Gate, Build Requirement or Tooling Authority |
| Governance limitation | Retirement neither cancels approved V3 Governance Controls nor treats any Gate, Build, Test or Validation as Passed |
| Readiness limitation | This decision approves no implementation or runtime/production readiness |
| Affected Asset ID | V2-AST-024 |
| ADR / OD impact | Applies ADR-V3-012; no Open Decision is closed |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `DEC-076: A — RETIRE` with non-transfer, read-only preservation, non-authority and no-passed-gate conditions |
| Date | 2026-10-23 |

### V3-002B-DEC-077 — Historical architecture/governance documents disposition

| Field | Recorded value |
| --- | --- |
| Exact question | What is the final disposition of V2-AST-025, the historical V2 architecture and governance documents? |
| Selected option | **A — NEEDS_REVIEW** |
| Evidence status | Preserve only read-only Historical Architecture/Governance Provenance and Secondary Evidence |
| Reconciliation rule | Every Candidate Concept requires individual comparison with Source Evidence, Governance Baseline, approved V3 ADRs, Release Scope and Owner Decisions |
| Authority limitation | Historical ADRs, Statuses, Boundaries, Review Results and Readiness Claims are not V3 authority and close no Open Decision |
| Evidence-quality rule | Contradictions, incomplete evidence and obsolete claims must be recorded explicitly |
| Future classification | Each Candidate must later be classified as covered in V3, requiring an independent decision, or non-transferable; classification itself creates no Approval |
| Explicit exclusions | Complete reconciliation and the final Asset disposition were Pending at this stage; final disposition was later recorded by V3-002B-DEC-086 while Concept Reconciliation remained Pending |
| Readiness limitation | This decision approves no implementation, runtime correctness, security validation or production readiness |
| Affected Asset ID | V2-AST-025 |
| ADR / OD impact | All approved V3 ADRs remain authoritative; all relevant Open Decisions remain Open |
| Approval status | Owner-approved intentional deferral at this stage; final disposition was later recorded by V3-002B-DEC-086 |
| Approval evidence | Explicit owner response `DEC-077: A — NEEDS_REVIEW` with provenance-only scope, individual reconciliation, future classification and non-approval conditions |
| Date | 2026-10-23 |

### V3-002B-DEC-078 — Historical V2 ADR corpus disposition

| Field | Recorded value |
| --- | --- |
| Exact question | What is the final disposition of V2-AST-026, the eleven accepted and one proposed historical V2 ADRs? |
| Selected option | **A — NEEDS_REVIEW** |
| Evidence status | Preserve only read-only Historical Decision Provenance |
| Non-transfer rule | Historical IDs, Statuses and Approvals do not transfer to V3 |
| Reconciliation rule | Every Decision Concept requires independent comparison with Source Evidence, approved V3 ADRs, Governance Baseline, Owner Decisions and Open Decisions |
| Classification | Aligned concepts become Covered Evidence; unresolved concepts become Requires Independent Decision; conflicting concepts become Non-transferable; insufficient evidence is recorded separately |
| Approval limitation | Mapping creates no Approval or Scope Change |
| Authority limitation | No V2 ADR changes or closes any V3 ADR or OD-002–OD-020 |
| Explicit exclusions | Complete reconciliation and final Asset disposition were Pending at this stage; final disposition was later recorded by V3-002B-DEC-087 while Concept Reconciliation remained Pending |
| Readiness limitation | This decision approves no implementation or runtime/security/production readiness |
| Affected Asset ID | V2-AST-026 |
| ADR / OD impact | ADR-V3-001–ADR-V3-012 remain authoritative; OD-002–OD-020 remain Open where applicable |
| Approval status | Owner-approved intentional deferral at this stage; final disposition was later recorded by V3-002B-DEC-087 |
| Approval evidence | Explicit owner response `DEC-078: A — NEEDS_REVIEW` with provenance-only scope, classification, non-approval and preserved V3 authority |
| Date | 2026-10-23 |

### V3-002B-DEC-079 — Historical engineering/quality documentation disposition

| Field | Recorded value |
| --- | --- |
| Exact question | What is the final disposition of V2-AST-027, the historical engineering patterns, quality gates and roadmap? |
| Selected option | **A — NEEDS_REVIEW** |
| Evidence status | Preserve only read-only Historical Engineering/Quality Evidence |
| Candidate use | Engineering Patterns, Acceptance Scenarios and Evidence Vocabulary may inform future independent design only after alignment with V3 Architecture, Technology, Release Scope, Requirements and Risks |
| Non-transfer rule | Historical V2 Stack, Product Assumptions, Gate Definitions, Roadmap, Phase Ordering and Implementation Priorities are neither transferred nor approved |
| Future gate requirements | Every future Gate requires independent Scope, Deployment Profile, Evidence, Owner and Failure Criteria |
| Evidence/readiness limitation | Historical Passed Status creates no Runtime, Security or Readiness Evidence; Architecture, Implementation and Production Readiness remain separate |
| Explicit exclusions | Test Strategy, Coverage, Tooling, CI Integration, Performance/Security Budgets and Operational Objectives remain Pending |
| Affected Asset ID | V2-AST-027 |
| ADR / OD impact | Applies ADR-V3-012; OD-020 and OD-023 remain Open |
| Approval status | Owner-approved intentional deferral at this stage; final disposition was later recorded by V3-002B-DEC-088 while reconciliation remained Pending |
| Approval evidence | Explicit owner response `DEC-079: A — NEEDS_REVIEW` with read-only scope, non-transfer of gates/roadmap/priorities and evidence/readiness separation |
| Date | 2026-10-23 |

### V3-002B-DEC-080 — Historical V2 agent-skill disposition

| Field | Recorded value |
| --- | --- |
| Exact question | What is the final disposition of V2-AST-028, the sixteen historical V2/NestJS agent skills? |
| Selected option | **A — RETIRE** |
| Retirement scope | Historical V2/NestJS Skills must not be transferred, installed, executed or directly rewritten for V3 |
| Source handling | Historical sources remain read-only Evidence and are not physically deleted |
| Authority limitation | These Skills create no Governance Authority, Coding Standard, Workflow Requirement or Tooling Selection for V3 |
| Current authority | Only authorized and synchronized V3 Skills under the current Governance Baseline are valid |
| Governance limitation | Retirement neither cancels an approved V3 Skill/Governance Control/Gate nor treats any Gate as Passed |
| Readiness limitation | This decision approves no implementation, validation or runtime/production readiness |
| Affected Asset ID | V2-AST-028 |
| ADR / OD impact | The current Governance Baseline remains authoritative; no Open Decision is closed |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `DEC-080: A — RETIRE` with non-transfer/execution, read-only preservation and V3 authority conditions |
| Date | 2026-10-23 |

### V3-002B-DEC-081 — Historical skill-audit provenance disposition

| Field | Recorded value |
| --- | --- |
| Exact question | What is the final disposition of V2-AST-029, the historical skill-audit inventory, coverage, dry runs and validation reports? |
| Selected option | **A — RETAIN** |
| Retention purpose | Preserve only read-only Historical Audit Provenance |
| Evidence meaning | Inventory, Coverage, Dry-run, Provenance and Validation Reports document only what V2 reviewed or claimed |
| Evidence limitation | Historical Pass, Coverage and Validation Status create no V3 Governance, Runtime, Security or Readiness Evidence |
| Conflict handling | Conflicts with Source Evidence, V3 Governance or Owner Decisions must be recorded explicitly |
| Source/tooling rule | Historical Script, Validator, Coverage Model and Gate Definition are neither transferred nor approved |
| Future validation requirements | Every future Validation requires independent Scope, Tool, Inputs, Expected Result, Actual Result and Evidence |
| Readiness limitation | This decision approves no Validation or readiness gate |
| Affected Asset ID | V2-AST-029 |
| ADR / OD impact | Applies ADR-V3-012; no Open Decision is closed |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `DEC-081: A — RETAIN` with provenance-only meaning, non-transfer of tooling and independent future-validation evidence requirements |
| Date | 2026-10-23 |

### V3-002B-DEC-082 — Bounded historical evidence-index disposition

| Field | Recorded value |
| --- | --- |
| Exact question | What is the final disposition of V2-AST-030, the 106-entry legacy evidence index and pinned Git provenance? |
| Selected option | **A — RETAIN** |
| Retention purpose | Preserve only a read-only Bounded Historical Evidence Index |
| Preserved provenance | `legacy-evidence.json`, paths, SHA-256 values and pinned Git Commit/Tree identify the limited set of 106 historical evidence items |
| Historical result meaning | The recorded 106/106 result means only that the indexed sample contents matched the pinned source during the historical review |
| Evidence limitations | The result proves neither completeness of the full V2 Inventory nor Behavioral Correctness, Security, Quality, Runtime Correctness or Architecture/Implementation/Production Readiness |
| Authority limitation | A Hash Match creates no Requirement, Scope, Ownership, Architecture Decision, Approval or Passed Gate |
| Coverage limitation | The Index is not a Full Repository Manifest |
| Future-use condition | Any future use of an item requires preserved Commit/Tree Provenance and independent semantic review within an authorized Task |
| Source handling | Historical Sources remain read-only |
| Execution limitation | No Hash Verification, Validator, Build, Test, CI or Runtime Execution was performed for this decision |
| Affected Asset ID | V2-AST-030 |
| ADR / OD impact | Applies ADR-V3-012; no Open Decision is closed |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `DEC-082: A — RETAIN` with bounded-provenance meaning, hash/coverage/authority limitations and no-execution condition |
| Date | 2026-10-23 |

### V3-002B-DEC-083 — Historical API-composition evidence disposition

| Field | Recorded value |
| --- | --- |
| Exact question | What is the final disposition of V2-AST-002, the historical GraphQL BFF and dependency-health composition asset? |
| Selected option | **A — RETAIN** |
| Retention purpose | Preserve only read-only Historical API-composition/Discovery Evidence |
| Technology limitation | GraphQL, Apollo, NestJS and the BFF pattern are not approved for V3; Query Composition is Candidate Evidence only |
| Boundary rule | A future BFF owns neither Business Facts nor final Authorization and must not use Direct Database Access |
| Operational separation | Dependency Health Aggregation remains independent within the approved Operational Core |
| Pending work | Public API Strategy, Client/API Boundary and Consumer Contracts require independent decisions |
| Affected Asset ID | V2-AST-002 |
| ADR / OD impact | Applies ADR-V3-008, ADR-V3-009 and ADR-V3-012; OD-007 and OD-008 remain Open |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `DEC-083: A — RETAIN` with evidence-only scope, technology non-selection and boundary conditions |
| Date | 2026-10-23 |

### V3-002B-DEC-084 — Historical Cache/security evidence disposition

| Field | Recorded value |
| --- | --- |
| Exact question | What is the final disposition of V2-AST-014, the historical Redis cache behavior? |
| Selected option | **A — RETAIN** |
| Retention purpose | Preserve only read-only Historical Cache/Security Evidence |
| Technology limitation | Redis, Cache-aside and a general Cache capability are not approved for V3 |
| Candidate behaviors | Tenant/Permission/Version-scoped Keys, Invalidation and Degraded Miss remain Candidate Behavior only |
| Authority limitation | Cache is not authoritative for Business Facts, Membership, Entitlement or Authorization |
| Safety rule | Failure or revocation must not cause Fail-open behavior or reuse of invalid authority |
| Future-use condition | Any use requires an independently approved Use Case, Owner, Requirements, Freshness rules and Failure Policy |
| Affected Asset ID | V2-AST-014 |
| ADR / OD impact | Applies ADR-V3-003, ADR-V3-007 and ADR-V3-012; no Open Decision is closed |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `DEC-084: A — RETAIN` with evidence-only scope, non-authority and fail-closed conditions |
| Date | 2026-10-23 |

### V3-002B-DEC-085 — Historical governance discovery/provenance disposition

| Field | Recorded value |
| --- | --- |
| Exact question | What is the final disposition of V2-AST-022, the historical governance manifest, validator and tests? |
| Selected option | **A — RETAIN** |
| Retention purpose | Preserve only read-only Historical Governance Discovery/Provenance |
| Authority limitation | Historical Contexts, Skills, Gates, Statuses and Invariants create no V3 authority |
| Non-transfer rule | The historical Manifest, Python Validator, Tests and Rules are not transferred or executed |
| Governance continuity | Approved V3 Governance Controls remain valid and unchanged |
| Future invariant condition | Each new Invariant requires independent Authority, Scope, Failure Semantics and Approval |
| Readiness limitation | No Gate, Validation or Readiness state is approved by this retention decision |
| Affected Asset ID | V2-AST-022 |
| ADR / OD impact | Applies ADR-V3-002, ADR-V3-011 and ADR-V3-012; no Open Decision is closed |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `DEC-085: A — RETAIN` with provenance-only scope, non-transfer and no-passed-gate conditions |
| Date | 2026-10-23 |

### V3-002B-DEC-086 — Historical architecture/governance provenance disposition

| Field | Recorded value |
| --- | --- |
| Exact question | What is the final disposition of V2-AST-025, the historical V2 architecture and governance documents? |
| Selected option | **A — RETAIN** |
| Retention purpose | Preserve only read-only Historical Architecture/Governance Provenance and Secondary Evidence |
| Content limitation | RETAIN does not approve the content, status or claims of the historical documents |
| Reconciliation rule | Candidate Concepts require independent comparison with Source Evidence, the Governance Baseline, V3 ADRs, Release Scope and Owner Decisions |
| Recording rule | Conflicts, incomplete evidence and obsolete claims must be recorded explicitly |
| Authority limitation | Historical Status or Readiness creates no V3 authority or Passed Gate |
| Pending work | Concept Reconciliation remains independent and Open Decisions remain Open |
| Affected Asset ID | V2-AST-025 |
| ADR / OD impact | All approved V3 ADRs remain authoritative; all relevant Open Decisions remain Open |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `DEC-086: A — RETAIN` with provenance-only scope, non-approval and independent-reconciliation conditions |
| Date | 2026-10-23 |

### V3-002B-DEC-087 — Historical decision provenance disposition

| Field | Recorded value |
| --- | --- |
| Exact question | What is the final disposition of V2-AST-026, the eleven accepted and one proposed historical V2 ADRs? |
| Selected option | **A — RETAIN** |
| Retention purpose | Preserve only read-only Historical Decision Provenance |
| Non-transfer rule | Historical ADR IDs, Accepted/Proposed Statuses and Approvals do not transfer to V3 |
| Reconciliation classes | Each concept must be independently recorded as Covered Evidence, Requires Independent Decision, Non-transferable or Insufficient Evidence |
| Approval limitation | Mapping creates no Approval or Scope Change |
| Authority protection | V2 ADRs do not alter V3 ADRs or close OD-002 through OD-020 |
| Completion limitation | Final Asset disposition does not mean Concept Reconciliation is complete |
| Affected Asset ID | V2-AST-026 |
| ADR / OD impact | ADR-V3-001–ADR-V3-012 remain authoritative; OD-002–OD-020 remain Open where applicable |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `DEC-087: A — RETAIN` with provenance-only scope, classification and non-approval conditions |
| Date | 2026-10-23 |

### V3-002B-DEC-088 — Historical engineering/quality evidence disposition

| Field | Recorded value |
| --- | --- |
| Exact question | What is the final disposition of V2-AST-027, the historical engineering patterns, quality gates and roadmap? |
| Selected option | **A — RETAIN** |
| Retention purpose | Preserve only read-only Historical Engineering/Quality Evidence |
| Candidate use | Patterns, Acceptance Scenarios and Evidence Vocabulary may inform future independent design only |
| Non-transfer rule | The V2 Stack, Product Assumptions, Gate Definitions, Roadmap, Phase Ordering and Implementation Priorities do not transfer |
| Evidence limitation | Historical Passed Status creates no Runtime, Security or Readiness Evidence |
| Future-gate condition | Every V3 Gate requires independent Scope, Deployment Profile, Owner, Evidence and Failure Criteria |
| Affected Asset ID | V2-AST-027 |
| ADR / OD impact | Applies ADR-V3-012; OD-020 and OD-023 remain Open |
| Approval status | Approved by project owner with the stated limitations |
| Approval evidence | Explicit owner response `DEC-088: A — RETAIN` with evidence-only scope, non-transfer and readiness-separation conditions |
| Date | 2026-10-23 |

### Approved FIRST_RELEASE capability definition — Customer/CRM core

| Concern | Current approved or pending record |
| --- | --- |
| Business objective | Maintain authoritative tenant-scoped customer company/person and contact information as the minimum CRM product nucleus |
| Minimum workflows | Create, view, update and relate company/person/contact records; exact lifecycle, merge and deletion rules remain Pending |
| Major user roles | Tenant CRM users and tenant administrators; exact role catalog remains Pending |
| Critical invariants | Tenant isolation; stable identity; owner authorization; no cross-service database writes; explicit relationship integrity; auditable sensitive changes |
| External dependencies | Linka/External Registry is LATER_RELEASE; Customer Core must support internal creation, editing and search without a Provider dependency |
| Security/tenant boundaries | Validated Tenant Context, active membership/entitlement where applicable, Customer-owned resource/action authorization and RLS for applicable Shared SaaS tables |
| Minimum acceptance criteria | Versioned contract; service-owned persistence/migrations; cross-tenant negative cases; authorization denials; three-profile compatibility; evidence remains to be defined and produced later |
| Open design questions | Aggregate boundaries, identifiers, duplicate/merge rules, retention/deletion, API shape, migration rules and deployment boundary |

### Approved FIRST_RELEASE capability definition — Sales core

| Concern | Current approved or pending record |
| --- | --- |
| Business objective | Track tenant-scoped sales opportunities through a pipeline while referencing Customer-owned parties through explicit contracts |
| Minimum workflows | Create/view/update an opportunity, record amount and currency without mandatory Product Catalog dependency, and move it through an approved pipeline lifecycle; exact stages and transition rules remain Pending |
| Major user roles | Tenant sales users and sales administrators; exact role catalog remains Pending |
| Critical invariants | Sales owns opportunity state; Customer references do not create shared writes; tenant isolation and owning-domain authorization apply |
| External dependencies | Versioned Customer Domain contract; Product Catalog, Lead Source, Pain Point and Use Case are LATER_RELEASE and cannot be mandatory FIRST_RELEASE dependencies |
| Security/tenant boundaries | Validated Tenant Context, applicable membership/entitlement and Sales-owned resource/action authorization |
| Minimum acceptance criteria | Versioned Customer integration; service-owned persistence; valid/invalid transition cases; cross-tenant and authorization denials; three-profile compatibility |
| Open design questions | Opportunity aggregate, pipeline stages/transitions, Line Item design, Pricing rules, Currency rules, API, migration and topology |

### Approved FIRST_RELEASE capability definition — Notification Core + In-App

| Concern | Current approved or pending record |
| --- | --- |
| Business objective | Provide tenant-scoped, traceable in-product notifications for approved domain events without requiring an external channel provider |
| Minimum workflows | Register/process an owned event, evaluate approved base rules/templates, create a deduplicated delivery, expose In-App state and record retry/audit lifecycle |
| Major user roles | Tenant users receiving In-App notifications and authorized tenant administrators managing allowed templates/rules; exact permissions remain Pending |
| Critical invariants | Tenant isolation; idempotent event/delivery handling; deduplication; explicit lifecycle; bounded retry; safe audit; producer remains owner of the originating business fact |
| External dependencies | Versioned domain event/API contracts; no Email/SMS/Push provider is required for FIRST_RELEASE |
| Security/tenant boundaries | Validated tenant provenance, Notification-owned authorization for its resources, minimized payloads and profile-local operation where required |
| Minimum acceptance criteria | Duplicate/retry/failure scenarios; cross-tenant denial; safe template/rule administration; In-App lifecycle; independent evidence for all three production profiles |
| Open design questions | API/event contracts, scheduling, retry budgets, retention, provider model, topology and detailed rule language |

### Approved FIRST_RELEASE capability definition — Customer Requests core

| Concern | Current approved or pending record |
| --- | --- |
| Business objective | Track an internal, tenant-scoped customer request through a minimal observable lifecycle without mandatory Portal or workflow-engine dependencies |
| Minimum workflows | Create internally, reference Customer by contract, view/track, assign work responsibility, transition through a base lifecycle and append Status History |
| Major user roles | Authorized internal request creators, assignees and viewers; exact role/permission catalog remains Pending |
| Critical invariants | Customer reference is contract-only; status history is append-oriented; assignment grants no membership or operation authority; every transition is owner-authorized and tenant-scoped |
| External dependencies | Versioned Customer contract only; Portal, Workflow Engine, Task, Opportunity and Technical Document automation are not required |
| Security/tenant boundaries | Validated Tenant Context, explicit membership/entitlement where applicable, owning-domain resource/action authorization and non-enumerating cross-tenant access |
| Minimum acceptance criteria | Valid/invalid transition cases; assignment without authority escalation; cross-tenant denial; history integrity; operation without Portal/Workflow Engine; all-profile compatibility |
| Open design questions | State machine, assignment semantics, API contracts, retention, migration and topology |

### Approved FIRST_RELEASE capability definition — Audit Core

| Concern | Current approved or pending record |
| --- | --- |
| Business objective | Preserve tenant- and platform-scoped evidence for security, administrative and privileged activity without taking ownership of the producing domain's Business Fact |
| Minimum workflows | Append an Audit event with Actor/Action/Target/Outcome/Correlation context, distinguish Tenant and Platform scope, support authorized viewing, apply integrity controls and enforce a base Retention Policy |
| Major user roles | Authorized tenant and platform audit viewers and privileged operators; exact role/permission catalog remains Pending |
| Critical invariants | Append-oriented records; explicit tenant/platform scope; integrity protection; authorized access; required retention and recovery; no direct access to private domain databases |
| External dependencies | Versioned producer contracts; Export, Archive Automation and advanced UI/Reporting are not FIRST_RELEASE dependencies |
| Security/tenant boundaries | Producing Domain retains its Business Fact and action authorization; Audit access is separately authorized; Dedicated Sovereign Audit authority remains local |
| Minimum acceptance criteria | Required event-context fields, append/integrity controls, tenant/platform isolation, authorized-view denials, retention/recovery evidence and independent compatibility evidence for all three profiles |
| Open design questions | Event Schema, Retention Duration, Archive Storage, API, persistence, migration and topology |

### Approved FIRST_RELEASE capability definition — Entitlement Core

| Concern | Current approved or pending record |
| --- | --- |
| Business objective | Determine whether a Tenant/Organization is eligible to use a capability without granting access to any specific business resource |
| Minimum workflows | Evaluate approved Feature Assignment and Plan/Subscription inputs and return a traceable eligibility result, reason and validity time |
| Major user roles | Tenant/organization consumers of eligibility decisions and authorized platform policy administrators; exact role catalog remains Pending |
| Critical invariants | Eligibility, Tenant Membership and Resource/Action Authorization are separate checks; Entitlement never grants a domain operation |
| External dependencies | Approved Feature Assignment and Plan/Subscription inputs; FIRST_RELEASE Sovereign evaluation cannot require a central service |
| Security/tenant boundaries | Tenant/Organization scope must be explicit and validated; owning domain must independently authorize every business-resource operation |
| Minimum acceptance criteria | Eligible/ineligible/expired decision cases; reason and validity traceability; cross-tenant denial; local Dedicated Sovereign evaluation; all-profile compatibility evidence |
| Open design questions | Plan/Subscription-fact ownership, Billing, Pricing, Quota, Policy Model, API, persistence, migration, disposition and topology |

### Approved FIRST_RELEASE capability definition — Quota Core

| Concern | Current approved or pending record |
| --- | --- |
| Business objective | Enforce approved tenant/organization capability consumption limits without granting eligibility, membership or access to business resources |
| Minimum workflows | Resolve an effective Limit, record Usage, atomically Reserve/Commit/Release consumption, reconcile state and return traceable Reason/Period/Correlation results |
| Major user roles | Capability consumers and authorized quota/policy operators; exact role and administration model remain Pending |
| Critical invariants | Reservation lifecycle is atomic and idempotent; Usage is reconcilable; Quota, Entitlement, Membership and Resource/Action Authorization are separate checks |
| External dependencies | Only capabilities with independently approved Quota requirements may integrate; FIRST_RELEASE Sovereign control cannot require a central service |
| Security/tenant boundaries | Tenant/Organization and Capability scope must be explicit and validated; owning domain independently authorizes every business-resource operation |
| Minimum acceptance criteria | Limit allow/deny, duplicate reservation, commit/release, concurrency and reconciliation cases; traceability; cross-tenant denial; local Dedicated Sovereign control; all-profile compatibility evidence |
| Open design questions | Policy/Limit Model, Plan/Subscription Ownership, Reset/Scheduling, API, persistence, migration, disposition and topology |

### Approved FIRST_RELEASE capability definition — Reporting Core

| Concern | Current approved or pending record |
| --- | --- |
| Business objective | Provide deterministic, tenant-scoped visibility required for approved FIRST_RELEASE capabilities without bypassing source-domain ownership or authorization |
| Minimum workflows | Run an independently approved Report Set, apply base filters and present results to an authorized viewer |
| Major user roles | Authorized tenant report viewers and administrators; each Report Set's exact roles remain Pending until its requirements are approved |
| Critical invariants | Deterministic results; explicit tenant scope; independent Report Set requirements/authorization; no cross-service database access; no implicit AI behavior |
| External dependencies | Versioned source-domain API/Event Contracts or authorized Projections only |
| Security/tenant boundaries | Report viewing is separately authorized; source-domain sharing constraints remain binding; cross-tenant data exposure is prohibited |
| Minimum acceptance criteria | Deterministic results, filter behavior, authorized/denied viewing, cross-tenant denial, stale/projection handling and all-profile compatibility evidence for each approved Report Set |
| Open design questions | Final Report Sets, projection design/freshness, API, retention, persistence, migration, disposition and topology |

### Approved FIRST_RELEASE capability definition — Work Core

| Concern | Current approved or pending record |
| --- | --- |
| Business objective | Track tenant-scoped work as base Tasks without requiring advanced collaboration or workflow automation |
| Minimum workflows | Create, view and edit a Task; assign responsibility; set Status and Due Date; add manual contract-based links to authorized Customer, Opportunity or Customer Request resources |
| Major user roles | Authorized task creators, assignees and viewers; exact roles and permissions remain Pending |
| Critical invariants | Assignment grants no Membership, Entitlement or Authorization; linked-resource access remains owner-authorized; links do not transfer Business Facts |
| External dependencies | Versioned authorized contracts with Customer, Sales and Customer Request domains; deferred Work capabilities are not FIRST_RELEASE dependencies |
| Security/tenant boundaries | Validated Tenant Context, explicit Work resource authorization and independent authorization for every linked resource |
| Minimum acceptance criteria | Create/view/edit/status/due-date behavior; assignment without privilege escalation; authorized/denied manual links; cross-tenant denial; operation without deferred features; all-profile compatibility evidence |
| Open design questions | Task State Machine, link semantics, API/event contracts, persistence, migration, disposition and topology |

### Approved FIRST_RELEASE capability definition — File/Attachment Core

| Concern | Current approved or pending record |
| --- | --- |
| Business objective | Provide tenant-scoped file handling and controlled attachment to approved FIRST_RELEASE resources without treating a File ID or Attachment Link as an access grant |
| Minimum workflows | Record File Metadata; validate and upload content; authorize and download content; apply a Basic File Lifecycle; attach or detach a file through an approved resource contract |
| Major user roles | Authorized uploaders, downloaders and resource actors; the exact role and permission catalog remains Pending |
| Critical invariants | Tenant Isolation, explicit Access Control and Upload Validation are mandatory; File IDs and Attachment Links grant no authority; every Domain/Resource attachment requires independently approved requirements and authorization |
| External dependencies | Versioned contracts with each Resource-owning Domain; Shared SaaS, Dedicated Managed and Dedicated Sovereign cannot require an external Storage Provider for base operation |
| Security/tenant boundaries | File access and access to the related business resource are independently enforced; cross-tenant upload, download and attachment are prohibited |
| Minimum acceptance criteria | Evidence for allowed and denied upload/download/attach/detach, invalid-upload rejection, cross-tenant denial, lifecycle transitions and provider-independent deployment across all three operational profiles |
| Open design questions | Storage Provider, Object Storage Strategy, Malware Scanning Design, Retention, API/Event Contracts, persistence, migration, Advanced Generated Artifacts ownership and Service Topology |

### Approved FIRST_RELEASE obligation definition — Operational Core

| Concern | Current approved or pending record |
| --- | --- |
| Operational objective | Provide the minimum authorized visibility and controls required to operate approved FIRST_RELEASE capabilities without creating a universal administration domain or superuser |
| Minimum workflows | Observe Health/Readiness and authorized operational status; distinguish Tenant and Platform scope; record Privileged Operations in Audit; invoke only independently approved minimum controls |
| Major operator roles | Authorized tenant and platform operators; the Privileged Role Model remains Pending |
| Critical invariants | Domain-owned Authorization, Tenant Isolation and Audit cannot be bypassed; privileged scope is explicit and least-authority; Dedicated Sovereign authority remains local |
| External dependencies | Owner-domain contracts and Audit; General Administration UI, advanced dashboards, bulk import, email administration and advanced remediation are not FIRST_RELEASE dependencies |
| Security/tenant boundaries | Tenant and Platform visibility/actions are separated; Operational Core cannot become a backdoor to business resources or private domain databases |
| Minimum acceptance criteria | Authorized/denied visibility, tenant/platform separation, privileged-action audit, cross-tenant denial, failure-safe behavior and profile-local authority evidence |
| Open design questions | Ownership, Privileged Role Model, Operational Action Catalog, API/Event Contracts, Observability Stack, persistence, migration, component dispositions and Service Topology |

## 7. Pending decisions and unresolved questions

- Owner Disposition Review covers all 46 assets and all 46 now have approved Final Dispositions. Concept Reconciliation, Open Decisions, Independent Architecture Review and implementation/readiness evidence remain separate and Pending.
- V2-AST-001 is approved as `REWRITE` for reproducible build and independent service build/version/artifact semantics only; its historical toolchain/configuration is not inherited and OD-002–OD-004/OD-020 remain Open.
- V2-AST-002 is approved as `RETAIN` only for read-only Historical API-composition/Discovery Evidence; no GraphQL/BFF pattern is approved, API/client composition decisions remain open and Dependency Health Aggregation remains independent in Operational Core.
- V2-AST-003 is approved as `RETAIN` only for read-only Historical Security/Performance Evidence; no GraphQL implementation or historical threshold is approved, and general Resource Exhaustion controls remain independent.
- V2-AST-006 is approved as `RETIRE`; TenantProbe is not a V3 capability or model, while its valid tenant-isolation and fail-closed scenarios remain historical inputs to independent test design.
- V2-AST-007 is approved as `RETAIN` only for read-only Historical Contract Evidence; historical TypeScript types/shapes are not V3 contracts, and Event Tenant Provenance never creates automatic trust.
- V2-AST-009 is approved as `RETAIN` only for read-only Historical Observability/Security Evidence; historical tooling/configuration is not inherited, and detailed policy plus evidence for all three deployment profiles remains Pending.
- V2-AST-010 is approved as `RETAIN` only for read-only Historical Test-support Evidence; its two-tenant scenarios are a minimum test-design input, not proof of isolation.
- V2-AST-011 is approved as `REWRITE` only for valid Outbox/Inbox/processed-event behavior; retired TenantProbe and historical Prisma/schema details are excluded, while physical persistence and migration choices remain Pending.
- V2-AST-012 is approved as `RETAIN` only for read-only Historical Tenant-isolation/RLS Evidence; historical SQL is not executable V3 material and every Service still requires independent design and runtime proof.
- V2-AST-013 is approved as `REWRITE` for per-Service least-privilege database identity separation only; historical bootstrap, credentials, roles and grants are excluded and profile-specific secrets design remains Pending.
- V2-AST-014 is approved as `RETAIN` only for read-only Historical Cache/Security Evidence; no Cache technology or pattern is approved, and future adoption requires an independently approved owned Use Case, freshness and failure policy.
- V2-AST-015 is approved as `REWRITE` for valid Transactional Outbox/publication-confirm semantics; exact delivery mechanics, topology, contracts and reconciliation design remain Pending.
- V2-AST-016 is approved as `REWRITE` for valid durable Inbox, ACK-after-effect, bounded retry and DLQ semantics; exact transaction/idempotency, topology, retry and reconciliation designs remain Pending.
- V2-AST-017 is approved as `RETAIN` only for read-only Historical Security Test Evidence; no historical test framework, fixture or cryptographic mechanism is approved.
- V2-AST-018 is approved as `RETAIN` only for a read-only Historical Regression Scenario Catalog; scenarios require selective requirement/risk mapping and historical results provide no runtime/security evidence.
- V2-AST-019 is approved as `REWRITE` only for independent Service artifact/deployment and three-profile verification requirements; historical build/container/topology choices are excluded.
- V2-AST-020 is approved as `RETAIN` only for read-only Historical CI/Governance Evidence; historical workflow execution and ordering provide no V3 evidence or tooling authority.
- V2-AST-021 is approved as `REWRITE` for independent Repository/Service CI and traceable gates/artifacts; historical provider/toolchain/workflow choices are excluded.
- V2-AST-022 is approved as `RETAIN` only for read-only Historical Governance Discovery/Provenance; no historical declaration, rule, manifest, validator or result receives V3 authority or Passed status.
- V2-AST-023 is approved as `RETAIN` only for read-only Historical Boundary-policy/Adversarial-test Evidence; its static checker proves neither database-access nor runtime-boundary compliance.
- V2-AST-024 is approved as `RETIRE`; its V2-stage scripts are not transferred or rewritten, physical history remains untouched, and approved V3 Governance Controls remain valid.
- V2-AST-025 is approved as `RETAIN` only for read-only Historical Architecture/Governance Provenance and Secondary Evidence; retention approves no document content and independent Concept Reconciliation remains Pending.
- V2-AST-026 is approved as `RETAIN` only for read-only Historical Decision Provenance; each ADR concept still requires independent classification and Final Asset Disposition does not complete Concept Reconciliation.
- V2-AST-027 is approved as `RETAIN` only for read-only Historical Engineering/Quality Evidence; historical gates, roadmap, priorities and Passed Status create neither V3 scope nor readiness evidence.
- V2-AST-028 is approved as `RETIRE`; historical V2/NestJS Skills remain read-only, are not transferred/executed and create no V3 governance or tooling authority.
- V2-AST-029 is approved as `RETAIN` only for read-only Historical Audit Provenance; historical pass/coverage/validation claims provide no V3 evidence.
- V2-AST-030 is approved as `RETAIN` only for a read-only Bounded Historical Evidence Index; its recorded 106/106 hash result proves sample identity only and creates no completeness, semantic, security, authority or readiness claim.
- Customer/CRM disposition, aggregate details, Business Service topology and physical persistence layout remain separate Pending decisions.
- Product capability scope decisions in the current V3-002B matrix are complete; detailed requirements and design gates remain separate.
- Line Item design, Pricing rules and Currency rules remain separate requirements/design decisions; V3-002B-DEC-005 did not approve them.
- Product Catalog ownership remains undecided; V3-002B-DEC-006 approved only Sales core ownership.
- Notification logical/data ownership is approved; Provider Credentials, contracts, scheduling, aggregate/physical persistence design and topology remain undecided.
- System-wide Audit product scope, Audit Domain ownership and `REWRITE` disposition of the Audit component in V2-AST-035 are approved. Producing Domains retain Business Facts and Domain-specific Audit; Notification Delivery Audit remains a separate Notification concern. Detailed Audit design remains undecided.
- Customer Request logical/data ownership and its `REWRITE` component disposition within mixed V2-AST-035 are approved. Portal Submission, Customer Sharing, automation and automatic cross-domain links are LATER_RELEASE.
- V2-AST-035 is finally reconciled as `REWRITE` after four approved component dispositions; its composite grouping is historical traceability only and does not merge their logical boundaries.
- Entitlement Core product scope, logical/data ownership and `REWRITE` component disposition are approved. Detailed policy/design choices, Plan/Subscription facts, Billing, Pricing and Quota remain separate Pending decisions.
- Quota Core product scope, logical/data ownership and `REWRITE` component disposition are approved. Detailed policy/design choices remain undecided, and each Capability-to-Quota integration requires separate requirements approval.
- Business invariants, role catalog, merge/deletion/retention rules and authoritative migration requirements for Customer/CRM remain incomplete.
- Linka/External Registry is LATER_RELEASE with split logical/data ownership and `REWRITE` disposition approved; Provider/design decisions remain open, and Customer Master cannot be changed without Customer-authorized validation/approval.
- Reporting Core is FIRST_RELEASE and advanced reporting is LATER_RELEASE; split Reporting ownership and `REWRITE` component dispositions in V2-AST-034/V2-AST-046 are approved. Final Report Sets remain undecided; AI scope is governed separately by V3-002B-DEC-030, and both composite assets now have final `REWRITE` reconciliation decisions.
- AI-generated Insights, Assistant and Business Action Proposals are LATER_RELEASE with split ownership and `REWRITE` component disposition approved; Model/RAG/retention/approval-replay design remains undecided.
- V2-AST-034 is finally reconciled as `REWRITE`; its composite grouping is historical traceability only, with Reporting and AI release scope and logical boundaries preserved independently.
- Work Core is FIRST_RELEASE with Work Domain ownership and V2-AST-039 `REWRITE` disposition approved; auxiliary Work/Collaboration requirements/ownerships remain independently gated.
- File/Attachment Core is FIRST_RELEASE and Public Sharing, Advanced Versioning, Media Processing and Advanced Generated Artifacts are LATER_RELEASE; split File/Attachment ownership and scope-aware `REWRITE` disposition of V2-AST-040 are approved, while Advanced Generated Artifacts ownership and detailed design remain Pending.
- Technical Knowledge is LATER_RELEASE and independent of FIRST_RELEASE and File Core; Technical Knowledge ownership and scope-aware `REWRITE` disposition of V2-AST-041 are approved, while lifecycle/classification/search/access/retention design remains Pending and OD-018 remains Open.
- Customer Portal is LATER_RELEASE and cannot become a FIRST_RELEASE dependency; split Portal ownership and scope-aware `REWRITE` disposition of V2-AST-042 are approved, while external-principal/trust decisions remain Pending.
- V2-AST-043 is approved as `REWRITE`; its shared Prisma schema, SQL migrations and tools remain read-only historical evidence and cannot be executed, replayed, imported or ported into V3.
- V2-AST-044 is approved as `RETAIN` only for read-only historical test evidence; no legacy test source, framework, execution result or one-to-one rewrite is approved.
- V2-AST-045 is approved as `RETAIN` only for read-only historical contract/documentation evidence; no historical API shape, compatibility promise, code generation or direct source/specification port is approved.
- Essential Operational Core is a FIRST_RELEASE architecture/operations obligation; General Administration UI, advanced operational dashboards, bulk import, email administration and advanced remediation are LATER_RELEASE. V2-AST-046 is finally reconciled as `REWRITE`; deferred capability requirements, ownership and authorization remain Pending.
- Operational Core ownership is approved for Operational Platform state only; source-service, business-domain, Audit, Tenant, Reporting and Notification authorities remain separate. Deferred Administration/Import/Email ownerships remain Pending.
- V2-AST-046 is finally reconciled as `REWRITE`; Reporting and Operational Core are FIRST_RELEASE, while deferred Administration/Operations capabilities require independent requirements, ownership and authorization approval.
- V2-AST-036 is approved as `RETAIN` only for a read-only Historical Capability/Traceability Map; it grants no scope, domain, service, topology or implementation authority.
- Identity Trust logical/data ownership and `REWRITE` dispositions of V2-AST-004, V2-AST-008 and V2-AST-031 are approved; provider/token/session/passkey/protocol design choices remain Pending.
- Tenant Management logical/data ownership and `REWRITE` disposition of V2-AST-005 are approved; role/policy, invitation, lifecycle, placement, contract, persistence, migration and topology designs remain Pending.
- Independent architecture reviewer sign-off remains outside this owner review.

## 8. Architecture and Open Decision dependency matrix

| Decision area | Binding authority | Open dependencies preserved |
| --- | --- | --- |
| Customer ownership and boundaries | ADR-V3-001, ADR-V3-002, ADR-V3-005, ADR-V3-011 | OD-004, OD-007–008, OD-013–014 |
| Identity/session/membership | ADR-V3-004, ADR-V3-005 | OD-009–012 |
| Tenant isolation/persistence | ADR-V3-003, ADR-V3-007 | OD-013–014, OD-022–023 |
| Notification/events | ADR-V3-002, ADR-V3-007–008 | OD-008, OD-019–020 |
| Frontend/Portal | ADR-V3-005, ADR-V3-008–009 | OD-005–007, OD-010 |
| Content/File and Knowledge | ADR-V3-002–003, ADR-V3-008, ADR-V3-010 | OD-017–018 |
| Production profiles | ADR-V3-003–004, ADR-V3-010, ADR-V3-012 | OD-001, OD-012, OD-015, OD-023 |

## 9. Security-sensitive carry-forward requirements

- Authentication, principal validity, tenant membership, entitlement, resource/action authorization and data-layer isolation remain distinct checks.
- Validate token signature, issuer, audience, expiry and required claims under a future approved identity/session design.
- Replace process-local Passkey challenge state with a lifecycle compatible with restart and multi-instance operation.
- Refresh-token reuse, rotation, revocation, tenant switching and privileged session actions require explicit threat and failure tests.
- Every resource-owning domain reauthorizes direct and mediated operations; gateways, AI, plugins and upstream services are not final authority.
- Tenant-aware Shared SaaS persistence requires transaction-local validated Tenant Context and non-bypass PostgreSQL RLS.
- Privileged cross-tenant operations require narrow identity, least privilege, audit and Sovereign-local authority where applicable.
- Notification processing must preserve validated tenant provenance, idempotency and profile-local operational authority; LATER_RELEASE channels cannot become mandatory for FIRST_RELEASE operation.
- Notification recipient access must be authorized and tenant-isolated; Notification authorization never grants an operation in Customer, Sales or another producing domain.
- Customer Request Assignment never establishes Tenant Membership, entitlement or resource/action authorization; the request owner must authorize every operation independently.
- Customer Requests FIRST_RELEASE must not depend on Portal or a generic Workflow Engine, and direct V2 source transfer is prohibited.
- Audit records must be append-oriented, integrity-controlled and explicitly Tenant- or Platform-scoped; Audit Core cannot query private domain databases directly, and Dedicated Sovereign Audit authority must remain local.
- Audit rewrite must preserve sensitive-data protection and must not transfer V2 source directly.
- Entitlement eligibility must remain distinct from Tenant Membership and owning-domain Resource/Action Authorization; Dedicated Sovereign evaluation cannot require a central service.
- Entitlement must be rewritten without direct V2 source transfer while preserving traceable Decision Reason and Validity behavior.
- Quota must remain distinct from Entitlement, Membership and owning-domain Authorization; its reservation lifecycle must be atomic and Dedicated Sovereign consumption control must remain local.
- Quota must be rewritten without direct V2 source transfer and preserve Idempotency, Concurrency Safety, Tenant Isolation and traceable decision behavior.
- Customer Core and Dedicated Sovereign base Customer operations must not depend on Linka or another external registry provider; any later Customer Master change requires validated, authorized approval.
- Providers and adapters cannot write directly to Customer Master or access its private database; Provider Snapshots require approved retention, security and data-protection controls.
- Reporting must use versioned contracts or authorized Projections, never cross-service database access; every Report Set requires explicit authorization and tenant-isolation evidence.
- Reporting Projections cannot bypass source-data disclosure constraints or Authorization; Operational Platform remains an operator and Dedicated Sovereign Reporting authority is local.
- Reporting components must be rewritten without direct V2 source transfer and may not use cross-service database access.
- AI access requires validated Tenant Context and current User Authorization; every business write requires explicit approval and execution-time owner-domain re-authorization, with autonomous writes prohibited and future replay/idempotency/sovereignty controls mandatory.
- Approval References grant no execution authority; AI cannot access target databases directly or authorize target-domain operations, and Model Providers own no authoritative Business Facts.
- AI must be rewritten without direct V2 source transfer; the disposition does not authorize implementation start or FIRST_RELEASE inclusion.
- Work Assignment grants no Membership, Entitlement or Authorization; manual cross-domain links require authorized contracts and independent access checks in each Resource-owning Domain.
- Work cannot access another domain's private database or change its Business Facts; it authorizes only Task resources and stores only contract-bound link metadata.
- File IDs and Attachment Links grant no authority; Upload Validation, Tenant Isolation and independent authorization of both the file and related resource are mandatory.
- Multiple links to one file cannot be used to inherit access from another resource; Attachment removal does not imply File Object deletion, and no domain may bypass contracts through direct database access.
- Technical Knowledge links cannot transfer Business Fact ownership or bypass Tenant Isolation and owner-domain Authorization; no FIRST_RELEASE capability may require its registry or search dependencies.
- Search Index is a rebuildable non-authoritative Projection and cannot bypass Tenant Isolation, Authorization or source disclosure restrictions; Knowledge Links grant no Membership, Entitlement or Authorization.
- Portal Authentication grants no Tenant Membership, Entitlement or Resource Authorization; every Portal-exposed operation requires owner-domain authorization and cannot use direct database access.
- Portal Account Linkage, Invitation, Session and Workspace State grant no authority over business resources; Portal may authorize only its own resources and must preserve local Dedicated Sovereign authority.
- Historical shared-schema or migration artifacts create no V3 data authority; every domain requires independently approved mappings, validation and rollback/cutover controls, with OD-013 and OD-014 remaining Open.
- Historical test scenarios require architecture/scope/ownership/requirements review before use; incomplete or contradictory evidence cannot automatically become a requirement or security-validation claim.
- Historical contracts and documents create no V3 API or compatibility authority; every V3 contract requires independent ownership, tenant, authorization, versioning, error-model and consumer review.
- Operational visibility and privileged controls cannot bypass Domain-owned Authorization, Tenant Isolation or Audit; no General Admin or universal Superuser is implied, and Dedicated Sovereign authority remains local.
- Privileged Operations require limited valid identity, explicit Tenant/Platform scope, destination-domain Authorization and traceable Audit; Operational Platform owns no Business Fact or universal authorization.
- Historical capability-map presence or absence is not product authority; folder/module layout cannot be converted into V3 services or used to override approved scope and ownership.
- Authentication, Token and Session establish no Membership, Entitlement or Business Authorization; Tenant Switching requires Membership and Tenant Context re-evaluation, and external assertions require approved validation/mapping.
- Membership and Membership Role Assignment grant no Entitlement or business-resource authority; Tenant Context requires valid Principal plus active Membership and must be revalidated across trust boundaries.
- Historical GraphQL query-depth/complexity code and thresholds create no V3 control baseline; independently designed Resource Exhaustion protection is required where future query or workload characteristics justify it.
- TenantProbe must not be recreated as a product or service; only its tenant-isolation, invalid-context, cross-tenant-denial and fail-closed scenarios may inform independently designed V3 tests.
- Tenant Provenance in a historical or future Event is evidence to validate, not proof that automatically establishes trusted Tenant Context at a consumer boundary.
- Logs and traces must not disclose credentials, tokens, sensitive Business Facts or cross-tenant data; redaction, trace trust and profile-specific observability evidence require independent design and verification.
- Historical two-tenant fixtures are not isolation proof; future tests require synthetic isolated data plus positive, negative, missing/invalid-context and cross-tenant-denial scenarios under ordinary non-bypass identities.
- Outbox records must share the owning Service transaction boundary with the state change, while Inbox/processed-event state must prevent duplicate message delivery from creating duplicate effects; physical implementation remains unapproved.
- Historical RLS SQL is evidence rather than an executable baseline; future Shared SaaS validation must use real pooled connections, transaction-local validated context, Missing/Invalid Context cases and ordinary Runtime Roles that neither own protected tables nor have `BYPASSRLS`.
- Migration, Runtime and justified Dispatcher/Worker database identities require per-Service least privilege; historical credentials/grants are prohibited, and Secret Provisioning/Rotation/Revocation must preserve local Dedicated Sovereign authority.
- Cache cannot authorize, establish membership/entitlement or become a Business Fact source; stale, failed or revoked authorization-related cache state must never produce fail-open access.
- Publisher Confirm proves broker acceptance rather than consumer success; Unroutable Messages cannot be marked Published, consumers require durable idempotency, and end-to-end Exactly-once is not claimed.
- Consumer ACK requires a durable business effect coordinated with Inbox/Processed-event state; duplicates, reordering and crash boundaries remain expected, and message Tenant/Workload Context must be validated.
- Historical signature/configuration tests preserve negative scenarios only; future protocol-specific tests must cover forgery, expiry, replay and missing/invalid trust context without inheriting algorithms, secrets or fixtures.
- Historical regression scenarios require approved Requirements/Risk mappings and later authorized execution; prior Passed results and historical test infrastructure provide no V3 runtime or security evidence.
- Co-deployment cannot erode independently versioned Service build/artifact boundaries; every Deployment Profile requires its own secrets, upgrade/rollback, recovery, observability and authority evidence.
- Historical CI workflows establish no passed Gate; future Gates require explicit scope, evidence, failure criteria/effect, least privilege and approved immutable dependency pinning.
- Shared governance and compatibility checks cannot couple otherwise independent Repository/Service builds, versions, artifacts or releases; CI credentials must remain minimal and short-lived.
- Historical governance declarations require item-level reconciliation with approved V3 authority; they cannot create or pass a Gate, while existing approved V3 Governance Controls remain unchanged.
- Static dependency rules must distinguish versioned contracts from business implementation but cannot alone prove absence of direct database access, reflection/dynamic loading or runtime boundary violations.
- Retired V2 bootstrap/report tooling remains read-only history and cannot cancel V3 controls or establish that any Gate, Build, Test or Validation passed.
- Historical architecture/governance documents close no Open Decision; contradictions, incomplete evidence and obsolete claims require explicit reconciliation, and candidate classification alone grants no approval.
- Historical ADR mapping can only record Covered Evidence, Requires Independent Decision, Non-transferable or Insufficient Evidence; it cannot alter V3 scope, decisions or Open Decision status.
- Historical engineering gates and roadmap priorities provide no V3 ordering or Passed status; every future Gate requires explicit profile, evidence, owner and failure criteria with readiness layers kept separate.
- Retired V2/NestJS Skills remain historical evidence only; they cannot be installed, executed or used to override synchronized V3 Skills and Governance.
- Historical audit reports prove only what V2 recorded; every future Validation needs explicit Scope, Tool, Inputs, Expected Result, Actual Result and Evidence, with conflicts documented.
- The 106-entry evidence index is bounded provenance rather than a full manifest; Hash Matches establish content identity only, and future semantic use requires preserved Commit/Tree provenance plus an authorized independent review.
- Static historical evidence is not runtime security or exploitation evidence.

## 10. Decision summary

| Dimension | Approved | Conditional | Pending |
| --- | ---: | ---: | ---: |
| Asset dispositions | 46 | 0 | 0 |
| Product capability scope | 31 | 0 | 0 |
| Domain/data ownership | 17 | 0 | All mappings except Customer/CRM, Identity Trust, Tenant Management, Sales core, Notification, Customer Requests, Audit, Entitlement, Quota, Linka, Reporting, AI, Work Core, File/Attachment, Technical Knowledge, Customer Portal and Operational Core |

## 11. Review outcome and remaining gates

**Current outcome: Owner Disposition Review Complete — All 46 Assets Have Final Dispositions.**

Customer/CRM, Sales Opportunity/Pipeline, Notification Core + In-App, minimal Customer Requests, Audit Core, Entitlement Core, Quota Core, Reporting Core, Work Core and File/Attachment Core are approved as `FIRST_RELEASE`; essential Operational Core is a FIRST_RELEASE architecture/operations obligation. Linka/External Registry, advanced Reporting, staged AI, auxiliary Work/Collaboration, advanced file capabilities, Technical Knowledge, Customer Portal and advanced Administration/Operations surfaces are `LATER_RELEASE`. Current V3-002B product-scope decisions are complete. Customer, Identity Trust, Tenant Management, Sales core, Notification, Customer Request, Audit, Entitlement, Quota, Linka, Reporting, AI, Work Core, split File/Attachment, Technical Knowledge, split Customer Portal and Operational Core ownerships are approved; deferred capability ownership decisions remain Pending. Owner Disposition Review now covers all 46 assets and all 46 have approved Final Dispositions. V2-AST-002, V2-AST-014, V2-AST-022 and V2-AST-025–V2-AST-027 are retained only as bounded read-only historical evidence under DEC-083 through DEC-088; this does not approve their technologies, content, historical statuses or claims. Concept Reconciliation remains independent and Pending. V2-AST-030 is retained only as a bounded provenance index; the historical 106/106 hash record creates no completeness, semantic or readiness claim. OD-002–OD-004, OD-007–OD-015, OD-017–OD-020 and OD-023 remain Open where applicable. Detailed design choices remain Pending. No decision creates an implementation, runtime-security or production-readiness claim. Runtime security, contract compatibility, migration correctness, operational-profile evidence and production readiness remain unverified. Independent architecture review remains required where applicable; this task does not start reconciliation or a subsequent implementation task.
