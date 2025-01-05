#!/bin/bash
# need chmod +
export BOT_TOKEN="$(grep "BOT_TOKEN" .env | cut -d= -f2 - )";
echo $BOT_TOKEN "BOT_TOKEN Load";
cd src;
python main.py;
unset BOT_TOKEN;
echo "BOT_TOKEN unset"