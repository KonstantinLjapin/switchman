#!/bin/bash

set -e

# Активируем окружение Poetry
source $(poetry env info --path)/bin/activate

# Устанавливаем PYTHONPATH
export PYTHONPATH="/home/laser_boy/switchman/src:$PYTHONPATH"

# Загрузка токена
export BOT_TOKEN=$(grep "BOT_TOKEN" .env | cut -d= -f2)
echo "$BOT_TOKEN : BOT_TOKEN loaded"

# Запускаем в режиме демона
nohup python -m main > /dev/null 2>&1 &

# Сохраняем PID процесса для возможности управления им later
echo $! > bot.pid

echo "Бот запущен в фоновом режиме с PID: $!"
