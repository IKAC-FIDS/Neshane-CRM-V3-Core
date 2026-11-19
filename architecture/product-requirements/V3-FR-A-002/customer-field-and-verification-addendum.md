# CM-1 — Customer Field and Verification Rules Addendum (v1.7.0 bounded candidate)

## Current v1.7.0 overlay

CM1-PD-082..091/095 govern current product rules; lower sections retain historical v1.1.0 provenance where noted. Current dictionary has 38 conceptual IDs, including all 31 prior IDs. Mandatory Person given/family names map independently to FLD-002-18/19, Company name to FLD-002-20; FLD-002-02 remains display concept, no mandatory Persian input or generic-name substitute. Optional registration number/country/Company website/notes map to FLD-002-21..24; English name uses FLD-002-03. Complete minimums in dictionary JSON minimumFieldMappings; optional supplied fields validated; exact schemas/normalization/limits OPEN.

Initial multi-identifier vocabulary and applicable Tenant+namespace uniqueness now product-confirmed by PD-083; exact namespace/issuer/legal-format evidence/mechanisms remain OPEN, not overall business uniqueness scope. Official names/identifier/type/issuer changes need reason; material evidence impact requires reverification, including ordinary contact facts when prior basis. Ordinary contact reason remains optional.

Permitted conceptual evidence methods: valid identity-document review, valid Company-registration-document review, authorized manual evidence-backed verification, future trusted system verification. No evidence-free/contact-only/unsupported-assertion formal proof. Required logical evidence information: evidence type, issuing authority, verifying authority, timestamp, outcome, reference; earlier method/identity revision/provenance/reason/correlation/effective-vs-recording information retained. No raw documents copied into Audit.

Three mandatory different-authorized-verifier cases: corrected already-verified identifier; definite-conflict resolution/verification; reverification after fundamental invalidity. Ordinary actor can register and verify only under independent authorities. Exact multi-step actor mapping and additional legal/contractual SoD OPEN. Dispute never automatically restores VERIFIED; three-state lifecycle/no blanket TTL/history preserved. Manual revocation reason/Audit mandatory; verification/reverification requires valid accepted evidence.

Manual verification CONDITIONALLY INCLUDED, subject to approved evidence/issuer/authorization/SoD; real external integration DEFERRED. No real customer data/documents in initial synthetic development; catalogs/legal applicability not resolved by conceptual method names or mock issuers. Retention/history preservation is subject to applicable policy, not unlimited personal retention. Detailed residual blockers and current individual questions: customer-bounded-readiness.json.

**Authority:** USER-CONFIRMED PRODUCT DIRECTION; repository acceptance pending. Complements, does not overwrite, the original `customer-field-dictionary.md/json` (16 fields all officially PROPOSED / OPEN). No database schema, IAM roles, approved technical field names or provider selection inferred.

## Company and Person minimum

| Domain concept | Company | Person | Disposition |
|---|---|---|---|
| Stable internal Customer ID | generated, immutable | generated, immutable | User-confirmed behavior; exact datatype OPEN |
| Display/identity name | Company name required | Given and family name required | User-confirmed minimum; normalization, multilingual rules OPEN |
| Official identifier | optional on create | optional on create | Conditional requirement only for consuming workflows requiring formal verification |
| Telephone/email | optional | optional | No mandatory contact channel at initial create; no global uniqueness |
| Record lifecycle | ACTIVE after successful create | ACTIVE after successful create | Distinct from commercial and verification status |
| Commercial engagement status | separate / may be absent | separate / may be absent (e.g. corporate contact person) | Taxonomy OPEN |
| Identity verification state | NOT_VERIFIED initially | NOT_VERIFIED initially | May be VERIFIED later via trusted workflow |

## Original candidate field mapping

- `FLD-002-01` stable internal identity: immutable, tenant-scoped visibility; not an official identifier.
- `FLD-002-02`: retained display-name concept; current v1.7.0 dictionary separately maps mandatory Person given/family and Company name (FLD-002-18/19/20). This is documented product mapping, not implementation.
- `FLD-002-04` Person identifier; `FLD-002-05` Company legal identifier: optional on create; issuer/type/jurisdiction, normalisation, proof of verification, uniqueness namespace and collision policy to be specified.
- `FLD-002-06` telephone and `FLD-002-07` email: optional; no dedup hard block solely on channel match.
- `FLD-002-09` commercial category distinct from verification and record lifecycle.
- `FLD-002-10` record status ACTIVE/INACTIVE/ARCHIVED; initial ACTIVE; transitions governed by PDR.
- `FLD-002-14` currently 'Validation state' is NOT automatically identical to formal 'verificationStatus'. Separate data-quality validation, identity verification and evidence decisions explicitly; update the canonical dictionary only after field owner review.
- `FLD-002-15` Audit correlation: continue existing coordinated durable obligations (DEC-012/13/14), no uncontrolled sensitive evidence dump.
- `FLD-002-11/12/13/16` unchanged and retain source proposal constraints.

## Verified identifier and matching guards

1. A missing official identifier does not block registration. An invalid present identifier must never be called valid or verified.
2. A structurally valid identifier is not the same as an externally or manually VERIFIED identity. Verification requires a trusted source and documented evidence.
3. Verified identifier collisions block contradictory create/update/verification. Match-warning override is only for probabilistic candidates and requires CUS-CREATE authorization, reason and coordinated Audit.
4. Identifier namespaces, cross-Tenant visibility, and exact race-safe DB enforcement remain OPEN. No cross-Tenant existence disclosure or identity sharing permitted.
5. Change of material verified identity fields invalidates reliance on the former verification; ordinary contact information updates do not unless that contact fact was explicitly material to verification.

## Verification evidence — candidate attributes, NOT approved schema

`verificationId`, `customerId`, `verificationStatus`, `verificationMethod` (SYSTEM/MANUAL), `source/issuer`, `verifiedBy`, `verifiedAt`, `identityRevision`, `evidenceReference`, `evidenceValidUntil` (when applicable), `reasonCode`, `effectiveAt`, `recordedAt`, `correlationId`.

- Evidence references must be access-controlled; do not copy identity documents into general Audit entries.
- Manual success requires a separately authorized verifier and adequate evidence. In regular workflows the creator may also verify; in designated sensitive workflows it must be another actor.
- No universal verification TTL. Necessary-evidence expiry or material identity changes → REQUIRES_REVERIFICATION; fundamentally wrong original verification → NOT_VERIFIED. No history destruction.
- Provider outage alone does not auto-revoke an existing verification, nor permit a new unverified claim to become VERIFIED. If previously known revocation cannot be persisted, sensitive consumers must not be assured a verified status; exact recovery OPEN.

## Still OPEN

Source/issuer trust catalog; identifier jurisdiction/formats and uniqueness scope; field-level normalization; formal verification trigger in consuming workflows; accepted evidence and expiry semantics; sensitive process catalog and SoD actor mappings; retention, legal hold, evidence storage; operation-specific Audit failure/recovery, integration boundaries and executable authorization.

## Current v1.8.0 refinement (overrides only corresponding historical OPEN product portions)

See `customer-v180-scope-and-document-catalog.md` and PDR.
- CM1-PD-99: Tenant-configurable document types, no code release needed for additions. Stable document ID and fixed unique document code; Persian title, optional English title, description, applicability PERSON/COMPANY/BOTH, mandatory/optional stage, single/multiple files, permitted formats, maximum size within platform bounds, expiry-date applicability, ACTIVE/INACTIVE, display order. Example document types are illustrative, not global obligations. Exact code grammar/namespace, configuration storage and platform file limits OPEN.
- CM1-PD-100: Tenant can require a document at initial registration or identity verification, or leave optional; default no mandatory initial registration documents. Add mandatory type or change optional to mandatory for subsequent applicable operations; mandatory to optional removes obligation; deactivate prevents new uploads for that type while preserving existing documents; rename retains identity; no physical deletion of type. Configuration changes do not automatically invalidate prior verification. Actual policy/legal prerequisites remain applicable.
- CM1-PD-101: Include authorized upload/view of one or multiple identity/company registration files as configured; record type, files, document number if needed, issue date, expiry when applicable, issuer, notes, uploader, upload date and version history. Replacement preserves prior versions. Upload alone does not set VERIFIED; independent authorized manual review with evidence and SoD still required. No OCR, automatic authenticity checking, external verification, general document-management or independent per-document approval workflow; expiry notifications deferred. File security and protected access mandatory; real evidence prohibited in initial synthetic development.
- CM1-PD-102: Show NOT_PROVIDED, PROVIDED, EXPIRED, SUPERSEDED, INVALIDATED. PROVIDED denotes upload, not authenticity. INVALIDATED by authorized user; replacement retains historical SUPERSEDED version. Show completed mandatory documents versus total applicable mandatory documents, separately from verification status. Exact computation for stage, expiry/invalidity, zero denominator and precedence remains OPEN where not expressly settled; no new verification shortcuts.
- CM1-PD-103: Independent authority for catalog management, upload/replacement/customer-document management, and view/download. Catalog, upload, replacement and other mutations and access to sensitive documents require Audit; no automatic rights from other responsibilities. Preserve durable Audit and evidence minimization constraints. File storage, malware controls, authorization mappings, lifecycle/retention and recovery contracts remain OPEN.

All 19 PDQs remain OPEN; no formal acceptance, executable contract or Gate change.
