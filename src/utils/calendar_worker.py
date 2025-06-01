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


async def mounts_bundle(statistic: str) -> str:
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


async def month_status(logger: Logger):
    await set_ru()
    today = datetime.now()
    statistic: str = await this_month(today.year, today.month, logger)
    bundle: str = await mounts_bundle(statistic)
    return bundle


async def day_status(day: str):
    await set_ru()
    answer: str = "Выходной" if int(day[1]) else "Рабочий"
    return f"Сегодня {datetime.now().day} {calendar.month_name[datetime.now().month]} и сегодня {answer}"
