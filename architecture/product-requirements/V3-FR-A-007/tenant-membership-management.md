# Tenant Membership Management

Bounded product direction; not executable policy or grant.

Source: DEC-054; Option B

Conceptual fields membershipId, principalId, tenantId, status, roleAssignments, validFrom, validUntil, createdAt, updatedAt, version. PENDING→ACTIVE/REVOKED; ACTIVE→SUSPENDED/EXPIRED/REVOKED; SUSPENDED→ACTIVE/EXPIRED/REVOKED; only ACTIVE and valid time, active Tenant, valid Principal and Context permit further authorization. Renewal of expired membership and precise timing/retention OPEN. No automatic reactivation of revoked membership.

| ID | Direction |
|---|---|
| T03-D01 | Tenant owns Membership |
| T03-D02 | Independent stable membership ID |
| T03-D03 | At most one nonterminal membership per Principal/Tenant |
| T03-D04 | Multiple Tenant memberships |
| T03-D05 | Independent lifecycle |
| T03-D06 | Permanent or time-limited membership |
| T03-D07 | Validate validity interval |
| T03-D08 | No operational access with inactive membership |
| T03-D09 | Suspend and resume |
| T03-D10 | Revoke |
| T03-D11 | No automatic reactivation after revoke |
| T03-D12 | Multiple roles per membership |
| T03-D13 | Tenant-specific roles |
| T03-D14 | Prevent privilege escalation |
| T03-D15 | Preserve membership/role history |
| T03-D16 | Audit under policy |
| T03-D17 | Concurrency control |
| T03-D18 | No ordinary physical deletion |
| T03-D19 | Independent of Entitlement and business authorization |
| T03-D20 | Sovereign local membership |
| T03-D21 | No executable grant or mechanism |

