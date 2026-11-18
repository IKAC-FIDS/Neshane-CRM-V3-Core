# Actor–resource policy matrix — V3-FR-A-002

**No permission, role, RBAC policy or IAM mechanism is defined or approved.** Candidate relationships only; Customer Domain retains final authorization.

## Actor references (accepted V3-FR-A-001)

- `ACT-A001-001` — Internal authenticated Principal (APPROVED class; no persona/role).
- `ACT-A001-002` — Customer maintenance participant (ANALYTICAL view, not approved role).
- `ACT-A001-022` — Product Decision Owner / TAO (governance, not runtime role).
- `ACT-A001-023` — Domain/Service Owner contributor (person UNASSIGNED).

## Candidate relationships (PROPOSED — no permission granted)

| Actor | Resource | Operation concept | Candidate? | Authorization note |
| --- | --- | --- | --- | --- |
| ACT-A001-001 | Customer Master | CUS-CREATE, CUS-UPDATE, CUS-VALIDATE, CUS-GET-FOR-UPDATE | PROPOSED | Customer Domain authorizes each operation; role/action matrix OPEN |
| ACT-A001-002 | Customer Master | maintenance participation | PROPOSED | analytical view only |

## Boundaries preserved

- Tenant isolation: validated Context; cross-tenant fails closed; selector untrusted.
- Identity vs authorization: identity/Membership/eligibility never substitute.
- No new roles/RBAC/permissions/IAM mechanism approved.

## Verification authorization (user-confirmed)

- Verification requires its own authority, separate from CUS-CREATE/CUS-UPDATE (CM1-PD-021/026).
- Normal workflow: creator may manually verify the same record only if independently authorized to verify.
- Sensitive workflows subject to SoD: verifier must differ from creator. Sensitive-process catalog and permission grants remain OPEN.
- A VERIFIED state confers no access or operational authorization (CM1-PD-056).

## Role Catalog authorization boundaries (v1.3.0 product direction)

Organizational Role Definitions are not IAM/RBAC roles or grants (CM1-PD-058). System catalog authority manages System Roles; Tenant users cannot modify them. Authorized owning-Tenant actors manage Tenant Roles; other-Tenant access/references require a separate governing contract, none granted here (CM1-PD-064). CUS-CREATE alone is insufficient. Incompatible applicability changes require appropriate management authority (CM1-PD-063), distinct from the ordinary Relationship overlap exception's no-supervisor rule. Exact operation/permission bindings and identity of catalog managers remain OPEN; no runtime actor is appointed. See `customer-role-catalog.md` RC-006/007.

## Tenant selectability responsibilities (v1.4.0 product direction)

- System catalog authority still owns global Role Definitions. Tenant management of System Role selectability (CM1-PD-067) is only a local assignment restriction, never authority to change the global definition/status/scope/identity.
- Appropriately authorized Tenant actor: manage own Tenant's hide/unhide setting with validated Tenant context; CUS-CREATE alone does not grant this authority. Exact management permissions and actor mapping remain OPEN; no runtime role or IAM grant is approved.
- Relationship actor: separately authorized for assignment; Customer Domain checks effective state and all existing guards, not just a UI list. A selectable Role does not itself grant Relationship authority.
- Historical viewer: retains otherwise authorized Role/Relationship history regardless of hide/unhide; this confers no new disclosure grant and must not expose other Tenants' settings/Relationships.
- Initial vocabulary titles (CM1-PD-066), including CEO/BOARD_MEMBER/PRIMARY_CONTACT, provide no IAM/RBAC or verified legal authority. Mandatory reason for ordinary hide/unhide remains OPEN, separate from incompatible scope management.
