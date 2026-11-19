# Customer lifecycle history and event direction

Owner Farzad confirmed 2026-11-19. Core basis 5d7395f; supplements
CM1-PD-139 without rewriting accepted historical requirements.

CM1-PD-144: business history is append-only in normal operations.
Record history/customer/tenant IDs, previous/new status, reason reference,
stable reason code and localized title snapshot, comment, actor, UTC
instant and correlation ID. History does not replace central Audit.

CM1-PD-145: versioned event envelope contains event ID, type and schema
version, aggregate ID and version, tenant, UTC instant, correlation and
causation IDs, payload. Lifecycle payload contains statuses only; exclude
unnecessary personal data, identifiers, documents, comments and actor.
Vocabulary: CustomerCreated, CustomerDeactivated, CustomerReactivated,
CustomerArchived, CustomerRestored. Unsuccessful or blocked changes must
not produce successful events. Synthetic candidate drafts are not events
of completed changes.

CM1-PD-146: Customer Service owns customer information; consumers do not
access its database directly. GraphQL for applicable API interactions,
asynchronous events for change notification. Transactional outbox is
target direction; transaction, delivery, deduplication, ordering, retention
and central Audit contracts require separate architecture and implementation.
Consumers must tolerate duplicate delivery without repeated effects.

03C isolated scope: immutable candidate history and prospective
deactivation event envelope only. No state change, persisted history,
trusted attribution, successful event publication, or gate change.
