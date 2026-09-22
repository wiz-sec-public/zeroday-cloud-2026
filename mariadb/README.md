# MariaDB

## Objective and eligibility

Achieve unauthenticated remote code execution through MariaDB on TCP port `3306` and execute `/flag.sh mariadb` in the target container.

Only pre-authentication scenarios are eligible. The service has authentication enabled; the entry must achieve RCE without credentials or an authenticated session. Authenticated (post-auth) scenarios are not eligible.

`LOCAL INFILE` is disabled.

## Local environment

```bash
docker compose pull
docker compose up -d
mariadb -h 127.0.0.1 -u demo -p'zerodaycloud1!' demo
```

The authenticated connection above is only a local setup/health check, not an eligible starting point for a competition entry.

The low-privileged `demo` account and the `root` account use the password `zerodaycloud1!` for local testing and administration only; neither account may be used as an authenticated starting point.
