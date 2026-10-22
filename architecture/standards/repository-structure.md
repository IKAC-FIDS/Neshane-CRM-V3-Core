# Repository structure

## Rules

- Keep deployable Business Services under `Backend/` and user-facing applications under `Frontend/`; the exact module layout is proposed until a V3 ADR approves it.
- Each service must have its own build boundary, configuration, migrations, tests, and deployment artifact.
- Do not import another service's implementation, domain model, persistence entity, repository, or database client.
- Shared modules may contain only versioned transport contracts or narrow, domain-neutral technical primitives. Shared business logic is forbidden.
- Architecture decisions belong in a future V3 ADR area; standards describe approved rules but must not disguise proposals as decisions.
- Do not create empty service skeletons or directories before a task requires them.

## Canonical service template

```text
src/main/java/<base-package>/
    domain/
        model/
        event/
        service/
        port/
    application/
        usecase/
        command/
        query/
        dto/
    adapter/
        in/
            web/
            messaging/
        out/
            persistence/
            messaging/
            integration/
    configuration/

src/main/resources/
    application.yml
    db/migration/

src/test/java/<base-package>/
```

This is a canonical template, not a requirement to create every directory. Feature implementations should use domain-specific subpackages while keeping dependency direction intact.

## Dependency direction

`adapter -> application -> domain`; configuration may wire all layers. Domain code has no Spring or infrastructure dependency. Application code depends on domain types and ports, not adapter implementations.

## Proposed choices requiring approval

- Java base-package prefix: proposed `ir.neshane.<service>`; approve before the first service is created.
- Exact multi-module build layout and shared-contract publication mechanism require a V3 ADR.

