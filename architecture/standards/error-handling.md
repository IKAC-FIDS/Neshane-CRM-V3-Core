# Error handling standard

## Internal errors

- Domain failures use domain-specific types and stable semantic codes.
- Application code translates expected port failures into use-case outcomes; unexpected failures remain failures and are not converted to success.
- Adapters translate internal failures once at the boundary. Do not leak framework, database, broker, or provider exceptions.
- Never catch and ignore an exception. Preserve the original cause when wrapping and avoid duplicate logging at multiple layers.

## External errors

- REST errors use a consistent Problem Details representation with safe `type`, `title`, `status`, `detail`, `instance`, stable application `code`, and `correlationId` fields.
- Validation errors may include safe field-level violations; authorization denials must not reveal resource existence or policy internals.
- Responses and logs must exclude stack traces, SQL, secrets, tokens, credentials, and sensitive payloads.
- Map the same failure class consistently to transport status and retryability.

## Proposed choices requiring approval

The exact Problem Details media type/version, problem type URI ownership, error-code namespace, localization policy, and message-consumer failure envelope.

