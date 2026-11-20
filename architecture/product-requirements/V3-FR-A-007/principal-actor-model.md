# Principal and Actor Model

Bounded product direction; not executable policy or grant.

Source: DEC-053/054; FR-PF-001 Option B

Internal Human included; Workload separate scope; External deferred; Anonymous no tenant access. Logical actors: Internal User, Tenant Owner, Tenant Administrator, Membership Administrator, Identity Administrator, Security Administrator, Audit Reviewer, Platform Administrator, Workload Principal (separate). Identity owns identity, credentials, session; Tenant owns association and roles; Entitlement owns eligibility; Domains authorize resources; Audit owns evidence.

| ID | Direction |
|---|---|
| T01-D01 | Stable unique Principal ID |
| T01-D02 | Separate Principal from Customer |
| T01-D03 | Separate Principal from Membership |
| T01-D04 | Multiple Tenant memberships |
| T01-D05 | Tenant-specific roles |
| T01-D06 | No automatic Membership from authentication |
| T01-D07 | Identity Trust owns Principal |
| T01-D08 | Tenant Management owns Membership |
| T01-D09 | Separate human and workload |
| T01-D10 | External Principal excluded now |
| T01-D11 | Anonymous cannot access Tenant |
| T01-D12 | No automatic Platform admin data access |
| T01-D13 | Independent business authorization |
| T01-D14 | Logical actor responsibilities only |
| T01-D15 | Local Sovereign authority |

