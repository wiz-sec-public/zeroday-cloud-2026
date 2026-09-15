# Apache Tomcat

## Objective and eligibility

Achieve unauthenticated remote code execution through Tomcat on HTTP port `8080` or HTTPS port `8443`, and execute `/flag.sh tomcat` in the target container.

## Local environment

```bash
docker compose pull
docker compose up -d
curl -I http://localhost:8080/
curl -kI https://localhost:8443/
```
