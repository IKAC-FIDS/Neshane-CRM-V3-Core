# Branch implementation direction

Owner Farzad confirmed 2026-11-19. Core basis 8f37266. Supplement to
CM1-PD-001/002/042..047/105; accepted historical baseline unchanged.

CM1-PD-150: Branch remains in Customer Service, subordinate to exactly
one Company in the same Tenant, not an independent Customer or service.
Stable branchId and companyId cannot be changed. Branch may be attributed
activities and Person Relationships, subject to owning operation policy.

CM1-PD-151: required branch name, optional English name, branch code,
type reference, description and independently owned ContactInfo.
Code, when supplied, is unique within Company; exact code normalization,
length, durable uniqueness and concurrent enforcement remain open.
Name uses existing bounded validation. No automatic contact inheritance.

CM1-PD-152: dynamic multilingual system/tenant branch type catalog.
Initial vocabulary HEAD_OFFICE, BRANCH, REGIONAL_OFFICE, SALES_OFFICE,
SUPPORT_CENTER, WAREHOUSE, FACTORY, REPRESENTATIVE_OFFICE, OTHER.
Tenant custom definitions supported; exact governance follows 04B.

CM1-PD-153: Branch stored ACTIVE/INACTIVE independent of Company status.
Effective availability requires active Company and Branch plus action
policy. No automatic stored state changes or reparenting. Transfer
remains a deferred coordinated new-branch/deactivate-old workflow;
history and existing relationships do not move automatically.

04A base; 04B type catalog; 04C contact; 04D lifecycle; 04E history/events;
04F integrated tests. Only isolated synthetic candidates authorized here.
No schema, API, IAM, durable Audit, runtime, real data or gate change.
