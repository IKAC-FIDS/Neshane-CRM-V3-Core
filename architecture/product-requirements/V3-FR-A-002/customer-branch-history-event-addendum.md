# Branch history and event direction

Owner Farzad confirmed 2026-11-19; Core basis ecd2615.
Supplement CM1-PD-139/144..146/153/157..159.

CM1-PD-160: independent append-only Branch business history records
history, tenant, Company and Branch IDs, operation, previous/new stored
status, localized reason snapshot, comment, actor, UTC instant and
correlation ID. No ordinary edit/delete of prior history; central Audit
remains separately governed.

CM1-PD-161: target event vocabulary BranchCreated, BranchUpdated,
BranchDeactivated, BranchReactivated, BranchContactChanged,
BranchTypeChanged. Versioned envelope follows customer event convention.
Lifecycle payload includes Company ID and stored statuses; no contact
values, reason/comment, names or documents. Only successful committed
operations may eventually publish events. Parent state changes do not
produce independent BranchDeactivated or BranchReactivated events.
Consumers derive effective state from parent and branch status.

04E isolated candidate history and prospective deactivation event only.
Inactive snapshot support and other actual operations remain pending.
Trusted actor/time/version, durable Audit, outbox, delivery and
authorization contracts remain open. No runtime or gate change.
