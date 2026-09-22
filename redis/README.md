# Redis

## Objective and eligibility

Achieve unauthenticated remote code execution through the password-protected Redis service on TCP port `6379` and execute `/flag.sh redis` in the target container.

Only pre-authentication scenarios are eligible. The entry must achieve RCE without credentials or an authenticated session. Authenticated (post-auth) scenarios are not eligible.

## Local environment

```bash
docker compose pull
docker compose up -d
redis-cli -h 127.0.0.1 -a 'zerodaycloud1!' ping
```

The authenticated command above is only a local health check, not an eligible starting point for a competition entry. The password is provided for local testing and administration only.
