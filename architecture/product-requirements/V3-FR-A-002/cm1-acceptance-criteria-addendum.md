# CM-1 — Candidate Acceptance Criteria Addendum (v1.3.0 proposed package)

**Status:** PROPOSED / NOT EXECUTED / OWNER REVIEW REQUIRED. This file supplements original `acceptance-criteria.md` and its canonical V3-FR-A-002-AC-01..05; it does NOT change canonical assessment or claim PASS. IDs are package-local and should be reconciled before adopting into an authoritative acceptance matrix.

| Candidate ID | Scenario and expected result | Status |
|---|---|---|
| `CM1-FLD-01` | Company can register with required name but no official ID, telephone or email; initial ACTIVE / NOT_VERIFIED. | PROPOSED / NOT TESTED |
| `CM1-FLD-02` | Person can register with required given and family names but no official ID/contact channel; contact person need not be commercial customer. | PROPOSED / NOT TESTED |
| `CM1-FLD-03` | Missing required Company/Person name rejects creation without durable mutation. | PROPOSED / NOT TESTED |
| `CM1-FLD-04` | Structurally valid but unverified official ID is never represented as VERIFIED. | PROPOSED / NOT TESTED |
| `CM1-FLD-05` | Collision with a confirmed verified identifier blocks create/update/verification; probabilistic duplicate warning can be overridden only by authorized CUS-CREATE with reason and Audit. | PROPOSED / NOT TESTED |
| `CM1-VER-01` | New Customer starts NOT_VERIFIED while lifecycle starts ACTIVE. | PROPOSED / NOT TESTED |
| `CM1-VER-02` | Trusted system response for unchanged identity revision and sufficient valid evidence can establish VERIFIED with evidence provenance and coordinated Audit. | PROPOSED / NOT TESTED |
| `CM1-VER-03` | Authorized manual verifier with sufficient evidence can establish VERIFIED; an unrelated CUS-UPDATE cannot set VERIFIED. | PROPOSED / NOT TESTED |
| `CM1-VER-04` | Creator and manual verifier may be same actor in regular workflow only with distinct verification permission. | PROPOSED / NOT TESTED |
| `CM1-VER-05` | Sensitive workflow with SoD requirement rejects creator self-verification even if creator holds a verification permission. | PROPOSED / NOT TESTED |
| `CM1-VER-06` | Expired necessary evidence or change to materially verified identity facts moves effective verification to REQUIRES_REVERIFICATION. | PROPOSED / NOT TESTED |
| `CM1-VER-07` | Fundamentally invalid former verification moves VERIFIED or REQUIRES_REVERIFICATION to NOT_VERIFIED while preserving history. | PROPOSED / NOT TESTED |
| `CM1-VER-08` | Successful new verification returns REQUIRES_REVERIFICATION/NOT_VERIFIED to VERIFIED without erasing prior records. | PROPOSED / NOT TESTED |
| `CM1-VER-09` | No automatic blanket expiry after 12 months when required evidence remains valid and no invalidating event exists. | PROPOSED / NOT TESTED |
| `CM1-VER-10` | Nonessential supporting document expiry and unrelated telephone/address changes do not automatically invalidate verification. | PROPOSED / NOT TESTED |
| `CM1-VER-11` | Missing/timeout/ambiguous provider result does not assert new VERIFIED; provider outage alone does not automatically revoke already-valid verification. | PROPOSED / NOT TESTED |
| `CM1-VER-12` | Stale provider result or manual proof bound to an old identity revision cannot mark a newly edited identity VERIFIED. | PROPOSED / NOT TESTED |
| `CM1-VER-13` | Known revocation that cannot be safely persisted must not be ignored by a consuming sensitive process; fail/recovery semantics remain an approval blocker. | PROPOSED / NOT TESTED |
| `CM1-VER-14` | An unauthorized actor cannot verify, revoke, or read protected evidence; cross-Tenant existence and evidence are not disclosed. | PROPOSED / NOT TESTED |
| `CM1-VER-15` | Each durable verification-state mutation maintains necessary evidence and coordinated durable Audit obligations; failure cannot be reported as a successful state change. | PROPOSED / NOT TESTED |
| `CM1-VER-16` | Customer archive/restore, company branch updates, or person relationship changes preserve prior verification histories and do not automatically propagate verification states. | PROPOSED / NOT TESTED |

## Traceability / exit gates

- Product decisions: CM1-PD-016..028; previous CM1-PD-001..015 retained.
- Original OPEN register stays at **14 OPEN** until explicit Product Decision Owner / TAO review. These decisions partially address PDQ-002-01, PDQ-002-07, PDQ-002-04, PDQ-002-03, PDQ-A001-002, PDQ-A001-003, PDQ-A001-049, PDQ-A001-050, PDQ-A001-052.
- Customer Domain owns final writer/resource authorization; validated Tenant and Membership context, no cross-tenant disclosure.
- New verification workflows and permissions are proposed **logical capabilities**, not additional approved operations or IAM grants. Four source operation concepts remain unchanged.
- Failure/recovery ownership, external provider trust, proof detail, SoD policy catalog, retention and integration deployment are not executable without separate review.

## Relationship / branch / overlap / audit criteria (v1.2.0)

Authoritative controlled-exception overlap policy. All PROPOSED / NOT TESTED. No obsolete absolute-overlap-denial relationship criteria existed to replace (see CM1-PD-041 supersession).

| Candidate ID | Scenario and expected result | Status |
|---|---|---|
| CM1-REL-01 | Same Person may hold multiple concurrent Relationships across Company/Branch; each role is a distinct Relationship. | PROPOSED / NOT TESTED |
| CM1-REL-02 | ENDED Relationship is not reopened; a later recurrence is a separate Relationship. | PROPOSED / NOT TESTED |
| CM1-REL-03 | Half-open interval [startDate,endDate); empty/backwards interval rejected. | PROPOSED / NOT TESTED |
| CM1-REL-04 | Same Person+TargetType+TargetId+RoleCode overlapping intervals allowed only through controlled exception (warning + valid authority + mandatory reason + Audit). | PROPOSED / NOT TESTED |
| CM1-REL-05 | Distinct role codes, different targets, and Company-vs-Branch overlap freely. | PROPOSED / NOT TESTED |
| CM1-REL-06 | Overlap warning permits selecting an existing Relationship OR creating with a mandatory exception reason; no supervisor approval. | PROPOSED / NOT TESTED |
| CM1-REL-07 | Each newly authorized overlap requires its own reason; an old reason does not auto-authorize future changes. | PROPOSED / NOT TESTED |
| CM1-REL-08 | ENDED intervals participate in historical overlap detection. | PROPOSED / NOT TESTED |
| CM1-REL-09 | Updating the same Relationship with a stale record version is rejected. | PROPOSED / NOT TESTED |
| CM1-REL-10 | Concurrent separate overlapping Relationships use a consistent authoritative overlap assessment; re-evaluation required if the conflict set changed after warning. | PROPOSED / NOT TESTED |
| CM1-REL-11 | Idempotent retries produce no unintended additional Relationship record. | PROPOSED / NOT TESTED |
| CM1-REL-12 | Overlap exception does not bypass stale-version, Tenant isolation, validation, or disclosure control. | PROPOSED / NOT TESTED |
| CM1-REL-13 | Warning output does not disclose non-visible Relationship details. | PROPOSED / NOT TESTED |
| CM1-BRN-01 | Branch has only ACTIVE/INACTIVE record states; no independent ARCHIVED. | PROPOSED / NOT TESTED |
| CM1-BRN-02 | Branch companyId is immutable after creation; direct reparenting rejected. | PROPOSED / NOT TESTED |
| CM1-BRN-03 | Branch transfer creates a new Branch and deactivates the original without automatic activity/relationship transfer. | PROPOSED / NOT TESTED |
| CM1-BRN-04 | Deactivating Company does not change stored Branch statuses; deactivating Branch does not modify Company/Person. | PROPOSED / NOT TESTED |
| CM1-BRN-05 | Restoring Company does not auto-activate inactive Branches. | PROPOSED / NOT TESTED |
| CM1-AUD-01 | Mandatory coordinated Audit failure never reported as a successful mutation. | PROPOSED / NOT TESTED |
| CM1-AUD-02 | Broker ACK / outbox is not treated as authoritative Audit ingestion. | PROPOSED / NOT TESTED |
| CM1-AUD-03 | Stale provider result does not overwrite a newer verification state. | PROPOSED / NOT TESTED |

## Expanded testable criteria (v1.2.1) — all PROPOSED / NOT TESTED

| Candidate ID | Scenario and expected result | Status |
|---|---|---|
| CM1-LC-04 | Successful authorized creation initializes lifecycle ACTIVE. | PROPOSED / NOT TESTED |
| CM1-LC-05 | ACTIVE → INACTIVE with open activities preserves them; none are closed or deleted automatically. | PROPOSED / NOT TESTED |
| CM1-LC-06 | INACTIVE → ACTIVE requires revalidation; invalid revalidation rejects the transition. | PROPOSED / NOT TESTED |
| CM1-LC-07 | Archive with any unresolved applicable open dependency is rejected. | PROPOSED / NOT TESTED |
| CM1-LC-08 | Dependency-check failure or unknown result does not authorize archive. | PROPOSED / NOT TESTED |
| CM1-LC-09 | ARCHIVED → INACTIVE restoration is the only restore path. | PROPOSED / NOT TESTED |
| CM1-LC-10 | Direct ARCHIVED → ACTIVE is rejected. | PROPOSED / NOT TESTED |
| CM1-LC-11 | A lifecycle change of one record does not implicitly change the lifecycle of related records. | PROPOSED / NOT TESTED |
| CM1-BRN-06 | Branch creation requires a valid same-Tenant Company parent. | PROPOSED / NOT TESTED |
| CM1-BRN-07 | Effective Branch availability is restricted when the parent Company is inactive or archived (new activities restricted per policy). | PROPOSED / NOT TESTED |
| CM1-BRN-08 | Branch status is preserved independently when the parent Company is deactivated. | PROPOSED / NOT TESTED |
| CM1-BRN-09 | Parent-Company archive is blocked while a Branch has unresolved applicable open dependencies. | PROPOSED / NOT TESTED |
| CM1-BRN-10 | Cross-Tenant Company reference is denied (fail closed). | PROPOSED / NOT TESTED |
| CM1-UPD-06 | Sensitive identifier change requires a mandatory reason. | PROPOSED / NOT TESTED |
| CM1-UPD-07 | Routine edit does not require a business reason but remains audited. | PROPOSED / NOT TESTED |
| CM1-UPD-08 | Verified identifier conflict blocks the update. | PROPOSED / NOT TESTED |
| CM1-UPD-09 | Routine edit of an ARCHIVED record is rejected. | PROPOSED / NOT TESTED |
| CM1-UPD-10 | Mandatory coordinated Audit failure prevents reporting a successful durable mutation. | PROPOSED / NOT TESTED |
| CM1-DUP-04 | Existing-record suggestion is disclosure-safe (no other-customer or cross-Tenant disclosure). | PROPOSED / NOT TESTED |
| CM1-DUP-05 | A repeated identical create request does not create a second Customer where an idempotency contract applies. | PROPOSED / NOT TESTED |
| CM1-REL-14 | Relationship target must be a valid Company/Branch in the same Tenant. | PROPOSED / NOT TESTED |
| CM1-REL-15 | Open-ended (null endDate) interval participates correctly in overlap assessment. | PROPOSED / NOT TESTED |
| CM1-REL-16 | Unauthorized overlap exception is rejected. | PROPOSED / NOT TESTED |
| CM1-REL-17 | Ending one Relationship leaves other Relationships unchanged. | PROPOSED / NOT TESTED |
| CM1-REL-18 | Changing personId or targetId through an ordinary edit is rejected. | PROPOSED / NOT TESTED (policy question: immutability not separately user-confirmed) |
| CM1-AUD-04 | Audit uses controlled evidence references; no identity-document copy into Audit. | PROPOSED / NOT TESTED |
| CM1-AUD-05 | Ordinary warnings/rejected validations carry no assumed mandatory Audit event absent explicit governing source. | PROPOSED / NOT TESTED |

## Role Catalog scenarios (v1.3.0)

Product basis: CM1-PD-058..065 / `customer-role-catalog.md#rc-001--hybrid-catalog-and-organizational-meaning` through RC-008. These are proposed test scenarios, not executed tests or approved API/IAM/persistence contracts. Fixtures use symbolic roles, not an approved standard vocabulary. Contract-dependent assertions require separate design disposition.

| Candidate ID | Scenario and expected result | Status |
| --- | --- | --- |
| CM1-ROL-01 | Given authorized access to a shared System Role and an owning-Tenant custom Role, both are available under their respective catalog boundaries; assigning either organizational role confers no IAM/RBAC grant. | PROPOSED / NOT TESTED |
| CM1-ROL-02 | Given otherwise valid new assignments, COMPANY scope permits Company and rejects Branch; BRANCH permits Branch and rejects Company; BOTH permits either. Missing, multiple or other scope values fail validation. | PROPOSED / NOT TESTED |
| CM1-ROL-03 | Valid authorized Role creation starts ACTIVE. Role lifecycle admits exactly ACTIVE/INACTIVE, not ARCHIVED or ENDED. | PROPOSED / NOT TESTED |
| CM1-ROL-04 | An authorized actor can deactivate ACTIVE and reactivate INACTIVE subject to validation; an actor lacking the applicable authority cannot perform either transition. | PROPOSED / NOT TESTED |
| CM1-ROL-05 | Attempted post-creation roleId or roleCode change is rejected; historical identity/references remain intact. Exact field/API enforcement remains OPEN. | PROPOSED / NOT TESTED |
| CM1-ROL-06 | Physical deletion is unsupported both for a Role with no Relationships and one with historical Relationships; identity and references remain preserved. | PROPOSED / NOT TESTED |
| CM1-ROL-07 | Deactivate then reactivate a Role referenced by ACTIVE and ENDED Relationships: none are created, terminated, reactivated, deleted or modified; individual statuses, intervals and historical references remain unchanged. New assignment to INACTIVE is rejected. | PROPOSED / NOT TESTED |
| CM1-ROL-08 | An appropriately authorized, validated scope change compatible with all existing Relationships is permitted; existing Relationships remain unchanged and subsequent assignments follow the current scope. No extra reason rule for this compatible case is inferred. | PROPOSED / NOT TESTED |
| CM1-ROL-09 | For an incompatible scope change, evaluate affected Relationships and show a disclosure-safe warning; require business reason and appropriate management authority, preserve existing Relationships, retain auditable change/justification, and apply new scope to subsequent assignments only. | PROPOSED / NOT TESTED |
| CM1-ROL-10 | Repeat an incompatible scope-change attempt with missing reason or absent management authority: neither attempt may finalize the change. Neither impact warnings nor rejection output disclose hidden Relationship details. | PROPOSED / NOT TESTED |
| CM1-ROL-11 | After a scope change, Person/Company/Branch states and all existing Relationship states/intervals remain unchanged, including incompatible historical references. | PROPOSED / NOT TESTED |
| CM1-ROL-12 | A Tenant user attempting System Role modification is denied; System Role management requires system catalog authority. Exact operation/permission bindings remain OPEN. | PROPOSED / NOT TESTED |
| CM1-ROL-13 | Tenant A's custom Role is owned by that Tenant: appropriately authorized A actor may manage it; unauthorized A actor and B actor cannot manage/access/reference it. No cross-Tenant exception is assumed without a separate governing contract. | PROPOSED / NOT TESTED |
| CM1-ROL-14 | An actor possessing only CUS-CREATE cannot manage the Role Catalog; organizational Role assignment itself does not provide catalog management authority. | PROPOSED / NOT TESTED |
| CM1-ROL-15 | Authorized title, lifecycle and applicability changes preserve roleId/roleCode and historical Relationship references. Exact historical display and reference representation are OPEN, not assumed snapshots. | PROPOSED / NOT TESTED |
| CM1-ROL-16 | After catalog changes, stale Relationship versions are still rejected; controlled overlapping assignment still requires valid authority/reason and preserves Tenant isolation and mandatory Audit obligations. No catalog change bypasses these checks. Exact reference, overlap key and consistency/Audit failure mechanism remain OPEN. | PROPOSED / NOT TESTED |
