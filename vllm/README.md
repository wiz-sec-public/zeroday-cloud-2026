# vLLM

## Objective and eligibility

Achieve unauthenticated remote code execution through the OpenAI-compatible HTTP API on port `8000` and execute `/flag.sh vllm` in the target container. The vulnerability must be in vLLM; malicious or backdoored model code is excluded.

The competition environment will run vLLM on an NVIDIA GPU. The model may be changed to any publicly available model from a reputable source. State the required model in the submission so it can be cached for demo day.

## Local environment

The provided Compose environment is for local testing and does not require a GPU. Allocate at least 4 GB of Docker memory; larger models require more RAM.

The provided Docker Compose file uses the lightweight `facebook/opt-125m` model as a default for the testing environment. **You are free to use a different model for your exploit.**

```bash
MODEL=facebook/opt-125m docker compose pull
MODEL=facebook/opt-125m docker compose up -d
curl http://localhost:8000/v1/models
```
