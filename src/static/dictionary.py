async def greeting_text(user_full_name: str) -> str:
    return (
        f'Привет, {user_full_name}!\n\n'
        f'Я бот проекта switchman https://github.com/KonstantinLjapin/switchman \n\n'
        f'Ознакомся  с документацией проекта\n\n'
        f'Доступные команды\n\n'
        f'/this_day_is даёт ответ на вопрос: рабочий ли день по рабочему календарю? \n\n'
    )
