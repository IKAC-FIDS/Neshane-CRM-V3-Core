# Relationship Role Catalog — v1.7.0 bounded candidate (catalog policies unchanged)

## v1.7.0 applicability only

CM1-PD-078..095 do not reopen/replace catalog policies PD-058..077 or exact initial vocabulary v1.0. Customer Catalog Manager is the logical owning-Tenant manager category of PD-076, not a System governance/IAM/assignment grant. New Customer/Branch deactivation reasons do not change optional ordinary Role lifecycle/Hide/Unhide reasons; incompatible-scope/publication reason+release reference remain mandatory. All RC-001..021 and RC-OPEN mechanisms preserved. PDQ-002-08 **PRODUCT_READY_TECHNICAL_OPEN within approved scope; status OPEN / PARTIALLY ANSWERED**, not closed. Adjacent Relationship ordinary identity edit/day/END rules in PD-086 are not reopening catalog identity/code policy. Current bounded scope/blockers: customer-bounded-readiness.md; no formal acceptance or implementation permission.

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
- v1.6.0 source: user task **TASK: V3-FR-A-002 — Customer Master Product Decisions v1.6.0**, CM1-PD-073..077. USER-CONFIRMED PRODUCT DIRECTION; formal acceptance PENDING. Reviewed baseline `895efd76595ca36a9ee5c8028a67c8854d5d318e`, branch `codex/v3-fr-a-002`, initially clean worktree/index. Recorded at `2026-11-19T06:31:30.259190+00:00`; owner issuance time not supplied. Previous records remain historical; no IAM grant or executable contract approval.

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

`roleId` and `roleCode` are immutable after creation; physical deletion is not supported. Historical Role identities and references must be preserved (`CM1-PD-061`). Titles, lifecycle and scope changes preserve Role identity and historical Relationship references (`CM1-PD-065`). Current versus event-time title policy is now answered by CM1-PD-075 (RC-019); exact fields, temporal/reference/history representation and namespace enforcement remain OPEN. No Role table, foreign key, snapshot or API shape is selected.

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

CM1-PD-073..077 additionally answer hide/unhide optional reason and mandatory Audit, display metadata governance, current/event-time historical display policy, three logical authority categories and catalog Audit coverage/reason/information/integrity policy (RC-017..021). These are product policies, not finalized executable contracts.

All remain under **OPEN / PARTIALLY ANSWERED `PDQ-002-08`**; affected executable design is blocked until separately dispositioned. Product policies above remain user-confirmed.

1. Exact catalog schema/configuration persistence, provisioning/default materialization and publication/migration mechanisms; initial vocabulary and default policy are answered, not an executable design.
2. System/Tenant namespace enforcement implementation, concurrent uniqueness/reservation consistency and technical normalization/Unicode/input-encoding edge cases. Basic ASCII output/length/trim-uppercase product policy is answered.
3. Exact Role Definition field schema and persistence contract.
4. Role management and Tenant-selectability operation IDs/IAM roles/permissions/grants/actor mappings and technical Backend authorization enforcement. Logical responsibilities are answered in RC-020; no permission bindings approved. Exact Audit schema/event names remain OPEN.
5. Concurrent updates, scope-change dependencies and selectability/assignment finalization consistency mechanism.
6. Temporal storage, versioning, snapshot mechanisms, localization/fallback and API/reference/history representation; current versus event-time title policy is answered in RC-019.
7. Exact Audit transactional guarantees, storage, retention, recovery, access and failure protocols (also `PDQ-002-10`); mandatory coverage, logical information and no-success-without-durable-guarantee product policy are answered in RC-021.
8. Relationship temporal representation and API compatibility (also `PDQ-002-12` for overlap consistency).
9. Cross-Tenant conflict detection authorization/privacy, catalog version publication/rollback and explicitly authorized collision-resolution workflow. The conflicting new Role is blocked at product level; private-data access authority and executable mechanics remain OPEN. Hide/unhide reason is now product-confirmed OPTIONAL (RC-017); publication reason/release reference and incompatible-scope reason are MANDATORY (RC-021). Ordinary metadata reason is optional; fundamental-semantic-change assessment procedure remains OPEN, not an invented heuristic.

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

These initial v1.0 codes, Persian titles and scopes are preserved exactly as versioned baseline evidence. Authorized future controlled display revisions under CM1-PD-074 do not rewrite this initial vocabulary or historical records. All are System Roles available to authorized Tenants subject to effective selectability; they grant no security permission or verified legal authority. Person may hold multiple independent roles; PRIMARY_CONTACT is not exclusive and titles confer no automatic authority. Identity/code immutability and no physical deletion remain authoritative. No specific English label value or required language field is confirmed; Persian/English labels may be maintained under RC-018. No fixed global roleId, seed, migration or publication/deployment mechanism is selected.

## RC-010 — Tenant-specific System Role selectability

**CM1-PD-067 — USER-CONFIRMED PRODUCT DIRECTION; formal acceptance PENDING.** An appropriately authorized actor in a Tenant may make an otherwise eligible System Role unavailable for new assignments in that Tenant, then make it selectable again. This is an assignment restriction, **not global Role deactivation** or definition editing.

- Do not modify the global System Role Definition, global status, scope, roleId or roleCode; do not affect other Tenants. Tenant users still cannot edit System Role Definitions.
- Do not create, modify, terminate, delete or reactivate existing Relationships; preserve ACTIVE/ENDED statuses, intervals, history and references. Non-selectability must not hide historical Role references from otherwise authorized historical viewers.
- Require validated Tenant context and applicable management authority. CUS-CREATE alone is insufficient; no IAM/RBAC permission is granted by this setting.
- The authoritative Customer Domain must enforce the restriction, not UI filtering alone. Management/warning/assignment responses must not disclose another Tenant's settings or Relationships.
- Restoring Tenant selectability does not reactivate a globally INACTIVE System Role or reopen an ENDED Relationship. No Tenant override of global lifecycle or applicableScope is permitted.
- Hide and Unhide reason is OPTIONAL and Audit MANDATORY under CM1-PD-073/077 (RC-017/021); only authorized tenant catalog managers act in their own Tenant. Incompatible scope-change mandatory reasons are not imported into this different operation.

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

Historical proposals for defaults/code policy are answered in RC-012..016. Hide/unhide reason, metadata governance, historical display policy, logical authorities and catalog Audit policy are now answered in RC-017..021. Remaining PROPOSED / OPEN choices: configuration/storage/materialization; namespace/index/tombstone/consistency; Unicode/input encoding/further grammar; cross-Tenant conflict detection privacy/authority; release/version/rollback/resolution mechanics; exact IAM/operations/actor mappings; localization/temporal/reference/API representation; Audit schema/event names/transactions/storage/retention/recovery/access. No extra first-letter/underscore-placement rule, mandatory language field, localization storage or implementation option is adopted. English display labels are permitted metadata, not identifiers or specific confirmed label values. No mandatory ordinary hide/unhide reason is introduced.

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

## RC-017 — Hide/Unhide governance

CM1-PD-073: authorized tenant catalog managers may Hide/Unhide only within their own Tenant. **Reason OPTIONAL; Audit MANDATORY** for both. Record actor, Tenant, Role identity, old/new selectability, timestamp and optional reason. Preserve existing Relationships/history and other Tenants. Unhide does not override global INACTIVE, scope or assignment authorization; local selectability restoration is not global activation. Backend Customer Domain authorization and effective-state guards still apply.

## RC-018 — Display metadata governance

CM1-PD-074: roleId/roleCode immutable. Authorized product governance can update System labels/translations/descriptions through controlled catalog release; authorized tenant catalog managers can update only their own custom Role metadata, never global System definitions. Persian/English labels may be maintained, with no mandatory language fields/localization storage implied. Display labels are not unique identifiers. Preserve identity/fundamental business semantics; a materially different Role requires a new Role/new roleCode under the existing uniqueness/reservation rules. No replacement, recreation or modification of existing Relationships. Audit MANDATORY; ordinary metadata reason OPTIONAL; preserve old/new values. Publication remains a separate logical obligation requiring reason/release reference (RC-021), even when the release contains ordinary metadata edits. No event-count or release workflow implementation is chosen.

## RC-019 — Current and historical Role representation

CM1-PD-075: authorized current Relationship views show the current valid Role title. Historical events/Audit retain the title applicable at event time; later rename never rewrites history. INACTIVE/hidden Roles remain visible in existing Relationships and otherwise authorized historical records; selection restrictions apply to new assignment, not automatic history suppression. Stable roleId/roleCode, Tenant isolation and historical access authorization remain mandatory. No new disclosure permission; no assumption that a view of another Tenant is allowed. Temporal storage/versioning/snapshots/API and language fallback representation remain OPEN.

## RC-020 — Three logical authority categories

CM1-PD-076 confirms responsibility categories, **not executable IAM roles, grants, permission IDs or named actor appointments**:

| Logical authority | Product responsibilities |
| --- | --- |
| System catalog governance authority | Create System Roles; update System display metadata; change System scope; activate/deactivate System Roles; publish controlled revisions |
| Authorized tenant catalog manager | Create own custom Roles; update own metadata/scope; activate/deactivate own Roles; Hide/Unhide System Roles for that Tenant |
| Authorized Customer Master operator | View applicable selectable Roles; assign Roles only with separately authorized Relationship operations |

Catalog management and Relationship assignment do not imply one another. Business Relationship roles grant neither IAM nor administrative authority. No category may physically delete Roles or edit existing roleId/roleCode. Backend authorization is mandatory, not UI-only filtering. Preserve RC-006 scope-change impact/reason/management guards and ordinary overlap's no-extra-supervisor rule. Categories need independent authority checks, not an invented requirement for three distinct people; one category never automatically inherits another. Technical enforcement, exact IAM/permission/grant/actor bindings remain OPEN.

## RC-021 — Catalog Audit coverage, reasons and integrity

CM1-PD-077 is explicit product-level Audit authority for the following catalog operations; it does not turn every ordinary warning/validation/read into a mandatory event.

| Logical catalog operation | Audit coverage | Reason policy |
| --- | --- | --- |
| System Role creation | MANDATORY | Optional for ordinary creation |
| Tenant Role creation | MANDATORY | Optional for ordinary creation |
| Labels/translations/descriptions changes | MANDATORY (CM1-PD-074/077) | Optional for ordinary metadata |
| Scope changes | MANDATORY | Optional if compatible; mandatory if incompatible with existing Relationships |
| Activation/deactivation | MANDATORY | Optional |
| Tenant Hide/Unhide | MANDATORY | Optional |
| System catalog publication | MANDATORY | Mandatory reason including release reference |
| Unauthorized catalog modification attempts | MANDATORY | No new caller-supplied mandatory reason rule; record denial/outcome safely |

Preserve all previously approved exception reasons, including controlled Relationship overlap and sensitive identifier changes. Optional ordinary reasons do not waive mandatory Audit; missing ordinary reason alone does not invalidate an otherwise authorized/valid operation. Neither optional metadata reason nor compatible-scope reason waives publication's mandatory reason/release reference.

Logical Audit information: Event ID; Actor ID or authorized system identity; Tenant ID when applicable; Role ID and roleCode when available; Role origin; operation; old/new values when applicable; reason according to operation; timestamp; outcome; correlation ID. Historical title requirements in RC-019 also apply. These are logical information requirements, not an approved event schema or physical field names.

Preserved old/new values belong in protected, disclosure-controlled Audit information, not unredacted public logs or unauthorized cross-Tenant views. Preserve existing data minimization and controlled-evidence-reference boundaries; exact protection/redaction/access mechanisms remain OPEN, not a reason to fabricate or rewrite required historical evidence.

Catalog managers and ordinary users cannot modify/delete Audit history. Isolate Tenant Audit records; preserve history through title/status/scope changes. **Do not report a state-changing operation successful unless durable Audit recording can be guaranteed.** Preserve existing coordinated durable obligations: broker ACK/outbox alone is not authoritative Audit ingestion; no new DURABLE_DEFER or transaction protocol is approved. Unauthorized attempts must remain denied and not disclose protected cross-Tenant information; Audit trouble never grants authorization.

Ordinary catalog reads have no independent product-level Audit requirement under this decision; existing disclosure-denial/source obligations and security monitoring remain unaffected. No blanket mandatory event is inferred for all unrelated warnings or validation failures. Exact schema, transactions, storage, retention, recovery and access/failure contracts remain OPEN; no requirement for one physical event per logical action or particular synchronous/outbox mechanism is invented.

New proposed scenarios: `cm1-acceptance-criteria-addendum.md#catalog-governance-history-and-audit-scenarios-v160`; implementation-dependent software execution BLOCKED.

## Governance preserved

`G-RUNTIME: BLOCKED`; `FE-BE: PENDING`; `AUTH/IAM: PENDING`; `Offline: PROHIBITED`; `Local-Infra: ACCEPTED — DEVELOPMENT-ONLY`; `Production: NOT AUTHORIZED`. Pending Submission remains PERMITTED NOT REQUIRED and non-authoritative. Existing coordinated durable Audit obligations remain unchanged; this task does not invent an operational Role Audit contract.
