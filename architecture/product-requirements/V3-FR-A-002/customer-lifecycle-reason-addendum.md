# Lifecycle reason catalog detail

Owner Farzad confirmed 2026-11-19. Supplement to CM1-PD-138, Core b09407c.

CM1-PD-141: initial system vocabulary (stable codes, multilingual titles):

| Code | Allowed transitions | Mandatory comment |
|---|---|---|
| CUSTOMER_REQUEST | DEACTIVATE, ARCHIVE | No |
| COOPERATION_ENDED | DEACTIVATE, ARCHIVE | No |
| BUSINESS_CLOSED | DEACTIVATE, ARCHIVE | No |
| TEMPORARY_SUSPENSION | DEACTIVATE | No |
| REGISTRATION_ERROR | ARCHIVE | No |
| COOPERATION_RESUMED | REACTIVATE | No |
| ARCHIVE_CORRECTION | RESTORE | No |
| OTHER | All four | Yes |

CM1-PD-142: Tenant custom reasons may be created and revised within that
tenant, hidden/unhidden and deactivated/reactivated. System definitions
are not editable by tenants; tenants may hide/unhide locally. Codes and
identities remain stable; no physical deletion. Inactive or hidden
reasons cannot be selected for new operations. A code collision with a
system reason or a reason within the tenant is rejected.

CM1-PD-143: reason mandatory except ordinary reactivation. Selected
reason must apply to the operation and required comment must be nonblank.
Historical title snapshot is retained independently of later revisions.
No actual history store or authorization is implied by a candidate.

All previously accepted transition guards remain unchanged. Durable
Audit, actor binding, version/concurrency, API and persistence remain open.
No runtime, IAM, real data or production permission is granted.
