from telebot.async_telebot import AsyncTeleBot
from telebot.types import CallbackQuery, Message
from utils.calendar_worker import month_status
from logging import Logger
import asyncio

async def calendar_callback_query(call: CallbackQuery, bot: AsyncTeleBot, logger: Logger) -> None:
    """Обработчик для callback-запросов в состоянии Calendar.month"""
    month_number = int(call.data.split('_')[1])  # Извлекаем номер месяца
    status: str = await month_status(month=month_number, logger=logger)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.id)
    msg: Message = await bot.send_message(call.message.chat.id, text=status)
    await asyncio.sleep(60)
    await bot.delete_message(chat_id=call.message.chat.id, message_id=msg.message_id)


async def echo_callback_query(call: CallbackQuery, bot: AsyncTeleBot) -> None:
    """Обработчик для callback-запросов без состояния"""
    await bot.answer_callback_query(call.id, text='Эхо-ответ')
    await bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.id)


def register_custom_group_callback_query_handlers(bot: AsyncTeleBot):
    # 1. Обработчик для состояния Calendar.month
    bot.register_callback_query_handler(
        calendar_callback_query,
        func=lambda call: call.data.startswith('mount_'),  # Только наши callback'и
        pass_bot=True, is_group_callback=True, state=None
    )

    # 2. Общий обработчик ТОЛЬКО когда нет состояния
    bot.register_callback_query_handler(
        echo_callback_query,
        func=lambda call: True,
        pass_bot=True, is_group_callback=True, state=None
    )
