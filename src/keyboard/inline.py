from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from utils.calendar_worker import day_status


async def gen_mount_markup(days_bundle: list):
    markup = InlineKeyboardMarkup()
    markup.row_width = 3
    for day in days_bundle:
        status: str = await day_status(day)
        markup.add(InlineKeyboardButton(status, callback_data="cb_yes"))
    return markup
