# FastAPI

## Objective and eligibility

Achieve unauthenticated remote code execution through the normal FastAPI stack on HTTP port `8000` and execute `/flag.sh fastapi` in the target container. FastAPI, Uvicorn, Starlette, Pydantic, and their default request/response path are eligible.

## Local environment

```bash
docker compose build --pull --no-cache
docker compose up -d
curl http://localhost:8000/
curl -X POST -H 'Content-Type: application/json' -d '{"text":"hello"}' http://localhost:8000/echo
docker compose exec fastapi python -c 'import fastapi,uvicorn,starlette,pydantic; print(fastapi.__version__, uvicorn.__version__, starlette.__version__, pydantic.__version__)'
```
