# Java coding standard

## Naming and layout

- Packages are lowercase and domain-oriented; avoid generic buckets such as `util` or `common` unless the contents are genuinely technical and narrow.
- Classes, records, enums, and interfaces use `PascalCase`.
- Methods, parameters, and fields use `camelCase`; constants use `UPPER_SNAKE_CASE`.
- Name ports by capability, not technology. Adapter names may identify the technology they implement.
- Keep public APIs small. Prefer immutable value objects and constructor injection.

## Code rules

- Keep domain behavior with the domain model or domain service that owns the invariant.
- Do not annotate domain types with Spring, web, messaging, or persistence annotations.
- Avoid static mutable state, reflection-heavy indirection, and speculative base classes.
- Validate input at trust boundaries and preserve domain validation inside the domain.
- Catch exceptions only to recover, translate at a boundary, or add safe context. Never swallow failures.
- Use domain-specific exceptions internally and the standardized external error mapping in `error-handling.md`.
- Write structured, parameterized logs; include correlation identifiers through logging context and never log secrets or sensitive payloads.

## Proposed choices requiring approval

- Java version, Spring Boot version, formatting tool, compiler warning policy, and nullability annotation library must be approved by the first foundation ADR/build task.

