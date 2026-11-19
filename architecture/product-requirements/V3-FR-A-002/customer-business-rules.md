# Customer business-rule catalog — V3-FR-A-002

## Current four-package rules — v1.7.0

CM1-PD-078..095 are user-confirmed product direction, formal acceptance PENDING. Read earlier OPEN clauses below as historical only where answered by these rules. Full scope and current 19 question dispositions: customer-bounded-readiness.md / .json.

- Ownership/actors: Farzad accountability and five independent logical responsibilities, no IAM grants. Exact operation/resource/disclosure boundaries remain OPEN.
- Fields/identifiers: Company name and Person given/family required; listed optional values validated if supplied, identifiers required only by formal-verification workflows. Six extensible jurisdiction-aware identifier concepts, multiple per entity; verified-valid uniqueness within applicable Tenant+namespace, no global dedup/definite override. Namespaces/legal formats/issuer evidence/technical validation OPEN.
- Basic duplicates: same verified-valid official identifier definite conflict blocks; same unverified identifier, Company name, Person given+family, phone or email warns; multiple signals higher warning priority, never identity proof. Reuse or authorized reason/Audit exception without supervisor; fuzzy detection deferred, merge/delete excluded.
- Critical edits: official Company/Person names and identifiers/type/issuer need reason. Material evidence impact requires reverification; ordinary contacts/address no default reason but evidence-basis changes still matter. PD-085/092 explicitly refine the narrower PD-015 interpretation; stale writes/unauthorized updates still denied.
- Relationships: Person/target/Role not replaced in ordinary edit; END+new correction. Manual END reason/Audit, natural expiry no manual END reason. Calendar-day half-open interval, future/open end allowed; reference selection OPEN. No inactive Person/Company/Branch new operational assignments; preserve history, no retrospective workflow grant. Controlled overlap PD-033..041 unchanged.
- Archive/reactivation: CM1-PD-087 applicable dependency catalog and unknown-blocks guard; no fictional integrations. Closed/history not independent blockers; archive/restoration conditional. Deactivate with dependencies permitted with mandatory reason/Audit; reactivation validates mandatory facts/conflicts/authority/Audit, ordinary reason optional, no universal VERIFIED prerequisite or related activation.
- Verification: evidence mandatory, issuer/evidence/legal catalogs OPEN and real documents prohibited. Three mandatory different-verifier cases in PD-090, ordinary independent dual authority allowed. No dispute auto-VERIFIED, no universal expiry; state/history rules retained.
- Audit/retention: all Customer mutations and unauthorized mutation attempts audited, protected evidence/Audit access independently authorized/traceable; reason matrix in operation catalog. PD-092 is explicit governing-source exception to PD-049, not blanket ordinary read/warning/validation Audit. No guaranteed durable obligation or unknown outcome -> no definite success; no executable continuation/fail-open. Preserve history subject to applicable retention, no unlimited personal retention. Catalog PD-073..077 unchanged.

Initial scope synthetic only; profile/nine branch applicability/time reference/exact disclosure and legal/evidence facts OPEN. Scope exclusions/deferrals do not delete roadmap obligations or authorize implementation.

Classification legend: **APPROVED SOURCE INVARIANT** (baseline architecture/audit) · **USER-CONFIRMED PRODUCT DIRECTION** (product policy, acceptance pending) · **PROPOSED IMPLEMENTATION/CONTRACT** · **OPEN DECISION**.

## APPROVED SOURCE INVARIANT

- Customer Domain owns Customer Master data; authoritative writer and final resource/action authorizer (V3-002B-DEC-002).
- Validated Tenant Context; client selector untrusted; cross-tenant fails closed.
- Durable CUS-CREATE/CUS-UPDATE require coordinated mandatory Audit obligation; success not reported without the durably recorded obligation (DEC-012).
- Explicit disclosure denial carries disclosure-safe Audit obligation; zero-result search is not a denial (DEC-012 p3).
- Broker ACK / Outbox record is not authoritative Audit ingestion (DEC-013/014).
- Pending Submission PERMITTED NOT REQUIRED; never authoritative; external recording prohibited (DEC-005).

## USER-CONFIRMED PRODUCT DIRECTION

**Entity model:** Company and Person independent; Branch subordinate to Company; Person may have multiple concurrent relationships without duplicating identity (CM1-PD-001..004).

**Duplicates (policy confirmed):** probabilistic match → warning + suggestion; authorized CUS-CREATE override with mandatory reason; no supervisor approval; verified identifier collision cannot be overridden; no automatic merge (CM1-PD-005..007, CM1-PD-052). *Still OPEN: exact matching algorithm, identifier namespace/uniqueness enforcement, full merge/delete/retention workflows.*

**Lifecycle:** ACTIVE/INACTIVE/ARCHIVED with the transition matrix in customer-lifecycle.md §B (CM1-PD-008..012, CM1-PD-054).

**CUS-UPDATE / concurrency (policy confirmed):** optimistic concurrency; reject stale versions; no auto-merge/last-write-wins (CM1-PD-013..015, CM1-PD-055). *Still OPEN: exact API contract and persistence enforcement.*

**Identity verification (policy confirmed):** system/manual verification; separate verification authority; evidence-based validity; no universal expiry; SoD for sensitive processes (CM1-PD-019..028, CM1-PD-056/057). *Still OPEN: trusted provider catalog, formal evidence acceptance, sensitive-process catalog, provider failure/recovery.*

**Relationship and overlap (authoritative):** multiple concurrent relationships; controlled overlap exception (warning + authority + mandatory reason + Audit); distinct roles/targets overlap freely; supersedes absolute-overlap prohibition (CM1-PD-029..041).

**Branch:** subordinate; immutable companyId; no direct reparenting; transfer via new Branch; only ACTIVE/INACTIVE (CM1-PD-042..047).

**Audit boundaries:** durable mutations honor coordinated obligations; proposed Branch/Relationship/Verification operations require auditability requirement (contract pending); no blanket mandatory Audit for unrelated warnings/rejected validations/reads; controlled evidence references; ACK != ingestion (CM1-PD-048..051). CM1-PD-077 now explicitly requires catalog-operation and unauthorized catalog-modification Audit; ordinary catalog reads gain no independent product Audit rule and security monitoring/source obligations remain unaffected.

Role Catalog product policy is user-confirmed in CM1-PD-058..065, not wholly undecided. [customer-role-catalog.md](customer-role-catalog.md) RC-001..008 is the detailed rule catalog: hybrid system/Tenant roles, applicability, lifecycle, immutable identity/no deletion, preservation, controlled scope changes, Tenant/system authority and overlap/history. Formal acceptance remains pending; exact executable contracts remain OPEN.

**Initial vocabulary / Tenant selectability:** CM1-PD-066/067 / RC-009..011 confirm the exact 12-entry initial System vocabulary and locally managed assignment restriction. Global ACTIVE, target applicability, Tenant selectability, Relationship authority and existing guards are jointly necessary, enforced by Customer Domain. Hide/unhide cannot modify global definitions, other Tenants or existing Relationships/history, grant permissions/legal authority, or bypass global INACTIVE. It has no inferred mandatory-reason rule and does not replace RC-006 management authority for incompatible scope changes. Preserve ordinary authorized overlap's no-extra-supervisor rule and conceptual roleCode key; technical reference/key remains OPEN.

**v1.5.0 product answers (not implementation):** CM1-PD-068..072 / `customer-role-catalog.md` RC-012..016 confirm ACTIVE System Role default selectability for new Tenants/new releases with prior settings preserved; canonical System-global versus owning-Tenant uniqueness; permanent scope-bound reservation; blocking only the conflicting new System Role without destructive resolution; and trim-uppercase / ASCII A-Z, 0-9, underscore / length 3..64. Matching custom codes across independent Tenants are allowed. No new lexical first-letter/underscore-placement restriction or central Tenant-private-data inspection right. Formal acceptance remains PENDING.

**v1.6.0 governance/history/Audit answers:** CM1-PD-073..077 / `customer-role-catalog.md` RC-017..021 confirm OPTIONAL Hide/Unhide reason with MANDATORY Audit by own-Tenant authorized managers; controlled System versus own-custom display metadata governance; current valid Relationship title versus preserved event-time historical title; three independent logical authority categories with Backend enforcement; catalog Audit coverage/logical information, history isolation/immutability and no successful state-change report without durable Audit guarantee. Ordinary reasons optional; incompatible-scope reason and publication reason including release reference mandatory. Metadata cannot alter fundamental Role semantics/identity or existing Relationships; materially different Role needs new Role/new code. No new IAM grant, required language field, localization/temporal/Audit transaction mechanism is approved.

## PROPOSED IMPLEMENTATION/CONTRACT

- Persistence/API schema for fields, relationships, and verification state (all unapproved).
- Overlap conflict-set token/snapshot/locking/transactional mechanics (technical design, not API contract).
- Branch reparenting coordination workflow and activity-transfer contracts.

## OPEN DECISION

- Other Customer field/identifier validation remains unresolved. Role code/default policies, Hide/Unhide reason, display/history policy, logical authorities and catalog Audit/reason/information policy are ANSWERED through CM1-PD-077. OPEN: exact schema/configuration/default materialization, namespace/concurrency, cross-Tenant detection/privacy, publication/rollback/resolution, Unicode/encoding/localization, IAM/operation/grant/actor/technical enforcement, Audit schema/transactions/storage/retention/recovery/access and temporal/version/snapshot/reference/API mechanisms (PDQ-002-08). Identifier namespace/scope remains separately OPEN.
- Merge/deletion/retention/legal-hold; operation-specific Audit failure/recovery owner and policy.
- Sensitive-process catalog and SoD actor mapping; trusted provider catalog; evidence acceptance/retention.

## Current v1.8.0 refinement (overrides only corresponding historical OPEN product portions)

See `customer-v180-scope-and-document-catalog.md` and PDR.
- CM1-PD-99: Tenant-configurable document types, no code release needed for additions. Stable document ID and fixed unique document code; Persian title, optional English title, description, applicability PERSON/COMPANY/BOTH, mandatory/optional stage, single/multiple files, permitted formats, maximum size within platform bounds, expiry-date applicability, ACTIVE/INACTIVE, display order. Example document types are illustrative, not global obligations. Exact code grammar/namespace, configuration storage and platform file limits OPEN.
- CM1-PD-100: Tenant can require a document at initial registration or identity verification, or leave optional; default no mandatory initial registration documents. Add mandatory type or change optional to mandatory for subsequent applicable operations; mandatory to optional removes obligation; deactivate prevents new uploads for that type while preserving existing documents; rename retains identity; no physical deletion of type. Configuration changes do not automatically invalidate prior verification. Actual policy/legal prerequisites remain applicable.
- CM1-PD-101: Include authorized upload/view of one or multiple identity/company registration files as configured; record type, files, document number if needed, issue date, expiry when applicable, issuer, notes, uploader, upload date and version history. Replacement preserves prior versions. Upload alone does not set VERIFIED; independent authorized manual review with evidence and SoD still required. No OCR, automatic authenticity checking, external verification, general document-management or independent per-document approval workflow; expiry notifications deferred. File security and protected access mandatory; real evidence prohibited in initial synthetic development.
- CM1-PD-102: Show NOT_PROVIDED, PROVIDED, EXPIRED, SUPERSEDED, INVALIDATED. PROVIDED denotes upload, not authenticity. INVALIDATED by authorized user; replacement retains historical SUPERSEDED version. Show completed mandatory documents versus total applicable mandatory documents, separately from verification status. Exact computation for stage, expiry/invalidity, zero denominator and precedence remains OPEN where not expressly settled; no new verification shortcuts.
- CM1-PD-104: Tenant-configurable timezone; initial Iran timezone Asia/Tehran. Relationship business dates are calendar days in Tenant timezone, half-open [start,end), future starts/open ends permitted. Issue/expiry of documents are calendar dates; date-only facts do not shift with timezone. Events and Audit timestamps UTC; user-local presentation and Persian/Gregorian calendar configurable independently of language. Preserve past business dates when Tenant timezone changes, and event history unchanged. Exact timezone-change effective evaluation and storage mechanisms OPEN.
- CM1-PD-105: Company name and Branch name required 1–255 characters; Person given/family names required 1–100 each; English name optional max 255; address max 1000, notes max 4000. Unicode, trim leading/trailing whitespace; preserve original display and normalized search/match representation. Phone supports domestic/international numbers, email structure, website HTTP/HTTPS, country catalog, province/city and postal validation per country. Optional fields validated if supplied; no uniqueness of names/phone/email. Backend validation mandatory. Exact character-count/normalization, country dataset and official identifier legal formats OPEN; structural validation is not identity proof.
- CM1-PD-106: Permit multiple phones, emails and addresses; allow designation of primary phone, primary email and primary address, and contact channel type. Removal/deactivation preserves required history and Audit. No new mandatory contact or address; exact primary replacement, contact type vocabulary and retention mechanisms OPEN.

All 19 PDQs remain OPEN; no formal acceptance, executable contract or Gate change.
