from telebot.async_telebot import AsyncTeleBot
from telebot.types import CallbackQuery


async def echo_callback_query(call: CallbackQuery, bot: AsyncTeleBot) -> None:
    await bot.answer_callback_query(call.id, text='all_echo')


def register_custom_callback_query_handlers(bot: AsyncTeleBot):
    bot.register_callback_query_handler(echo_callback_query, func=lambda call: True, pass_bot=True)
