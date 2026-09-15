# Envoy

## Objective and eligibility

Achieve unauthenticated remote code execution through the edge Envoy HTTPS service on port `10000` and execute `/flag.sh envoy` in the target container.

This is the official Google VRP environment: the edge Envoy forwards `/content/*` to an internal origin Envoy and returns `403` for other paths. The origin returns `hidden treasure` for `/blockedz` and `normal` otherwise. Both Envoy processes in the image are part of the target.

## Local environment

```bash
docker compose pull
docker compose up -d
curl -k https://localhost:10000/content/
```
