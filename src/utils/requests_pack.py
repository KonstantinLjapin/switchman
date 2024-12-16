from typing import Any

import aiohttp

# TODO logging


async def this_day() -> Any:

    async with aiohttp.ClientSession() as session:
        async with session.get('https://isdayoff.ru/today') as response:

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            day_status = "D" + await response.text()
            print("Body:", day_status)
            return day_status


async def this_month(year: str, month: str) -> Any:

    month: str = f"https://isdayoff.ru/api/getdata?year={year}&month={month}"
    async with aiohttp.ClientSession() as session:
        async with session.get(month) as response:

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            days_in_mount_status: str = "M"+(await response.text())
            print("Body:", days_in_mount_status)
            return days_in_mount_status


async def this_year(year: str) -> Any:

    month: str = f"https://isdayoff.ru/api/getdata?year={year}"
    async with aiohttp.ClientSession() as session:
        async with session.get(month) as response:

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = "Y"+(await response.text())
            print("Body:", html)
            print(len(html))
