# Branch type governance

Owner Farzad confirmed 2026-11-19; Core basis 0579b5d.
Supplement to CM1-PD-152.

CM1-PD-154: initial nine system types HEAD_OFFICE, BRANCH, REGIONAL_OFFICE,
SALES_OFFICE, SUPPORT_CENTER, WAREHOUSE, FACTORY, REPRESENTATIVE_OFFICE,
OTHER. Each has stable ID and code, multilingual title/description,
status and display order.

CM1-PD-155: tenant custom type creation and metadata/status revision
within own tenant; system definitions cannot be edited by tenants.
Tenant-local hide/unhide, protected stable IDs and codes, no physical
deletion. System codes reserved; custom codes unique within own tenant.
Inactive or hidden types cannot be newly selected.

CM1-PD-156: Branch type reference optional; new selection must be
selectable in the same tenant or system scope. Existing branch references
remain unchanged after catalog revision, hiding or deactivation.
Historical title storage and Audit are downstream contracts.

No IAM grant, persistence, API, real data or gate change.
