# Contact Type Catalog — confirmed governance

Authority: Farzad, explicit conversation confirmation, 2026-11-19.
Core basis bf6a1df9bf9ed03ba9b2e657342439be4d43dad9; extends
contact-info-and-localization-addendum (CM1-PD-107–112).
Owner-confirmed product direction only. Historical acceptance and manifest unchanged.

| ID | Decision |
| --- | --- |
| CM1-PD-113 | System definitions are global; Tenant can create/manage own custom types and hide/unhide system types for new assignments in its own Tenant. No automatic effect on existing contact facts. |
| CM1-PD-114 | Stable ID, normalized code and valueType immutable; ACTIVE/INACTIVE; no physical deletion. Titles/translations/descriptions and order may change. |
| CM1-PD-115 | Scope and multiplicity changes require warning; preserve existing values. New assignments use new scope/multiplicity; revised validation applies prospectively to new or edited values. |
| CM1-PD-116 | System codes reserved globally; custom code unique within Tenant, reusable across independent Tenants; inactive codes permanently reserved. Trim and uppercase then match A-Z/0-9/_ length 3–64. |
| CM1-PD-117 | Initial mappings: PHONE/MOBILE/FAX/WHATSAPP to PHONE; EMAIL to EMAIL; WEBSITE/LINKEDIN to URL; ADDRESS to ADDRESS; TELEGRAM/INSTAGRAM to TEXT. Supported shape selection allows custom types without new release. |
| CM1-PD-118 | Catalog titles/descriptions use extensible locale-keyed LocalizedText, not fixed language columns. All management changes require Audit. |

No runtime IAM grant, Audit success, schema, validation interpreter or API contract is approved.
Exact per-system default applicability/multiplicity, validation profiles, locale/fallback,
Unicode edge cases, durable reservation and coordinated future release/conflict handling,
authorization, warning workflow, historical title behavior and concurrency remain open.
The 19 existing questions remain open; no historical criterion promoted to software PASS.
Increment 02B is limited to pure candidate snapshots and synthetic unit specifications.
