# Customer search and review requirements

Logical operations (labels, not API or permission IDs). Scope: D01–D03, D07, D11–D16, D19–D20 and approved Customer 360 direction.

| Operation | Inputs / preconditions | Output / expected outcome |
|---|---|---|
| Browse directory | Authorized Tenant and general-read authority; optional permitted filters/sort/page | Authorized Customer summary records and authorized count if exposed |
| Search | Authorized context, supported field and matching mode, query | Authorized matching records only; no external existence signal |
| Retrieve profile | Authorized context and Customer identifier | Authorized fields of current Customer record; no mutation |
| Browse Branches | Authorized Customer and Branch resource access | Authorized Branch summaries; no inaccessible count |
| Browse Contacts | Authorized Customer general-read and field policy | Authorized contact facts |
| Review Relationships / related persons | Authorized Customer, Relationship and relevant related-resource authority | Disclosed relationship facts only |
| Review verification | Authorized general read | Current verification status; evidence separately protected |
| Review documents | Independent document view authority | Authorized metadata/content subject to approved secure file contracts |
| Review history | Independent history authority | Immutable authorized historical facts; no Audit-log grant |

Directory includes Person and Company and active/inactive/archived states; no automatic inclusion of any archived resource a user cannot access. Exact default lifecycle filter remains OPEN. Empty result, denied/unknown, unavailable and validation-error states must not be confused. Query UX must support permitted filtering and paginated navigation; detailed visual behavior, empty-query semantics, validation thresholds and combinations remain OPEN. No export, AI search, external customer access, offline, write operations, cross-Tenant aggregation, or downstream service integration. Customer-owned information only.
