---
name: neshane-review
description: Review Neshane V3 changes for task scope, approved architecture, service boundaries, tenant isolation, contracts, and evidence without running code.
---

# Neshane review

Apply when reviewing an implementation or before reporting an implementation task complete.

Read the root `AGENTS.md`, the standards matching changed files, and applicable approved V3 ADRs. Review only the requested Task ID and inspect narrowly. Check: unrelated changes; dependency direction; service/data ownership; cross-service imports or SQL; tenant propagation and owning-service authorization; secrets; DTO/entity separation; versioned contracts; error/log safety; configuration validation; tests written for the changed risks; and claims supported by evidence.

Report findings by severity with precise file locations, then list open decisions and unverified assumptions. If there are no findings, say so while retaining limitations. Provide exact manual verification commands but never execute builds, tests, services, containers, deployments, CI/CD, or dependency installation.

