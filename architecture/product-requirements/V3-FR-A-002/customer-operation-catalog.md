# Customer operation catalog — V3-FR-A-002

## Current logical operation and reason matrix — v1.7.0

CM1-PD-078..095 approve product behavior/scope, not new executable CUS IDs, permission reuse, API/schema or implementation. Earlier source/candidate decomposition below remains historical representation where refined. All Customer Master mutations and unauthorized mutation attempts require Audit; exact event classification/contracts remain OPEN. Validation-only failures/warnings/ordinary reads do not automatically require a new event absent governing obligations; protected evidence/Audit reads are independently authorized and traceable. Four source operation IDs retained.

| Logical operation/resource | Scope | Reason policy | Other required boundary |
| --- | --- | --- | --- |
| Ordinary Company/Person registration | INCLUDED | Optional | Required mapped names; optional supplied fields validated; initial ACTIVE/NOT_VERIFIED; authority/Audit |
| Exceptional duplicate registration | INCLUDED | REQUIRED | Basic warning, reuse option, valid authority; no supervisor; definite conflict never overrideable; Audit |
| Sensitive official name/identifier/type/issuer update | INCLUDED | REQUIRED | Version, validation, evidence-impact/reverification, authority/Audit |
| Ordinary non-sensitive Customer/contact/Branch update | INCLUDED | Optional | Version, supplied-value validation, authority/Audit; contact evidence impact may require reverification |
| Customer deactivation / Branch deactivation | INCLUDED | REQUIRED | Preserve histories/related states; existing open dependencies allowed, new-use restrictions retained; Audit |
| Ordinary reactivation | INCLUDED | Optional | Mandatory fields/conflicts/authority/Audit; no universal VERIFIED; no related auto-activation |
| Customer archive / restoration | CONDITIONALLY INCLUDED | REQUIRED | Applicable dependency rules/available evidence; unknown blocks; restore to INACTIVE only; authority/Audit |
| Branch creation | INCLUDED | Optional | Valid same-Tenant immutable Company parent; authority/Audit |
| Ordinary Relationship creation/editing | INCLUDED | Optional | Person/target/Role immutable during edit; calendar-day interval/eligibility/version/authority/Audit |
| Exceptional Relationship overlap | INCLUDED | REQUIRED each new decision | Disclosure-safe warning/authority/Audit; conflict-set reevaluation, no supervisor; stale/Tenant/idempotency guards |
| Manual Relationship termination | INCLUDED | REQUIRED | END+new correction rather than in-place identity replacement; Audit; natural expiry has no manual END reason |
| Manual verification / reverification | CONDITIONALLY INCLUDED | Valid evidence REQUIRED; no new universal ordinary reason requirement | Independent authority, approved evidence/issuer/legal rules and SoD; Audit/provenance; preserve previously governed evidence reason information |
| Manual verification revocation | Conditional verification boundary | REQUIRED | Independent authority, preserve invalidation history, no dispute auto-restore; Audit |
| Role Catalog operations | INCLUDED | PD-073..077 remain authoritative | Ordinary Role lifecycle/Hide/Unhide reasons optional; incompatible scope reason/publication reason+release reference mandatory; full RC safeguards/Audit |
| Search/review and read-for-update | INCLUDED product scope | No automatic reason/product Audit | Exact disclosure OPEN; search details A-003; source disclosure-denial/security obligations preserved |
| Sensitive evidence / Audit access | Restricted independently authorized access | Exact access/reason contracts OPEN | Traceability mandatory, no inferred permission from Operator/Reviewer label; no cross-Tenant disclosure |
| Unauthorized mutation attempt | No mutation allowed | No new caller-supplied reason obligation inferred | Mandatory safe Audit; fail closed, Audit outage never grants permission |

Deferred: real system verification, Branch transfer coordination, advanced fuzzy detector. Excluded: merge/physical deletion/Pending Submission/draft/direct external customer access. Prohibited: offline and real customer/documents in initial synthetic scope. Profile/nine branches OPEN. See customer-bounded-readiness.md; no existing roadmap task removed/started.

Logical Audit information (CM1-PD-093): event ID; applicable Tenant ID; actor ID/type; resource type/ID when available; operation; applicable old/new values; required/provided reason; timestamp; outcome; correlation ID; applicable evidence reference. Preserve earlier catalog origin/identity/publication/history and verification provenance requirements. No credentials/tokens/full identity documents or unnecessary sensitive values; protected access only, no cross-Tenant disclosure. Exact schemas/transactions/publication/retry/recovery/reconciliation/retention OPEN.

Mutation success needs guaranteed coordinated durable Audit obligation; unknown is not definite success. Central Audit outage permits no automatic continuation or new executable policy. Producer obligation/outbox/ACK is distinct from authoritative ingestion, and Sovereign local authority is preserved. Prevent unauthorized Audit edits/deletion and treat attempts as security events without fabricating recording success during failure.

**Four documented Customer operation concepts** derived from authoritative sources (V3-003 decision record + V3-FR-A-001 actor inventory). Operation concepts, NOT permission grants or fully specified operations.

| Operation ID | Name | Summary | Business criticality | Audit boundary |
| --- | --- | --- | --- | --- |
| CUS-CREATE | Register Customer | Create a durable authoritative Customer Master record | CUS-BC-001 BC-3 (bounded scenario only) | Durable mandatory Audit obligation coordinated with mutation (DEC-012/013/014) |
| CUS-VALIDATE | Validate Customer | Validate customer information; boundary with CUS-CREATE defined in analysis | NOT_ASSESSED | No separate mandatory event for validation rejection (DEC-012 non-approval) |
| CUS-GET-FOR-UPDATE | Retrieve Customer for Update | Read current authoritative state prior to mutation | NOT_ASSESSED | Disclosure-denial evidence where explicit denial issued |
| CUS-UPDATE | Update Customer Information | Apply authoritative change to Customer Master | NOT_ASSESSED | Durable mandatory Audit obligation coordinated with mutation (DEC-012/013/014) |

## Candidate action decomposition (task brief candidates, NOT approved operations)

| Candidate action | Maps to | Status |
| --- | --- | --- |
| register customer | CUS-CREATE | PROPOSED_DECOMPOSITION |
| retrieve customer details | CUS-GET-FOR-UPDATE / disclosure | PROPOSED — may span FR-BJ-002 |
| update customer information | CUS-UPDATE | PROPOSED_DECOMPOSITION |
| manage contact information | CUS-UPDATE (contact sub-set) | PROPOSED_DECOMPOSITION |
| manage addresses | CUS-UPDATE (address sub-set) | PROPOSED_DECOMPOSITION |
| manage customer relationships | CUS-UPDATE (relationship sub-set) | PROPOSED_DECOMPOSITION |
| change customer status | CUS-UPDATE (status field) | PROPOSED_DECOMPOSITION |
| archive or deactivate customer | CUS-UPDATE (lifecycle) | PROPOSED executable decomposition; product lifecycle confirmed, exact contracts OPEN |
| detect potential duplicates | CUS-VALIDATE (detection) | PROPOSED executable decomposition; warning/exception product policy confirmed, matching contract OPEN |
| handle duplicate customer records | CUS-UPDATE / merge | PROPOSED — merge/deletion NOT approved |

## Per-operation detail template (OPEN unless source-approved)

- **Actor:** internal authenticated Principal (APPROVED class); persona/role UNASSIGNED; Customer Domain final authorizer.
- **Preconditions:** validated identity + active Membership + validated Tenant Context; destination authorization.
- **Required permissions:** none granted; resource/action matrix OPEN.
- **Inputs/outputs:** authoritative Customer facts only; no aggregate/API shape selected.
- **Business rules / transitions / validation:** user-confirmed product policies are distinguished from OPEN executable contracts; see business rules, lifecycle, field dictionary and Role Catalog through CM1-PD-077. No permission binding or implementation is approved.
- **Tenant boundary:** validated Context; cross-tenant fails closed.
- **Failure:** see customer-failure-scenarios.md.
- **Audit:** CUS-CREATE/CUS-UPDATE durable obligation; validation rejection has no separate mandatory event.
- **Acceptance:** see acceptance-criteria.md.

No candidate executable operation contract is approved. Duplicate/lifecycle product policies have user-confirmed directions, not blanket OPEN status; merge/deletion and affected technical contracts remain unresolved. Formal acceptance stays PENDING.

## Proposed logical capabilities (NOT new approved CUS operation IDs)

- **Identity verification workflow** (trusted system + evidence-backed manual): establishes NOT_VERIFIED/VERIFIED/REQUIRES_REVERIFICATION transitions with evidence provenance and coordinated Audit. Never set VERIFIED directly via CUS-UPDATE. (CM1-PD-019..028, CM1-PD-056/057)
- **Relationship management** (create/update/end): distinct Relationship per role; ACTIVE/ENDED lifecycle; half-open intervals; controlled overlap exception. (CM1-PD-029..041)
- **Branch management** (create/update/deactivate/transfer): Branch subordinate to Company; immutable parent; transfer via new Branch. (CM1-PD-042..047)

These are product-direction proposals; the four documented operation concepts (CUS-CREATE, CUS-VALIDATE, CUS-GET-FOR-UPDATE, CUS-UPDATE) remain unchanged. No permission grant or operation approval is implied.

## Role Catalog logical capability (v1.3.0 product direction)

Create/manage Role title/applicability, deactivate/reactivate, and validate new Relationship assignments against ACTIVE status and current applicability (CM1-PD-058..065). Physical deletion and identity/code mutation are unsupported. Scope changes preserve existing Relationships; incompatible changes require management authority, impact evaluation, disclosure-safe warning, mandatory reason and auditability. System/Tenant management boundaries: `customer-role-catalog.md#rc-007--authority-and-tenant-boundaries`.

These are logical capabilities only, not new approved CUS operation IDs or CUS-UPDATE permission reuse. Exact management operation/IAM/API/persistence, concurrent scope-dependency evaluation and operation-specific Audit failure/recovery remain OPEN under PDQ-002-08/10/12. CUS-CREATE does not confer catalog management authority.

## Tenant System Role selectability (v1.4.0 logical capability)

CM1-PD-067 permits authorized Tenant-local hide/unhide for new assignments of System Roles (including the initial vocabulary, CM1-PD-066). It is neither global Role deactivation nor System definition editing. Customer Domain enforces RC-010/011 eligibility including direct API attempts and concurrent hide/finalization safety. Existing Relationships and authorized historical references remain intact; no reactivation, other-Tenant change or disclosure is permitted. Validated Tenant context and management authority are necessary; CUS-CREATE alone is insufficient.

No new approved operation ID, request/response schema, permission or Audit event name is introduced. Configuration/default materialization, concurrency enforcement and Audit failure/recovery remain OPEN. Product defaults are answered by CM1-PD-068; Hide/Unhide reason OPTIONAL and Audit MANDATORY under CM1-PD-073/077. The incompatible scope-change mandatory-reason rule is not imported here.

## Defaults, code validation and publication gate (v1.5.0 logical capabilities)

CM1-PD-068..072 add conceptual defaults on new-Tenant/new-System-Role availability while retaining prior settings, canonical code validation/uniqueness/reservation on Role creation, identity-preserving reactivation, and pre-publication collision assessment with non-destructive authorized resolution. See `customer-role-catalog.md` RC-012..016. Conflict blocks that proposed System Role only, not all unrelated catalog changes. Same custom code in independent Tenants is permitted; cross-Tenant detection does not imply private-data access. No new operation ID/API, provisioning/migration, persistence/index/tombstone, IAM or publication mechanism is chosen; concurrency, privacy/authority, rollback/resolution and Audit contracts remain OPEN.

## Catalog governance and Audit logical operations (v1.6.0)

CM1-PD-073..077: manage own-Tenant System Role selectability; update display metadata under System controlled release or own-custom authority; render current versus event-time historical titles; enforce three logical authority categories at the Backend. Exact responsibilities and full operation/Audit/reason matrix: `customer-role-catalog.md` RC-017..021 and actor policy matrix.

Creation, metadata, scope, lifecycle, Hide/Unhide, publication and unauthorized catalog modification attempts have mandatory Audit coverage. Reasons are optional for ordinary creation/metadata/compatible-scope/activation/deactivation/Hide/Unhide; incompatible scope requires reason; publication requires reason including release reference. Metadata optional reason cannot waive publication's mandatory reason. Preserve previous exception rules, old/new applicable values, isolated immutable history and durable no-success guard. Ordinary catalog reads have no independent Audit requirement here, not a waiver of security/source obligations. No operation IDs, event schemas/counts, transaction protocols or permission grants are selected; exact execution/recovery/access contracts remain OPEN.
