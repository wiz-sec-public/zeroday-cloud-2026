# PostgreSQL

## Objective and eligibility

Achieve unauthenticated remote code execution through PostgreSQL on TCP port `5432` and execute `/flag.sh postgresql` in the target container.

Only pre-authentication scenarios are eligible. The service has authentication enabled; the entry must achieve RCE without credentials or an authenticated session. Authenticated (post-auth) scenarios are not eligible.

## Local environment

```bash
docker compose pull
docker compose up -d
PGPASSWORD='zerodaycloud1!' psql -h 127.0.0.1 -U demo -d demo
```

The authenticated connection above is only a local setup/health check, not an eligible starting point for a competition entry.

The initialization script creates `demo` without superuser, database-creation, role-creation, inheritance, or replication privileges. The `demo` and `postgres` passwords are `zerodaycloud1!` for local testing and administration only; neither account may be used as an authenticated starting point.
