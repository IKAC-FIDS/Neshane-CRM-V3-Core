---
name: neshane-service
description: Create or extend a Neshane V3 Java/Spring Boot microservice while preserving hexagonal boundaries and independent ownership.
---

# Neshane service

Apply when a task creates or changes service domain, application, adapter, or configuration code.

1. Read the root `AGENTS.md`, `architecture/standards/repository-structure.md`, `service-architecture.md`, and `java-coding.md`.
2. Confirm the Task ID, owning bounded context, approved ADRs, and affected ports before editing.
3. Keep dependency direction `adapter -> application -> domain`; keep the domain framework-independent.
4. Preserve independent build/deployment and forbid cross-service implementation or database dependencies.
5. Add only packages required by the feature; do not scaffold unused layers or create a shared business framework.
6. Select the API, security, persistence, or messaging skill when those boundaries change.

Deliver the smallest implementation, relevant unexecuted test code when required, configuration notes, contract/ADR impacts, and the Persian completion report required by `AGENTS.md`. Never run builds, tests, services, containers, deployments, or dependency installation.

