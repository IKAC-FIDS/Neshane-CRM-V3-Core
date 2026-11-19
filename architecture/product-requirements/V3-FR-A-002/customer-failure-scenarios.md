# Customer failure scenarios — V3-FR-A-002

## Current additional failure boundaries — v1.7.0

User-confirmed policies CM1-PD-078..095; scenarios PROPOSED / NOT TESTED; all implementation-dependent execution BLOCKED. Exact new coverage CM1-BND-01..54 in addendum. No failure simulation/runtime executed.

| Failure/scenario | Product-required outcome / limitation | New scenarios |
| --- | --- | --- |
| Generic display name without required Person parts | Mandatory given/family validated independently; no substitution or extra mandatory language inferred | CM1-BND-09, CM1-BND-10 |
| Invalid optional supplied field / unknown identifier validator | Optional does not mean unvalidated; no made-up legal format/issuer/checksum or fake validation PASS | CM1-BND-11, CM1-BND-13 |
| Same unverified identifier/name/phone/email | Warning, not definite proof; multiple signals raise warning priority, not verification; controlled exception reason/Audit, no supervisor | CM1-BND-17, CM1-BND-18, CM1-BND-19, CM1-BND-20, CM1-BND-21 |
| Definite verified conflict / unauthorized correction | Block override; require controlled authorized correction/SoD and no cross-Tenant leakage | CM1-BND-15, CM1-BND-16 |
| Missing critical-name/type/issuer/lifecycle/END/revocation reason | Cannot finalize as valid successful mutation; optional ordinary reasons cannot bypass sensitive/exception class | CM1-BND-22, CM1-BND-34, CM1-BND-36, CM1-BND-46 |
| Relationship Person/target/Role replacement / inactive assignment | Reject in-place identity replacement/new inactive operational assignment; authorized END+new preserves history and overlap guards | CM1-BND-25, CM1-BND-29, CM1-BND-30 |
| No selected time reference / natural expiry | Day-granularity selected, exact boundary results not guessed; natural expiry requires no manual END reason or inferred scheduling mutation | CM1-BND-26, CM1-BND-27, CM1-BND-28 |
| Unknown applicable archive dependency, unavailable or unimplemented source | Affected archive blocked; no mock/no-service result treated as clearance; closed/history alone not blocker | CM1-BND-31, CM1-BND-32, CM1-BND-33 |
| Invalid/unauthorized reactivation | Block on mandatory fields/definite conflicts/authority/Audit; no universal VERIFIED guard or related activation added | CM1-BND-35, CM1-BND-36 |
| Evidence-free or sensitive same-actor verification / dispute | No evidence-free success; enforce three different-verifier cases, independent grants, no dispute auto-VERIFIED/history erasure | CM1-BND-39, CM1-BND-41, CM1-BND-42, CM1-BND-43, CM1-BND-44 |
| Unauthorized mutation or protected evidence/Audit access | Fail closed and disclosure-safe; unauthorized mutation attempts require Audit; protected access independently authorized/traceable, exact event/access contracts OPEN | CM1-BND-45, CM1-BND-49 |
| Audit obligation unavailable or unknown | No definite success; preserve originating effect/obligation consistency, no ACK/outbox-as-ingestion | CM1-BND-51 |
| Central Audit unavailable / unauthorized Audit edit | No automatic fail-open/continuation; preserve Sovereign local authority; deny Audit change and treat attempt as security event, no fabricated durable recording | CM1-BND-52, CM1-BND-53 |
| Real data/document or excluded/deferred workflow requested | Outside scope, not executed or PASS; no production/profile/control waiver | CM1-BND-04, CM1-BND-05, CM1-BND-07, CM1-BND-08, CM1-BND-40, CM1-BND-54 |

The preserved older validation-only no-assumed-event wording below does not waive the explicit PD-092 Audit of unauthorized mutation attempts or protected-access traceability. It also does not impose a new mandatory event for every unrelated warning/read/validation failure. No executable transaction/retry/continuation policy selected.

PROPOSED acceptance examples; not executed; not accepted.

The first matrix retains historical source-baseline dispositions. Its former policy-OPEN notes do not override later user-confirmed lifecycle/duplicate/concurrency directions or the Role Catalog overlays below; exact operational mechanisms/formal acceptance remain OPEN/PENDING. No existing policy is superseded by this source-baseline table.

| Scenario | Type | Required behavior | Status |
| --- | --- | --- | --- |
| CUS-CREATE with invalid/incomplete data | Validation failure | Reject; no authoritative record; no mandatory Audit event for rejection | PROPOSED |
| CUS-CREATE where Audit obligation cannot be durably recorded | Audit failure | Do not report success; do not commit mutation (DEC-012 p4) | APPROVED boundary, mechanics OPEN |
| CUS-UPDATE concurrent modification | Concurrency | Detect conflict; no silent overwrite (policy OPEN) | PROPOSED |
| Potential duplicate detection | Duplicate | Flag for review; no automatic merge (policy OPEN) | PROPOSED |
| Unauthorized operation | Authorization | Fail closed; Customer Domain denies; disclosure-safe | APPROVED invariant, matrix OPEN |
| Cross-tenant access attempt | Tenant isolation | Fail closed | APPROVED invariant |
| Invalid lifecycle transition | Lifecycle | Reject; no approved transition bypass | PROPOSED |
| Audit ingestion unavailable | Audit outage | Per DEC-013/014; no executable DURABLE_DEFER | OPEN |

Every scenario requires owner-approved examples before acceptance. See PDQ-002-06, PDQ-A001-049.

## Concurrency, race and idempotency (user-confirmed)

| Scenario | Required behavior | Status |
| --- | --- | --- |
| CUS-UPDATE stale record version | Reject without changing data; no auto-merge / last-write-wins | PROPOSED (CM1-PD-014) |
| Same Relationship updated with stale version | Reject stale version | PROPOSED (CM1-PD-038) |
| Concurrent creation of separate overlapping Relationships | Consistent authoritative overlap assessment; re-evaluate if conflict set changed | PROPOSED (CM1-PD-038) |
| Idempotent retry of Relationship create | No unintended additional Relationship record | PROPOSED (CM1-PD-039) |
| Intentional overlap vs accidental duplicate | Distinguished; exception requires reason | PROPOSED (CM1-PD-039) |
| Overlap exception vs Tenant isolation/validation | Exception never bypasses stale/tenant/validation/disclosure | PROPOSED (CM1-PD-040) |
| Mandatory coordinated Audit failure | Do not report successful mutation | APPROVED invariant (CM1-PD-051) |
| Stale provider result vs newer verification state | Stale result never overwrites newer state | PROPOSED (CM1-PD-051) |

## Catalog governance, historical integrity and Audit failures (v1.6.0)

CM1-PD-073..077 product scenarios; **PROPOSED / NOT TESTED; implementation-dependent execution BLOCKED** pending exact operation/IAM/temporal/Audit transaction/recovery contracts. Existing Customer mutation boundaries above remain unchanged; no runtime execution or protocol approval.

| Scenario | Required product outcome | Proposed criterion |
| --- | --- | --- |
| Missing reason for otherwise valid Hide/Unhide or ordinary metadata change | Reason omission alone is not a rejection condition; mandatory Audit and old/new information remain required | CM1-ROL-46, CM1-ROL-49, CM1-ROL-63 |
| Wrong-Tenant/unauthorized catalog modification attempt | Backend denies; mandatory Audit without protected cross-Tenant disclosure; no change to other Tenant/Role/Relationships | CM1-ROL-48, CM1-ROL-67 |
| System metadata edit by Tenant manager or through uncontrolled release | No authority inferred; reject unauthorized path, preserve global definition, record mandatory Audit of unauthorized attempt | CM1-ROL-50, CM1-ROL-57, CM1-ROL-67 |
| Materially different business responsibility disguised as rename | Cannot repurpose existing identity/code; new Role/new code needed under existing namespace/reservation rules, no automatic Relationship migration | CM1-ROL-52 |
| Rename followed by current/history read | Current valid title in authorized current view; historical event/Audit title stays event-time value. Missing historical representation must not be fabricated from current title; representation/recovery contract OPEN | CM1-ROL-54, CM1-ROL-55 |
| Hidden/INACTIVE Role or denied historical view | Existing references remain visible only to otherwise authorized viewers; hide/inactive is not history deletion, nor a new access grant | CM1-ROL-56 |
| Missing incompatible-scope reason or publication reason/release reference | Do not finalize as valid successful change; preserve scope safeguards; ordinary optional reasons do not waive these requirements | CM1-ROL-64, CM1-ROL-65 |
| Mandatory durable catalog Audit guarantee unavailable | Do not report successful state change; preserve existing coordinated mutation/Audit obligations, no ACK/outbox-as-ingestion or unapproved DURABLE_DEFER. Exact transaction/failure/recovery outcome remains OPEN | CM1-ROL-69 |
| Unauthorized modification with Audit subsystem failure | Remain denied and disclosure-safe; inability to establish Audit evidence is not success/compliance or permission to proceed. Failure/recovery contract remains OPEN | CM1-ROL-67, CM1-ROL-69 |
| Catalog manager or ordinary user edits/deletes Audit history | Deny; protect isolated historical values through title/status/scope changes; no Audit-administration grant inferred | CM1-ROL-68 |

Ordinary catalog reads have no independent mandatory product Audit event under CM1-PD-077; security monitoring and prior governing source obligations remain unaffected. Unauthorized catalog modification attempts now have an explicit Audit basis, unlike a blanket assumption for every warning/read/rejected validation.

## Current v1.8.0 refinement (overrides only corresponding historical OPEN product portions)

See `customer-v180-scope-and-document-catalog.md` and PDR.
- CM1-PD-96: Operator: ordinary customer create/update, Branch/Relationship management and general read; independent explicit authority for duplicate exception, activation/deactivation, archive/restore. Reviewer: general read; Catalog Manager: selectable roles and own-Tenant role catalog; Verifier: general read and verification, separate authority for revocation/evidence; Audit Reviewer: authorized Audit review only. Operator/Reviewer/Catalog Manager may view selectable roles. General customer read includes contact and verification status; official identifiers masked absent independent identity-field access; Branch/Relationship require relevant resource access; evidence content and business history require independent authority; Audit access separately authorized. Deny by default, no foreign-Tenant disclosure, warnings limited to authorized facts, Backend authorization mandatory; no IAM grants.
- CM1-PD-100: Tenant can require a document at initial registration or identity verification, or leave optional; default no mandatory initial registration documents. Add mandatory type or change optional to mandatory for subsequent applicable operations; mandatory to optional removes obligation; deactivate prevents new uploads for that type while preserving existing documents; rename retains identity; no physical deletion of type. Configuration changes do not automatically invalidate prior verification. Actual policy/legal prerequisites remain applicable.
- CM1-PD-101: Include authorized upload/view of one or multiple identity/company registration files as configured; record type, files, document number if needed, issue date, expiry when applicable, issuer, notes, uploader, upload date and version history. Replacement preserves prior versions. Upload alone does not set VERIFIED; independent authorized manual review with evidence and SoD still required. No OCR, automatic authenticity checking, external verification, general document-management or independent per-document approval workflow; expiry notifications deferred. File security and protected access mandatory; real evidence prohibited in initial synthetic development.
- CM1-PD-102: Show NOT_PROVIDED, PROVIDED, EXPIRED, SUPERSEDED, INVALIDATED. PROVIDED denotes upload, not authenticity. INVALIDATED by authorized user; replacement retains historical SUPERSEDED version. Show completed mandatory documents versus total applicable mandatory documents, separately from verification status. Exact computation for stage, expiry/invalidity, zero denominator and precedence remains OPEN where not expressly settled; no new verification shortcuts.
- CM1-PD-103: Independent authority for catalog management, upload/replacement/customer-document management, and view/download. Catalog, upload, replacement and other mutations and access to sensitive documents require Audit; no automatic rights from other responsibilities. Preserve durable Audit and evidence minimization constraints. File storage, malware controls, authorization mappings, lifecycle/retention and recovery contracts remain OPEN.
- CM1-PD-104: Tenant-configurable timezone; initial Iran timezone Asia/Tehran. Relationship business dates are calendar days in Tenant timezone, half-open [start,end), future starts/open ends permitted. Issue/expiry of documents are calendar dates; date-only facts do not shift with timezone. Events and Audit timestamps UTC; user-local presentation and Persian/Gregorian calendar configurable independently of language. Preserve past business dates when Tenant timezone changes, and event history unchanged. Exact timezone-change effective evaluation and storage mechanisms OPEN.
- CM1-PD-105: Company name and Branch name required 1–255 characters; Person given/family names required 1–100 each; English name optional max 255; address max 1000, notes max 4000. Unicode, trim leading/trailing whitespace; preserve original display and normalized search/match representation. Phone supports domestic/international numbers, email structure, website HTTP/HTTPS, country catalog, province/city and postal validation per country. Optional fields validated if supplied; no uniqueness of names/phone/email. Backend validation mandatory. Exact character-count/normalization, country dataset and official identifier legal formats OPEN; structural validation is not identity proof.

All 19 PDQs remain OPEN; no formal acceptance, executable contract or Gate change.
