import socket
import os


def check_db(host, port, timeout=3):
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return f"База {host}:{port} доступна"
    except OSError as ошибка:
        return f"База {host}:{port} НЕДОСТУПНА: {ошибка}"


if __name__ == "__main__":
    host = os.getenv("DB_HOST", "db")
    port = int(os.getenv("DB_PORT", "5432"))
    print(check_db(host, port))

