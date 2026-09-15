# Grafana

## Objective and eligible scenarios

Achieve remote code execution through Grafana's HTTP service on port `3000` and execute `/flag.sh grafana` in the target container.

- **Authenticated:** username `admin`, password `zerodaycloud1!`.
- **Unauthenticated:** obtain RCE without credentials against the same authenticated instance.

Plugin installation, preinstallation, external plugin management, and unsigned-plugin loading are disabled. Third-party plugins are not part of this target.

## Local environment

```bash
docker compose pull
docker compose up -d
curl http://localhost:3000/api/health
```
