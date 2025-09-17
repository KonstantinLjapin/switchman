#!/bin/bash
set -e

# Проверяем существование файла с PID
if [ ! -f bot.pid ]; then
    echo "Файл bot.pid не найден"
    exit 1
fi

# Читаем PID из файла
PID=$(cat bot.pid)

# Завершаем процесс
if kill -0 $PID 2>/dev/null; then
    kill $PID
    echo "Процесс бота (PID: $PID) остановлен"
    rm -f bot.pid
else
    echo "Процесс с PID $PID не найден"
    rm -f bot.pid
    exit 1
fi