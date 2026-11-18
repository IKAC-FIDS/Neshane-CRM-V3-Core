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
