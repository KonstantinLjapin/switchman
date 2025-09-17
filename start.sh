#!/bin/bash

set -e

# Активируем окружение Poetry
source $(poetry env info --path)/bin/activate

# Устанавливаем PYTHONPATH
export PYTHONPATH="/home/laser_boy/switchman/src:$PYTHONPATH"

# Загрузка токена
export BOT_TOKEN=$(grep "BOT_TOKEN" .env | cut -d= -f2)
echo "$BOT_TOKEN : BOT_TOKEN loaded"

# Проверяем наличие аргумента
if [ "$1" = "y" ]; then
    # Запускаем в фоновом режиме
    nohup python -m main > /dev/null 2>&1 &
    pid=$!
    echo "Бот запущен в фоновом режиме с PID: $pid"
    echo $pid > bot.pid
else
    # Запускаем в foreground режиме
    echo "Запуск бота в foreground режиме..."
    python -m main
fi