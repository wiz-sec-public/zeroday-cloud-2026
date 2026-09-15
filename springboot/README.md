# Spring Boot

## Objective and eligibility

Achieve unauthenticated remote code execution through the default Spring Boot Web stack on HTTP port `8080` and execute `/flag.sh springboot` in the target container. Spring Boot, Spring Framework, Jackson, and the default embedded servlet-container stack selected by Spring Boot are eligible.

## Local environment

```bash
docker compose build --pull --no-cache
docker compose up -d
curl http://localhost:8080/
docker compose run --rm --entrypoint cat springboot /app/spring-boot-version
```
