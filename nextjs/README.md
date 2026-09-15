# Next.js

## Objective and eligibility

Achieve unauthenticated remote code execution through the default Next.js/React production stack on HTTP port `3000` and execute `/flag.sh nextjs` in the target container. Next.js, React, ReactDOM, and their normal embedded production server path are eligible.

## Local environment

```bash
docker compose build --pull --no-cache
docker compose up -d
curl http://localhost:3000/
docker compose exec nextjs sh -c 'test "$NODE_ENV" = production && npm ls next react react-dom'
```
