# V3-FR-A-002 — Customer Master Product Decision Package v1.3.0 (PROPOSED)

## Included
- Reconciled requirements, business rules, field dictionary, lifecycle (explicit source-baseline vs user-confirmed target), operation catalog, actor policy, failure/deployment scenarios, acceptance criteria, open decisions, source traceability.
- `customer-master-product-decision-record.md` / `.json`: 65 user-confirmed decisions (CM1-PD-001..065) plus supersession record; formal acceptance PENDING.
- `customer-role-catalog.md`: CM1-PD-058..065 policy and exact residual contracts; Role Definitions are organizational responsibilities, not IAM/RBAC grants.
- `customer-decision-coverage-matrix.md` / `.json`: coverage map of all 65 decisions (FULL=3, PARTIAL=55, DOCUMENTED_ONLY=5, BLOCKED_BY_OPEN_DECISION=2). Eight Role decisions are PARTIAL because executable contracts remain OPEN.
- `cm1-acceptance-criteria-addendum.md`: detailed CM1 acceptance criteria (all PROPOSED / NOT TESTED).
- Inventory: 5 canonical + 99 detailed = 104 unique criteria; 16 new CM1-ROL-01..16 scenarios, none executed.
- `sha256-manifest.json`: integrity manifest (self-reference omitted by convention).

## Key policy (user-confirmed, authoritative)
- Relationship overlap: same Person+TargetType+TargetId+RoleCode overlapping intervals allowed only via controlled exception. Distinct roles/targets/Company-vs-Branch overlap freely. Supersedes any absolute-overlap prohibition.
- Branch: subordinate to Company, immutable companyId (Required/Immutable parent reference), no direct reparenting, only ACTIVE/INACTIVE.
- Identity verification: NOT_VERIFIED/VERIFIED/REQUIRES_REVERIFICATION, independent of record lifecycle; no universal expiry; no implicit access.

## Governance
- 19 OPEN questions (14 original + PDQ-002-08..12); 8 partial resolutions recorded (including PDQ-002-08); none closed.
- Not an approved DB design, IAM grant, API, or provider integration; does not authorize runtime/offline/production.
- G-RUNTIME BLOCKED, FE-BE & AUTH/IAM PENDING; no Git commit/push performed by this task.
- Offline PROHIBITED; Local-Infra ACCEPTED — DEVELOPMENT-ONLY; Production NOT AUTHORIZED. Pending Submission PERMITTED NOT REQUIRED, non-authoritative. No runtime, architecture, IAM, or formal requirements acceptance is inferred.
