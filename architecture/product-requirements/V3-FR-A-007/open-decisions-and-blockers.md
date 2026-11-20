# Eight canonical requirement gaps

Owner Farzad for all product dispositions; implementation team drafts options only.

| Gap | Bounded direction | Residual OPEN / decision needed |
|---|---|---|
| Principal journeys and roles | T01/T04/T08 | Exact actor bindings, journeys and role permissions |
| Onboarding responsibility | T02 | Invitation validity, identity linkage/recovery, bootstrap authority and provisioning |
| Membership policy | T03 | Expiry/renewal, timing, retention, exact role rules/authority |
| Switching semantics | T04/T05 | Old context invalidation, concurrent tabs and in-flight commitments |
| Session transport/storage | T06 | OD-010 token/storage, timeouts, session limits |
| Revocation/freshness | T07 | Exact latency, exposure, revalidation points, propagation/recovery |
| Business Owner and actor catalog | T01/T10: Farzad | Actual actor binding and executable grants |
| Operation/profile acceptance and failure scenarios | T09 | Exact approved actor/operation/Tenant/profile cases and independent runtime evidence |

OD-009 IdP, OD-010 session/token, OD-011 workload, OD-012 custody, OD-014 RLS integration, OD-023 operational objectives remain OPEN as applicable. Context transport, Audit event/durability/recovery and security thresholds OPEN. No mechanism selected; affected implementation blocked.

