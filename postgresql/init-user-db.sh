#!/bin/sh
set -eu

psql -v ON_ERROR_STOP=1 \
  --set=demo_user="$POSTGRES_DEMO_USER" \
  --set=demo_db="$POSTGRES_DEMO_DB" \
  --set=demo_password="$POSTGRES_DEMO_PASSWORD" <<'SQL'
CREATE ROLE :"demo_user" LOGIN PASSWORD :'demo_password'
  NOSUPERUSER NOCREATEDB NOCREATEROLE NOINHERIT NOREPLICATION;
CREATE DATABASE :"demo_db" OWNER :"demo_user";
SQL
