from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message, BotCommand
from static.dictionary import greeting_text
from utils.requests_pack import this_day
from utils.calendar_worker import day_status, month_status
from logging import Logger
# TODO write head_states


async def start_message(message: Message, bot: AsyncTeleBot) -> None:
    """"Хендлер приветственное соообщение с описанием возможностей:
        # TODO заполнить
        """
    user_name = message.from_user.full_name
    text = await greeting_text(user_name)
    await bot.send_message(message.chat.id, text=text)


async def this_day_is(message: Message, bot: AsyncTeleBot, logger: Logger) -> None:
    status: str = await day_status(await this_day(logger))
    await bot.send_message(message.chat.id, text=status)
logger: Logger


async def this_mount_is(message: Message, bot: AsyncTeleBot, logger: Logger) -> None:
    status: str = await month_status(logger)
    await bot.send_message(message.chat.id, text=status)


async def echo_message(message, bot: AsyncTeleBot) -> None:
    await bot.reply_to(message, message.text)
    await bot.send_message(message.chat.id, "echo all message")


def register_chat_custom_message_handlers(bot: AsyncTeleBot):
    bot.register_message_handler(start_message, commands=["start"], pass_bot=True)
    bot.register_message_handler(this_day_is, commands=["this_day_is"], pass_bot=True)
    bot.register_message_handler(this_mount_is, commands=["this_mount_is"], pass_bot=True)
    #bot.register_message_handler(echo_message, func=lambda message: True, pass_bot=True)
