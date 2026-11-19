# Customer Master — contact groups and validation profiles

Owner decision: Farzad, 2026-11-19. Supplemental decisions for the accepted
bounded requirements v1.8.0; this addendum does not rewrite the historical
acceptance package or its manifest. Core baseline 68b3248.

| Decision | Approved product behavior |
|---|---|
| CM1-PD-131 | Contact and identity candidates use reusable declarative validation profiles within the customer domain. Profile reference is separate from the raw value. |
| CM1-PD-132 | Rules are bounded and declarative. Initial executable subset: required, minimum/maximum length, allowed values. Format, pattern, range, algorithm, country-specific and cross-field rules remain blocked until contracts exist; arbitrary executable user code is excluded. |
| CM1-PD-133 | Tenant contact profiles are restricted to their own tenant; system types and official legal identifier profiles remain system-governed. Missing, mismatched or unsupported profiles must not yield a validation success. |
| CM1-PD-134 | Stable system contact group mapping below. Tenant custom contact types may choose an existing group; no automatic migration of historical grouping. |
| CM1-PD-135 | A contact owner may explicitly designate at most one active primary point per group. Selection is optional; a new selection replaces the previous selection. Clearing or deactivating a primary does not automatically choose a successor. |
| CM1-PD-136 | Preserve historical facts and audit selection, clearing, deactivation and configuration changes. Structural or profile validation is not evidence verification, identity verification or legal authenticity. |

| Contact group | Initial system types |
|---|---|
| TELEPHONE | PHONE, MOBILE |
| FAX | FAX |
| EMAIL | EMAIL |
| ADDRESS | ADDRESS |
| WEBSITE | WEBSITE |
| MESSENGER | TELEGRAM, WHATSAPP |
| SOCIAL | INSTAGRAM, LINKEDIN |

Acceptance examples (proposed, not runtime tested): a mobile primary can
be replaced by a phone primary without changing email primary; deactivation
retains the inactive point and clears only its own selection; missing
required values fail; unknown rules block; foreign-tenant and tenant-owned
legal profiles block. Existing selections are not rewritten by catalog hide.

Open technical contracts: trusted profile registry and version references,
Unicode and normalization, legal format and issuer/expiry algorithms,
safe pattern and cross-field evaluation, historical multiplicity and
group migration, concurrent selection, durable Audit, authorization and
GraphQL/API mapping. No new authorization, runtime, persistence, event
transport, real data or offline support is granted. All existing gates
remain unchanged. Isolated synthetic domain work only under V3-FR-F-000.
