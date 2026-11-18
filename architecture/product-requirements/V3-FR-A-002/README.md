# V3-FR-A-002 — Customer Master Product Decision Package v1.2.1

## Included
- Reconciled requirements, business rules, field dictionary, lifecycle (explicit source-baseline vs user-confirmed target), operation catalog, actor policy, failure/deployment scenarios, acceptance criteria, open decisions, source traceability.
- `customer-master-product-decision-record.md` / `.json`: 57 user-confirmed decisions (CM1-PD-001..057) plus supersession record.
- `customer-decision-coverage-matrix.md` / `.json`: coverage map of all 57 decisions (FULL=3, PARTIAL=47, DOCUMENTED_ONLY=5, BLOCKED_BY_OPEN_DECISION=2).
- `cm1-acceptance-criteria-addendum.md`: detailed CM1 acceptance criteria (all PROPOSED / NOT TESTED).
- `sha256-manifest.json`: integrity manifest (self-reference omitted by convention).

## Key policy (user-confirmed, authoritative)
- Relationship overlap: same Person+TargetType+TargetId+RoleCode overlapping intervals allowed only via controlled exception. Distinct roles/targets/Company-vs-Branch overlap freely. Supersedes any absolute-overlap prohibition.
- Branch: subordinate to Company, immutable companyId (Required/Immutable parent reference), no direct reparenting, only ACTIVE/INACTIVE.
- Identity verification: NOT_VERIFIED/VERIFIED/REQUIRES_REVERIFICATION, independent of record lifecycle; no universal expiry; no implicit access.

## Governance
- 19 OPEN questions (14 original + PDQ-002-08..12); 7 partial resolutions recorded; none closed.
- Not an approved DB design, IAM grant, API, or provider integration; does not authorize runtime/offline/production.
- G-RUNTIME BLOCKED, FE-BE & AUTH/IAM PENDING; no Git commit/push performed by this task.
