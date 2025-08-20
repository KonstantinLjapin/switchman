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
    """Формирует календарь на месяц с эмодзи, выровненный по дням недели."""
    import calendar

    # Создаем матрицу календаря
    cal = calendar.monthcalendar(year, month)

    # Формируем заголовок с днями недели (фиксированная ширина 4 символа)
    weekdays = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]
    header_parts = [f"📅{day:2}" for day in weekdays]
    weekdays_header = " ".join(header_parts)

    result_lines = [weekdays_header]

    for week in cal:
        week_days = []
        for day in week:
            if day == 0:
                # Пустой день (принадлежит другому месяцу)
                week_days.append("    ")
            else:
                # Получаем данные для дня
                if day - 1 < len(statistic) and statistic[day - 1].isdigit():
                    emoji = "🔴" if int(statistic[day - 1]) else "🟢"
                else:
                    emoji = "⚪"  # Если данных нет

                # Форматируем число дня
                day_str = f"{day:2d}" if day > 9 else f" {day}"
                week_days.append(f"{emoji}{day_str}")

        result_lines.append(" ".join(week_days))

    return "\n".join(result_lines)


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
