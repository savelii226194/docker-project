FROM python:3.12-slim
WORKDIR /app
ARG APP_VERSION=local
RUN printf 'Savelii DevOps app\nVersion: %s\n' "$APP_VERSION" > index.html
USER 10001:10001
EXPOSE 8000
CMD ["python3", "-m", "http.server", "8000"]
