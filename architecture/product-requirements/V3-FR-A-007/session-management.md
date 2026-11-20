# Session Management

Bounded product direction; not executable policy or grant.

Source: DEC-053; Option B; OD-010

Concepts sessionId, principalId, status, authenticatedAt, createdAt, lastActivityAt, expiresAt, authenticationContext, revokedAt, revocationReason. ACTIVE→EXPIRED/REVOKED/TERMINATED; no revival. Renewal only after validation and within approved limits. Session independent of selected Tenant; revoking session invalidates all dependent contexts; membership revocation affects only applicable tenant. Numeric timeouts/count limits, session transport/storage and multi-tab handling OPEN.

| ID | Direction |
|---|---|
| T06-D01 | Identity owns Session |
| T06-D02 | Unique independent Session ID |
| T06-D03 | Bind Principal |
| T06-D04 | Independent lifecycle |
| T06-D05 | Multiple concurrent sessions |
| T06-D06 | Absolute timeout |
| T06-D07 | Idle timeout |
| T06-D08 | Controlled renewal |
| T06-D09 | Logout |
| T06-D10 | Logout all |
| T06-D11 | Authorized revocation |
| T06-D12 | Authorized session inventory |
| T06-D13 | Prevent hijacking/replay |
| T06-D14 | Policy reauthentication |
| T06-D15 | Conditional step-up |
| T06-D16 | Independent Membership |
| T06-D17 | Independent business authorization |
| T06-D18 | Invalidate dependent Context |
| T06-D19 | Protect sensitive data |
| T06-D20 | Security Audit under policy |
| T06-D21 | Sovereign local session |
| T06-D22 | OD-010 storage/token OPEN |

