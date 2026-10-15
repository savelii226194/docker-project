import socket

try:
    with socket.create_connection(("db", 5432), timeout=3):
        print("База db:5432 доступна")
except OSError as ошибка:
    print("База db:5432 НЕДОСТУПНА:", ошибка)

