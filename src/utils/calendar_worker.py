import asyncio
import calendar
from datetime import datetime
import locale


async def set_ru():
    """# устанавливаем локаль
          # 'ru_RU.UTF-8'"""
    locale.setlocale(locale.LC_ALL, ('ru_RU', 'UTF-8'))


async def now_year():
    """плучение текущего года"""
    now = datetime.now().year
    return int(now)


async def mounts_bundle(statistic: str):
    days: list = []
    for i in range(0, calendar.monthrange(datetime.now().year, datetime.now().month)[1] + 1):
        days.append([i, statistic[i]])
    return days


async def day_status(day: str):
    answer: str = "Выходной" if day[1] else "Рабочий"
    return f"Сегодня {datetime.now().day} и сегодня {answer}"
