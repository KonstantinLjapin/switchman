### Постановка задачи для проекта

- постановка первичных целей
  написать структурированый проект телеграмм бота с календарём рабочих дней

- постановка целей долгой перспективы

### Первичные цели 
- Задача бот помошник предоставляет рабочий календарь сотрудникам 
- Технологии git, docker, python, database, CI/CD, UML

### Технологии
- UML представление моделей проекта и взаимодействия компонентов в графическом виде
* CI/CD (выбор сервиса и способа для деплоя (Ansible?))
* выбор database
- выбор версии python3 
* мой пресет docker compose
- Использовать git без GUI
#
- python3.12
- aiohttp
- pyTelegramBotAPI (asynchronous_telebot)
- poetry (сомнительный инструмент)
- Ruff ( настраевыемый)
### Используемые API 
- https://www.isdayoff.ru/ получение статуса дня рабочий или нет

### Задача
- После выбора компонентов создать фрейм бота # done
- Определить модели и компоненты, визуализировать взаимодействие # need rework
- деплой CI/CD # hot task

### постановка целей долгой перспективы
- Выбор лицензии распостронения 
- ROAD MAP

### Холодный старт
- poetry init -n --python "^3.12"
- poetry config virtualenvs.in-project true
- poetry env use python3.12
- mkdir src
- poetry install --no-root
- sudo chmod +x stop_bot.sh
- sudo chmod +x ./start.sh

### Запуск проекта
- poetry run ./start.sh с помощью поетри  виртуальном окружении
- poetry run ./stop_bot.sh  остановка бота
- ./start_doc_com.sh с помощью докер компосе