# Customer field dictionary — V3-FR-A-002

**No executable field schema is formally accepted.** Five approved master entities remain source-derived; candidate representations are PROPOSED/OPEN while user-confirmed business constraints and logical Audit information are identified in the overlays below. Mandatory product information does not approve persistence/API fields. Jurisdiction-specific fields are NOT universally mandatory.

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
| FLD-002-15 | Audit correlation | Safe actor/tenant/outcome correlation for Audit | All | derived | Required-for-Audit | OPEN | Data-minimized; covered obligations only, including explicit catalog Audit (CM1-PD-073/077). RC-021 logical information is not an approved event schema | Restricted | Append-oriented | OPEN (schema); logical coverage confirmed |
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
| REL-002-05 | roleCode | enum (candidate reference shape; schema OPEN) | Required | CM1-PD-066/067 effective guards preserved; CM1-PD-068 defaults preserve Tenant settings. Referenced Role Definition codes follow trim-uppercase, ASCII A-Z/0-9/underscore, normalized length 3..64, namespace uniqueness/permanent reservation and future collision blocking (CM1-PD-069..072). Repeated Relationship references allowed; not roleCode uniqueness across Relationships. Enforcement/reference/configuration/Unicode edge cases remain OPEN |
| REL-002-06 | roleTitle | text (candidate representation) | Optional (storage shape not selected) | CM1-PD-074/075: current valid title in current Relationship views; event-time title in historical events/Audit, never rewritten. Inactive/hidden references remain visible under authorization. Persian/English labels permitted without mandatory language fields; labels are not identifiers. Exact temporal/localization/reference/API mechanisms OPEN |
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

System vocabulary v1.0 is the exact 12-entry documentation catalog in PDR JSON CM1-PD-066 and `customer-role-catalog.md` RC-009; it does not select fixed roleIds or a seed. Future authorized controlled display changes do not rewrite that versioned baseline or historical events. Tenant selectability remains a local assignment restriction; defaults are answered, not their storage. Hide/Unhide reason is now OPTIONAL with mandatory Audit (CM1-PD-073/077). No configuration names, persistence representation, roleId-based overlap key or new field ID is approved; existing Relationships/history remain intact.

Code policy (RC-013..016) is confirmed for Role Definitions: System codes globally unique/reserved against Tenant codes; custom codes unique/reserved in their own Tenant, not across all Tenants. Permanent reservations include inactive/history and cannot be reassigned. Reactivation preserves roleId/roleCode. Do not turn this registry policy into a unique roleCode constraint on Relationship rows, rename existing codes, or replace the conceptual overlap key with roleId. Normalization is not authority to edit an existing immutable code. ASCII digits and leading/trailing/consecutive underscores are not separately prohibited; Unicode trim/uppercase/input encoding and further grammar stay PROPOSED / OPEN. No tombstone/index/schema mechanism is chosen.

## Display and Audit logical information (v1.6.0)

CM1-PD-074/075 permits System labels/translations/descriptions under authorized controlled release and own-custom metadata under Tenant manager authority. Stable identity/fundamental semantics preserved; materially different Role needs new Role/new code, not a label-based identity change. Current title rendering is not authority to overwrite Relationship rows or event-time titles. No mandatory Persian/English field, uniqueness constraint on labels, localization storage or snapshot mechanism is selected.

CM1-PD-073/077 requires actor/Tenant/Role identity, old/new selectability/time/optional reason for Hide/Unhide and the complete logical Audit information in `customer-role-catalog.md` RC-021: event ID, actor/authorized system identity, applicable Tenant, available Role ID/code, origin, operation, applicable old/new values, operation-governed reason, timestamp, outcome, correlation. FLD-002-15 is still only a correlation concept, not a container/schema for this entire list. Exact Audit schema/transactions/storage/retention/recovery/access and temporal/reference/API contracts remain OPEN; all 31 existing field IDs preserved.

## Branch parent reference — user-confirmed vs schema

- **User-confirmed business constraint:** every Branch has exactly one Company parent (CM1-PD-047); the parent reference is required and immutable after creation (CM1-PD-044); direct reparenting is rejected (CM1-PD-045).
- **Persistence/API schema and referential-integrity enforcement:** still unapproved; these are technical design matters, not changed by the user-confirmed product direction.
- The earlier `Optional / Mutable` status for FLD-002-11 is superseded by the user-confirmed `Required / Immutable` target policy.
