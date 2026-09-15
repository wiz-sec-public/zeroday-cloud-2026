# Redis

## Objective and eligibility

Achieve unauthenticated remote code execution through the password-protected Redis service on TCP port `6379` and execute `/flag.sh redis` in the target container.

## Local environment

```bash
docker compose pull
docker compose up -d
redis-cli -h 127.0.0.1 -a 'zerodaycloud1!' ping
```
