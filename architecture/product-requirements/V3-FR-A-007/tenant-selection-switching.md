# Tenant Selection and Switching

Bounded product direction; not executable policy or grant.

Source: DEC-053/054; Option B

Zero active memberships: no operational access. One: auto-select. Multiple: authorized list or valid default. A stale default returns to selection. Switching validates identity/session and destination membership then creates new Context; source request remains bound to original context, no reinterpretation. Client state scoped; old Context invalidation/multiple-tab policy OPEN.

| ID | Direction |
|---|---|
| T04-D01 | Selection after authentication |
| T04-D02 | Only valid memberships listed |
| T04-D03 | Auto-select single eligible Tenant |
| T04-D04 | Manual choice among multiple without valid default |
| T04-D05 | Default Tenant support |
| T04-D06 | Revalidate default |
| T04-D07 | Remember last used Tenant |
| T04-D08 | Tenant switching |
| T04-D09 | Validate Session |
| T04-D10 | Validate destination Membership |
| T04-D11 | Create new Context |
| T04-D12 | Evaluate destination roles |
| T04-D13 | No source privilege transfer |
| T04-D14 | Separate client state/cache |
| T04-D15 | Prevent old requests executing in new Tenant |
| T04-D16 | No existence disclosure |
| T04-D17 | Fail closed invalid destination |
| T04-D18 | Audit under policy |
| T04-D19 | Sovereign local authority |
| T04-D20 | No token/session mechanism choice |

