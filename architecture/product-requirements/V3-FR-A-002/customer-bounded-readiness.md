# Customer Master bounded requirements acceptance candidate — v1.7.0

**USER-CONFIRMED PRODUCT DIRECTION; PREPARED FOR SEPARATE OWNER REVIEW; NOT ACCEPTED.** Task V3-FR-A-002 only. Baseline `6f79975ab974c285dbac2547847add53513f8467`, branch `codex/v3-fr-a-002`. Actual recording time `2026-11-19T08:51:49.335997+00:00`; owner issuance time not supplied. Exact approved clauses: PDR JSON CM1-PD-078..095, one per numbered user clause. No product/IAM/schema/API/runtime implementation or continuation authorization.

## Accountability and authority

Farzad is Business Owner for FR-BJ-001 and product requirements decision authority, and interim accountable authority for Audit failure/ingestion/recovery/reconciliation policy until a separate owner is designated (CM1-PD-078). Software development team is responsible for technical design/implementation; this responsibility is NOT permission to begin. Existing unified project authority and distinct Gate/evidence requirements remain. No appointment certificate, external sign-off or new IAM grant inferred.

Logical responsibilities (CM1-PD-079): Customer Operator, Customer Reviewer, Customer Catalog Manager, Customer Verifier, Audit Reviewer. One person may independently hold several responsibilities. Detailed operation/resource/disclosure matrix: `actor-resource-policy-matrix.md`. No implication from registration to verification, catalog management to assignment, or Customer Catalog Manager to System governance.

## Selected product scope

| Disposition | Operations / boundary |
| --- | --- |
| INCLUDED | Individual and Company registration; information maintenance; Contact channel, Branch, Related Person, Relationship and Role Catalog management; Basic duplicate detection; Customer search/review; activation/deactivation |
| CONDITIONALLY INCLUDED | Archive/restoration subject to applicable dependency rules and available clearance evidence; manual identity verification subject to approved evidence/issuer/authorization/SoD |
| DEFERRED | Real external identity verification integration; executable Branch transfer coordination; advanced intelligent/fuzzy duplicate detection |
| EXCLUDED FROM CM-1 | Merge; physical Customer deletion; Pending Submission/draft; direct external customer access |
| PROHIBITED | Offline operation; use of real customer information or real identity documents in initial synthetic development |
| OPEN | Deployment profile; all nine conditional roadmap branch applicability dispositions; exact Relationship day time reference |

CM1-PD-080/081 do not remove future capabilities or modify the roadmap. Search/review is in selected CM-1 product scope, but its detailed requirements remain FR-BJ-002 / V3-FR-A-003; this task does not complete that task or authorize it. Existing Branch transfer semantics are preserved but their coordinated executable workflow is deferred. Retained provider/transfer criteria are NOT executed or PASS.

All nine branches remain OPEN: SELECTED_PUBLIC_GATEWAY_BFF, CUSTOMER_FEATURE_ELIGIBILITY, CUSTOMER_QUOTA, AUTHORIZED_OPERATIONAL_AGGREGATION, SELECTED_DURABLE_SCHEDULING, SELECTED_NUMERIC_OBJECTIVES, CUSTOMER_INAPP_NOTIFICATION, CUSTOMER_ATTACHMENTS, CUSTOMER_APPROVED_REPORT_SET. In particular, conceptual verification evidence references do not select an attachments integration. Only explicit applicability can determine required branches; no waiver from synthetic scope.

## Approved behavior and remaining boundaries

- CM1-PD-082..085: mandatory Company name and Person given/family names; optional supplied fields validated; official identifiers required only by formal-verification workflows. Extensible six-concept identifier vocabulary, multiple identifiers/entity, verified-valid uniqueness within applicable Tenant/namespace, no cross-Tenant global deduplication or definite-conflict override. Basic matching signals warn except definite verified conflicts; multi-signal priority higher without invented scoring. Official name/identifier/type/issuer changes require reason; reverification follows material evidence impact, including contact facts when part of verification basis.
- CM1-PD-086: ordinary Relationship Person/target/Role identity immutable; END+new is the correction path, not in-place replacement. Manual END reason and Audit mandatory; natural expiry has no manually supplied reason obligation. Calendar-day [start,end), future starts/open ends allowed; exact time reference and calendar presentation/storage remain OPEN. Inactive Person/Company/Branch cannot receive new operational assignment; preserve existing history, no retrospective assignment workflow authorized. Existing controlled overlap, fresh reason, no supervisor, Tenant/version/conflict-set/idempotency guards remain.
- CM1-PD-087/088: applicable open opportunities/contracts/orders/tickets/projects/tenders/delivery commitments/activities/follow-ups/active Branches/active Relationships block archive. Closed/history alone do not. Unknown/unavailable evidence cannot clear a dependency; do not fabricate service integrations. Deactivation still allowed with dependencies, now with required reason. Reactivation validates mandatory facts/definite conflicts/authority/Audit; ordinary reason optional; VERIFIED not universally required. ARCHIVED -> INACTIVE -> ACTIVE only; no automatic related-record activation.
- CM1-PD-089..091: valid evidence mandatory; contact/assertions alone insufficient. Logical evidence type/issuer/verifying authority/time/outcome/reference supplement earlier provenance/revision information. Different authorized verifier required after corrected verified identifier, definite-conflict resolution/verification, and fundamental-invalidity reverification. Ordinary independently authorized dual responsibility allowed. NOT_VERIFIED/VERIFIED/REQUIRES_REVERIFICATION remain independent of record lifecycle; fundamental invalidity -> NOT_VERIFIED, essential-evidence expiry/material change -> REQUIRES_REVERIFICATION, authorized fresh success -> VERIFIED. Dispute alone never restores VERIFIED; no universal TTL.
- CM1-PD-092..095: all Customer Master mutations and unauthorized mutation attempts require Audit, plus independently authorized/traceable evidence/Audit access. Ordinary reads gain no automatic product Audit obligation; original disclosure-denial/security obligations remain. Required reasons and logical safe Audit information: operation catalog and actor matrix. No successful/definite-success mutation report without guaranteed durable obligation; no executable continuation policy or automatic fail-open. ACK/outbox is not ingestion evidence. Preserve histories/evidence references under applicable policy, never infer unlimited personal retention. Role Catalog CM1-PD-073..077 remains authoritative, including its optional ordinary lifecycle reasons and mandatory incompatible-scope/publication reasons.

## Precise reconciliation of preserved history

All 77 prior decision objects remain unchanged. `refinementsV170` in PDR JSON records the exact narrowed/extended applicability, not silent rewriting. CM1-PD-085/092 refine PD-015's narrower identifier-only reading: official names/type/issuer are sensitive; specified lifecycle/END/revocation reasons are mandatory. Catalog lifecycle is NOT Customer/Branch lifecycle; catalog reason policy is unchanged.

All five canonical and 153 earlier detailed criterion definition lines remain unchanged. Their original remarks are historical where later product decisions answer a gap. Specifically:

- Canonical AC-03's preserved `Business Owner UNASSIGNED` describes the initial inventory; current accountable owner is Farzad, not an active unassigned-owner requirement. Formal canonical assessment remains for owner review; no canonical definition edited.
- CM1-REL-18's old parenthetical immutability question is answered by CM1-PD-086; new executable scenario criteria supplement it without editing the old line.
- CM1-VER-02 (system integration) and CM1-BRN-03 (transfer workflow) remain retained/deferred, not current execution evidence.
- CM1-AUD-05 retains its governing-source exception: CM1-PD-092 is now that explicit source for unauthorized mutation attempts/protected-access traceability, not blanket Audit of every rejected input/warning/read.
- Historical PDR `unresolved` strings contain duplicate legacy entries and answered owner/scope questions. They are provenance, not additional question IDs. The authoritative current per-question disposition is the 19-entry `questions` array in `customer-bounded-readiness.json`.

## All 19 OPEN question dispositions

Every question remains **OPEN**. Full per-question title, answered product portions, residual product/scope/technical/external dependencies, canonical task IDs and separate acceptance/implementation impacts are in `customer-bounded-readiness.json`. The table is a human summary, not a closure decision.

| Question ID | Answered / bounded | Residual acceptance or execution boundary |
| --- | --- | --- |
| PDQ-A001-001 | Farzad named Business Owner | Formal acceptance separate; no execution grant |
| PDQ-A001-002 | Five independent logical responsibilities; protected access traceable | Exact actor/operation/resource/field/warning/history/evidence disclosure and grants OPEN |
| PDQ-A001-003 | Included/conditional/deferred/excluded journeys and new behavior defined | Exact examples, validation/time/disclosure and legal boundaries remain |
| PDQ-A001-049 | Farzad interim accountable Audit policy authority | Technical ingestion/recovery and any bounded continuation policy OPEN |
| PDQ-A001-050 | Synthetic-only, no unlimited personal retention | Actual legal/contract/evidence applicability and durations/hold/disclosure OPEN |
| PDQ-A001-052 | Product operations and development-data boundary selected | Deployment profile and all nine branches OPEN; not waived |
| PDQ-A001-053 | Direct external Customer access excluded; real verification deferred | Future external scope/trust decisions retained |
| PDQ-002-01 | Minimum fields mapped, optional validation, identifier conditions | Exact unspecified observable validation/normalization and authoritative identifier facts OPEN |
| PDQ-002-02 | Dependency categories and reactivation guards/reasons | Archive conditional; applicability/clearance evidence and race-safe contracts OPEN |
| PDQ-002-03 | Basic signals/conflict/warning/priority and exception defined | Merge/deletion excluded; fuzzy deferred; detector/disclosure/concurrency contracts OPEN |
| PDQ-002-04 | Sensitive fields/reasons and Relationship editing/END/day rules | Exact day time reference, actors/disclosure, API/version/storage OPEN |
| PDQ-002-05 | Pending Submission/draft excluded from CM-1 | No new lifecycle necessary for this candidate; future scope separately decided |
| PDQ-002-06 | No success without durable obligation; unknown not success | No executable continuation approved; actual failure/ingestion/recovery contracts OPEN |
| PDQ-002-07 | Six identifier concepts, extensible multi-ID Tenant+namespace model | Exact namespaces/legal formats/issuer validity/technical enforcement OPEN |
| PDQ-002-08 | PRODUCT_READY_TECHNICAL_OPEN within approved catalog scope | All RC-OPEN contracts retained; no policy reopened or question closed |
| PDQ-002-09 | Transfer semantics preserved | Executable coordination deferred; succession optional/future |
| PDQ-002-10 | All mutation/unauthorized-attempt Audit, reasons/information, interim owner | Transactions/events/ingestion/recovery/access contracts OPEN |
| PDQ-002-11 | Three mandatory different-verifier cases, evidence and dispute policy | Manual verification conditional; evidence/issuer/legal/extra SoD/actor bindings OPEN |
| PDQ-002-12 | Controlled overlap behavior preserved | Technical conflict-set/locking/token/idempotency OPEN; day reference tracked under PDQ-002-04 |

## Remaining acceptance blockers and review decision

Prepared for separate formal owner review, **not unconditionally ready for acceptance/implementation**. Owner accountability, broad scope and main product behavior gaps are answered. Residual blockers to exact selected-operation/profile acceptance are:

1. Exact actor/disclosure boundaries and approved examples; logical responsibilities do not authorize data access.
2. Deployment profile and all nine conditional branch dispositions.
3. Explicit Relationship calendar-day time reference.
4. Unspecified observable validation rules where needed, exact issuer/evidence acceptance and legal/retention/disclosure applicability; manual verification remains conditional and real data/documents forbidden.
5. Applicable archive dependency clearance evidence; unavailable/unknown is blocked, not assumed clear.
6. Separate explicit owner acceptance of exact deliverables, evidence, retained OPENs and bounded exclusions.

Technical design residuals alone need not block acceptance of already approved isolated product rules. A future owner decision may accept an explicitly bounded subset while retaining unresolved operations blocked; this task makes no such acceptance, profile choice, waiver or executable policy. No unresolved behavioral contradiction was silently resolved; missing details above remain OPEN. No external approval authority or legal format fabricated.

## Canonical downstream disposition and F-000 prerequisites

Canonical source: `architecture/product-planning/V3-PRODUCT-PLAN-003/execution-roadmap.json`, with V3-PRODUCT-PLAN-004 acceptance overlay. The machine-readable `downstreamTasks` list mirrors exact canonical IDs/titles. These are disposition/ownership references, NOT invented dependency edges.

- K-001 contract design requires A-002 and A-003 directly, explicit design authorization, approved rules and effective OD-007 before first public contract.
- F-BJ-001 implementation directly requires A-002, C-003, C-004, C-005, D-003, A-017, F-000, K-001, E-000 and K-002. Applicable OD-013/014, actual favorable G-RUNTIME and explicit implementation/AUTH/FE-BE scopes still mandatory. E-003 is CM-1 exit evidence, not a newly added direct prerequisite.
- E-000 directly requires A-017/C-001; K-002 directly requires E-000/C-005/D-003. D-003 submission is not favorable Gate acceptance; D-002 is a tracking parent. No all-task or all-OD barrier introduced.

**V3-FR-F-000 — Implement isolated Customer domain rules candidate** has exactly one direct canonical prerequisite: **V3-FR-A-002 — Define requirements: Register and Maintain Customer Master**. Before starting, the applicable bounded A-002 rules must be accepted and exact independent-scope applicability/implementation approval supplied, including repository/files and validation boundaries. Pure isolated approved rules only; no Spring/persistence/API/trust/live data/runtime reliance or guessing OPEN rules. No blanket requirement to close every technical question first. It may later overlap independently authorized IAM/runtime work; it is **NOT AUTHORIZED OR STARTED HERE**.

## Gates unchanged

G-RUNTIME: BLOCKED; FE-BE: PENDING; AUTH/IAM: PENDING; Offline: PROHIBITED; Local-Infra: ACCEPTED — DEVELOPMENT-ONLY; Production: NOT AUTHORIZED; Formal acceptance: PENDING.
