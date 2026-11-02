#!/usr/bin/env bash
set -euo pipefail

image="${1:?Укажи образ}"
version="${2:?Укажи версию}"
current=savelii-web
previous=savelii-web-previous
url=http://127.0.0.1:8080

docker pull "$image"

if docker container inspect "$previous" >/dev/null 2>&1; then
    docker rm "$previous"
fi

had_previous=false
if docker container inspect "$current" >/dev/null 2>&1; then
    docker stop "$current"
    docker rename "$current" "$previous"
    had_previous=true
fi

if docker run -d --name "$current" --restart unless-stopped \
    -p 127.0.0.1:8080:8000 "$image"; then
    for attempt in {1..15}; do
        if curl -fsS --max-time 2 "$url" | grep -Fxq "Version: $version"; then
            echo "Новая версия работает: $version"
            exit 0
        fi
        sleep 1
    done
fi

echo "Новая версия не прошла проверку" >&2
if docker container inspect "$current" >/dev/null 2>&1; then
    docker rm -f "$current"
fi

if "$had_previous"; then
    docker rename "$previous" "$current"
    docker start "$current"
    curl --retry 5 --retry-connrefused --retry-delay 1 -fsS --max-time 3 "$url"
    echo "Предыдущий контейнер восстановлен"
else
    echo "Первый запуск: предыдущего контейнера для возврата нет" >&2
fi

exit 1
