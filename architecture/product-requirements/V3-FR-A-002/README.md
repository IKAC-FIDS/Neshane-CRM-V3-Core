# V3-FR-A-002 — Customer Master Product Decision Package v1.4.0 (PROPOSED)

## Included
- Reconciled requirements, business rules, field dictionary, lifecycle (explicit source-baseline vs user-confirmed target), operation catalog, actor policy, failure/deployment scenarios, acceptance criteria, open decisions, source traceability.
- `customer-master-product-decision-record.md` / `.json`: 67 user-confirmed decisions (CM1-PD-001..067) plus supersession record; formal acceptance PENDING. Original 65 decision objects preserved.
- `customer-role-catalog.md`: CM1-PD-058..067 policy and residual contracts; RC-009 holds the exact 12-entry initial System Role Vocabulary v1.0, mirrored in PDR JSON catalogEntries. Roles describe organizational responsibilities, not IAM/RBAC grants or verified legal representation.
- `customer-decision-coverage-matrix.md` / `.json`: all 67 decisions (FULL=3, PARTIAL=57, DOCUMENTED_ONLY=5, BLOCKED_BY_OPEN_DECISION=2). Two new decisions PARTIAL because executable/governance contracts remain OPEN, not because initial vocabulary/selectability policy is unanswered.
- `cm1-acceptance-criteria-addendum.md`: detailed CM1 acceptance criteria (all PROPOSED / NOT TESTED).
- Inventory: 5 canonical + 112 detailed = 117 unique criteria. Added CM1-ROL-17..29; five canonical and CM1-ROL-01..16 unchanged. All new criteria PROPOSED / NOT TESTED; contract-dependent execution BLOCKED pending design.
- `sha256-manifest.json`: integrity manifest (self-reference omitted by convention).

## Key policy (user-confirmed, authoritative)
- Tenant System Role hide/unhide restricts new assignments locally; it does not edit/deactivate global Roles, alter other Tenants, mutate existing Relationships or hide otherwise authorized history. Customer Domain enforces global ACTIVE + scope + Tenant selectability + Relationship authority and existing guards, including concurrency. No Tenant override of global lifecycle/scope.
- Initial vocabulary is not exhaustive; no exclusive PRIMARY_CONTACT, automatic CEO/BOARD_MEMBER authority, English title, global roleId or seed/migration choice is inferred. Ordinary hide/unhide reason policy and default selectability remain OPEN, not inherited from incompatible scope changes.
- Relationship overlap: same Person+TargetType+TargetId+RoleCode overlapping intervals allowed only via controlled exception. Distinct roles/targets/Company-vs-Branch overlap freely. Supersedes any absolute-overlap prohibition.
- Branch: subordinate to Company, immutable companyId (Required/Immutable parent reference), no direct reparenting, only ACTIVE/INACTIVE.
- Identity verification: NOT_VERIFIED/VERIFIED/REQUIRES_REVERIFICATION, independent of record lifecycle; no universal expiry; no implicit access.

## Governance
- 19 OPEN questions (14 original + PDQ-002-08..12); 8 partial resolutions recorded (including PDQ-002-08); none closed.
- Not an approved DB design, IAM grant, API, or provider integration; does not authorize runtime/offline/production.
- G-RUNTIME BLOCKED, FE-BE & AUTH/IAM PENDING; no Git commit/push performed by this task.
- Offline PROHIBITED; Local-Infra ACCEPTED — DEVELOPMENT-ONLY; Production NOT AUTHORIZED. Pending Submission PERMITTED NOT REQUIRED, non-authoritative. No runtime, architecture, IAM, or formal requirements acceptance is inferred.
