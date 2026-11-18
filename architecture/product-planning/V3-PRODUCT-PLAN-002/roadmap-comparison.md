# Comparison with original 67-task proposal

PROPOSED — no existing proposal or source is changed.

- Original identifiers retained: **67/67**. Original identifiers deleted/renumbered/merged: **0**.
- Added candidate execution units: **23**. Total inventory records: **90**, not 90 independent execution assignments.
- Disposition counts: `{"EXECUTION_CANDIDATE": 74, "CONDITIONAL_BACKLOG_NOT_FIRST_SLICE": 4, "TRACKING_PARENT_NOT_EXECUTION_UNIT": 7, "ROLLING_BOUNDED_INCREMENTS": 4, "CONDITIONAL_EXECUTION_IF_SELECTED": 1}`. Split tracking parents are coverage records, not duplicated work. Do not optimize by summing parents plus children as effort.
- Four conditional backlog tasks B-001/016/021/022 are removed only from the mandatory Customer/first-release execution queue. Their OPEN decisions and original milestone obligations remain; no scope cancellation is approved.

## Findings and exact treatment

| Finding | Original location | Proposed correction |
| --- | --- | --- |
| Generic source references lack task-specific authority | All 67 task sourceReferences | Add exact FR/OD/owner locators; separate normative sources from planning inputs; authority remains existing sources |
| Objective often equals title; criteria are templates | E/F capability records; C-002/D-002/G-002 | Scope concrete increments with actual deliverables and observable examples; approved rules remain OPEN until owner disposition |
| Decision preparation self-blocked on its own outcome | B-001..023 original acceptanceCriteria | Accept evidence/alternatives package independently; dependent path still waits for effective decision |
| Unrelated architecture backlog inflates mandatory queue | B-001/016/021/022 | Conditional backlog; no prerequisite of Customer or all-15 support without actual feature commitment |
| Global actor/owner gate serializes requirement drafting | A-002..016; G-001 | Draft in parallel; owner/actor confirmation required before accepting each scope, not all fifteen before drafting |
| Multiple ownership boundaries and large scopes conflated | C-002 | Three children: Principal/session C-003; Membership/Context C-004; workload/custody/lifecycle C-005; no authority merge |
| Runtime remediation all-or-nothing engineering batch | D-002 | D-004 persistence/pool, D-005 routing/fence, D-006 operational/recovery; real joint-path coverage retained before D-003 |
| Gate submission mistaken for Gate clearance | D-003 and dependent tasks | Explicit favorable actual-scope G-RUNTIME decision predicate, not predecessor completion |
| All Frontend features block first Customer | G-002 → H-001 | G-003 foundation, G-004 Customer, G-005 rolling remainder; H-001 waits only Customer UI plus real providers |
| Full Audit/operations scope blocks first slice | E-SO-001/E-SO-003 → H-001 | E-003 selected Customer Audit and E-001 safe instrumentation first; E-004/E-002 retain remaining/authorized operational scope |
| Missing explicitly owned integration code | E-000 contract design and H integration validation | K-002 real reliable publication/consumption implementation; contracts/validation are not implementation |
| Missing before-code Customer API/reference contract task | F-BJ-001/002 implicitly design and implement together | K-001 Customer-owned contract design; OD-007 before public contract, OD-018 before search-dependent path |
| Conditional public boundary implementation absent | B-007 decision vs G-002 client/H-001 | K-003 ONLY IF approved strategy selects gateway/BFF; no blanket new service |
| Full provider implementation over-serializes consumers | F-BJ-002/003/004 wait F-BJ-001 | Owned schema/reference contract for isolated work; actual ready authorized provider/data required for live tests |
| Duplicate Customer model risk | F-000 and F-BJ-001 | F-BJ-001 consumes F-000 output, adds adapters; no second model or repeated implementation |
| All-capability integration precedes any security execution | H-002/I-002 | Rolling H-003/H-004 and I-003/I-004; all-15/profile final coverage still required |
| Readiness dossiers hide missing runtime/deployment work | J-001/002/003 | J-005/006/007 execution artifacts/evidence per profile; dossier lead Core, Backend/Frontend contributors separately authorized |
| Sovereign prose copied into Shared/Managed | J-001/002 scope[1] | Scope Sovereign-specific obligations to J-003/J-007; common security invariants unchanged |

## Every original change and addition

`roadmap-comparison.json` lists all 67 original dispositions, old/new sequence and every dependency/split/refinement rationale, plus all 23 additions and their parent/source. `task-by-task-review.md` explains each original individually; `complete-task-table.md` includes every original and new record with all thirteen requested columns.

No pure requirement/design scope is blocked merely because an unrelated OD is OPEN. No live IAM/Runtime/tenant-aware path is called independent to evade a mandatory control. None of the 23 additions is authorized by this review.
