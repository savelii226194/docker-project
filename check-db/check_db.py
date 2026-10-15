import socket
import os

host = os.getenv("DB_HOST", "db")
port = int(os.getenv("DB_PORT", "5432"))

try:
    with socket.create_connection((host, port), timeout=3):
        print(f"База {host}:{port} доступна")
except OSError as ошибка:
    print(f"База {host}:{port} НЕДОСТУПНА:", ошибка)

