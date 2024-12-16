from telebot.async_telebot import AsyncTeleBot
from telebot.types import CallbackQuery

async def this_mount_message(message: Message, bot: AsyncTeleBot) -> None:
    # TODO rewrite to callback
    mount_bundle: list = await mounts_bundle(await this_month("2024", "12"))
async def echo_callback_query(call: CallbackQuery, bot: AsyncTeleBot) -> None:
    await bot.answer_callback_query(call.id, text='all')


def register_custom_callback_query_handlers(bot: AsyncTeleBot):
    bot.register_callback_query_handler(echo_callback_query, func=lambda call: True, pass_bot=True)
