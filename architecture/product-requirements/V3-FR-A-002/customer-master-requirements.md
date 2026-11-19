# Customer Master requirements — V3-FR-A-002

## Current bounded requirements — v1.7.0

CM1-PD-078..095 record four user-approved packages; formal acceptance PENDING. Farzad Business Owner/product requirements authority and interim Audit failure/ingestion/recovery/reconciliation accountable authority; development team technical responsibility, no runtime grants. Five independent logical actors and unresolved disclosure bindings: actor-resource-policy-matrix.md.

Current scope/acceptance limitations: customer-bounded-readiness.md / .json. Registration/maintenance/contact/Branch/Related Person/Relationship/catalog/basic duplicates/activation/deactivation included; Customer search/review included in selected CM-1 scope but detailed FR-BJ-002 requirements remain V3-FR-A-003, not completed here. Archive/restoration and manual verification conditional. Real external verification, executable Branch transfer coordination and fuzzy matching deferred. Merge/physical Customer deletion/Pending Submission/draft/direct external access excluded from CM-1; offline prohibited. Deferred scope remains on roadmap.

Approved behavior: mapped Company/Person minimums; multi-identifier Tenant+namespace model; basic duplicate signals; sensitive official names/type/issuer reasons; immutable ordinary Relationship Person/target/Role with END+new correction/manual-END reason; calendar-day [start,end) with exact time reference OPEN; inactive assignment prohibition; archive dependency list/reactivation guards; evidence-backed verification/three SoD cases/no dispute auto-restore; all mutations/unauthorized attempts Audit, reason matrix and protected-access traceability. Exact rules in PDR JSON, field dictionary/lifecycle/operation catalog; no schema/API/IAM mechanism selected.

Earlier source OPEN statements below are historical where refined by PDR. Exact actors/disclosure/profile/nine branches/time reference/unspecified validations/legal-issuer-evidence applicability and technical contracts remain OPEN. Synthetic only, no real customer data/documents; no implementation/F-000 or formal acceptance authorized. Tenant isolation, owning-Domain authorization and all Gates preserved.

**Requirements engineering / specification preparation only.** FR-BJ-001 scope. No product implementation, field approval, role/RBAC, API/schema or technology selection. APPROVED / PROPOSED / OPEN are explicit and source-located. This specification does NOT cover FR-BJ-002 Customer Search and Browse.

## Approved scope (source-derived, not inferred)

- **Company/person/contact master maintenance**; Customer owns branch and relationship facts. (V3-002B-DEC-002; support-matrix §5 FR-BJ-001). Evidence EVID-002-002, EVID-002-003, EVID-002-001.
- **Customer Domain** is authoritative writer and final resource/action authorizer; Platform Core supplies validated Tenant/Membership context. Evidence EVID-002-003, EVID-002-015.
- Three deployment profiles with compatible semantics and independent evidence; local Sovereign authority retained.

## Domain model

- **ENT-002-01 — Company** (APPROVED_CONCEPT): Legal/organizational customer master entity. Authoritative organization customer master; detailed attributes/identifiers OPEN
- **ENT-002-02 — Person** (APPROVED_CONCEPT): Individual customer master entity. Individual/contact person master; national identifiers OPEN
- **ENT-002-03 — Contact** (APPROVED_CONCEPT): Contact point associated with a company or person. Contact master; relationship to company/person and channel details OPEN
- **ENT-002-04 — Branch** (APPROVED_CONCEPT): Organizational branch/unit owned by Customer Domain. Branch fact owned by Customer Domain; hierarchy/validation OPEN
- **ENT-002-05 — Relationship** (APPROVED_CONCEPT): Relationship fact between customer master records. Customer-owned relationship facts; type and referential rules OPEN

Individual vs organizational: Person vs Company are documented; Contact, Branch and Relationship are Customer Domain-owned facts. This source-derived entity inventory did not specify detailed fields/identifiers/classification/lifecycle. Current user-confirmed overlays below and in the lifecycle/field documents apply; exact executable contracts and formal acceptance remain separately OPEN/PENDING, not a blanket rejection of confirmed product rules.

## Non-functional and security boundaries (existing, preserved)

- Validated/revalidated Tenant Context; client Tenant values are selectors only; invalid context fails closed. Evidence EVID-002-013.
- Owning Domain authorizes every operation/object; identity/Membership/eligibility never substitute. Evidence EVID-002-014, EVID-002-015.
- Customer durable CUS-CREATE/CUS-UPDATE require coordinated Audit obligations (DEC-012); executable DURABLE_DEFER NOT approved (DEC-013/014). Evidence EVID-002-010, EVID-002-011, EVID-002-012.
- Pending Submission PERMITTED NOT REQUIRED and never authoritative; external recording prohibited. Evidence EVID-002-008, EVID-002-009.

## Scope boundary

FR-BJ-001 covers create/maintain of authoritative Customer Master. FR-BJ-002 (CUS-SEARCH / CUS-GET disclosure) remains separate, not specified here. Lifecycle/duplicate product directions are documented in the overlays; executable contracts are not approved and full merge/deletion remains OPEN. No formal acceptance or scope extension is inferred.

## Source facts

- EVID-002-001 <- SRC-002-001:166
- EVID-002-002 <- SRC-002-002:89
- EVID-002-003 <- SRC-002-002:128
- EVID-002-004 <- SRC-002-003:299
- EVID-002-005 <- SRC-002-003:323
- EVID-002-006 <- SRC-002-003:324
- EVID-002-007 <- SRC-002-003:325
- EVID-002-008 <- SRC-002-003:450
- EVID-002-009 <- SRC-002-003:456
- EVID-002-010 <- SRC-002-003:1610
- EVID-002-011 <- SRC-002-003:1776
- EVID-002-012 <- SRC-002-003:1887
- EVID-002-013 <- SRC-002-004:13
- EVID-002-014 <- SRC-002-004:7
- EVID-002-015 <- SRC-002-005:17

## Relationship model (user-confirmed)

- Each Person may have multiple concurrent Relationships with Company and/or Branch; each independent role is a distinct Relationship (CM1-PD-029).
- Relationship fields: relationshipId, personId, targetType (COMPANY|BRANCH), targetId, roleCode, roleTitle, status, startDate, endDate, recordVersion, createdAt, updatedAt, endedReason, optional source/evidence reference (CM1-PD-030).
- Relationship lifecycle: ACTIVE / ENDED; ENDED not reopened; recurrence = separate Relationship (CM1-PD-031).
- Half-open interval `[startDate, endDate)` (CM1-PD-032).
- Overlap policy (LATEST/authoritative): same Person+TargetType+TargetId+RoleCode overlapping intervals allowed only via controlled exception; distinct roles/targets/Company-vs-Branch overlap freely (CM1-PD-033..041).

## Relationship Role Catalog (user-confirmed product direction; formal acceptance pending)

CM1-PD-058..065 add a hybrid System/Tenant catalog of organizational responsibilities, not IAM/RBAC roles. See [customer-role-catalog.md](customer-role-catalog.md) RC-001..008 for applicability COMPANY/BRANCH/BOTH, ACTIVE/INACTIVE lifecycle, immutable identity/no deletion, Relationship preservation, controlled scope changes and authority/history/overlap boundaries. Role reference schema and executable contracts remain OPEN under PDQ-002-08. The earlier source-derived entities remain unchanged; no sixth approved source entity or new service is inferred.

CM1-PD-066 confirms initial System Role Vocabulary v1.0: exact 12 entries in `customer-role-catalog.md` RC-009 and PDR JSON catalogEntries. This is not an exhaustive future universe, security permission or proof of legal representation; PRIMARY_CONTACT is not exclusive and Person may hold multiple independent roles.

CM1-PD-067 adds Tenant-specific assignment restriction, not System Role editing/deactivation. Appropriately authorized Tenant management can hide/unhide an otherwise eligible System Role locally; validated Tenant context and Customer Domain enforcement are required, not UI-only filtering. New assignments require global ACTIVE, applicability, current Tenant selectability, Relationship authority and existing validation/concurrency/overlap guards together. Existing Relationships/history, global identity/status/scope and other Tenants stay unchanged; re-enabling does not reactivate global INACTIVE or ENDED records. Concurrent hide/finalization must not accept invalid effective state. RC-010/011 define policy; representation, technical permissions/Audit and consistency contracts remain OPEN. Defaults are answered by CM1-PD-068; optional reason/mandatory Hide-Unhide Audit and own-Tenant manager authority by CM1-PD-073. Formal acceptance remains PENDING.

CM1-PD-068..072 extend product requirements through `customer-role-catalog.md` RC-012..016: ACTIVE default selectability for new Tenants/new System releases while preserving existing Tenant settings; canonical global System/owning-Tenant uniqueness and permanent reservation; conflict assessment blocking only the conflicting future System Role without automatic Role/Relationship mutations; canonical trim-uppercase then ASCII A-Z/digits/underscore validation with 3..64 length. Separate Tenants may share custom codes without mixing identities or data. No physical deletion, code reassignment, INACTIVE bypass, new IAM/legal authority or new overlap key is permitted. Code grammar beyond confirmed output/length and all technical enforcement/privacy/publication/recovery contracts remain OPEN.

CM1-PD-073..077 / RC-017..021 confirm Hide/Unhide optional reason and mandatory Audit; authorized System controlled-release versus own-custom display metadata edits with old/new values, stable IDs and semantics; new Role/new code for materially different semantics; current Relationship title versus preserved event-time history, including inactive/hidden Role visibility under existing authorization; three logical authority categories with no management/assignment implication; catalog Audit matrix, operation-specific reasons, logical information and durable no-success guard. Labels/translations/descriptions do not identify or grant permissions; Persian/English labels may be maintained without mandatory language/storage fields. No existing Relationship replacement/recreation/mutation or historical rewrite. Unauthorized catalog modification attempts require disclosure-safe Audit; ordinary catalog reads have no independent product-level Audit requirement, security monitoring unaffected. Exact IAM/operations/grants/actor mappings, temporal/snapshot/reference/API/localization and Audit schema/transactions/storage/retention/recovery/access remain OPEN. Initial vocabulary v1.0 is unchanged evidence, not overwritten by future permitted display releases.

## Identity verification model (user-confirmed)

- Verification independent of record lifecycle and commercial status; states NOT_VERIFIED / VERIFIED / REQUIRES_REVERIFICATION (CM1-PD-019/056).
- Two methods: trusted system verification + evidence-backed manual verification by independently authorized actor; Customer Domain remains authoritative state writer (CM1-PD-020).
- Manual verification SoD: normal workflow may allow creator to verify if independently authorized; sensitive workflows require a distinct verifier (CM1-PD-021).
- No universal expiry; evidence-based validity; fundamental invalidity → NOT_VERIFIED; evidence/identity change → REQUIRES_REVERIFICATION (CM1-PD-022..028).
