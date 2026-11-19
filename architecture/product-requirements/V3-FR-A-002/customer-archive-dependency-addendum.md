# Archive dependency assessment

Owner Farzad confirmed 2026-11-19. Core basis 7f4382b; supplements CM1-PD-140.

CM1-PD-147: system-maintained extensible dependency catalog with stable
identity/code, multilingual title/description, owning service, customer
type applicability, status and display order. Tenant cannot disable
mandatory controls. Initial proposed ownership and scope:

| Code | Owner label | Scope |
|---|---|---|
| OPEN_OPPORTUNITIES | Sales | Both |
| ACTIVE_CONTRACTS | Contract | Both |
| OPEN_ORDERS | Order | Both |
| OPEN_TICKETS | Support | Both |
| ACTIVE_PROJECTS | Project | Both |
| ONGOING_TENDERS | Tender | Both |
| DELIVERY_COMMITMENTS | Delivery | Both |
| OPEN_ACTIVITIES | Activity | Both |
| ACTIVE_BRANCHES | Customer | Company |
| ACTIVE_RELATIONSHIPS | Customer | Both |

Owner labels are illustrative, not service topology decisions.

CM1-PD-148: CLEARED and policy-derived NOT_APPLICABLE may satisfy an
individual dependency. BLOCKED, UNKNOWN, UNAVAILABLE and missing evidence
block. A service response alone cannot declare a required dependency
not applicable. Contradictory scope or inactive applicable definition
must not silently remove a required check.

CM1-PD-149: evidence bound to request, customer, tenant, dependency and
owning service; reference and UTC observation time included. No direct
database access or automatic closure of dependencies. Events alone do
not prove clearance. Authenticity, freshness, concurrent change, registry
authority, deployed capability applicability and Audit contracts remain open.

03D is a synthetic structural assessment. Even ALL_CLEARED_CANDIDATE
does not permit execution or change the archive lifecycle guard.
No actual integrations, runtime, API, real data or gate change.
