# Customer lifecycle implementation direction

Farzad confirmed the lifecycle design on 2026-11-19. Core basis 476d110.
This supplement preserves the accepted v1.8.0 baseline and existing gates.

| Decision | Direction |
|---|---|
| CM1-PD-137 | Retain ACTIVE, INACTIVE, ARCHIVED and the existing transition matrix. Inactive records remain readable and editable subject to authorization; new sales opportunities, contracts, orders and relationships are restricted. Existing activity continuation follows owning-service policy. Archived records are read-only and not available for new or continued operational activity. Physical deletion remains excluded. |
| CM1-PD-138 | Dynamic multilingual lifecycle reason catalog: stable code, title, description, allowed transitions, comment requirement, status, tenant and display order. Deactivation, archive and restoration require reasons; ordinary reactivation reason optional. Exact catalog governance remains to be implemented. |
| CM1-PD-139 | Lifecycle history requires customer/tenant identity, prior/new status, reason/comment, actor, UTC timestamp and operation correlation. Proposed event vocabulary: CustomerCreated, CustomerDeactivated, CustomerReactivated, CustomerArchived, CustomerRestored. Durable audit and publication remain downstream contracts. |
| CM1-PD-140 | Archive dependency clearance belongs to the owning services; unavailable or unknown evidence blocks archive. No automatic cascade, reopen or activation of related stored entities. Verification, commercial status and document state remain independent. |

## Implementation sequence

03A: pure transition assessment, mandatory reason presence and rejected
state combinations. Only deactivation may be an eligible synthetic
candidate; reactivation, archive and restoration remain blocked until
required contracts are established. No mutation or authorization.
03B: reason catalog. 03C: history and event descriptors.
03D: dependency assessment. 03E: integrated independent domain tests.

No new permissions, runtime gate changes, real data, persistence, APIs,
Spring, IAM or broker integration. Archive and restoration remain conditional,
and reactivation requires mandatory-field and identifier-conflict checks.
