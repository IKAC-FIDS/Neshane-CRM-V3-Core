# CM-1 — Customer Field and Verification Rules Addendum (v1.1.0)

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
- `FLD-002-02`: existing candidate is Persian *display name*. User-confirmed legal/person name minimum should NOT be represented as already implemented by this single field; structured names/naming fields require dictionary expansion/review.
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
