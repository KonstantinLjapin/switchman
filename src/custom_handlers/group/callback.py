
from telebot.async_telebot import AsyncTeleBot
from telebot.types import CallbackQuery

# TODO select handlers group


async def calendar_action_handler(call: CallbackQuery, bot: AsyncTeleBot):
    await bot.send_message(call.id, text='calendar_all_button')


async def simpl_callback_query(call: CallbackQuery, bot: AsyncTeleBot) -> None:
    await bot.answer_callback_query(call.id, text='simpl_callback')


async def echo_callback_query(call: CallbackQuery, bot: AsyncTeleBot) -> None:
    await bot.answer_callback_query(call.id, text='all_echo')


def register_custom_callback_query_handlers(bot: AsyncTeleBot):
    """bot.register_callback_query_handler(simpl_callback_query, func=None,
                                        pass_bot=True)
    bot.register_callback_query_handler(calendar_action_handler, func=None,
                                        pass_bot=True)

    bot.register_callback_query_handler(echo_callback_query, func=lambda call: True,
                                        pass_bot=True)"""
