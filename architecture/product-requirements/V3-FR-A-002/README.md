# V3-FR-A-002 — Customer Master Product Decision Package v1.5.0 (PROPOSED)

## Included
- Reconciled requirements, business rules, field dictionary, lifecycle (explicit source-baseline vs user-confirmed target), operation catalog, actor policy, failure/deployment scenarios, acceptance criteria, open decisions, source traceability.
- `customer-master-product-decision-record.md` / `.json`: 72 user-confirmed decisions (CM1-PD-001..072) plus supersession record; formal acceptance PENDING. Original 67 decision objects preserved.
- `customer-role-catalog.md`: Role policy through CM1-PD-072; RC-009's exact 12-entry System vocabulary v1.0 and PDR JSON catalogEntries unchanged. RC-012..016 confirm defaults, canonical uniqueness, permanent reservation, future collision gate and basic normalization; implementation remains OPEN. Roles grant no IAM/RBAC or verified legal authority.
- `customer-decision-coverage-matrix.md` / `.json`: all 72 decisions (FULL=3, PARTIAL=62, DOCUMENTED_ONLY=5, BLOCKED_BY_OPEN_DECISION=2). Five new decisions PARTIAL due to explicit technical/operational gaps, not unanswered product policy. No earlier coverage class promoted.
- `cm1-acceptance-criteria-addendum.md`: detailed CM1 acceptance criteria (all PROPOSED / NOT TESTED).
- Inventory: 5 canonical + 128 detailed = 133 unique criteria; added CM1-ROL-30..45 (16). All previous definition lines, including five canonical and CM1-ROL-01..29, unchanged. New criteria PROPOSED / NOT TESTED; software execution BLOCKED pending design.
- `sha256-manifest.json`: integrity manifest (self-reference omitted by convention).

## Key policy (user-confirmed, authoritative)
- Tenant System Role hide/unhide restricts new assignments locally; it does not edit/deactivate global Roles, alter other Tenants, mutate existing Relationships or hide otherwise authorized history. Customer Domain enforces global ACTIVE + scope + Tenant selectability + Relationship authority and existing guards, including concurrency. No Tenant override of global lifecycle/scope.
- Initial vocabulary is not exhaustive; no exclusive PRIMARY_CONTACT, automatic CEO/BOARD_MEMBER authority, English title, global roleId or seed/migration choice. Ordinary hide/unhide reason policy stays OPEN and is not inherited from incompatible scope changes. Default selectability is now product-confirmed (CM1-PD-068), not its storage/materialization.
- Globally ACTIVE System Roles default selectable in new Tenants/new releases, subject to guards; preserve prior Tenant settings and existing Relationships. Canonical codes are System-global versus owning-Tenant unique and permanently reserved; independent Tenants may share custom codes. Conflicting new System Role publication is blocked without automatic data mutation or private-data access grant; unrelated releases are not automatically blocked. Normalize trim-uppercase then ASCII A-Z/0-9/underscore, length 3..64; no extra first-letter/underscore-placement grammar. Unicode/encoding, enforcement/concurrency and publication/resolution mechanics remain OPEN.
- Relationship overlap: same Person+TargetType+TargetId+RoleCode overlapping intervals allowed only via controlled exception. Distinct roles/targets/Company-vs-Branch overlap freely. Supersedes any absolute-overlap prohibition.
- Branch: subordinate to Company, immutable companyId (Required/Immutable parent reference), no direct reparenting, only ACTIVE/INACTIVE.
- Identity verification: NOT_VERIFIED/VERIFIED/REQUIRES_REVERIFICATION, independent of record lifecycle; no universal expiry; no implicit access.

## Governance
- 19 OPEN questions (14 original + PDQ-002-08..12); 8 partial resolutions recorded (including PDQ-002-08); none closed.
- Not an approved DB design, IAM grant, API, or provider integration; does not authorize runtime/offline/production.
- G-RUNTIME BLOCKED, FE-BE & AUTH/IAM PENDING; no Git commit/push performed by this task.
- Offline PROHIBITED; Local-Infra ACCEPTED — DEVELOPMENT-ONLY; Production NOT AUTHORIZED. Pending Submission PERMITTED NOT REQUIRED, non-authoritative. No runtime, architecture, IAM, or formal requirements acceptance is inferred.
