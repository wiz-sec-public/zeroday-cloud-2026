# PostgreSQL

## Objective and eligible scenarios

Achieve remote code execution through PostgreSQL on TCP port `5432` and execute `/flag.sh postgresql` in the target container.

- **Authenticated:** use only low-privileged user `demo`, password `zerodaycloud1!`, database `demo`.
- **Unauthenticated:** obtain RCE without credentials.

The `postgres` superuser password is `zerodaycloud1!` for environment administration only and is not an eligible authenticated starting point.

## Local environment

```bash
docker compose pull
docker compose up -d
PGPASSWORD='zerodaycloud1!' psql -h 127.0.0.1 -U demo -d demo
```

The initialization script creates `demo` without superuser, database-creation, role-creation, inheritance, or replication privileges.
