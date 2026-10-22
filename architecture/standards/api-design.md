# API design

## Contracts

- Public REST contracts must be explicitly versioned. The exact URI/header strategy is proposed until approved; `/api/v1/<resources>` is the default proposal.
- Use plural, resource-oriented, lowercase paths; use path segments for identity and query parameters for filtering, sorting, and pagination. Avoid verbs in resource paths.
- Define request and response DTOs at the inbound boundary. Never expose persistence entities or accept them as API input.
- Map DTOs explicitly to application commands/queries and back to response contracts.
- Validate syntax and shape at the API boundary; enforce business invariants in the domain.
- Use consistent HTTP semantics, idempotency rules, pagination bounds, and content types.
- Breaking contract changes require a new version or an approved compatibility and migration plan.

## Security and operations

- Treat tenant identifiers supplied by clients as selectors, never proof of membership or authority.
- Authenticate callers and authorize the operation and target resource in the owning service.
- Propagate a validated correlation identifier and return standardized problem details from `error-handling.md`.
- Do not expose stack traces, internal class names, credentials, authorization details, or sensitive domain data.

## Proposed choices requiring approval

- Exact versioning mechanism, pagination format, idempotency-key contract, and compatibility tooling.

