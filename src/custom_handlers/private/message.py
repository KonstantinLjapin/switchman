from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message
from telebot.states.asyncio.context import StateContext
from static.dictionary import greeting_text
from utils.requests_pack import this_day
from utils.calendar_worker import day_status, month_status
from head_states.calendar import Calendar
from keyboard.inline import gen_markup
from logging import Logger


async def start_message(message: Message, bot: AsyncTeleBot) -> None:
    """"Хендлер приветственное соообщение с описанием возможностей:
        # TODO заполнить
        """
    user_name = message.from_user.full_name
    text = await greeting_text(user_name)
    await bot.send_message(message.from_user.id, text=text)


async def this_day_is(message: Message, bot: AsyncTeleBot, logger: Logger) -> None:
    status: str = await day_status(await this_day(logger))
    await bot.send_message(message.from_user.id, text=status)


async def this_mount_is(message: Message, bot: AsyncTeleBot, logger: Logger) -> None:
    status: str = await month_status(logger)
    await bot.send_message(message.from_user.id, text=status)


async def this_year_is(message: Message, bot: AsyncTeleBot, logger: Logger) -> None:
    logger.debug(f"состояние до {await bot.get_state(user_id=message.from_user.id)}")
    await bot.set_state(user_id=message.from_user.id, state=Calendar.month)
    logger.debug(f"состояние после {await bot.get_state(user_id=message.from_user.id)}")
    await bot.send_message(chat_id=message.from_user.id, text="Все дни для:", reply_markup=gen_markup())


async def echo_message(message, bot: AsyncTeleBot) -> None:
    await bot.reply_to(message, message.text)
    await bot.send_message(message.chat.id, "echo private message")


def register_custom_message_handlers(bot: AsyncTeleBot):
    # Основные хендлеры без состояний
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
