# Apache2 (Apache HTTP Server)

## Objective and eligibility

Achieve unauthenticated remote code execution through Apache HTTP Server on HTTP port `8080` or HTTPS port `8443`, and execute `/flag.sh apache2` in the target container.

The official server, its stock modules, and the default embedded APR/OpenSSL stack are eligible. The certificate generator and static page are fixtures; PHP and external application frameworks are intentionally absent.

## Local environment

```bash
docker compose pull
docker compose up -d
curl http://localhost:8080/
curl -k https://localhost:8443/
```
