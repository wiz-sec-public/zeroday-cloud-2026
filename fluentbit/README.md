# Fluent Bit

## Objective and eligibility

Achieve unauthenticated remote code execution through the HTTP input on port `9880` or monitoring server on port `2020`, and execute `/flag.sh fluentbit` in the target container.

## Local environment

```bash
docker compose pull
docker compose up -d
curl -X POST -H 'Content-Type: application/json' \
  -d '{"message":"zdc test"}' http://localhost:9880/test
curl http://localhost:2020/api/v1/health
```
