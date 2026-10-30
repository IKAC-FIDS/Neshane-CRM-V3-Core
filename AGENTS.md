# Neshane V3 repository instructions

## Scope and authority

- Implement only the explicitly requested Task ID. If no Task ID is supplied, stop and request one before changing files.
- Apply the proportionate approval levels in `architecture/task-governance.md`. Ordinary development/documentation task acceptance is distinct from architecture approval, security authorization, and production release authorization.
- Follow approved Neshane V3 ADRs and the standards under `architecture/standards/`. A legacy repository is read-only evidence, never authority for V3.
- The Root Workspace owns cross-repository architecture and review policy. `Backend/` and `Frontend/` are independent Git repositories and are not submodules or tracked by a Root Git history.
- Follow `architecture/governance-synchronization.md` when shared guidance changes. The current synchronization reference is `NESHANE-V3-GOV-P00-000A`.
- Do not silently introduce an architectural decision. Record unresolved choices as proposed and request architecture approval.
- Do not modify unrelated files. Preserve existing user changes and reconcile existing instructions before editing them.

## Architecture invariants

- Use Java and Spring Boot microservices with Hexagonal Architecture and explicit domain boundaries.
- Keep each Business Service independently buildable and deployable.
- A service owns its domain implementation, data, schema, migrations, and persistence access. Cross-service implementation imports, ORM/entity sharing, and database access are forbidden.
- Share only explicitly versioned contracts or narrow technical primitives; never create a common framework that forces services to share business logic.
- The domain must not depend on Spring or infrastructure implementations. Application code orchestrates use cases; inbound adapters expose entry points; outbound adapters implement ports; configuration owns Spring wiring and technical setup.
- Preserve validated Tenant Context through every tenant-aware operation and enforce authorization in the owning service. Missing or invalid tenant or authorization context fails closed.
- Never add secrets, credentials, tokens, or production-sensitive values to source control.
- Prefer the smallest maintainable solution. Avoid speculative abstractions and premature infrastructure.
- Apply the naming, exception, configuration, logging, and contract conventions in the standards documents consistently.

## Required standards and local skills

Read only the standards and repository skill(s) relevant to the task. Skills live at `.agents/skills/<name>/SKILL.md`:

- `neshane-service`: Spring Boot service structure and boundaries.
- `neshane-api`: REST contracts, DTOs, validation, versioning, and errors.
- `neshane-security`: identity, workload authentication, Tenant Context, and authorization.
- `neshane-persistence`: PostgreSQL ownership, RLS, transactions, and migrations.
- `neshane-messaging`: events, RabbitMQ, outbox/inbox, retry, and idempotency.
- `neshane-plugin`: plugin manifests, installation, grants, gateway, events, and hooks.
- `neshane-review`: architecture compliance review and completion evidence.

## Controlled local execution policy

- Codex may execute local builds, unit tests, formatting checks, architecture/dependency checks, static analysis, offline dependency inspection, and local integration tests only when the current Task ID explicitly requires them and the commands remain within that task's bounded development scope.
- Local integration tests must use isolated non-production resources. Never access production systems, live customer data, real credentials, or shared environments whose state is not dedicated to the task.
- Prefer offline execution when requested by the task. Dependency installation, remote repository access, network downloads, and other external fetches require separate explicit authorization; an authorized build/test task does not grant them implicitly.
- Do not perform destructive database operations, disable tests, suppress meaningful failures, weaken architecture/security checks, or bypass failed controls to obtain a passing result.
- Do not run deployments or production services, publish artifacts, push, open pull requests, or execute CI/CD without separate explicit authorization. Docker, containers, or local application services require explicit task scope and isolated non-production configuration.
- Do not perform expensive or unrelated validation. Record the exact commands, results, failures, skipped checks, resource assumptions, and any network or dependency activity.
- Never treat local execution as Security Sign-off, Production Readiness, release authorization, or proof for an untested deployment profile.

## Completion report

At the end of every implementation task, respond in Persian and include:

1. What was implemented.
2. Files created or modified.
3. Required configuration.
4. Build/test commands actually executed and their results, plus exact manual commands for anything not executed.
5. Exact manual run or deployment instructions when applicable and authorized.
6. Simple verification commands for the user.
7. Known limitations and unverified assumptions.

For documentation-only tasks, do not invent build, run, or deployment commands. Report changed documentation, decisions requiring approval, files needing manual review, missing or conflicting instructions, and the next authorized task instead.


