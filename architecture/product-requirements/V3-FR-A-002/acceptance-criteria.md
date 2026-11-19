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

Historical initial assessment: MET — documentary, not owner acceptance. Current user-confirmed product directions are not wholly OPEN; distinguish them from unresolved executable field/schema/operation/IAM/Audit contracts and PENDING formal acceptance. Canonical field-OPEN language concerns the unapproved exact contract, not a denial of confirmed business constraints. Detailed software scenarios remain PROPOSED / NOT TESTED and contract-dependent execution BLOCKED; no runtime/Gate acceptance is claimed.

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

Detailed CM1 scenarios (CM1-REL-*, CM1-BRN-*, CM1-AUD-*, plus lifecycle/branch/CUS-UPDATE/duplicate/relationship/audit edge cases added in v1.2.1) are carried in `cm1-acceptance-criteria-addendum.md` (single source of truth; not duplicated here). The controlled-exception Relationship overlap policy is the authoritative policy and supersedes any prior absolute-overlap denial (see CM1-PD-041).

## Inventory (v1.7.0 bounded candidate)

- Canonical criteria: **5** (V3-FR-A-002-AC-01..05).
- Detailed CM1 criteria: **207** (FLD 6, VER 18, REL 18, BRN 10, AUD 5, DUP 5, LC 11, UPD 10, ROL 70, BND 54).
- Total unique criterion IDs: **212**. All detailed criteria remain PROPOSED / NOT TESTED.
- v1.7.0 adds CM1-BND-01..54 only; all five canonical and 153 prior detailed definition lines preserved verbatim. New implementation-dependent execution BLOCKED. Prior canonical AC-03's UNASSIGNED owner and CM1-REL-18's immutability parenthetical are historical inventory notes answered by CM1-PD-078/086, not current requirements to remain unassigned/undecided. Deferred system verification/transfer and excluded workflows are not PASS. Current acceptance candidate still has explicit blockers; see customer-bounded-readiness.md.
- Previous v1.6.0 inventory: 5 canonical +153 detailed =158; 77 decisions. This historical count is not the current inventory.
- Previous v1.5.0 inventory: 5 canonical +128 detailed =133; added CM1-ROL-46..70 (25). Earlier definition lines unchanged; new implementation-dependent scenarios explicitly BLOCKED. Catalog-specific Audit coverage now has explicit product authority (CM1-PD-077); this does not negate existing no-assumed-event criteria for ordinary reads/warnings/validation absent a governing requirement.
- Previous v1.4.0 inventory: 5 canonical + 112 detailed = 117. Added CM1-ROL-30..45 (16); all earlier definition lines unchanged. Software execution remains BLOCKED pending relevant executable design; no scenario marked executed.
- Previous v1.3.0 inventory: 5 canonical + 99 detailed = 104. Added CM1-ROL-17..29; original five canonical definitions and CM1-ROL-01..16 are unchanged. See the addendum's v1.4.0 execution-dependency column: software scenarios are BLOCKED pending executable design.
- Previous v1.2.1 inventory: 5 canonical + 83 detailed = 88. Added: CM1-ROL-01..16; no existing criterion ID removed or changed.
