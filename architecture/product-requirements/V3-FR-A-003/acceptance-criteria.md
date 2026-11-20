# Acceptance criteria and evidence matrix

Status: documentary examples prepared for bounded review; no software PASS, tests or runtime evidence. All examples require approved authority and synthetic records. Canonical criteria retain source meaning.

| Canonical criterion | Evidence / review disposition |
|---|---|
| V3-FR-A-003-AC-01 | README deliverable list and this package; owner review pending |
| V3-FR-A-003-AC-02 | Decision record D01–D20 and source trace; unresolved rules retained |
| V3-FR-A-003-AC-03 | Nine-gap ledger in decision record; remaining blockers explicit |
| V3-FR-A-003-AC-04 | Examples below; proposed observable outcomes, not evaluated |
| V3-FR-A-003-AC-05 | README authority/profile boundary; no Gate transition |

| Example ID | Synthetic scenario | Expected outcome | Decision |
|---|---|---|---|
| EX01 | Reviewer authorized for both Person and Company in Tenant A | Both eligible types returned, no Tenant B data | D01, D11 |
| EX02 | Authorized name Alpha, test prefix/contains/exact modes | Matching mode differentiates expected name examples | D04 |
| EX03 | Authorized official identity search using exact synthetic value | Exact match only; no partial identifier probe | D05, D11 |
| EX04 | Actor lacks identity-search authority, hidden matching identifier exists | No result/count/error side channel attributable to hidden identifier | D12–D13 |
| EX05 | Persian/English strings and corresponding approved digit variants | Equivalent approved forms match; unsupported equivalences remain blocked | D06 |
| EX06 | Authorized active/inactive/archive filter | Only selected authorized lifecycle results | D07 |
| EX07 | Two authorized records with different last-change timestamps | Descending last-change default | D08–D09 |
| EX08 | 101 authorized matching records, each permitted page size | No page exceeds selected 20/50/100; exact paging mechanism pending | D10 |
| EX09 | Similar records in Tenant A and B | Only Tenant A authorized matches and counts | D11–D13 |
| EX10 | Request missing Tenant/actor context | No disclosure | D11 |
| EX11 | Known Customer ID without resource authority vs nonexistent ID | No differentiating existence signal; precise contract OPEN | D13 |
| EX12 | Latest valid Customer state vs outdated projection | No silent stale substitution; mechanism OPEN | D14 |
| EX13 | Reviewer with general read but no history/evidence grant | Status visible subject to policy; history/evidence not disclosed | D12,D15 |
| EX14 | Independently authorized protected evidence read | Traceability obligation preserved; contract and actual execution pending | D16 |
| EX15 | Mandatory Audit unavailable during protected read | No bypass; exact response/recovery OPEN | D16 |
| EX16 | Ordinary authorized search | No automatic product Audit obligation, existing security duties retained | D16 |
| EX17 | Request Excel export or AI search | Outside this scope, no implementation/claim | D17–D18 |
| EX18 | Shared Cell synthetic test vs actual customer data or offline | Synthetic-only design, real data/offline prohibited | D20 |
| EX19 | Dedicated/Sovereign profile | Target obligations retained; separate evidence required | D20 |
| EX20 | Authorized Customer 360 Branches, contacts and relationships with partial resource access | Only authorized resource and fields; no hidden counts | D11–D13 |

No unknown, unexecuted or deferred example is passed. Exact approved actor/resource/profile examples and any unresolved observable outcome must be decided before affected implementation. Review artifacts are candidate evidence only.
