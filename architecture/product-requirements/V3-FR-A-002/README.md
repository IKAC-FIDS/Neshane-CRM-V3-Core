# V3-FR-A-002 — Customer Master Product Decision Package v1.2.0

## Included
- The 13 original authoritative-source candidate files (requirements, operations, fields, business rules, lifecycle, actor policy, failure/deployment scenarios, acceptance criteria, open decisions, source-traceability, validation) are retained and reconciled in place.
- `customer-master-product-decision-record.md` and `.json` carry **57 user-confirmed product-direction decisions** (CM1-PD-001..028 + CM1-PD-029..057) plus a supersession record.
- `customer-field-and-verification-addendum.md` maps new decisions to candidate FLD-002-* definitions.
- `cm1-acceptance-criteria-addendum.md` adds proposed acceptance scenarios (CM1-FLD-*, CM1-VER-*, CM1-REL-*, CM1-BRN-*, CM1-AUD-*, CM1-DUP-*, CM1-LC-*, CM1-UPD-*); NOT EXECUTED.
- `sha256-manifest.json` captures integrity hashes (regenerated for v1.2.0).

## Key policy (user-confirmed, authoritative)
- Relationship overlap: same Person+TargetType+TargetId+RoleCode overlapping intervals are allowed only via controlled exception (warning + authority + mandatory reason + Audit). Distinct roles/targets/Company-vs-Branch overlap freely. This supersedes any absolute-overlap prohibition.
- Branch: subordinate to Company, immutable companyId, no direct reparenting (transfer = new Branch + deactivate original), only ACTIVE/INACTIVE states.
- Identity verification: NOT_VERIFIED/VERIFIED/REQUIRES_REVERIFICATION, independent of record lifecycle; no universal expiry; no implicit access.

## Governance
- All existing open-product-decisions entries remain OPEN (14 + 5 new); none closed.
- Not an approved DB design, IAM grant, API, or provider integration; does not authorize runtime/offline/production.
- G-RUNTIME BLOCKED, FE-BE & AUTH/IAM PENDING; no Git commit/push performed.
