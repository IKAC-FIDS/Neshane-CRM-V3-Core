# Customer IdentityInfo — confirmed product direction

Owner: Farzad, conversation confirmation 2026-11-19. Core basis
4f1de2928e61423797c4ac16c4cd8e5705ed9712; extends accepted v1.8.0 and
supplements. Historical manifest and acceptance unchanged.

| Decision | Confirmed direction |
| --- | --- |
| CM1-PD-125 | Independent optional IdentityInfo owned by Person or Company; multiple identity identifiers; internal customer ID independent of official IDs. |
| CM1-PD-126 | Identifier facts: stable internal ID, type reference, string value preserving leading zeros, issuing country/authority, optional issue/expiry calendar dates and ACTIVE/INACTIVE status. Preserve history; verification/evidence handled separately. |
| CM1-PD-127 | Legal identifier types are system-controlled, multilingual and extensible; Tenant may hide/unhide types for new use, not define or change legal identity/validation/uniqueness rules. |
| CM1-PD-128 | Initial vocabulary: IR_NATIONAL_ID, PASSPORT, FOREIGN_NATIONAL_ID for PERSON; IR_LEGAL_ENTITY_ID and COMPANY_REGISTRATION_NO for COMPANY; TAX_ID for BOTH. The last extends the Company economic identifier direction in PD-083, without claiming any legal eligibility. |
| CM1-PD-129 | Country/issuer applicability, optional expiry, validation and verification profile metadata belong to type definitions. Actual rules require authoritative contracts. |
| CM1-PD-130 | Registration does not verify identity. Verified-valid uniqueness remains scoped to applicable Tenant+legal namespace; authoritative collisions block ordinary override. Sensitive full disclosure requires independent authority. |

Trace: CM1-PD-001/007/019/083/085/095/105 and CM1-PD-107–124.
All 19 OPEN questions retained. No authoritative identifier grammar, namespace,
issuer eligibility, country dataset, expiry validity, retention, history storage,
Audit, IAM, matching or external verification contract approved here.
Increment 02D is an isolated synthetic candidate only; no runtime or legal validity.
