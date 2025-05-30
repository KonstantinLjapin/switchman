from typing import Any

import aiohttp

from logging import Logger


async def this_day(logger: Logger) -> Any:
    """Запрос к Api алиасом этот день возвращаает строку
     на 1 индексе статус дня при ответе от сервера 200"""

    async with aiohttp.ClientSession() as session:
        async with session.get('https://isdayoff.ru/today') as response:
            day_status = "D" + await response.text()
            logger.info(f" || response calendar API https://isdayoff.ru/today "
                        f" || Content-type: {response.headers['content-type']}"
                        f" || Body {day_status}")
            return day_status


async def this_month(year: int, month: int, logger: Logger) -> Any:
    """Запрос к Api получение статуста дней возращает строку с 1 по 31(28) индексы
     в месяце конкретного года при статусе ответа от сервера 200"""

    data: str = f"https://isdayoff.ru/api/getdata?year={year}&month={month}"
    async with aiohttp.ClientSession() as session:
        async with session.get(data) as response:
            days_in_mount_status: str = "M" + (await response.text())
            logger.info(f" || response calendar API https://isdayoff.ru/today "
                        f" || Content-type: {response.headers['content-type']}"
                        f" || Body {days_in_mount_status}")
            return days_in_mount_status


async def this_year(year: str) -> Any:
    """Запрос к Api получение статуста  до 366 дней
          конкретном году при статусе ответа от сервера 200"""

    data: str = f"https://isdayoff.ru/api/getdata?year={year}"
    async with aiohttp.ClientSession() as session:
        async with session.get(data) as response:
            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = "Y" + (await response.text())
            print("Body:", html)
            print(len(html))
