from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.calendar_worker import day_status, now_year


def gen_markup():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    markup.add(InlineKeyboardButton("Yes", callback_data="cb_yes"),
               InlineKeyboardButton("No", callback_data="cb_no"))
    return markup


async def gen_precending_now_coming_year_markup() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    markup.row(InlineKeyboardButton(str(await now_year() - 1),
                                    callback_data=f"calendar_year{str(await now_year() - 1)}"),
               InlineKeyboardButton(str(await now_year()),
                                    callback_data=f"calendar_year{str(await now_year())}"),
               InlineKeyboardButton(str(await now_year() + 1),
                                    callback_data=f"calendar_year{str(await now_year() + 1)}"))
    return markup


async def gen_mounts_in_year_markup(days_bundle: list) -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    markup.row_width = 3
    for day in days_bundle:
        status: str = await day_status(day)
        markup.add(InlineKeyboardButton(status, callback_data="cb_yes"))
    return markup


async def gen_days_in_mount_markup(days_bundle: list) -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    markup.row_width = 3
    for day in days_bundle:
        status: str = await day_status(day)
        markup.add(InlineKeyboardButton(status, callback_data="cb_yes"))
    return markup
