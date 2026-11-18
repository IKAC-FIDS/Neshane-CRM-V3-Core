# Optimized First Release proposed roadmap

**V3-PRODUCT-PLAN-002 — PROPOSED; planning review only.** No product implementation, architecture decision closure, tests, Docker, staging, commit or push. All V3-PRODUCT-PLAN-001 files remain unchanged. This is an alternative proposal, not an approved replacement.

## Optimization rule

Prefer one complete Customer Management vertical slice over layer-only/global batches, but do not invent fields, CRUD rules, roles, lifecycles, deletion/merge behavior, identity technology or failure policies. FR-BJ-001 and FR-BJ-002 approved scope supports a create/maintain/find/review candidate. Its detailed requirements remain OPEN. All fifteen approved capabilities and all three production profiles remain First Release obligations; the first synthetic milestone is not full product release or production acceptance.

## Incremental sequence

1. Parallel selected requirements A-002/A-003/A-007/A-013/A-015, actor ownership A-001, bounded integration/failure policies A-017, framework-neutral G-001, security criteria I-001 and applicability D-001/B-024.
2. Parallel applicable OD evidence preparation (not all ODs): trusted access/custody, migration/RLS, Frontend/public boundary and Customer search. C-001/E-000/K-001 refine provider-owned contracts. F-000 pure domain candidate after approved rules and independent-scope permission; no live data/path.
3. Separately approved IAM children C-003/004/005 and Runtime remediation D-004/005/006 can overlap with approved interfaces/fixtures. Final D-002 roll-up requires actual integrated paths and all applicable verification obligations, no simulated identity substitute. D-003 merely submits; distinct favorable Gate decision is mandatory before accepted Runtime reliance.
4. Implement selected Customer provider writes/read/search, G-003/004 client, E-003 Audit, K-002 reliable producer/consumer and E-001 safe signals after their own policies/controls. K-003 only if effective OD-007 strategy selects a public composition component. Work split does not create one service per capability or merge Identity/Tenant/Audit/Customer authority.
5. H-001 real synthetic vertical slice and I-003 security evidence run per ready path. A Tenant switch must not leak prior-Tenant data. Customer mutation and durable Audit obligation must be coordinated; ACK is not ingestion; failure policy must be explicitly approved, no automatic DURABLE_DEFER.
6. Sales/Request/Work and platform paths proceed independently after their own rules and actual dependencies. G-005, H-003/004, I-004 are rolling scopes: each execution request must name a bounded path and exact real components; final parents retain all-15/profile coverage. No giant final batch required before assessing an available path.
7. J-005/006/007 separately implement and verify approved profile release/recovery controls; final J-001/002/003 dossiers and J-004 decision request retain all mandatory security, measured objectives and distinct release permissions. Early runbook/criteria drafting need not wait for all product code; final evidence uses final approved candidates.

## Preserved mandatory gates

G-RUNTIME BLOCKED; AUTH/IAM and FE-BE PENDING. Neither task completion, document acceptance, local container success, nor an owner review converts failed/unexecuted evidence into PASS. Readiness/Gate acceptance and permission to execute remain separate. All 36 gaps, 32 residual/obligation records, 11 dependency groups and 79 underlying Runtime items remain; RT-002 scope conflict, five PARTIAL requirements, GS-01/04, TI-14, actual Java/RLS/pool/IAM integration, routing/fencing, lifecycle and freshness obligations are not waived. Four raw SESSION-GUC FAILs remain with applicability to establish, not automatic standalone blockers. Offline continuation PROHIBITED. No production authorization.

## Scope-conditional decisions

OD-005/006 before affected Frontend code; OD-007 before first public contract; OD-009/010/011/012 before corresponding selected trust/session/custody implementation; OD-013 before owned migrations; OD-014 before tenant-aware repository; OD-018 before search-dependent implementation, not an external engine mandate. OD-015 before affected deployment implementation, OD-023 before production architecture sign-off and earlier where a selected security/numeric policy is required. OD-017 for File/object content or selected report artifact storage; OD-019 only where selected durable-job behavior needs it. B-001/016/021/022 are conditional/future task records, not Customer prerequisites. No new OD is closed or alternative selected.

## Where to review

`complete-task-table.md` is the full human-readable 90-record inventory (67 originals + 23 proposed children/additions), with sequence, workstream, objective/scope, repository, prerequisites, deliverables, acceptance, blockers, authority, disposition and parallel eligibility. `optimized-task-inventory.json` retains references/exclusions. `original-task-review.json` and its Markdown companion contain nine-dimension assessments of each original task. Display sequence is not a mandatory sequential schedule, approval, staffing assignment or time estimate.
