# Proposed critical path and concurrency

**PROPOSED — NOT AUTHORIZED.** Dependency order is not a duration estimate. No single global freeze is proposed.

## First Customer end-to-end path

V3-FR-A-001 → V3-FR-A-002/A-003 (Customer rules/search) and A-007 (trusted access) → A-017 (selected integration/failure policies) → C-001 and E-000 contracts. Parallel B-009/010/011/012 (IAM), B-013/014 (migration/RLS), B-007 (public boundary) and B-005/006 (Frontend) must reach their affected milestones.

D-001 resolves the RT-002 scope conflict and maps actual accepted control paths; C-002 and approved D-002 remediation then provide real evidence → D-003 reassessment. Only an explicit satisfactory Gate decision clears relying paths; D-003 task completion alone does not. F-BJ-001 and F-BJ-002 plus E-SO-001/E-SO-003 and G-002 → H-001. Approved capability-to-eligibility/quota matrices determine whether E-PF-002/003 join this first slice; do not assume either mandatory per operation or safely omitted.

## Parallel workstreams

- All fifteen requirements packages after actor/owner framing; common policy questions feed A-017.
- Provider-neutral IAM design, framework-neutral UX G-001, Audit/event contract design, OD alternatives and security acceptance design I-001 can be proposed independently of accepted Runtime enforcement.
- Once separately approved rules exist, F-000 pure Customer domain model is an independently implementable candidate with no live/persistence/trust adapter. It still needs explicit scope authorization, not granted here.
- Frontend fixture-only module work may be separately proposed after framework and contract decisions; G-002 is not automatically authorized and live requests remain blocked by actual dependencies.
- Later Sales/Request/Work can proceed in parallel after their own requirements and shared control prerequisites; no unnecessary File, Reports or advanced workflow coupling.

## Dependency classes

Cross-cutting A-017 and E-000 deliver incremental, explicitly bounded approvals for the selected slice. Completion of every other capability's requirements is not a blanket prerequisite; pending integrations remain OPEN individually. OD-019 is conditional on durable scheduling, OD-017 on File/object or selected artifact storage, and OD-018 on approved search/query requirements. Raw OD references in task blockers must be read with the per-path classifications in the dependency matrices, not as mandatory external technology selections.

IAM-dependent: protected sessions, Membership/context, user/workload calls and privileged paths. Runtime-dependent: tenant-aware persisted data, actual pools/RLS, routing/fencing and live E2E. Production-dependent: profile deployment/recovery, custody, supply-chain enforcement, measured objectives, readiness/release; not ordinary requirements work. Optional/future: Air Gap OD-001, plugin hosting/marketplace OD-016/021 and placement migration OD-022 unless explicitly selected. Scheduling OD-019 applies only to selected durable-job paths.

## Runtime residual obligations

Preserve 36 gaps, 32 residual/obligation records, 11 dependency groups and 79 undecided items from G-RUNTIME.04. Five mandatory verification requirements remain PARTIAL. Raw four SESSION-GUC FAILs remain supporting evidence requiring accepted-path applicability, not automatic standalone blockers; private safe-path PASS is not production-pool proof. GS-01, GS-04, TI-14 and OF-006/10 remain unresolved; no offline continuation. Routing requires independently validated destination and no unauthorized forwarding; generation fencing must prevent an old validated mutation committing after a new fence. Credential lifecycle must distinguish replacement from emergency containment and address sessions/transactions/pools and unknown outcomes.
