# Customer Master requirements — V3-FR-A-002

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

Individual vs organizational: Person vs Company are documented; Contact, Branch and Relationship are Customer Domain-owned facts. Detailed fields/identifiers/classification/lifecycle remain OPEN.

## Non-functional and security boundaries (existing, preserved)

- Validated/revalidated Tenant Context; client Tenant values are selectors only; invalid context fails closed. Evidence EVID-002-013.
- Owning Domain authorizes every operation/object; identity/Membership/eligibility never substitute. Evidence EVID-002-014, EVID-002-015.
- Customer durable CUS-CREATE/CUS-UPDATE require coordinated Audit obligations (DEC-012); executable DURABLE_DEFER NOT approved (DEC-013/014). Evidence EVID-002-010, EVID-002-011, EVID-002-012.
- Pending Submission PERMITTED NOT REQUIRED and never authoritative; external recording prohibited. Evidence EVID-002-008, EVID-002-009.

## Scope boundary

FR-BJ-001 covers create/maintain of authoritative Customer Master. FR-BJ-002 (CUS-SEARCH / CUS-GET disclosure) is a separate capability, not specified here. Status change, archive/deactivate, duplicates, merge/delete remain PROPOSED.

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

## Identity verification model (user-confirmed)

- Verification independent of record lifecycle and commercial status; states NOT_VERIFIED / VERIFIED / REQUIRES_REVERIFICATION (CM1-PD-019/056).
- Two methods: trusted system verification + evidence-backed manual verification by independently authorized actor; Customer Domain remains authoritative state writer (CM1-PD-020).
- Manual verification SoD: normal workflow may allow creator to verify if independently authorized; sensitive workflows require a distinct verifier (CM1-PD-021).
- No universal expiry; evidence-based validity; fundamental invalidity → NOT_VERIFIED; evidence/identity change → REQUIRES_REVERIFICATION (CM1-PD-022..028).
