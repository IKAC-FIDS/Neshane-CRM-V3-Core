# Open product decisions — V3-FR-A-002

**19 OPEN decisions** for FR-BJ-001 (14 original + PDQ-002-08..12); some product-level answers are partial, none is closed. Carried IDs preserved verbatim; new use PDQ-002-*.

## PDQ-A001-001 — FR-BJ-001

**Status:** OPEN; selected answer NONE.

**Carried from:** V3-FR-A-001

**Missing decision:** Which named person/team is the accountable Business Owner for FR-BJ-001?

**Dependent tasks:** V3-FR-A-002

**Required decision authority:** Product Decision Owner / TAO

## PDQ-A001-002 — FR-BJ-001

**Status:** OPEN; selected answer NONE.

**Carried from:** V3-FR-A-001

**Missing decision:** Which actual participants/operations and disclosure requirements are needed (not a new RBAC model)?

**Dependent tasks:** V3-FR-A-002

**Required decision authority:** Product Decision Owner / TAO

## PDQ-A001-003 — FR-BJ-001

**Status:** OPEN; selected answer NONE.

**Carried from:** V3-FR-A-001

**Missing decision:** Which Customer actor journeys, field/validation, duplicate, merge/deletion/retention, concurrency and Audit failure boundaries does the selected milestone support?

**Dependent tasks:** V3-FR-A-002

**Required decision authority:** Product Decision Owner / TAO

## PDQ-A001-049 — FR-BJ-001

**Status:** OPEN; selected answer NONE.

**Carried from:** V3-FR-A-001

**Missing decision:** Who owns operation-specific Audit failure, ingestion, recovery and reconciliation decisions before executable deferral?

**Dependent tasks:** V3-FR-A-002

**Required decision authority:** Product Decision Owner / TAO

## PDQ-A001-050 — FR-BJ-001

**Status:** OPEN; selected answer NONE.

**Carried from:** V3-FR-A-001

**Missing decision:** Which binding legal/regulatory/contractual obligations impose retention/disclosure/separation conditions?

**Dependent tasks:** V3-FR-A-002

**Required decision authority:** Product Decision Owner / TAO

## PDQ-A001-052 — FR-BJ-001

**Status:** OPEN; selected answer NONE.

**Carried from:** V3-FR-A-001

**Missing decision:** Which selected CM-1 operation/actor/profile boundaries and integrations apply?

**Dependent tasks:** V3-FR-A-002

**Required decision authority:** Product Decision Owner / TAO

## PDQ-A001-053 — FR-BJ-001

**Status:** OPEN; selected answer NONE.

**Carried from:** V3-FR-A-001

**Missing decision:** Are external actor interactions required beyond admitted issuer/profile coordination?

**Dependent tasks:** V3-FR-A-002

**Required decision authority:** Product Decision Owner / TAO

## PDQ-002-01 — FR-BJ-001

**Status:** OPEN; selected answer NONE.

**Existing requirement:** Company/person/contact master; Customer owns branch/relationship facts (V3-002B-DEC-002)

**Category:** PRODUCT

**Missing decision:** Exact field dictionary, required/optional/conditional status and validation rules per customer type?

**Proposed options:**
- [PROPOSED] Approve a bounded field set for CM-1 with explicit exclusions
- [PROPOSED] Keep detailed field rules OPEN pending owner input

**Dependent tasks:** V3-FR-A-002

**Required decision authority:** Product Decision Owner / TAO

## PDQ-002-02 — FR-BJ-001

**Status:** OPEN; selected answer NONE.

**Existing requirement:** No approved Customer state machine

**Category:** PRODUCT

**Missing decision:** Authoritative Customer lifecycle states and permitted transitions?

**Proposed options:**
- [PROPOSED] Approve minimal states with transition matrix
- [PROPOSED] Keep lifecycle OPEN

**Dependent tasks:** V3-FR-A-002

**Required decision authority:** Product Decision Owner / TAO

## PDQ-002-03 — FR-BJ-001

**Status:** OPEN; selected answer NONE.

**Existing requirement:** Duplicate/merge/deletion/retention remain incomplete (DEC-002 gap)

**Category:** PRODUCT

**Missing decision:** Duplicate detection criteria, handling and merge/delete policy?

**Proposed options:**
- [PROPOSED] Define detection-only for CM-1 without automatic merge
- [PROPOSED] Defer duplicates entirely; manual review

**Dependent tasks:** V3-FR-A-002

**Required decision authority:** Product Decision Owner / TAO

## PDQ-002-04 — FR-BJ-001

**Status:** OPEN; selected answer NONE.

**Existing requirement:** CUS-UPDATE impact NOT_ASSESSED

**Category:** PRODUCT

**Missing decision:** Which update use-cases/critical-field categories are in scope and what concurrency control applies?

**Proposed options:**
- [PROPOSED] Concurrency via optimistic version for CM-1
- [PROPOSED] Keep concurrency policy OPEN

**Dependent tasks:** V3-FR-A-002

**Required decision authority:** Product Decision Owner / TAO

## PDQ-002-05 — FR-BJ-001

**Status:** OPEN; selected answer NONE.

**Existing requirement:** Pending Submission PERMITTED NOT REQUIRED (DEC-005)

**Category:** PRODUCT

**Missing decision:** Is in-system Pending Submission needed for CM-1, and with what lifecycle?

**Proposed options:**
- [PROPOSED] Exclude from CM-1
- [PROPOSED] Include with separately approved lifecycle

**Dependent tasks:** V3-FR-A-002

**Required decision authority:** Product Decision Owner / TAO

## PDQ-002-06 — FR-BJ-001

**Status:** OPEN; selected answer NONE.

**Existing requirement:** DEC-012/013/014; executable DURABLE_DEFER NOT approved

**Category:** SECURITY

**Missing decision:** Operation-specific Customer mutation Audit failure policy (reject vs controlled handling)?

**Proposed options:**
- [PROPOSED] Approve explicit outcome policy per operation
- [PROPOSED] Keep OPEN; no executable deferral assumed

**Dependent tasks:** V3-FR-A-002

**Required decision authority:** Product Decision Owner / TAO

## PDQ-002-07 — FR-BJ-001

**Status:** OPEN; selected answer NONE.

**Existing requirement:** Customer classification/identifiers not approved

**Category:** PRODUCT

**Missing decision:** Customer type taxonomy and identifier/national-ID policy?

**Proposed options:**
- [PROPOSED] Approve minimal type + optional identifiers for CM-1
- [PROPOSED] Keep taxonomy/identifiers OPEN

**Dependent tasks:** V3-FR-A-002

**Required decision authority:** Product Decision Owner / TAO


## Partial-resolution ledger (v1.2.0 — does not close any question)

The user-confirmed product decisions CM1-PD-001..057 partially answer existing OPEN questions without closing them. See `customer-master-product-decision-record.json` `openQuestionTraceability` for the exact mapping. Each existing question remains OPEN until the authoritative register is separately revised.

## New OPEN items (relationship / branch / audit / technical)

| Question ID | Capability | Category | Missing decision |
| --- | --- | --- | --- |
| PDQ-002-08 | FR-BJ-001 | PRODUCT | OPEN / PARTIALLY ANSWERED through CM1-PD-072: vocabulary, selectability/defaults, namespace uniqueness/permanent reservation, future-collision blocking and basic normalization ANSWERED at product level; exact schema/configuration, enforcement/concurrency, cross-Tenant detection authority/privacy, publication/rollback/resolution, Unicode/encoding edge cases, operations/IAM/Audit/reason policy, history/reference and temporal/API contracts remain OPEN |
| PDQ-002-09 | FR-BJ-001 | PRODUCT | Branch reparenting coordination workflow and activity-transfer contracts (succession reference semantics) |
| PDQ-002-10 | FR-BJ-001 | SECURITY | Operation-specific Audit contract for proposed Branch/Relationship/Verification operations (owner, failure/recovery, ingestion evidence) |
| PDQ-002-11 | FR-BJ-001 | SECURITY | Sensitive-process catalog and SoD actor mapping for manual verification |
| PDQ-002-12 | FR-BJ-001 | TECHNICAL | Overlap conflict-set token/snapshot/locking/transactional implementation (technical design, not API contract) |

## v1.2.1 partial-resolution clarification

Total OPEN questions remain **19** (14 original + PDQ-002-08..12). The user-confirmed decisions partially answer the following without closing them:

| PDQ | Confirmed product-level answer | Remaining OPEN aspects |
| --- | --- | --- |
| PDQ-002-01 | Company name + Person given/family required; official IDs/phone/email optional at create | exact field definitions, normalization, validation, national-ID rules |
| PDQ-002-02 | ACTIVE/INACTIVE/ARCHIVED lifecycle + transition matrix | full dependency catalog, activity-specific restriction, race-safe semantics |
| PDQ-002-03 | probabilistic warning + controlled override; verified-ID collision blocks; no auto-merge | match algorithm, identifier namespace/scope, merge/delete/retention |
| PDQ-002-04 | optimistic concurrency; stale reject; no auto-merge | API contract and persistence enforcement |
| PDQ-002-07 | Company/Person independent; relationship + verification models | role catalog, identifier/taxonomy policy |
| PDQ-A001-003 | duplicate override, lifecycle, concurrency direction | field/validation/duplicate/merge/retention/disclosure specifics |
| PDQ-A001-052 | Branch attribution + archive guards | CM-1 operation/actor/profile boundaries and integrations |

No PDQ is closed; formal closure requires explicit authority.

## v1.3.0 Role Catalog partial resolution — PDQ-002-08

Historical v1.3.0 residuals below are updated by later ledgers, currently v1.5.0; initial vocabulary is no longer wholly unresolved.

**Disposition: OPEN / PARTIALLY ANSWERED; formal acceptance PENDING.** CM1-PD-058..065 confirm product policy, not executable design. Exact answers and all eight residual contracts are in `customer-role-catalog.md` RC-001..008 / RC-OPEN. Dependent proposed scenarios: CM1-ROL-01..16; related technical/Audit questions: PDQ-002-10/12. Total remains 19; no new question ID and no closure. Earlier role-catalog-as-wholly-open wording describes the historical baseline only; the residuals now concern the listed contracts, not the confirmed hybrid/lifecycle/authority policies. No physical Role deletion is supported; general Customer deletion/retention questions remain separate.

## v1.4.0 partial-resolution ledger — PDQ-002-08

Historical v1.4.0 disposition only. Defaults, uniqueness/reservation/collision and basic normalization mentioned as OPEN below are answered at product level by the current v1.5.0 ledger; technical contracts are not closed.

**OPEN / PARTIALLY ANSWERED; formal requirements acceptance PENDING; total OPEN remains 19.**

- Product-level ANSWERED: CM1-PD-066 exact 12-entry initial System vocabulary v1.0 (codes, Persian titles, scopes) and CM1-PD-067 Tenant-specific System Role selectability/effective eligibility. These are not IAM grants or verified legal representation and do not authorize Tenant modification of global Roles.
- Remaining OPEN: all RC-OPEN / RC-PROPOSED contracts, including new-Tenant/later-role defaults, configuration/schema/reference, normalization/length/namespaces, present/future custom-code collisions, catalog publication/version mechanics, exact permissions/Audit events, ordinary hide/unhide reason policy, concurrent hide/assignment consistency, history/display, Audit failure/recovery and temporal/API compatibility. No mandatory hide/unhide reason is inferred from incompatible scope changes.
- Dependents: CM1-PD-066/067 and CM1-ROL-17..29, in addition to earlier Role decisions/scenarios; related PDQ-002-10/12 unchanged. Contract-dependent software scenarios BLOCKED pending executable design. See `source-traceability.json` partialResolutionLedger and coverage matrix for exact links.
- No PDQ closure, new ID, runtime approval, global roleId/seed/migration choice, roleCode-to-roleId overlap substitution or governance relaxation.

## v1.5.0 partial-resolution ledger — PDQ-002-08

**OPEN / PARTIALLY ANSWERED; formal acceptance PENDING; all 19 OPEN IDs preserved.**

- Newly ANSWERED product policy: CM1-PD-068 default ACTIVE System selectability for new Tenants/new releases with prior Tenant settings preserved; CM1-PD-069 canonical System-global/owning-Tenant uniqueness while independent Tenants may share custom codes; CM1-PD-070 permanent scoped reservation/identity-preserving reactivation; CM1-PD-071 blocking only a conflicting proposed System Role without destructive automatic resolution or inferred private-data access; CM1-PD-072 trim-uppercase, ASCII A-Z/0-9/underscore, length 3..64, no extra first-letter/underscore-placement grammar.
- Still OPEN: exact catalog schema/configuration persistence and default materialization; namespace and concurrent uniqueness/reservation enforcement; cross-Tenant conflict detection authorization/privacy; publication/version/rollback and authorized resolution workflow; Unicode trim/uppercase/input encoding edge cases/additional proposed grammar; operation IDs/IAM/actor mappings; Role Audit/failure/recovery; ordinary hide/unhide mandatory reason; history/reference/temporal/API; scope-change/assignment concurrency. See `customer-role-catalog.md` RC-OPEN / RC-PROPOSED.
- Dependents: CM1-PD-068..072; CM1-ROL-30..45 (all PROPOSED / NOT TESTED, software execution BLOCKED pending relevant design). Full links in `source-traceability.json` partialResolutionLedger and decision coverage matrix. Earlier decisions/scenarios and PDQ-002-10/12 dependencies retained.
- No formal closure, new PDQ, absolute-overlap prohibition, extra supervisor requirement for ordinary overlap, global custom-code prohibition across independent Tenants, roleId overlap implementation, automatic IAM/legal grant, or executable schema/contract approval.
