# Apache Airflow

## Objective and eligibility

Achieve remote code execution through the Airflow API/UI on HTTP port `8081` without authentication and execute `/flag.sh airflow` in an Airflow target container. PostgreSQL and Redis are infrastructure fixtures and are excluded.

Authentication is enabled using Airflow's default `SimpleAuthManager`; scoring requires unauthenticated RCE. Airflow generates the `admin` user's password on first startup and stores it in the shared local config directory. No Airflow password or signing key is checked in.

## Local environment

Allocate at least 8 GB of Docker memory, then run:

```bash
docker compose pull
docker compose up -d
docker compose ps
curl http://localhost:8081/api/v2/monitor/health
```

The UI and login page are available at `http://localhost:8081/` and `http://localhost:8081/auth/login/`. To retrieve the generated local testing password:

```bash
docker compose exec airflow-apiserver \
  cat /opt/airflow/config/simple_auth_manager_passwords.json.generated
```

Initialization and first startup can take several minutes.
