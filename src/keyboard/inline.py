from typing import Union, Optional

from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def gen_markup():
    markup = InlineKeyboardMarkup()
    buttons = []
    for i in range(1, 13):
        buttons.append(InlineKeyboardButton(text=str(i), callback_data=f"mount_{i}"))
        if i % 3 == 0 or i == 12:
            markup.row(*buttons)
            buttons = []
    return markup
