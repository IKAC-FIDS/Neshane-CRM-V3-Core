# First end-to-end Customer Management milestone — PROPOSED

## Claim boundary

Candidate **CM-1: an authorized internal Principal selects a valid Tenant, creates and maintains Customer Master, finds/browses and reviews authorized Customer data, with safe Audit and observability across the actual approved stack**. Detailed fields, rules, duplicate/concurrency behavior and acceptance examples remain OPEN. Complete means all selected operations and security/failure evidence for this bounded synthetic milestone, not every Customer lifecycle feature or all fifteen First Release capabilities. No mandatory merge/delete/Portal/Pending Submission feature is invented. No production acceptance or implicit profile-wide isolation acceptance.

## Minimum required inputs, implementation and verification

| Layer | Minimum for CM-1 | Tasks / mandatory predicate |
| --- | --- | --- |
| Product | Exact internal actors; Customer fields/validation and maintenance; duplicate/concurrency handling; find/browse filters/pagination/disclosed fields; operation examples; deny/failure/recovery; selected profile/environment | A-001/002/003; product disposition before implementing selected rule; unresolved non-selected extensions remain explicitly outside milestone, not removed from approved product scope |
| Access | Validated internal Principal/session, active Membership, Tenant selection/switching and Context revalidation; resource-owning authorization | A-007, C-001/C-003/004/005; explicit AUTH/IAM permission and approved exact trust/session/revocation/custody policies; no fake identity |
| Tenant controls | Ordinary non-owner/non-bypass role, transaction-local context, read/write RLS where applicable, actual accepted pool, direct-service authorization, destination/routing/fence controls as applicable to chosen path | D-001/D-004/005/006/D-002/D-003; explicit favorable G-RUNTIME applicability/acceptance disposition before reliance, NOT completion of submission task |
| Backend | Customer-owned create/update and find/review, owned schema/migrations and versioned public/reference contracts; no shared ORM/business implementation | F-000 reused by F-BJ-001; F-BJ-002; K-001; approved OD-013/014 and public/search choice at original milestone; same Customer owning boundary, not separate read/write services by default |
| Frontend | Approved framework/design system, Persian/RTL/responsive/accessibility; selected Customer create/edit/find/list/detail, safe loading/empty/denied/error/conflict, session/Tenant switch UX | G-001/G-003/G-004; FE-BE explicit permission; approved session/client boundary; K-003 only if selected public Gateway/BFF needs it |
| Audit | Coordinated durable obligation for successful CUS-CREATE/CUS-UPDATE and safe explicit Customer disclosure-denial evidence; authentic authorized ingestion and recovery | A-013 and selected A-017; E-000/E-003/K-002; approved operation-specific failure/ingestion/integrity/retention policy; no automatic DURABLE_DEFER, no Audit failure permitting denied operation |
| Observability | Safe source health/readiness/log/metric/trace signals, approved access/export and redaction, attributable errors and evidence visibility | Selected A-015/E-001; E-002 if selected milestone includes privileged aggregation; no global operational dashboard or all numeric production SLOs as an unrelated prerequisite |
| Integration | Real approved providers and public/client path, authorized synthetic data, positive create/update/search/detail and negative wrong-tenant/invalid context/role/session/switching, failure/retry/Audit recovery and selected concurrency tests | H-001/I-003 plus ADR-V3-015 provider/consumer/risk-based real-integration controls and separately authorized CI where required; mocks/echo not E2E proof |

## Conditional inclusions — explicit decision, never silent omission

- Entitlement/Quota: A-017 must state whether selected Customer operations are eligibility/quota controlled. If required, E-PF-002/003 and their actual-path evidence join CM-1 before completion; their optional per-operation integration does not remove platform capabilities from First Release.
- Attachments, notifications and reports: not automatic dependencies of Customer CRUD/search. Include only if approved selected operation requires them; then exact platform policy/implementation/authorization is mandatory.
- Customer Audit failure: DEC-013/014 qualitative direction does not approve executable deferral. Specify approved alternative outcome/failure policy without guessing a synchronous dependency or asserting Outbox alone permits success.
- Chosen development reference host/profile must satisfy applicable GS-01/04, trust and runtime prerequisites. One synthetic development slice does not claim three-profile production readiness. Offline continuation stays prohibited.

## Exit and stop conditions

Exit requires explicit approval of selected detailed requirements, exact mechanism decisions, FE-BE and AUTH/IAM execution scopes, satisfactory applicable Runtime Gate disposition, executed artifact-bound contract/security/failure evidence and unresolved findings treatment consistent with unchanged controls. No criterion or Task is considered accepted merely by this roadmap. Stop affected path on missing provenance/authority, tenant mismatch, unknown trust, failed durability/visibility/integrity or unapproved rules; do not invent fallback. No Gate transition or risk waiver is issued here.
