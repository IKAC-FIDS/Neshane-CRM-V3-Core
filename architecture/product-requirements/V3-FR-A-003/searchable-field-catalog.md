# Searchable field catalog

Concepts refer to A-002 field dictionary and accepted product rules; not physical schema names. Search permission is independent of detail disclosure. A field that cannot be searched by the actor must not affect matches, counts, facets, ordering, or errors (D11–D13).

| Field concept | Applicability | Match/filter | Disclosure constraint |
|---|---|---|---|
| Individual name | Person | Exact, Prefix, Contains | Authorized ordinary fields only |
| Company name | Company | Exact, Prefix, Contains | Authorized ordinary fields only |
| Customer identifier | Both | Searchable; precise matching OPEN | Authorized own-Tenant records only |
| Official identifier | Applicable Person/Company identity concepts | Exact | Independent identity search authority; masked absent identity-field disclosure authority |
| Phone/contact number | Both, supplied authorized contact | Searchable; precise matching OPEN | Apply contact field authority, no hidden matches |
| Email | Both, supplied authorized contact | Searchable; precise matching OPEN | Apply contact field authority, no hidden matches |
| Customer type | Both | Person / Company filter | Authorized records only |
| Lifecycle | Both | Active / Inactive / Archived filter | Scope and lifecycle authorization preserved |
| Creation / last-change dates | Both | Sortable | No hidden ordering; exact optional date filter OPEN |

Advanced filtering only on explicitly authorized fields from the accepted catalog. Additional candidate fields, namespace/issuer ambiguity, identifier and contact normalization, alias/multi-name behavior and missing-value rules remain OPEN. No implicit full-text search over documents, evidence, Audit, notes or external service information. No source field invented.
