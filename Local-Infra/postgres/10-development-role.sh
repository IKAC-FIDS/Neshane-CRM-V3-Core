#!/usr/bin/env bash
# Fresh synthetic dev volume only. Not a product migration or RLS implementation.
set -Eeuo pipefail
: "${POSTGRES_APP_PASSWORD:?Set POSTGRES_APP_PASSWORD}"
if [ "$POSTGRES_APP_PASSWORD" = "$POSTGRES_PASSWORD" ]; then
  printf '%s\n' 'Development app and bootstrap passwords must differ.' >&2
  exit 1
fi

# psql obtains the value from its environment, not a password-bearing argument.
psql -X --set=ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<'SQL'
\getenv app_password POSTGRES_APP_PASSWORD
CREATE ROLE neshane_dev_app LOGIN NOSUPERUSER NOCREATEDB NOCREATEROLE NOREPLICATION NOBYPASSRLS PASSWORD :'app_password';
REVOKE ALL ON DATABASE neshane_dev FROM PUBLIC;
GRANT CONNECT ON DATABASE neshane_dev TO neshane_dev_app;
REVOKE CREATE ON SCHEMA public FROM PUBLIC;
GRANT USAGE ON SCHEMA public TO neshane_dev_app;
SQL
# No schema/table creation or blanket table privileges; future services own them.
