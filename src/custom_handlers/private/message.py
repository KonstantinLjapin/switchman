from datetime import datetime
from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message
from static.dictionary import greeting_text
from utils.requests_pack import this_day
from utils.calendar_worker import day_status, month_status
from keyboard.inline import gen_markup
from logging import Logger
import asyncio


async def start_message(message: Message, bot: AsyncTeleBot, logger: Logger) -> None:
    """"Хендлер приветственное соообщение с описанием возможностей:"""
    logger.info(f" || {message.__class__.__name__}"
                f" || user {message.from_user.full_name}"
                f" || id {str(message.from_user.id)}"
                f" || chat_id {str(message.chat.id)}")
    user_name = message.from_user.full_name
    text = await greeting_text(user_name)
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
    msg: Message = await bot.send_message(chat_id=message.from_user.id, text=text)
    await asyncio.sleep(60)
    await bot.delete_message(chat_id=message.from_user.id, message_id=msg.message_id)


async def this_day_is(message: Message, bot: AsyncTeleBot, logger: Logger) -> None:
    status: str = await day_status(await this_day(logger))
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
    msg: Message = await bot.send_message(message.from_user.id, text=status)
    await asyncio.sleep(60)
    await bot.delete_message(chat_id=message.from_user.id, message_id=msg.message_id)


async def this_mount_is(message: Message, bot: AsyncTeleBot, logger: Logger) -> None:
    today = datetime.now()
    status: str = await month_status(month=today.month, logger=logger)
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)
    msg: Message = await bot.send_message(message.from_user.id, text=status)
    await asyncio.sleep(60)
    await bot.delete_message(chat_id=message.from_user.id, message_id=msg.message_id)


async def this_year_is(message: Message, bot: AsyncTeleBot, logger: Logger) -> None:
    await bot.send_message(chat_id=message.from_user.id, text="Все дни для:", reply_markup=gen_markup())
    await bot.delete_message(chat_id=message.from_user.id, message_id=message.message_id)


async def echo_message(message, bot: AsyncTeleBot, logger: Logger) -> None:
    await bot.send_message(message.chat.id, "echo private message")


def register_custom_message_handlers(bot: AsyncTeleBot):
    bot.register_message_handler(
        start_message,
        commands=["start"],
        pass_bot=True,
        is_private=True,
        state=None
    )
    bot.register_message_handler(
        this_day_is,
        commands=["this_day_is"],
        pass_bot=True,
        is_private=True,
        state=None
    )
    bot.register_message_handler(
        this_mount_is,
        commands=["this_mount_is"],
        pass_bot=True,
        is_private=True,
        state=None
    )

    # Хендлер с состоянием (без state=None!)
    bot.register_message_handler(
        this_year_is,
        commands=["this_year_is"],
        pass_bot=True,
        is_private=True
    )

    # Эхо-хендлер только для сообщений без состояния
    bot.register_message_handler(
        echo_message,
        func=lambda message: True,
        pass_bot=True,
        is_private=True,
        state=None  # Явно указываем "без состояния"
    )
