# LiteLLM

## Objective and eligibility

Achieve remote code execution in LiteLLM through HTTP port `4000` without a master key and execute `/flag.sh litellm` in the target container. The private mock OpenAI service is a deterministic fixture and is not eligible.

The LiteLLM instance requires master-key authentication. For authenticated environment checks, use `sk-zdc-litellm-master-key`; scoring remains **unauthenticated RCE**.

## Local environment

```bash
docker compose pull
docker compose build --pull
docker compose up -d

# Expected: 401 without the master key.
curl -i http://localhost:4000/v1/chat/completions \
  -H 'Content-Type: application/json' \
  -d '{"model":"zdc-mock","messages":[{"role":"user","content":"hello"}]}'

# Expected: a response from the private mock backend.
curl http://localhost:4000/v1/chat/completions \
  -H 'Authorization: Bearer sk-zdc-litellm-master-key' \
  -H 'Content-Type: application/json' \
  -d '{"model":"zdc-mock","messages":[{"role":"user","content":"hello"}]}'
```
