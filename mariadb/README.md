# MariaDB

## Objective and eligible scenarios

Achieve remote code execution through MariaDB on TCP port `3306` and execute `/flag.sh mariadb` in the target container.

- **Authenticated:** use only the low-privileged `demo` account, password `zerodaycloud1!`, database `demo`.
- **Unauthenticated:** obtain RCE without credentials.

The root account (`root` / `zerodaycloud1!`) exists for environment administration and is not an eligible authenticated starting point. `LOCAL INFILE` is disabled.

## Local environment

```bash
docker compose pull
docker compose up -d
mariadb -h 127.0.0.1 -u demo -p'zerodaycloud1!' demo
```
