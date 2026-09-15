# React

## Objective and eligibility

Achieve unauthenticated remote code execution through the React/ReactDOM server-rendering stack on HTTP port `3000` and execute `/flag.sh react` in the target container. Node's built-in HTTP server is only the transport fixture; no additional web framework is installed.

## Local environment

```bash
docker compose build --pull --no-cache
docker compose up -d
curl http://localhost:3000/
docker compose exec react npm ls react react-dom
```
