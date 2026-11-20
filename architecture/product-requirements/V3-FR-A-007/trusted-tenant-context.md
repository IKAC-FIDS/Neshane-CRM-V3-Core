# Trusted Tenant Context

Bounded product direction; not executable policy or grant.

Source: Option B; ADR-V3-003/004/005; DEC-053/054

Conceptual fields principalId/type, tenantId, membershipId, sessionId, membershipVersion, contextId, issuedAt, expiresAt; not token claims. Identity and Tenant owners validate independent facts; Cell Management placement; Entitlement eligibility; owning domain final resource/action authorization. Missing/conflicting/expired/tampered Context or invalid destination denied unless approved revalidation establishes validity. No prescribed network call sequence. Shared SaaS application + RLS; dedicated isolation and sovereign local validation.

| ID | Direction |
|---|---|
| T05-D01 | Context from authoritative sources |
| T05-D02 | Bind valid Principal |
| T05-D03 | Bind valid Membership |
| T05-D04 | Bind valid Session |
| T05-D05 | Single Tenant per Context |
| T05-D06 | Client tenant selector untrusted |
| T05-D07 | Revalidate at trust boundaries |
| T05-D08 | Prevent tampering |
| T05-D09 | Immutable request context |
| T05-D10 | No unauthorized transfer |
| T05-D11 | Validate destination and Cell placement |
| T05-D12 | Validate freshness |
| T05-D13 | Fail closed invalid Context |
| T05-D14 | Independent business authorization |
| T05-D15 | Application isolation |
| T05-D16 | Shared SaaS PostgreSQL RLS |
| T05-D17 | Sovereign local authority |
| T05-D18 | No sensitive context logging |
| T05-D19 | No offline |
| T05-D20 | No transport/token selection |

