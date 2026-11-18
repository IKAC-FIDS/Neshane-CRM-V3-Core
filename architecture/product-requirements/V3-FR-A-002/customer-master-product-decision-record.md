# Customer Master — Product Decision Record

**Record ID:** `V3-FR-A-002-PDR-001`
**Version:** `1.2.1`
**Date:** 2026-11-18
**Scope:** `FR-BJ-001` / `V3-FR-A-002` / `CM-1`
**Disposition:** `USER-CONFIRMED PRODUCT DIRECTION — FORMAL REPOSITORY ACCEPTANCE PENDING`

> Newly authored decision record; not an approved IAM/RBAC/API/DB design; not an implementation authorization. Customer Domain remains authoritative writer and final resource/action authorizer; Tenant Context validated; cross-tenant fails closed; durable mutations honor coordinated Audit obligations.

## 1. Decisions confirmed by the product stakeholder (v1.1.0 — CM1-PD-001..028)

| Decision ID | Topic | Confirmed rule |
|---|---|---|
| `CM1-PD-001` | Customer taxonomy | Company and Person are independent customer types; Branch is a Company subordinate, with its own facts, not an independent customer. |
| `CM1-PD-002` | Branch attribution | CRM activities may reference Branch as an attribution target, while Company remains the parent; activity-specific authorization and scope remain separate. |
| `CM1-PD-003` | Person multiplicity | One Person may have multiple concurrent relationships with Companies and Branches in the same authorized Tenant scope; relationships do not duplicate identity. |
| `CM1-PD-004` | Contact persons | A corporate contact is represented by Person, even without individual active commercial engagement; Contact stores communication channels, Relationship stores affiliation. |
| `CM1-PD-005` | Duplicate warning | Potential matches generate an access-controlled warning and existing-record suggestion; authorized new records are allowed with a mandatory reason. |
| `CM1-PD-006` | Duplicate exception authorization | A user authorized for CUS-CREATE may override a probabilistic duplicate warning with a required reason and Audit obligation; no supervisor approval is required. |
| `CM1-PD-007` | Verified identity conflicts | Ordinary duplicate override must not bypass a collision with a validated authoritative unique identifier; the identifier registry/scope and conflict resolution remain OPEN. |
| `CM1-PD-008` | Record/business status separation | Record lifecycle is separate from commercial engagement/classification; commercial taxonomy is not fixed here. |
| `CM1-PD-009` | Lifecycle states and initial status | Record states are ACTIVE, INACTIVE, ARCHIVED; after successful authorized creation and validation, initial state is ACTIVE. |
| `CM1-PD-010` | Deactivation | ACTIVE -> INACTIVE may occur with ongoing activities preserved; initiating new activities is restricted by activity-specific policy. |
| `CM1-PD-011` | Archive guard | ACTIVE/INACTIVE -> ARCHIVED is blocked until every applicable open activity/dependency is disposed of; unknown dependency outcome cannot be treated as clear. |
| `CM1-PD-012` | Restore | ARCHIVED -> INACTIVE is the only restore transition; INACTIVE -> ACTIVE requires revalidation. Direct ARCHIVED -> ACTIVE is forbidden. |
| `CM1-PD-013` | Identity edit authorization | CUS-UPDATE permits authorized users to edit identity facts, including sensitive business identifiers, with revalidation and Audit; no separate supervisor approval. |
| `CM1-PD-014` | Optimistic concurrency | CUS-UPDATE requires a record version; stale-version writes are rejected fully. No automatic merge or last-write-wins. |
| `CM1-PD-015` | Mandatory edit reasons | An edit reason is mandatory only for changes to sensitive identity identifiers and exceptional changes; routine edits do not require a reason. All durable updates retain Audit obligations. |
| `CM1-PD-016` | Minimal identification | Company legal/display name and Person given/family names are required for initial registration; system-issued stable identity and ACTIVE initial record status. Structured name parts and normalization rules require field-dictionary review. |
| `CM1-PD-017` | Official identifiers optional at onboarding | Official Person and Company identifiers are optional at initial create; workflows requiring formal identity verification may require the identifier and qualifying verification. Neither phone nor email is mandatory at initial registration. |
| `CM1-PD-018` | Verified identifier collision | A sufficiently verified official identifier must be unique within its approved identity/issuer/Tenant scope; confirmed conflicts block create/update or confirmation and cannot be bypassed with probabilistic-match exception. Identifier namespace and technical unique key remain OPEN. |
| `CM1-PD-019` | Verification lifecycle separation | Formal identity verification is distinct from record lifecycle and commercial status. Its states are NOT_VERIFIED, VERIFIED, REQUIRES_REVERIFICATION; initial creation is NOT_VERIFIED unless a separate trusted verification occurs. |
| `CM1-PD-020` | Verification routes | Both trusted external/system verification and evidence-backed manual verification by separately authorized actor are permitted; both produce attributable evidence/history and coordinated Audit obligations. Customer Domain remains final authoritative state writer. |
| `CM1-PD-021` | Manual verification and separation of duties | An actor who created the customer may manually verify that customer if independently permitted in normal processes; sensitive processes require a different verifying actor. Sensitive-process catalog and permission grants remain OPEN. |
| `CM1-PD-022` | No blanket verification expiry | No universal time-based identity verification expiry. Effective validity depends on underlying required evidence, material identity changes, trusted revocation, and evidence validity rules. Age alone does not invalidate VERIFIED. |
| `CM1-PD-023` | Reverification trigger | Expiry/loss of validity of evidence necessary to substantiate an otherwise valid earlier verification, or a material change to identity facts supporting it, moves VERIFIED to REQUIRES_REVERIFICATION; successful new trusted verification returns VERIFIED. |
| `CM1-PD-024` | Fundamental verification invalidation | If prior verification is proven fundamentally invalid (false/misattributed/invalid from outset), effective status becomes NOT_VERIFIED, including from REQUIRES_REVERIFICATION. Requires an independent new trusted verification for VERIFIED; never erase historical evidence. |
| `CM1-PD-025` | Verification evidence provenance | Verification decisions preserve method (SYSTEM/MANUAL), source/issuer, verified actor/service, decision time, relevant identity revision, controlled evidence reference, reason and correlation. Protect sensitive evidence and retain histories subject to unresolved retention and disclosure rules. |
| `CM1-PD-026` | Verification authorization and consistency | Generic CUS-UPDATE must not directly set VERIFIED; trusted verification workflow authorizes and verifies actor or provider result, identity revision, duplicate collision, evidence and required durable Audit. Stale or ambiguous responses do not confer VERIFIED. |
| `CM1-PD-027` | Operational use of verification | NOT_VERIFIED and REQUIRES_REVERIFICATION can coexist with ACTIVE Customer; any consuming operation requiring verified identity must check effective evidence validity before relying on VERIFIED, not assume status flag alone suffices. |
| `CM1-PD-028` | Revocation history and safe failure | Verification expiry/revocation preserves Customer ID, historical relationships and an auditable, provenance-bound record. Trusted fundamental invalidation cannot silently be ignored by sensitive consumers when persistence is temporarily unavailable; precise fail/recovery contract remains OPEN. |

## 2. Additional decisions — v1.2.0 (CM1-PD-029..057)

| Decision ID | Topic | Confirmed rule |
|---|---|---|
| `CM1-PD-029` | Relationship multiplicity | Each Person may have multiple concurrent Relationships with Company and/or Branch. Each independent role is represented by a distinct Relationship; roles/affiliations belong to Relationship, not to duplicate Person records. |
| `CM1-PD-030` | Relationship conceptual fields | Recommended conceptual Relationship fields: relationshipId, personId, targetType (COMPANY/BRANCH), targetId, roleCode, roleTitle, status, startDate, endDate, recordVersion, createdAt, updatedAt, endedReason, optional source/evidence reference. These are conceptual, not an approved schema or API. |
| `CM1-PD-031` | Relationship lifecycle | Relationship lifecycle states are ACTIVE and ENDED (proposed for formal review). An ENDED historical Relationship is not reopened; a later recurrence of the same role is a separate Relationship. |
| `CM1-PD-032` | Relationship temporal interval convention | Use the conceptual half-open interval [startDate, endDate): start inclusive, end exclusive, null end means open-ended, empty or backwards intervals are invalid. Effective usability considers status, interval, Person status, target status and permissions. |
| `CM1-PD-033` | Relationship overlap — controlled exception (LATEST/authoritative) | For the same Person, TargetType, TargetId and RoleCode, overlapping Relationship intervals are allowed only through a controlled exception with a warning, valid authority, mandatory reason and Audit. |
| `CM1-PD-034` | Overlap — free cases | Distinct role codes may overlap freely; the same role may overlap across different companies/targets; the same role in Company vs its Branch concerns different targets (different TargetId). |
| `CM1-PD-035` | Overlap — warning and reuse-or-exception | Same Person + same target + same role + overlapping intervals produces a warning. The user may select/use an existing Relationship instead of creating a new one. An authorized user may intentionally create/update an overlapping Relationship with a mandatory exception reason; no separate supervisor approval is required. |
| `CM1-PD-036` | Overlap — reason scope | A reason is required for each newly authorized overlap decision; old reasons do not authorize all future changes automatically. |
| `CM1-PD-037` | Overlap — historical participation | Even ENDED Relationship intervals participate in historical overlap detection. |
| `CM1-PD-038` | Overlap — concurrency | Two cases are distinguished: (1) updating the same Relationship rejects stale record versions; (2) creating separate overlapping Relationships concurrently uses a consistent, authoritative overlap assessment. If the relevant conflict set changed after the user reviewed a warning, require re-evaluation before finalizing. |
| `CM1-PD-039` | Overlap — idempotency and intent | Idempotent retries must not produce unintended additional Relationship records. An intentional, approved overlap exception and an accidental duplicate request are distinct cases. |
| `CM1-PD-040` | Overlap — invariants preserved | Overlap exception authorization does not bypass stale-version checks, Tenant isolation, input validation, or disclosure control. Avoid disclosing non-visible Relationship details through warning output. |
| `CM1-PD-041` | Overlap — supersession of absolute prohibition | The controlled-exception overlap policy SUPERSEDES any prior rule prohibiting all overlapping Relationships (same Person+target+role). No active absolute-overlap-prohibition rule remains; historical absolute-denial expectations, if imported later, are superseded. |
| `CM1-PD-042` | Branch record states | Branch has only two independent record states: ACTIVE and INACTIVE. Branch does not have an independently managed ARCHIVED state. Effective operational availability depends on its own status, its parent Company lifecycle status, and applicable resource/action policy. |
| `CM1-PD-043` | Branch/Company deactivation independence | Deactivating Company does not automatically change stored Branch statuses. Deactivating Branch does not automatically modify Company or Person. Existing open activities remain available for permitted continuation; creating new activities is restricted if Branch or parent Company is effectively inactive. |
| `CM1-PD-044` | Branch parent immutability | Direct Branch reparenting is prohibited. branchId and companyId are immutable after creation. |
| `CM1-PD-045` | Branch transfer | When a Branch is genuinely transferred, create a new Branch under the target Company with a new Branch ID and deactivate the original. Do not transfer historical activities or Person Relationships automatically; historical activities remain attributed to the original Company/Branch. New Relationships and activity assignments use their own authorized operations. An optional succession reference between old and new branches may be proposed but must not transfer ownership/permissions. |
| `CM1-PD-046` | Branch lifecycle dependency rules | Archiving Company requires resolution of applicable open dependencies across Company and Branches. Branch records and historical associations remain intact after Company archiving. Restoring Company does not automatically activate inactive Branches. |
| `CM1-PD-047` | Branch identity and relationships | Branch is subordinate to Company (not an independent Customer), has its own stable ID and independently maintained data, and has exactly one Company parent whose ID is immutable after creation. Branches can have Person Relationships. Company/Branch references respect Tenant isolation. |
| `CM1-PD-048` | Audit obligations for durable and proposed operations | Customer durable mutations honor existing coordinated persistent Audit obligations. Proposed independent Branch, Relationship and Verification operations require an auditability product requirement, with the precise operational contract still requiring formal approval. |
| `CM1-PD-049` | Audit — no assumed mandatory events | Rejected validations, warnings, or read-only queries do not carry an assumed mandatory Audit rule unless supported by existing authoritative sources. |
| `CM1-PD-050` | Audit — controlled evidence references | Prefer controlled references to sensitive evidence over copying entire identity documents or private identifiers into Audit logs. |
| `CM1-PD-051` | Audit — safe failure and concurrency | A mandatory coordinated Audit failure must not result in a successful mutation being reported. Broker ACK or outbox publication alone is not authoritative Audit ingestion. Preserve version/concurrency safety and prevent stale provider results from silently overwriting newer verification states. |
| `CM1-PD-052` | Duplicate signals non-conclusive | Similar names, shared phone numbers, or shared emails alone are not conclusive identity matches. Automatic merging of Customer records is not authorized. Distinguish an intentional duplicate-warning override from an accidental duplicate caused by retrying the same request. Avoid unauthorized disclosure of other customers/Tenant data through duplicate detection. |
| `CM1-PD-053` | Minimum fields consolidation | Address and Latin name are optional unless a specific consuming workflow requires them. Official identification may be required later by a workflow requiring formal identity verification. A structurally valid identifier is not automatically verified. Verified official identifiers must be unique within the formally defined identity scope; conclusive conflicts block the conflicting create/update. No silent assumption of global cross-Tenant identity deduplication. |
| `CM1-PD-054` | Lifecycle consolidation | Deactivation is allowed even with open activities; existing open activities and historical data remain intact. Starting new activities for INACTIVE customers is restricted per owning-module policy. Archiving must not delete Customer data, relationships, or audit history. Restoring an archived Customer must not automatically reopen historical activities/relationships. |
| `CM1-PD-055` | CUS-UPDATE consolidation | Updating Company must not silently reparent Branches; updating Person must not silently alter unrelated Relationships. Converting Company into Person or vice versa is not supported as a normal CM-1 update. Routine edits of ARCHIVED records are not allowed (use authorized recovery). INACTIVE records may be corrected without automatically becoming ACTIVE. |
| `CM1-PD-056` | Verification independent of authorization | A record can be ACTIVE and NOT_VERIFIED, and can be VERIFIED without automatically receiving access or operational authorization. Verification state never substitutes for resource authorization or membership. |
| `CM1-PD-057` | Verification time semantics and open items | Effective time and recording time are recorded distinctly when relevant. The specific evidence-retention period, trusted-provider catalog, revocation dispute process, and detailed failure/recovery mechanism remain open. |

## 3. Supersession

The controlled-exception Relationship overlap policy (**CM1-PD-041**) is the authoritative product policy and SUPERSEDES any prior rule prohibiting all overlapping Relationships for the same Person+TargetType+TargetId+RoleCode. No active absolute-overlap-denial rule remains in this working tree; any later-imported absolute-denial expectation is superseded.

## 4. State machines

**Record lifecycle (Company/Person):** ACTIVE / INACTIVE / ARCHIVED. Create → ACTIVE; ACTIVE → INACTIVE; INACTIVE → ACTIVE (revalidation); ACTIVE/INACTIVE → ARCHIVED (dependencies resolved); ARCHIVED → INACTIVE (recovery); ARCHIVED → ACTIVE forbidden.

**Branch record states:** ACTIVE / INACTIVE (no independent ARCHIVED). Effective availability = own status + parent Company status + resource/action policy.

**Relationship lifecycle (proposed):** ACTIVE / ENDED. ENDED is not reopened; recurrence is a separate Relationship.

**Identity verification:** NOT_VERIFIED / VERIFIED / REQUIRES_REVERIFICATION — independent of record lifecycle and commercial status.

## 5. Traceability to OPEN register

Partial resolutions are recorded in `openQuestionTraceability` (JSON). Every existing question retains OPEN status; no question is closed. New OPEN items PDQ-002-08..12 are added for the relationship role catalog, branch-transfer contracts, operation-specific Audit for Branch/Relationship/Verification, sensitive-process SoD catalog, and overlap concurrency implementation.

## 6. Source integrity and governance

- Original 13 source artifacts remain the requirements baseline; this decision record overlays user-confirmed product direction without replacing them.

- G-RUNTIME: BLOCKED; FE-BE and AUTH/IAM: PENDING; Offline: PROHIBITED; Production: NOT AUTHORIZED.

- No staging, commit, push, code, tests or execution approval is implied.


## 9. v1.2.1 coverage reconciliation

- FLD-002-11 corrected: Branch parent Company reference is Required and Immutable (supersedes the earlier Optional/Mutable status), per CM1-PD-044/045/047; persistence/API schema remains unapproved.
- Lifecycle restated as (A) formal source baseline vs (B) user-confirmed target state machine, with explicit transition matrices and guard conditions; no unapproved API/DB/IAM choice presented as accepted.
- Stale OPEN/PROPOSED statements reconciled to distinguish user-confirmed product policy from still-OPEN technical/operational contract and still-PENDING formal acceptance.
- Relationship overlap controlled-exception policy (CM1-PD-033..041) remains authoritative; absolute-overlap prohibition remains superseded.
- Decision coverage matrix: `customer-decision-coverage-matrix.json` / `.md` maps all 57 decisions; coverage counts FULL=3, PARTIAL=47, DOCUMENTED_ONLY=5, BLOCKED_BY_OPEN_DECISION=2.
