# Customer field dictionary — V3-FR-A-002

**No field is approved as a mandatory product requirement.** Five approved master entities are source-derived; every candidate field below is PROPOSED with decision status OPEN. Jurisdiction-specific fields are NOT made universally mandatory.

## Approved master entities (detailed fields OPEN)

- **ENT-002-01 — Company**: Legal/organizational customer master entity. Authoritative organization customer master; detailed attributes/identifiers OPEN
- **ENT-002-02 — Person**: Individual customer master entity. Individual/contact person master; national identifiers OPEN
- **ENT-002-03 — Contact**: Contact point associated with a company or person. Contact master; relationship to company/person and channel details OPEN
- **ENT-002-04 — Branch**: Organizational branch/unit owned by Customer Domain. Branch fact owned by Customer Domain; hierarchy/validation OPEN
- **ENT-002-05 — Relationship**: Relationship fact between customer master records. Customer-owned relationship facts; type and referential rules OPEN

## Candidate fields (PROPOSED — decision status OPEN)

| ID | Business name | Description | Customer type | Logical type | Required | Uniqueness | Validation | Sensitivity | Mutability | Authority |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| FLD-002-01 | Customer identifier | Stable non-topology-encoding internal identifier | Company, Person, Contact | identifier | Required | OPEN | Unique per Tenant; no cell/db encoding | Tenant Confidential | Immutable | OPEN |
| FLD-002-02 | Persian display name | Primary Persian name for display/search | Company, Person, Contact | text | Required | OPEN | Non-empty; normalization policy OPEN | Tenant Confidential | Mutable | OPEN |
| FLD-002-03 | Latin/transliterated name | Optional secondary name form | Company, Person | text | Optional | OPEN | No jurisdiction requirement | Tenant Confidential | Mutable | OPEN |
| FLD-002-04 | National identifier | Iranian national/legal identifier where applicable | Person | text | Conditional | OPEN | Format/uniqueness OPEN; NOT universally mandatory | Restricted | Controlled | OPEN |
| FLD-002-05 | Legal entity identifier | Company registration/legal identifier | Company | text | Conditional | OPEN | Jurisdiction-specific; NOT universally mandatory | Restricted | Controlled | OPEN |
| FLD-002-06 | Telephone number | Primary/secondary phone channels | Company, Person, Contact | contact-list | Optional | OPEN | Format policy OPEN | Tenant Confidential | Mutable | OPEN |
| FLD-002-07 | Email address | Electronic contact channel | Company, Person, Contact | contact-list | Optional | OPEN | Format/verified-status OPEN | Tenant Confidential | Mutable | OPEN |
| FLD-002-08 | Address | Postal/physical address components | Company, Person, Contact, Branch | structured | Optional | OPEN | Persian address parts/normalization OPEN | Restricted | Mutable | OPEN |
| FLD-002-09 | Customer classification | Type/category within Customer Domain | Company, Person | enum | Optional | OPEN | Taxonomy/lifecycle effect OPEN | Tenant Confidential | Mutable | OPEN |
| FLD-002-10 | Customer status | Lifecycle status value | Company, Person | enum | Required | OPEN | Allowed values/transitions OPEN | Tenant Confidential | Controlled | OPEN |
| FLD-002-11 | Branch parent Company reference | Parent Company reference for a Branch (immutable after creation) | Branch | reference | Required | OPEN | Parent Company must exist, same Tenant, authorized; direct reparenting rejected; real transfer = new Branch | Tenant Confidential | Immutable | USER_CONFIRMED (CM1-PD-044/045/047); schema unapproved |
| FLD-002-12 | Relationship type | Typed relationship between customer records | Relationship | enum | Required | OPEN | Allowed taxonomy OPEN | Tenant Confidential | Controlled | OPEN |
| FLD-002-13 | External reference | Optional external-system reference | Company, Person | text | Optional | OPEN | Provenance/authority OPEN | Tenant Confidential | Mutable | OPEN |
| FLD-002-14 | Validation state | Customer validation outcome | Company, Person | enum | Required | OPEN | Values/transitions OPEN | Tenant Confidential | Controlled | OPEN |
| FLD-002-15 | Audit correlation | Safe actor/tenant/outcome correlation for Audit | All | derived | Required-for-Audit | OPEN | Data-minimized; covered obligations only | Restricted | Append-oriented | OPEN |
| FLD-002-16 | Pending submission marker | Non-authoritative pending submission flag | Company, Person | boolean | Conditional | PROPOSED | PERMITTED NOT REQUIRED; never authoritative | Tenant Confidential | Controlled | OPEN |

Sensitivity uses candidate DC notation, not an approved classification model.

## Identity verification state (user-confirmed direction)

- `FLD-002-17` identity verification state: NOT_VERIFIED / VERIFIED / REQUIRES_REVERIFICATION; distinct from record lifecycle and commercial status; never set directly through ordinary CUS-UPDATE. (CM1-PD-019..028)

## Relationship conceptual fields (user-confirmed direction, proposed for review)

| ID | Field | Type | Required | Notes |
| --- | --- | --- | --- | --- |
| REL-002-01 | relationshipId | identifier | Derived | Unique per Relationship |
| REL-002-02 | personId | reference | Required | Reference integrity |
| REL-002-03 | targetType | enum | Required | One of COMPANY/BRANCH |
| REL-002-04 | targetId | reference | Required | Reference integrity + Tenant isolation |
| REL-002-05 | roleCode | enum (candidate; schema OPEN) | Required | Hybrid catalog and exact initial System codes confirmed (CM1-PD-066); System assignments require global ACTIVE, applicability, Tenant selectability, Relationship authority and existing guards, enforced by Customer Domain (CM1-PD-067). Exact reference/namespace/configuration/defaults/schema OPEN (PDQ-002-08) |
| REL-002-06 | roleTitle | text | Optional | Initial System titleFa values exact in CM1-PD-066 catalogEntries; no confirmed English-title field or legal authority. Title changes/hide/unhide preserve identity/history; historical display/reference representation OPEN (PDQ-002-08) |
| REL-002-07 | status | enum | Required | ACTIVE/ENDED |
| REL-002-08 | startDate | date/time | Required | Half-open [start,end) |
| REL-002-09 | endDate | date/time | Optional | null allowed; not before start |
| REL-002-10 | recordVersion | integer | Required | Stale-version rejected |
| REL-002-11 | createdAt | timestamp | Derived | Immutable |
| REL-002-12 | updatedAt | timestamp | Derived | Mutable |
| REL-002-13 | endedReason | text | Conditional | Required on END |
| REL-002-14 | source/evidence reference | reference | Optional | Access-controlled |

## Branch parent immutability

- `companyId` (Branch parent) is immutable after creation; direct Branch reparenting is prohibited; transfer uses a new Branch under the target Company (CM1-PD-044/045). Branch has its own stable ID and only ACTIVE/INACTIVE record states (CM1-PD-042/047).

## Role reference — product policy vs schema

Role Definition identity/code immutability (CM1-PD-061) is distinct from an existing Relationship's conceptual roleCode field. No Role schema, Relationship reference shape or change-of-role editing contract is selected. See `customer-role-catalog.md` RC-004/008. Existing field IDs are preserved; no executable Role schema or new approved source entity is added.

System vocabulary v1.0 is the exact 12-entry documentation catalog in PDR JSON CM1-PD-066 and `customer-role-catalog.md` RC-009; it does not select fixed roleIds or a database seed. Tenant selectability (RC-010/011) is a conceptual Tenant-local assignment restriction, not a new global lifecycle field. No configuration field names, missing-setting defaults, persistence representation, roleId-based overlap key or new field ID is approved here. Global identity/status/scope and existing Relationships/history remain unchanged; RC-PROPOSED retains configuration/reason/default contracts as OPEN.

## Branch parent reference — user-confirmed vs schema

- **User-confirmed business constraint:** every Branch has exactly one Company parent (CM1-PD-047); the parent reference is required and immutable after creation (CM1-PD-044); direct reparenting is rejected (CM1-PD-045).
- **Persistence/API schema and referential-integrity enforcement:** still unapproved; these are technical design matters, not changed by the user-confirmed product direction.
- The earlier `Optional / Mutable` status for FLD-002-11 is superseded by the user-confirmed `Required / Immutable` target policy.
