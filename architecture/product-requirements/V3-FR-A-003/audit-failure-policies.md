# Audit and failure policies

D16 retains A-002 policy: ordinary authorized reads have no automatic product Audit obligation; sensitive evidence and Audit access independently authorized and traceable; sensitive document access audited. Unauthorized attempts subject to existing disclosure-denial/security obligations. No new blanket Audit for ordinary reads or invented failure policy. No raw credentials, query secrets, full identifiers/documents, or unnecessary personal data in operational logs. Exact audit-required classification, event schema, read failure policy and durability/recovery contract remain OPEN; sensitive access requiring Audit must not bypass its obligations when unavailable.

| Scenario | Required product boundary |
|---|---|
| Missing/invalid Tenant or actor context | Deny; no data or count |
| Alternate Tenant identifier or related resource | Deny without revealing existence |
| No authorized match | Empty authorized result; no inaccessible count |
| Invalid or forbidden filter/page/sort | No unsafe execution; enumeration-safe validation behavior; precise response contract OPEN |
| Protected document/evidence/history | Independent authority and required traceability; no unapproved content |
| Read/Audit dependency unavailable | No fail-open for protected access; no fabricated current data; precise response/retry policy OPEN |
| Concurrent update | Latest valid recorded state at approved consistency boundary; snapshot and pagination policy OPEN |

Shared SaaS/Shared Cell synthetic-only is initial scope D20. Dedicated Managed and Sovereign retain FR-BJ-002 first-release target; independent profile evidence deferred, no inherited Shared Cell PASS. Online authorized context required; client offline prohibited. No runtime or integration executed. Audit owner interim Farzad per A-002 until separately designated; source policy remains authoritative.
