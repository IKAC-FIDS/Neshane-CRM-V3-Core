# Authorization Boundaries

Bounded product direction; not executable policy or grant.

Source: ADR-V3-005; DEC-053/054/018; Option B

Identity validates Principal/session; Tenant validates membership and manages assignments; Entitlement evaluates eligibility; resource/action/field decision belongs to owning Domain. RBAC/ABAC/resource controls are conceptual support only. Platform/Identity/Tenant/Membership/Security/Domain administrators and Audit reviewers have independently bounded responsibilities, no implied business access.

| ID | Direction |
|---|---|
| T08-D01 | Authentication independent |
| T08-D02 | Membership independent |
| T08-D03 | Entitlement independent |
| T08-D04 | Owning Domain final authority |
| T08-D05 | Shared Policy Governance |
| T08-D06 | Deny by default |
| T08-D07 | Least privilege |
| T08-D08 | Policy separation of duties |
| T08-D09 | Conceptual RBAC |
| T08-D10 | Conceptual ABAC |
| T08-D11 | Resource-level control |
| T08-D12 | Field-level control |
| T08-D13 | Independent operation authorization |
| T08-D14 | No unlimited administrator access |
| T08-D15 | Prevent escalation |
| T08-D16 | Client permissions untrusted |
| T08-D17 | Gateway not final authority |
| T08-D18 | Independent privileged operation controls |
| T08-D19 | Security Audit under policy |
| T08-D20 | Sovereign local authority |
| T08-D21 | No authorization engine chosen |
| T08-D22 | No executable IAM grants |

