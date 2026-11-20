# Product decision record

Owner Farzad explicitly confirmed D01–D20 in conversation, 2026-11-20 (Asia/Tehran); no exact issuance time or signature asserted. Approved product direction, not an architecture/security decision, software acceptance, or Git publication authority.

| ID | Confirmed direction | Trace / elaboration |
|---|---|---|
| D01 | Person and Company | Search requirements |
| D02 | General search by name, Customer ID, official ID, phone and email | Field catalog |
| D03 | Combined authorized field filters | Matching rules |
| D04 | Exact, Prefix, Contains name match | Matching rules |
| D05 | Exact official identifier match | Field catalog |
| D06 | Persian/English and character/digit normalization | Matching rules; exact equivalences OPEN |
| D07 | Active, Inactive, Archived | Field catalog |
| D08 | Name, creation and last-change sorting | Matching rules |
| D09 | Default last change descending | Matching rules |
| D10 | Page sizes 20/50/100 | Matching rules |
| D11 | Tenant, Resource and Field-level access | Access matrix |
| D12 | Permission-based masking | Access matrix; precise mask OPEN |
| D13 | No unauthorized data even in count | Access matrix |
| D14 | Latest valid recorded state | Matching rules |
| D15 | Read-only permission-controlled history | Customer 360 |
| D16 | Sensitive access and unauthorized attempts per approved Audit policy | Audit policy; A-002 inherited |
| D17 | Excel export out of scope | Search requirements |
| D18 | AI/intelligent search deferred | Search requirements |
| D19 | Farzad Business Owner | README |
| D20 | Shared Cell synthetic initial scope | Audit/profile policy |

## Nine canonical requirements gaps

All entries have owner Farzad for product disposition; technical team drafts options, not authority to treat them as approved. Source: roadmap A-003 and FR-BJ-002; A-002 accepted limits remain.

| Gap | Disposition | Residual / blocker |
|---|---|---|
| Filters | Bounded direction D02–D03,D07 | Exact additional fields, Boolean combination, blank/default filter OPEN |
| Matching and sorting | Bounded D04–D09 | Customer ID/phone/email modes, Unicode/namespace, ties and locale/null ordering OPEN |
| Pagination | Bounded D10 | Default size, cursor/offset contract, concurrent paging and invalid requests OPEN |
| Disclosed fields | Bounded D11–D12,D15; A-002 PD-096/103 | Exact field allowlist, masking and actor grants OPEN |
| Freshness | Bounded D14 | Consistency boundary and lag mechanism/threshold OPEN |
| Enumeration-safe responses | Bounded D13 | Concrete error semantics and side-channel examples OPEN |
| Read/Audit failure policy | Bounded D16 | Failure/retry/durability and classification contracts OPEN |
| Accountable owner and actor catalog | D19 and inherited logical actors | Actual actor binding and executable grants OPEN |
| Operation/profile examples | D20 and acceptance examples | Exact approved actor/operation/profile cases and independent profile validation OPEN |

Query UX detailed design OPEN. No OD-007/OD-018 resolution, no architecture change. Source trace: roadmap A-003 scope and criteria; A-002 acceptance and actor/resource matrix CM1-PD-096/103; operation catalog PD-092/093; support matrix FR-BJ-002. All decision directions trace to the user-approved list above, with no inferred extra approval. K-001 contract design requires separate permission and applicable requirements dispositions. Pending owner review of this assembled candidate.
