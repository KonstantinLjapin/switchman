from telebot.async_telebot import AsyncTeleBot
from telebot.types import CallbackQuery
from head_states.calendar import Calendar


async def calendar_callback_query(call: CallbackQuery, bot: AsyncTeleBot) -> None:
    """Обработчик для callback-запросов в состоянии Calendar.month"""
    await bot.answer_callback_query(call.id, text='Обработка календаря')

    # Пример обработки данных
    month_number = int(call.data.split('_')[1])  # Извлекаем номер месяца
    print(f"Выбран месяц: {month_number}")

    # Ваша логика обработки календаря здесь...

    # Сбрасываем состояние после обработки
    await bot.set_state(call.from_user.id, state=None)


async def echo_callback_query(call: CallbackQuery, bot: AsyncTeleBot) -> None:
    """Обработчик для callback-запросов без состояния"""
    current_state = await bot.get_state(call.from_user.id)
    print(f"Текущее состояние: {current_state}")

    await bot.answer_callback_query(call.id, text='Эхо-ответ')

    # Только для callback-запросов без активного состояния
    if not current_state:
        print("Обработка echo callback")


def register_custom_callback_query_handlers(bot: AsyncTeleBot):
    # 1. Обработчик для состояния Calendar.month
    bot.register_callback_query_handler(
        calendar_callback_query,
        func=lambda call: call.data.startswith('mount_'),  # Только наши callback'и
        pass_bot=True,
        state=Calendar.month  # Явно указываем состояние!
    )

    # 2. Общий обработчик ТОЛЬКО когда нет состояния
    bot.register_callback_query_handler(
        echo_callback_query,
        func=lambda call: True,
        pass_bot=True,
        state=None  # Явно указываем "без состояния"
    )
