from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message
from static.dictionary import greeting_text


async def start_message(message: Message, bot: AsyncTeleBot) -> None:
    user_name = message.from_user.full_name
    text = await greeting_text(user_name)
    await bot.send_message(message.from_user.id, text=text)


async def echo_message(message, bot: AsyncTeleBot) -> None:
    await bot.reply_to(message, message.text)


def register_custom_message_handlers(bot: AsyncTeleBot):
    bot.register_message_handler(start_message, commands=["start"], pass_bot=True)
    bot.register_message_handler(echo_message, func=lambda message: True, pass_bot=True)
