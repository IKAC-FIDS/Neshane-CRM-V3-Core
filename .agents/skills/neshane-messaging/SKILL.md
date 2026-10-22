---
name: neshane-messaging
description: Implement or review Neshane V3 events, RabbitMQ adapters, transactional outbox/inbox, retries, and idempotent consumers.
---

# Neshane messaging

Apply when a task changes event contracts, publication, consumption, RabbitMQ topology, retry, dead-letter, or idempotency behavior.

Read the root `AGENTS.md` plus `architecture/standards/messaging.md`, `service-architecture.md`, and `security.md`; also read `persistence.md` for outbox/inbox work. Confirm producer ownership, event meaning/version, tenant provenance, delivery assumptions, and consumer failure behavior. Use atomic outbox publication for owned state changes and durable inbox/effect handling before acknowledgment. Assume duplicates and possible reordering; use bounded retry and explicit dead-letter/re-drive handling. Do not share producer implementation types or claim exactly-once delivery.

Deliver contracts/adapters, relevant unexecuted failure and idempotency tests, topology/configuration notes, and compatibility assumptions. Never run brokers, builds, tests, containers, services, or deployments.

