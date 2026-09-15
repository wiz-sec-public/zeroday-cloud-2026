# nginx

## Objective and eligibility

Achieve unauthenticated remote code execution through nginx on HTTP port `8080` or HTTPS port `8443`, and execute `/flag.sh nginx` in the target container. The certificate helper is not eligible.

## Local environment

```bash
docker compose pull
docker compose up -d
curl -I http://localhost:8080/
curl -k https://localhost:8443/
```
