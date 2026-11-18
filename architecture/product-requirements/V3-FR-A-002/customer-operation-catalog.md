# Customer operation catalog — V3-FR-A-002

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
| archive or deactivate customer | CUS-UPDATE (lifecycle) | PROPOSED — no approved archive/deactivate policy |
| detect potential duplicates | CUS-VALIDATE (detection) | PROPOSED — no approved duplicate policy |
| handle duplicate customer records | CUS-UPDATE / merge | PROPOSED — merge/deletion NOT approved |

## Per-operation detail template (OPEN unless source-approved)

- **Actor:** internal authenticated Principal (APPROVED class); persona/role UNASSIGNED; Customer Domain final authorizer.
- **Preconditions:** validated identity + active Membership + validated Tenant Context; destination authorization.
- **Required permissions:** none granted; resource/action matrix OPEN.
- **Inputs/outputs:** authoritative Customer facts only; no aggregate/API shape selected.
- **Business rules / transitions / validation:** see business-rules, lifecycle and field dictionary; all OPEN.
- **Tenant boundary:** validated Context; cross-tenant fails closed.
- **Failure:** see customer-failure-scenarios.md.
- **Audit:** CUS-CREATE/CUS-UPDATE durable obligation; validation rejection has no separate mandatory event.
- **Acceptance:** see acceptance-criteria.md.

No candidate operation assumed approved; duplicates and merge/delete are PROPOSED with no approved policy.

## Proposed logical capabilities (NOT new approved CUS operation IDs)

- **Identity verification workflow** (trusted system + evidence-backed manual): establishes NOT_VERIFIED/VERIFIED/REQUIRES_REVERIFICATION transitions with evidence provenance and coordinated Audit. Never set VERIFIED directly via CUS-UPDATE. (CM1-PD-019..028, CM1-PD-056/057)
- **Relationship management** (create/update/end): distinct Relationship per role; ACTIVE/ENDED lifecycle; half-open intervals; controlled overlap exception. (CM1-PD-029..041)
- **Branch management** (create/update/deactivate/transfer): Branch subordinate to Company; immutable parent; transfer via new Branch. (CM1-PD-042..047)

These are product-direction proposals; the four documented operation concepts (CUS-CREATE, CUS-VALIDATE, CUS-GET-FOR-UPDATE, CUS-UPDATE) remain unchanged. No permission grant or operation approval is implied.

## Role Catalog logical capability (v1.3.0 product direction)

Create/manage Role title/applicability, deactivate/reactivate, and validate new Relationship assignments against ACTIVE status and current applicability (CM1-PD-058..065). Physical deletion and identity/code mutation are unsupported. Scope changes preserve existing Relationships; incompatible changes require management authority, impact evaluation, disclosure-safe warning, mandatory reason and auditability. System/Tenant management boundaries: `customer-role-catalog.md#rc-007--authority-and-tenant-boundaries`.

These are logical capabilities only, not new approved CUS operation IDs or CUS-UPDATE permission reuse. Exact management operation/IAM/API/persistence, concurrent scope-dependency evaluation and operation-specific Audit failure/recovery remain OPEN under PDQ-002-08/10/12. CUS-CREATE does not confer catalog management authority.
