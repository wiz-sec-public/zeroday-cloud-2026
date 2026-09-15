# WordPress

## Objective and eligibility

Achieve unauthenticated remote code execution through WordPress core on HTTP port `8080` and execute `/flag.sh wordpress` in the target container. Plugin and theme vulnerabilities—including vulnerabilities in bundled defaults—are excluded. The bundled Apache/PHP runtime, base image, MariaDB, and WP-CLI installer are fixtures rather than eligible vulnerability sources.

## Local environment

```bash
docker compose pull
docker compose up -d
docker compose wait installer
curl http://localhost:8080/
```

The site is installed automatically. Administrative verification credentials are `admin` / `zerodaycloud1!`, but scoring requires no authentication. The installer deletes every plugin and all inactive themes, leaving only the active core-distributed default theme; it installs no third-party code.
