# Acceptance criteria — V3-FR-A-002

Canonical measurable criteria plus inherited criteria, plus cross-cutting user-confirmed criteria. Relationship/branch/audit criteria are carried in `cm1-acceptance-criteria-addendum.md` (single source; no duplication). None evaluated as PASS; all user-confirmed criteria PROPOSED / NOT TESTED.

## Canonical criteria (V3-FR-A-002-AC-01..05)

- **V3-FR-A-002-AC-01 — Complete declared deliverable set**: all artifacts present and non-empty.
- **V3-FR-A-002-AC-02 — Trace scope to normative requirements and gaps**: every capability/operation/field/rule source-located or OPEN/PROPOSED.
- **V3-FR-A-002-AC-03 — Inventory FR-BJ-001 requirements with actor/owner facts and gaps**: 5 master entities, 4 documented operations, candidate fields OPEN, Business Owner UNASSIGNED.
- **V3-FR-A-002-AC-04 — Demonstrate inherited criteria**: Company/person/contact master + branch/relationship facts (V3-002B-DEC-002); no aggregate/API/mechanism inferred; OPEN rules not guessed.
- **V3-FR-A-002-AC-05 — Preserve scoped authority and readiness boundaries**: no IAM/RBAC/technology/Gate/production decision; roadmap and A-001 unchanged.

## Inherited criteria (canonical)

- Obtain explicit disposition of each required rule or retain OPEN and block affected implementation
- Acceptance examples cover Company/person/contact master maintenance; Customer owns branch and relationship facts
- No aggregate, API or mechanism inferred from inventory
- Trace every outcome to approved requirements/source revision; retain failed/unexecuted evidence and exclusions
- Acceptance references exact operation/role/Tenant/profile examples approved for this bounded scope; OPEN rules cannot be guessed.

## Assessment

MET — documentary; not owner acceptance. All detailed rules/fields/lifecycle/duplicates/permissions remain OPEN and block affected implementation.

## Cross-cutting user-confirmed criteria (PROPOSED / NOT TESTED)

| ID | Criterion | Status |
| --- | --- | --- |
| CM1-FLD-06 | Address and Latin name optional unless a consuming workflow requires them | PROPOSED / NOT TESTED |
| CM1-DUP-01 | Similar names/phones/emails alone are not conclusive matches | PROPOSED / NOT TESTED |
| CM1-DUP-02 | Intentional duplicate-warning override requires reason + Audit; no supervisor approval | PROPOSED / NOT TESTED |
| CM1-DUP-03 | Automatic merge is never performed | PROPOSED / NOT TESTED |
| CM1-LC-01 | Deactivation allowed with open activities; new activities restricted per module policy | PROPOSED / NOT TESTED |
| CM1-LC-02 | Archiving does not delete data/relationships/audit history | PROPOSED / NOT TESTED |
| CM1-LC-03 | Restore never auto-reopens historical activities/relationships | PROPOSED / NOT TESTED |
| CM1-UPD-01 | CUS-UPDATE rejects stale version atomically; no auto-merge | PROPOSED / NOT TESTED |
| CM1-UPD-02 | Company update never silently reparents Branches | PROPOSED / NOT TESTED |
| CM1-UPD-03 | Person update never silently alters unrelated Relationships | PROPOSED / NOT TESTED |
| CM1-UPD-04 | Company↔Person conversion not supported as normal CM-1 update | PROPOSED / NOT TESTED |
| CM1-UPD-05 | INACTIVE record correctable without becoming ACTIVE | PROPOSED / NOT TESTED |
| CM1-VER-17 | A record may be ACTIVE and NOT_VERIFIED | PROPOSED / NOT TESTED |
| CM1-VER-18 | VERIFIED confers no access/operational authorization | PROPOSED / NOT TESTED |

## Relationship, branch and audit criteria

Carried in `cm1-acceptance-criteria-addendum.md` under CM1-REL-*, CM1-BRN-* and CM1-AUD-* (single source of truth; not duplicated here). The controlled-exception Relationship overlap policy is the authoritative policy and supersedes any prior absolute-overlap denial (see CM1-PD-041).
