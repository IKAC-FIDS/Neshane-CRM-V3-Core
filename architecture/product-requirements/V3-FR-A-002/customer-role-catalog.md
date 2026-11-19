# Relationship Role Catalog — v1.5.0 proposed package

## Authority and scope

- Task: `V3-FR-A-002`; Customer Master / Relationship / `PDQ-002-08`.
- Source: user conversation titled **V3-FR-A-002 — Role Catalog Product Decisions**, sections `CM1-PD-058..065` and Remaining OPEN Contracts.
- Authority: **USER-CONFIRMED PRODUCT DIRECTION**. Formal acceptance: **PENDING**. Not an approved executable API, persistence or IAM contract.
- Reviewed baseline: `5d9c2f491e24a5afdc8349fd067be982e1e64365`, branch `codex/v3-fr-a-002`; working tree initially clean.
- Recorded at: `2026-11-18T21:36:02.131992+00:00`. Owner issuance timestamp was not supplied; this is recording time only.
- Exact v1.3.0 decisions are preserved in the Product Decision Record JSON (`CM1-PD-058..065`). The rules below organize them without expanding their authority.
- v1.4.0 source: user task **Codex Task — V3-FR-A-002 / Customer Master v1.4.0**, CM1-PD-066/067 and Proposed supplementary governance rules. Authority: USER-CONFIRMED PRODUCT DIRECTION; formal requirements acceptance PENDING.
- v1.4.0 reviewed baseline: `41a0620ba8216cc86afcccfccbb849ee5e33782e`, branch `codex/v3-fr-a-002`, initially clean working tree/index. Recording time: `2026-11-18T22:09:06.916567+00:00`; owner issuance time not supplied. Earlier baseline/timestamp above remain historical v1.3.0 provenance.
- v1.5.0 source: user task **Codex Task — V3-FR-A-002 / Customer Master v1.5.0**, exact decisions CM1-PD-068..072 and OPEN contracts. Authority: USER-CONFIRMED PRODUCT DIRECTION; formal acceptance PENDING. Reviewed baseline `92d02d2c45103d5223e5d9ffd7a6bafc556e3443`, branch `codex/v3-fr-a-002`, initially clean worktree/index. Recorded at `2026-11-18T22:41:53.576356+00:00`; issuance time not supplied. Previous authority/baselines remain historical.

## RC-001 — Hybrid catalog and organizational meaning

System-defined roles are shared across authorized Tenants; custom roles are owned by their respective Tenant. Roles describe organizational responsibilities, never IAM/RBAC grants (`CM1-PD-058`). Initial System Role Vocabulary v1.0 is now user-confirmed by CM1-PD-066 (RC-009); the earlier vocabulary-as-OPEN position is partially answered, not a closure of PDQ-002-08. Availability for new assignments depends on effective eligibility (RC-011).

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

Vocabulary/selectability product answers are in RC-009..011 below; defaults, uniqueness, permanent reservation, future-collision blocking and basic normalization are now **ANSWERED at product level** by CM1-PD-068..072 / RC-012..016. Earlier v1.4.0 blanket OPEN wording for those policies is updated here; no PDQ is closed.

All remain under **OPEN / PARTIALLY ANSWERED `PDQ-002-08`**; affected executable design is blocked until separately dispositioned. Product policies above remain user-confirmed.

1. Exact catalog schema/configuration persistence, provisioning/default materialization and publication/migration mechanisms; initial vocabulary and default policy are answered, not an executable design.
2. System/Tenant namespace enforcement implementation, concurrent uniqueness/reservation consistency and technical normalization/Unicode/input-encoding edge cases. Basic ASCII output/length/trim-uppercase product policy is answered.
3. Exact Role Definition field schema and persistence contract.
4. Role management and Tenant-selectability operation/IAM permission contracts; exact permissions and Audit event names.
5. Concurrent updates, scope-change dependencies and selectability/assignment finalization consistency mechanism.
6. Role history representation and historical display contract.
7. Operation-specific Audit failure and recovery behavior (also `PDQ-002-10`).
8. Relationship temporal representation and API compatibility (also `PDQ-002-12` for overlap consistency).
9. Cross-Tenant conflict detection authorization/privacy, catalog version publication/rollback and explicitly authorized collision-resolution workflow. The conflicting new Role is blocked at product level; access authorities and resolution/publication mechanics remain OPEN. Ordinary hide/unhide mandatory-reason policy also remains OPEN; RC-006's scope-change reason is not imported.

See `cm1-acceptance-criteria-addendum.md#role-catalog-scenarios-v130` for proposed, unexecuted scenarios and the decision coverage matrix for each decision's residual gaps. No PDQ is closed.

## RC-009 — Initial System Role Vocabulary v1.0

**CM1-PD-066 — USER-CONFIRMED PRODUCT DIRECTION; formal acceptance PENDING.** These exact 12 entries are the initial vocabulary, not the complete future role universe. Machine-readable counterpart: `customer-master-product-decision-record.json`, decision CM1-PD-066 `catalogEntries`; documentation data only, not a seed or executable schema.

| roleCode | titleFa | applicableScope |
| --- | --- | --- |
| CEO | مدیرعامل | COMPANY |
| BOARD_MEMBER | عضو هیئت‌مدیره | COMPANY |
| BRANCH_MANAGER | مدیر شعبه | BRANCH |
| GENERAL_MANAGER | مدیر / مسئول واحد | BOTH |
| PRIMARY_CONTACT | رابط اصلی | BOTH |
| SALES_CONTACT | رابط امور فروش | BOTH |
| TECHNICAL_CONTACT | رابط فنی | BOTH |
| SUPPORT_CONTACT | رابط پشتیبانی | BOTH |
| PROCUREMENT_CONTACT | مسئول خرید و تدارکات | BOTH |
| CONTRACT_CONTACT | مسئول امور قراردادها | BOTH |
| TENDER_CONTACT | مسئول امور مناقصات | BOTH |
| LEGAL_CONTACT | رابط حقوقی | BOTH |

Codes, Persian titles and scopes are preserved exactly. All are System Roles available to authorized Tenants subject to effective selectability. They describe organizational Relationships, not security permissions or verified legal representation. A Person may hold multiple independent roles; PRIMARY_CONTACT is not made exclusive. CEO, BOARD_MEMBER and other titles confer no automatic authority. Identity/code immutability and no physical deletion remain authoritative. No English title is confirmed or required. No global fixed roleId, database seed, migration, publication or deployment mechanism is selected.

## RC-010 — Tenant-specific System Role selectability

**CM1-PD-067 — USER-CONFIRMED PRODUCT DIRECTION; formal acceptance PENDING.** An appropriately authorized actor in a Tenant may make an otherwise eligible System Role unavailable for new assignments in that Tenant, then make it selectable again. This is an assignment restriction, **not global Role deactivation** or definition editing.

- Do not modify the global System Role Definition, global status, scope, roleId or roleCode; do not affect other Tenants. Tenant users still cannot edit System Role Definitions.
- Do not create, modify, terminate, delete or reactivate existing Relationships; preserve ACTIVE/ENDED statuses, intervals, history and references. Non-selectability must not hide historical Role references from otherwise authorized historical viewers.
- Require validated Tenant context and applicable management authority. CUS-CREATE alone is insufficient; no IAM/RBAC permission is granted by this setting.
- The authoritative Customer Domain must enforce the restriction, not UI filtering alone. Management/warning/assignment responses must not disclose another Tenant's settings or Relationships.
- Restoring Tenant selectability does not reactivate a globally INACTIVE System Role or reopen an ENDED Relationship. No Tenant override of global lifecycle or applicableScope is permitted.
- Whether ordinary hide/unhide requires a reason is OPEN. The mandatory reason for incompatible scope changes (RC-006) is not imported into this different operation.

## RC-011 — Effective new-assignment eligibility

For a System Role, all relevant conditions must pass together: global ACTIVE status; current applicability to target COMPANY/BRANCH; selectability in the current Tenant; required Relationship-operation authority; and existing Tenant, validation, concurrency and controlled-overlap guards. These are necessary conditions, not a replacement for owning-Domain authorization or an exhaustive executable contract.

| Global status | Applicable to target | Tenant selectable | Other required guards | New assignment |
| --- | --- | --- | --- | --- |
| ACTIVE | Yes | Yes | Pass | Eligible under the confirmed product policy |
| INACTIVE | Any | Any | Any | Not eligible; no Tenant override |
| ACTIVE | No | Any | Any | Not eligible; no Tenant scope override |
| ACTIVE | Yes | No | Any | Not eligible, including direct API attempts |
| ACTIVE | Yes | Yes | Fail | Not eligible |

If a Role becomes non-selectable while an assignment is finalized, it must not accept the assignment against an invalid effective state. Exact concurrency/consistency enforcement is OPEN; no token, lock, transaction shape or last-write-wins mechanism is chosen. Missing Tenant context fails closed under existing invariants. Default selectability is now confirmed in RC-012; exact setting/default representation and materialization remain OPEN, not an authorization bypass. A permitted selection is not proof of legal representation or authority to perform a business action.

## RC-PROPOSED — Supplementary governance proposals, not confirmed rules

Historical proposals for default selectability, role-code uniqueness, permanent reservation, future System collisions and basic normalization/length are now product-level ANSWERED in RC-012..016, not still undecided. The remaining PROPOSED / OPEN design choices are exact configuration names/storage/materialization, namespace/index/tombstone/consistency mechanisms, Unicode trim/uppercase/input encoding edge cases and any further lexical grammar, cross-Tenant detection authorization/privacy, catalog release/version/rollback and authorized resolution mechanics, exact permissions/Audit events, and ordinary hide/unhide mandatory-reason policy. No start-letter requirement or ban on consecutive/leading/trailing underscores is confirmed. Optional English titles remain metadata only. No implementation option, event name or hide/unhide reason requirement is adopted.

New vocabulary/selectability scenarios: `cm1-acceptance-criteria-addendum.md#vocabulary-and-tenant-selectability-scenarios-v140`. Contract-dependent software scenarios are explicitly BLOCKED pending executable design.

## RC-012 — Default System Role selectability

CM1-PD-068: new Tenants receive default selectability of all globally ACTIVE System Roles, subject to applicability, operation authority and other existing guards. Newly released globally ACTIVE System Roles are selectable by default in existing Tenants. Authorized managers may subsequently hide/unhide under CM1-PD-067; established settings survive catalog releases. Global INACTIVE always prevents assignment. Neither defaulting nor publication changes existing Relationships. No storage, Tenant provisioning, migration or default-materialization mechanism is selected.

## RC-013 — Canonical uniqueness and namespace scope

CM1-PD-069: System codes are unique globally within the System Catalog and reserved against Tenant Roles. Tenant Roles cannot use canonical codes of existing or permanently reserved System Roles. Custom codes are unique within their owning Tenant, including inactive/historical reservations; separate Tenants may use the same custom code, with independent Role identities, ownership and Relationships. All comparisons use CM1-PD-072 canonical normalization. No global ban on matching custom codes across independent Tenants and no disclosure/authorization exception is introduced.

## RC-014 — Permanent reservation and identity

CM1-PD-070: an assigned roleCode stays permanently reserved in its applicable ownership/namespace scope, including INACTIVE and historical Roles, and cannot be reassigned to a different Role. Deactivate/reactivate preserves roleId and roleCode. No physical deletion (CM1-PD-061); historical Relationship references survive. No tombstone table, index or retention mechanism is chosen. A matching custom code in a different Tenant is not a reuse within the original Tenant's namespace.

## RC-015 — Future System Catalog collision gate

CM1-PD-071: before releasing a new System code, assess conflicts with existing/historically reserved Tenant codes across relevant Tenants using canonical comparisons. A conflict blocks publication of **that new System Role** until explicitly authorized resolution; it does not impose a blanket block on unrelated catalog changes/releases. Never automatically rename, delete, convert or reassign Tenant Roles or migrate, terminate or modify existing Relationships. Choosing a different proposed System code is a valid non-destructive option. Cross-Tenant detection authorities/privacy, authorized resolution and publication/rollback mechanics remain OPEN. Central catalog administration alone does not authorize inspection of Tenant-private data.

## RC-016 — Canonical normalization and validation

CM1-PD-072: trim leading/trailing whitespace, uppercase letters, then validate the normalized output: only ASCII A-Z, 0-9 and underscore; length **3..64 inclusive**. Use this canonical value for uniqueness/reservation and preserve immutability after creation. These are product constraints, not an approved API or normalization library.

| Incoming roleCode | Canonical result / outcome |
| --- | --- |
| ` technical_contact ` | `TECHNICAL_CONTACT`, valid |
| `CEO` | `CEO`, lexically valid |
| `ceo` | `CEO`, canonical collision with existing System Role, not a distinct code |
| `BRANCH-MANAGER` | Invalid: hyphen not allowed |
| `مدیر_شعبه` | Invalid: non-ASCII output |
| Normalized length below 3 or above 64 | Invalid |

No extra first-letter rule, underscore adjacency rule or leading/trailing underscore ban: `1_A`, `_AB`, `AB_` and `A__B` satisfy the confirmed lexical constraints when not otherwise reserved/conflicting. This does not assign these codes to actual Roles. Unicode trim/uppercase semantics, input encoding and any further lexical grammar are PROPOSED / OPEN; all eventual tests must enforce the confirmed allowed ASCII output. No new value is assigned to an existing immutable Role through normalization.

New proposed scenarios: `cm1-acceptance-criteria-addendum.md#defaults-and-canonical-code-scenarios-v150`; software execution BLOCKED pending the relevant contracts.

## Governance preserved

`G-RUNTIME: BLOCKED`; `FE-BE: PENDING`; `AUTH/IAM: PENDING`; `Offline: PROHIBITED`; `Local-Infra: ACCEPTED — DEVELOPMENT-ONLY`; `Production: NOT AUTHORIZED`. Pending Submission remains PERMITTED NOT REQUIRED and non-authoritative. Existing coordinated durable Audit obligations remain unchanged; this task does not invent an operational Role Audit contract.
