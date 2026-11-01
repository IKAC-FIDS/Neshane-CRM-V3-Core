# API design

## Contracts

- Public REST contracts use URI major versioning: `/api/v<major>/<resources>`. Minor and patch revisions are recorded in contract metadata/history. Header-only and media-type versioning are not part of the initial baseline.
- Use plural, resource-oriented, lowercase paths; use path segments for identity and query parameters for filtering, sorting, and pagination. Avoid verbs in resource paths.
- Define request and response DTOs at the inbound boundary. Never expose persistence entities or accept them as API input.
- Map DTOs explicitly to application commands/queries and back to response contracts.
- Validate syntax and shape at the API boundary; enforce business invariants in the domain.
- Use consistent HTTP semantics, idempotency rules, pagination bounds, and content types.
- Breaking contract changes require a new major version, bounded coexistence, consumer inventory and migration ownership, explicit deprecation/removal criteria and evidence before retirement.

## Security and operations

- Treat tenant identifiers supplied by clients as selectors, never proof of membership or authority.
- Authenticate callers and authorize the operation and target resource in the owning service.
- Propagate a validated correlation identifier and return standardized problem details from `error-handling.md`.
- Do not expose stack traces, internal class names, credentials, authorization details, or sensitive domain data.

## Choices still requiring approval

- Public REST/GraphQL/hybrid strategy under `OD-007`, GraphQL versioning if selected, pagination format, idempotency-key contract, and compatibility tooling under `OD-020`.

