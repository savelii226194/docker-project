FROM python:3.12-slim AS builder
WORKDIR /app
RUN pip install --target=/app/deps requests

FROM python:3.12-slim
WORKDIR /app
COPY --from=builder /app/deps /usr/local/lib/python3.12/site-packages
COPY hello.py .
RUN useradd -m savelii
USER savelii
CMD ["python3", "hello.py"]

