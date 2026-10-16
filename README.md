# docker-project

Учебный проект: Python-скрипт в Docker, от одиночного контейнера до
Compose-стека с PostgreSQL и nginx.

## Структура

- `check-db/` — Python-скрипт `check_db.py`, который проверяет доступность
  базы данных по хосту и порту. Multi-stage Dockerfile, образ < 100 МБ,
  запускается не от root.
- `stack/` — полноценный стек из трёх сервисов на Docker Compose: `app`
  (Python HTTP-сервер), `db` (PostgreSQL 16, данные в именованном томе),
  `nginx` (reverse proxy на порт 8080).

## Как запустить

### check-db (одиночный контейнер)

cd check-db
docker build -t check-db:1 .
docker run check-db:1

### stack (Docker Compose)

cd stack
docker compose up -d
curl http://localhost:8080

