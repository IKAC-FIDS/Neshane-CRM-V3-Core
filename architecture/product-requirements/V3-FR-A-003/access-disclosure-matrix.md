# Logical access and disclosure matrix

D11–D13, D15–D16; constrained by A-002 CM1-PD-096, 103 and PD-092. This describes product responsibilities, not executable IAM roles or grants. Tenant, resource, operation and field authority are verified independently; unknown or invalid context denies. No scope inference from title or possession of ID.

| Responsibility | General search / review | Branch / Relationship | Official identity | Documents / evidence | History / Audit |
|---|---|---|---|---|---|
| Customer Operator | General read | Relevant independent resource access | Masked absent independent disclosure authority; search separately authorized | Independent authority | Independent business-history / Audit authority |
| Customer Reviewer | General read | Relevant independent resource access | Same restricted rule | Independent authority | Independent business-history / Audit authority |
| Customer Verifier | General read; verification status | Relevant independent resource access | Same restricted rule | Independent evidence authority | Independent business-history / Audit authority |
| Customer Catalog Manager | Selectable roles / own catalog only; no general grant implied | No implied access | No implied access | No implied access | No implied access |
| Audit Reviewer | Authorized Audit review only; no general grant implied | No implied access | No implied access | No implied access | Separately authorized Audit review |

General read includes contact and verification status within existing resource/field authority. Identity masking does not grant filtering or exact-match probing. Suppress unauthorized fields/resources from results, totals, pagination, sorting, facets, logs, errors and related summaries. Cross-Tenant and inaccessible/not-found responses must not provide differentiating existence signals. Exact mask, query grant IDs/actor bindings, enumeration-safe error contract and permitted field examples remain OPEN. Unauthorized positive access cannot be inferred from this matrix. No external direct Customer access or IAM changes.
