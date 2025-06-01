import calendar
from utils.calendar_worker import keyboard_set_ru
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def gen_markup() -> InlineKeyboardMarkup:
    """
    Генерирует клавиатуру с кнопками месяцев, расположенными по 3 в ряд.
    Использует названия месяцев из модуля calendar.

    Returns:
        InlineKeyboardMarkup: Клавиатура с 12 кнопками месяцев (3x4)

    """
    keyboard_set_ru()
    markup = InlineKeyboardMarkup()
    buttons = []
    for month_num in range(1, 13):
        # Получаем название месяца (полная форма)
        month_name = calendar.month_name[month_num]
        # Создаем кнопку с названием месяца
        buttons.append(
            InlineKeyboardButton(
                text=month_name,
                callback_data=f"mount_{month_num}"
            )
        )

        # Формируем ряды по 3 кнопки
        if month_num % 3 == 0 or month_num == 12:
            markup.row(*buttons)
            buttons = []

    return markup
