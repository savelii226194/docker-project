FROM python:3.12-slim AS builder
WORKDIR /app
COPY check_db.py .

FROM python:3.12-slim
WORKDIR /app
COPY --from=builder /app/check_db.py .
RUN useradd -m savelii
USER savelii
CMD ["python3", "check_db.py"]

