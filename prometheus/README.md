# Prometheus

## Objective and eligibility

Achieve unauthenticated remote code execution through Prometheus on HTTP port `9090` and execute `/flag.sh prometheus` in the target container. The Python scrape fixture is not eligible.

## Local environment

```bash
docker compose pull
docker compose build --pull
docker compose up -d
curl http://localhost:9090/-/ready
curl 'http://localhost:9090/api/v1/targets'
```
