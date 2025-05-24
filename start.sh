#!/bin/bash
set -e

# Загрузка токена
export BOT_TOKEN=$(grep "BOT_TOKEN" .env | cut -d= -f2 -)
echo "$BOT_TOKEN : BOT_TOKEN loaded"

# Запуск через Poetry
poetry run python -m src.main

# Очистка
unset BOT_TOKEN