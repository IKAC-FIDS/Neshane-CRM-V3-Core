# CRM V3 — platform localization direction

Owner: Farzad, explicit confirmation 2026-11-19. Baseline Core
d59a163d8005a89f7ec130e467bbf44f17a222d5. This records product and architecture
direction to be reconciled with existing platform ADRs; no runtime contract or
new formal architecture gate acceptance is asserted. Existing historical
acceptance and manifest remain unchanged.

| Decision | Confirmed direction |
| --- | --- |
| CM1-PD-119 | Platform-wide localization conventions, service-owned translations and messages, no independent translation microservice initially. |
| CM1-PD-120 | Initial Persian (fa) and English (en), extensible languages; Tenant-selectable enabled languages and default, optional user preference. Initial platform default fa, configurable. RTL/LTR independently supported. |
| CM1-PD-121 | Translation fallback: selected user language, Tenant default, platform default, original value or stable display code. No mutation of business facts. |
| CM1-PD-122 | Stable machine error code and translation key independent of display language. Backend behavior and authorization do not depend on language. |
| CM1-PD-123 | Appropriate facts may have multiple language representations (names, company/trade/branch names, descriptions, catalog titles); canonical identity, legal IDs, phone/email and stable codes remain language-independent. |
| CM1-PD-124 | Calendar, timezone, date/number formats and display direction are independent of language and canonical dates; Tenant defaults and user presentation preferences. |

Trace: CM1-PD-104/105/111/112/118. Existing 19 OPEN questions retained.
Exact locale tag handling, language registry, supported-language changes,
preference migration, fallback exposure, translation bundle/version contracts,
fact provenance/validation, rendering and error mapping, API negotiation,
and governance alignment remain open. No runtime GraphQL, event, API, schema,
authorization grant or localization service approved here.

Increment 02C candidate: exact-key immutable translation resolution, logical
locale preferences and stable code/key representation within Customer Domain;
no cross-service implementation dependency or shared business framework.
Future platform reuse is subject to approved contract and module governance.
Calendar conversion, time/number formatting, actual customer fact translations,
storage, UI and adapter wiring are separate work.
