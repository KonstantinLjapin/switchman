import asyncio
import calendar
from datetime import datetime
from utils.requests_pack import this_month, this_day

# TODO установка локального языка

#print(calendar.month_name[datetime.now().month])
#print(calendar.monthrange(datetime.now().year, datetime.now().month)[1])


async def mounts_bundle(statistic: str):
    days: list = []
    for i in range(0, calendar.monthrange(datetime.now().year, datetime.now().month)[1] + 1):
        days.append([i, statistic[i]])
    return days


async def day_status(day: str):
    answer: str = "Выходной" if day[1] else "Рабочий"
    return f"Сегодня {datetime.now().day} и сегодня {answer}"

