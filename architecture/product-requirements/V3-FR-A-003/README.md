# V3-FR-A-003 — Find and Review Customer

Status: requirements candidate for bounded owner review; D01–D20 explicitly confirmed in conversation on 2026-11-20 (Asia/Tehran). This is not acceptance of executable software. Target Core baseline: main `2df1f496b68b0e91a75591a56c5cb8ac4f3204e0` (observed). Business Owner: Farzad. Technical implementation: software development team, subject to separate authorization.

Capability FR-BJ-002, CM-1. Parent roadmap APP-CRM.01. The accepted A-002 v1.8.0 requirements and later addenda remain authoritative. This package covers authorized search and retrieval only, not writes, API contracts, implementation, IAM grants, or production.

## Deliverables

| File | Purpose |
|---|---|
| customer-search-requirements.md | Operations, scope, logical inputs/outputs, states, query UX |
| searchable-field-catalog.md | Field allowlist and restrictions |
| filtering-matching-sorting.md | Search and paging behavior |
| customer-360-requirements.md | Profile sections and resource boundaries |
| access-disclosure-matrix.md | Logical responsibilities and field/resource policies |
| audit-failure-policies.md | Audit, failures, isolation and profile scenarios |
| acceptance-criteria.md | Criterion mapping and non-executed examples |
| product-decision-record.md | Confirmed decisions, open questions and source traceability |

Sources: `../../product-planning/V3-PRODUCT-PLAN-003/execution-roadmap.md` (A-003); `../V3-FR-A-002/acceptance-decision.md`, `actor-resource-policy-matrix.md`, `customer-operation-catalog.md`; `../../../deployment/support-matrix.md` §5 FR-BJ-002 and §11 Option B; `../../task-governance.md`. No core source files altered. K-001 remains separately authorized and blocked for affected unresolved rules. G-RUNTIME BLOCKED; FE-BE and AUTH/IAM PENDING; offline prohibited; production not authorized.
