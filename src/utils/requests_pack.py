from typing import Any

import aiohttp
import asyncio


async def this_day() -> Any:

    async with aiohttp.ClientSession() as session:
        async with session.get('https://isdayoff.ru/today') as response:

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = "D" + await response.text()
            print("Body:", html)
            print(len(html))


async def this_month(year: str, month: str) -> Any:

    month: str = f"https://isdayoff.ru/api/getdata?year={year}&month={month}"
    async with aiohttp.ClientSession() as session:
        async with session.get(month) as response:

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = "M"+(await response.text())
            print("Body:", html)
            print(len(html))


async def this_year(year: str) -> Any:

    month: str = f"https://isdayoff.ru/api/getdata?year={year}"
    async with aiohttp.ClientSession() as session:
        async with session.get(month) as response:

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = "Y"+(await response.text())
            print("Body:", html)
            print(len(html))

asyncio.run(this_year("2025"))

