from telebot.async_telebot import AsyncTeleBot
from telebot.types import CallbackQuery
from filters.filters import calendar_factory

 # TODO register filter

async def calendar_action_handler(call: CallbackQuery, bot: AsyncTeleBot):

    await bot.send_message(call.from_user.id, text='all_button')


async def echo_callback_query(call: CallbackQuery, bot: AsyncTeleBot) -> None:
    await bot.answer_callback_query(call.from_user.id, text='all_echo')


def register_custom_callback_query_handlers(bot: AsyncTeleBot):
    bot.register_callback_query_handler(calendar_action_handler, func=lambda call: True,
                                        pass_bot=True)
    bot.register_callback_query_handler(echo_callback_query, func=lambda call: True,
                                        pass_bot=True)

