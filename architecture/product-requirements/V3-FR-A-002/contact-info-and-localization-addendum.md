# Customer Master — contact information and localization addendum

- Task: V3-FR-A-002; downstream isolated candidate V3-FR-F-000 Increment 02.
- Authority: Farzad, explicit confirmation of the ContactInfo and multilingual design in conversation, 2026-11-19. No exact issuance time or signature asserted.
- Accepted baseline: v1.8.0, reviewed Core commit df6463d16390518bc5607e0a5c3d300128b75a9e; acceptance overlay and Core main at 156f4c4997ab34af8d2934bfbdc42b54ba6ec260.
- Status: OWNER-CONFIRMED PRODUCT DIRECTION; separate addendum, not replacement or new formal acceptance of the historical 106-decision baseline. Proposed implementation contracts remain OPEN.

## Decisions supplemental to the accepted baseline

| ID | Confirmed direction | Earlier trace |
| --- | --- | --- |
| CM1-PD-107 | Person, Company and Branch own independent ContactInfo collections of ContactPoint values. No direct phone/email/address properties on Customer. Shared domain model does not mean shared instance, cross-service database, or separate service. | PD-001, PD-004, PD-106 |
| CM1-PD-108 | System contact type vocabulary plus Tenant-customizable types; new supported types can be configured without a product code release. Definitions have stable identity, unique code, multilingual title, value type, validation rules, applicability, multiplicity, active/inactive status and display order. | PD-105, PD-106 |
| CM1-PD-109 | Contact values are typed, not unrestricted string bags: different structures for telephone, email, website and address; additional contact types must select supported value/validation capabilities. Tenant configuration must not execute arbitrary code. | PD-105, PD-106 |
| CM1-PD-110 | Preserve historical contact facts on type change/deactivation; no automatic removal. Existing Audit and Tenant boundaries remain applicable. | PD-96, PD-095, PD-106 |
| CM1-PD-111 | Multilingual platform direction: initially Persian and English, extensible languages, user-selectable interface, error/notification translation keys, catalog translations and multilingual customer facts where appropriate. Stable business codes independent of language. | PD-104, PD-105 |
| CM1-PD-112 | RTL/LTR presentation, calendar, number/date formatting and timezone are separate presentation settings; localization must not change canonical business dates or identities. | PD-104 |

The preceding Increment 02 proposal was also accepted: legal identity types are system-controlled; multiple identifiers per Person or Company, issuer/jurisdiction information, optional at ordinary creation; no verification inferred. Country catalog is a reference catalog. Existing PD-083, PD-105 and PD-106 apply. The design below refines PD-106 representation, not its optionality, uniqueness or Audit requirements.

## Initial system vocabulary — confirmed

| Code | fa | en |
| --- | --- | --- |
| PHONE | تلفن ثابت | Landline |
| MOBILE | تلفن همراه | Mobile |
| FAX | فکس | Fax |
| EMAIL | پست الکترونیکی | Email |
| WEBSITE | وب‌سایت | Website |
| ADDRESS | نشانی | Address |
| WHATSAPP | واتس‌اپ | WhatsApp |
| TELEGRAM | تلگرام | Telegram |
| LINKEDIN | لینکدین | LinkedIn |
| INSTAGRAM | اینستاگرام | Instagram |

ContactInfo is a Customer Domain component, not a shared service or identity registry. Each ContactPoint refers to a type by stable identity; the same model may support Branch later without treating Branch as independent Customer. Structured address retains country/province-or-state/city/postal code/address line. Multiple phones, emails and addresses are allowed; at most one designated primary in each of these categories, no mandatory contact at creation; phone/email not globally or per-Tenant unique across customers. The exact grouping of PHONE/MOBILE/FAX, replacement/removal and defaults must be decided before implementing primary selection. Type definitions are separate from contact values and from usage labels (e.g. work/personal). No automatic marketing consent, messaging delivery, or contact verification.

## Remaining decisions (not settled by this confirmation)

- Product: per-type applicability/defaults/multiplicity, exact primary groups and replacement policy, usage-label vocabulary, required/default languages and missing-translation fallback, names/addresses eligible for translation and historical title behavior. Contact type code namespace/normalization/reuse/deactivation/semantic changes; role catalog policies are not automatically imported.
- Technical: approved value shape catalog and declarative validation descriptors, country/telephone/email/URL/address validation and legal identifier rules; storage, versioning, identity/tenant context, Audit durability, concurrency, disclosure and IAM authority; i18n locale negotiation/persistence/fallback and localization contracts. No arbitrary executable validation from Tenant.
- GraphQL and event integration remain subject to architecture/contract alignment; no runtime protocol or schema approval follows from this addendum.
- All 19 existing OPEN questions remain OPEN. Related PDQ-002-01, PDQ-002-03, PDQ-002-04, PDQ-002-07 and PDQ-002-10; do not close or renumber legacy IDs.

## Proposed incremental unit specification

| Scenario | Expected result |
| --- | --- |
| CM1-CNT-01 | Person/Company independent ContactInfo; empty collection allowed. |
| CM1-CNT-02 | No direct phone or email properties; add multiple ContactPoint values using catalog definitions. |
| CM1-CNT-03 | A custom type resolves to supported typed values; no code release needed for configuration within supported capabilities. |
| CM1-CNT-04 | Different owners cannot implicitly share mutable ContactInfo; synthetic mismatched Tenant references fail closed. |
| CM1-CNT-05 | Incompatible value shape, inactive or inapplicable type rejected for new assignment; historical entries retained. |
| CM1-CNT-06 | User-facing catalog title can be Persian or English without changing type code or identity. |
| CM1-CNT-07 | Multiple contact channels and addresses allowed; primary rule enforced once exact grouping/replacement contracts are approved. |
| CM1-CNT-08 | Optional identifiers and contacts do not imply verification; no cross-customer phone/email uniqueness constraint. |
| CM1-CNT-09 | Domain error code remains stable independent of presentation language. |
| CM1-CNT-10 | Localized formatting does not mutate canonical date or identity. |

All scenarios PROPOSED / NOT TESTED; contract-dependent execution BLOCKED. This supplemental register does not change the historical counts/manifest; reconcile into the next version only with explicit review.

## Next bounded implementation proposal

Increment 02A: framework-independent ContactInfo and ContactPoint values, stable references, typed value representation, minimal unambiguous invariants and synthetic tests. Person/Company attach owned empty ContactInfo on creation; Branch attachment when Branch is implemented. No primary behavior with unsettled policy, no executable tenant catalog management, no production validation/normalization, no trust, API, persistence or messaging. Increment 02B: identity descriptors and remaining contact rules as their product/technical contracts are settled. Record any excluded behavior explicitly. All gates remain unchanged.
