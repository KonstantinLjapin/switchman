import asyncio
import calendar
from datetime import datetime
import locale
from logging import Logger
from utils.requests_pack import this_month


async def set_ru():
    """# устанавливаем локаль
          # 'ru_RU.UTF-8'"""
    locale.setlocale(locale.LC_ALL, ('ru_RU', 'UTF-8'))


def keyboard_set_ru():
    """# устанавливаем локаль
          # 'ru_RU.UTF-8'"""
    locale.setlocale(locale.LC_ALL, ('ru_RU', 'UTF-8'))

async def now_year():
    """плучение текущего года"""
    now = datetime.now().year
    return int(now)


async def mounts_bundle(statistic: str, month: int, year: int) -> str:
    """Формирует ровное отображение дней с эмодзи, разделяя каждые 7 дней.

    Пример вывода:
    🔴 1, 🟢 2, 🔴 3, 🟢 4, 🔴 5, 🟢 6, 🔴 7
    🟢 8, 🔴 9, 🟢10, 🔴11, 🟢12, 🔴13, 🟢14...
    ...
    """
    days: str = ""

    for day in range(len(statistic)):
        if statistic[day].isdigit():
            emoji = "🔴" if int(statistic[day]) else "🟢"
            day_number = str(day)
            days += f"{emoji}{day_number}, "
    return days.rstrip(", ")


async def modern_mounts_bundle(statistic: str, month: int, year: int) -> str:
    """Формирует календарь в виде таблицы с правильным отображением дней недели."""
    # Определяем количество дней в месяце
    _, days_in_month = calendar.monthrange(year, month)

    first_weekday = datetime(year, month, 1).weekday()  # Понедельник=0, Воскресенье=6
    # Формируем календарь
    output = " Пн| Вт| Ср| Чт| Пт| Сб| Вс\n"

    days: list = []
    emojis: list = []
    # form a bundl days - emojis
    for day in range(len(statistic)):
        if statistic[day].isdigit():
            emojis.append("ВЫХ" if int(statistic[day]) else "БУД")
            days.append(str(day))
    size_tale_of_week: int = (len(days) + first_weekday) % 7
    day_line: str = ""
    emoji_line: str = ""
    n = 0
    print(first_weekday)
    for day_in_week in range(7):
        if day_in_week >= first_weekday:
            day_line += f"  {days[n]}|"
            emoji_line += f"{emojis[n]}|"
            n = n + 1
        else:
            day_line += f"   |"
            emoji_line += f"  H|"

    output += emoji_line[:-1] + "\n" + day_line[:-1] + "\n"
    del emojis[:7-first_weekday]
    del days[:7-first_weekday]
    f = 0
    # clear temp string line
    day_line = ""
    emoji_line = ""
    # form full week
    for day, emoji, t_index in zip(days, emojis, range(len(emojis))):
        f += 1
        day_line += f" {days[t_index]}|" if len(days[t_index]) > 1 else f"  {days[t_index]}|"
        emoji_line += f"{emojis[t_index]}|"
        if f % 7 == 0:
            # заполняются толко полные недели не полная неделя вылетает
            output = output + emoji_line[:-1] + "\n" + day_line[:-1] + "\n"
            day_line = ""
            emoji_line = ""
            f = 0
    print(days)
    del emojis[:-size_tale_of_week]
    del days[:-size_tale_of_week]
    print(days)
    day_line = ""
    emoji_line = ""
    if len(days) % 7 > 0:
        for day, emoji, t_index in zip(days, emojis, range(len(emojis))):
            day_line += f" {days[t_index]}|" if len(days[t_index]) > 1 else f"  {days[t_index]}|"
            emoji_line += f"{emojis[t_index]}|"
    output = output + emoji_line[:-1] + "\n" + day_line[:-1] + "\n"
    return output


async def month_status(month, logger: Logger):
    await set_ru()
    year = datetime.now().year
    statistic: str = await this_month(year, month, logger)
    bundle: str = await modern_mounts_bundle(statistic, month, year)
    return bundle


async def day_status(day: str):
    await set_ru()
    answer: str = "Выходной" if int(day[1]) else "Рабочий"
    return f"Сегодня {datetime.now().day} {calendar.month_name[datetime.now().month]} и сегодня {answer} день"


if __name__ == '__main__':
    # "M0000110000011000001100000110000" jul 2025

    print(asyncio.run(modern_mounts_bundle("M0000110000011000001100000110000", 7, 2025)))
