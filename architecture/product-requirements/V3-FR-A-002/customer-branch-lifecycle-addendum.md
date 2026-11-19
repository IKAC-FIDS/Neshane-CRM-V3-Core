# Branch lifecycle and shared reason catalog

Owner Farzad confirmed 2026-11-19; Core basis 62f8c0e.
Supplement CM1-PD-153 and existing lifecycle decisions.

CM1-PD-157: effective state is derived, not an independently stored state.
ACTIVE requires both stored Branch and Company ACTIVE. State eligibility
does not replace action authorization. Inactive parent does not rewrite
Branch state; no new operational activity or relationship if effectively
inactive. Existing activity continuation follows owning-service policy.
Archived parent blocks routine changes; no independent Branch archive
or physical deletion.

CM1-PD-158: branch transition assessment is separate from customer
lifecycle. ACTIVE to INACTIVE requires a reason; INACTIVE to ACTIVE
requires active parent and applicable validation/authorization. Ordinary
reactivation reason optional, selected mandatory comment enforced.
No automatic parent, contact, type or relationship change.

CM1-PD-159: shared reason catalog adds CUSTOMER, BRANCH, BOTH scope.
CUSTOMER_REQUEST, COOPERATION_ENDED, COOPERATION_RESUMED and OTHER
are BOTH; remaining eight-entry original vocabulary otherwise CUSTOMER.
Add BRANCH_CLOSED, BRANCH_RELOCATION (deactivation), BRANCH_REOPENED
(reactivation), BRANCH only. Branch supports only DEACTIVATE/REACTIVATE
regardless of shared metadata. Existing tenant reason constructors retain
CUSTOMER scope; new tenant definitions may specify scope. Existing code,
tenant hiding, status and history rules remain.

04D isolated assessments only. Actual mutation, trusted state, Audit,
authorization, transfer, persistence and runtime remain out of scope.
