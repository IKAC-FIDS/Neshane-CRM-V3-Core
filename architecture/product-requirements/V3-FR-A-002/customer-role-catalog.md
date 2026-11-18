# Relationship Role Catalog — v1.3.0 proposed package

## Authority and scope

- Task: `V3-FR-A-002`; Customer Master / Relationship / `PDQ-002-08`.
- Source: user conversation titled **V3-FR-A-002 — Role Catalog Product Decisions**, sections `CM1-PD-058..065` and Remaining OPEN Contracts.
- Authority: **USER-CONFIRMED PRODUCT DIRECTION**. Formal acceptance: **PENDING**. Not an approved executable API, persistence or IAM contract.
- Reviewed baseline: `5d9c2f491e24a5afdc8349fd067be982e1e64365`, branch `codex/v3-fr-a-002`; working tree initially clean.
- Recorded at: `2026-11-18T21:36:02.131992+00:00`. Owner issuance timestamp was not supplied; this is recording time only.
- Exact decisions are preserved in the Product Decision Record JSON (`CM1-PD-058..065`). The rules below organize them without expanding their authority.

## RC-001 — Hybrid catalog and organizational meaning

System-defined roles are shared across authorized Tenants; custom roles are owned by their respective Tenant. Roles describe organizational responsibilities, never IAM/RBAC grants (`CM1-PD-058`). Initial system vocabulary and exact codes remain OPEN; no example role names or permission grants are adopted here.

## RC-002 — Applicability

Every Role Definition has exactly one scope: `COMPANY`, `BRANCH` or `BOTH`. New Relationship assignments must satisfy the Role's current applicability scope (`CM1-PD-059`). Scope-change compatibility of existing Relationships follows RC-006, not automatic migration.

## RC-003 — Lifecycle

Exactly two states: `ACTIVE`, `INACTIVE` (`CM1-PD-060`).

| From | To | Guard / outcome |
| --- | --- | --- |
| Creation | ACTIVE | Valid Role; applicable validation and authorization |
| ACTIVE | INACTIVE | Authorized actor; applicable validation |
| INACTIVE | ACTIVE | Authorized actor; applicable validation |
| Either | Physical deletion | Not supported, including when no Relationships exist |

## RC-004 — Stable identity and history

`roleId` and `roleCode` are immutable after creation; physical deletion is not supported. Historical Role identities and references must be preserved (`CM1-PD-061`). Titles, lifecycle and scope changes preserve Role identity and historical Relationship references (`CM1-PD-065`). Exact fields, reference representation and historical display remain OPEN: this document does not select a Role table, foreign key, snapshot, code namespace or API shape.

## RC-005 — Relationship preservation

Role deactivation/reactivation must not create, terminate, reactivate, delete or modify existing Relationships. INACTIVE Roles are unavailable for new assignments; existing Relationships retain their own status, time intervals and historical references (`CM1-PD-062`). Reactivating a Role is not reactivation of an ENDED Relationship.

## RC-006 — Controlled scope changes

Authorized applicability changes are permitted (`CM1-PD-063`). If existing Relationships would become incompatible, evaluate the affected Relationships, show a disclosure-safe impact warning, capture a mandatory business reason, validate appropriate management authority, preserve existing Relationships unchanged, apply the new scope to subsequent assignments, and retain auditability of the change and justification. Do not implicitly change Person, Company, Branch or Relationship state.

Management authority is not inferred from CUS-CREATE or the ordinary overlap exception. The latter needs no separate supervisor approval; this scope-change decision explicitly requires appropriate management authority. Exact grants, evaluation consistency and operation-specific Audit failure/recovery remain OPEN. No additional supervisor workflow is invented.

## RC-007 — Authority and Tenant boundaries

System catalog authority governs System Roles; Tenant users cannot modify them. Each Tenant Role is owned by exactly one Tenant and managed only by appropriately authorized actors in that Tenant. Cross-Tenant access/references are prohibited unless a separate governing contract explicitly authorizes them; no such exception is granted by this package. Authorized shared System Role consumption under RC-001 is not authority to read another Tenant's custom roles. CUS-CREATE alone never grants catalog management authority (`CM1-PD-064`). Customer Domain remains authoritative writer and final resource/action authorizer with validated Tenant Context and fail-closed boundaries.

## RC-008 — Overlap and consistency boundaries

The controlled-exception policy `CM1-PD-033..041` remains authoritative. Role changes cannot bypass Relationship version checks, overlap authorization, Tenant isolation or mandatory Audit obligations (`CM1-PD-065`). Neither mutable titles nor catalog changes authorize bypass. Exact Role reference contract and technical overlap key require formal design approval; no switch from the existing conceptual Person+TargetType+TargetId+RoleCode key is approved here.

## RC-OPEN — Remaining OPEN Contracts

All remain under **OPEN / PARTIALLY ANSWERED `PDQ-002-08`**; affected executable design is blocked until separately dispositioned. Product policies above remain user-confirmed.

1. Initial standard System Role vocabulary and exact roleCode values.
2. Role code normalization and namespace enforcement.
3. Exact Role Definition field schema and persistence contract.
4. Role management operation and IAM permission contracts.
5. Concurrent updates and scope-change dependency consistency mechanism.
6. Role history representation and historical display contract.
7. Operation-specific Audit failure and recovery behavior (also `PDQ-002-10`).
8. Relationship temporal representation and API compatibility (also `PDQ-002-12` for overlap consistency).

See `cm1-acceptance-criteria-addendum.md#role-catalog-scenarios-v130` for proposed, unexecuted scenarios and the decision coverage matrix for each decision's residual gaps. No PDQ is closed.

## Governance preserved

`G-RUNTIME: BLOCKED`; `FE-BE: PENDING`; `AUTH/IAM: PENDING`; `Offline: PROHIBITED`; `Local-Infra: ACCEPTED — DEVELOPMENT-ONLY`; `Production: NOT AUTHORIZED`. Pending Submission remains PERMITTED NOT REQUIRED and non-authoritative. Existing coordinated durable Audit obligations remain unchanged; this task does not invent an operational Role Audit contract.
