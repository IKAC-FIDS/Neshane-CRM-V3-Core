---
name: neshane-api
description: Implement or review Neshane V3 REST endpoints, DTO mapping, validation, contract versioning, and safe error responses.
---

# Neshane API

Apply when a task changes a public or service-to-service REST contract or inbound web adapter.

Read the root `AGENTS.md` plus `architecture/standards/api-design.md`, `error-handling.md`, `security.md`, and `service-architecture.md`. Confirm the owning service and approved contract/versioning decisions. Keep transport DTOs separate from domain and persistence types, validate at the boundary, map explicitly to a use case, and enforce authorization in the owner. Preserve tenant/correlation context and return standardized, non-sensitive problem details. Treat breaking changes as a new version or approved migration.

Deliver endpoint/DTO/mapping changes, validation and error mappings, relevant unexecuted tests, and explicit compatibility or proposal notes. Never run builds, tests, services, deployments, or dependency installation.

