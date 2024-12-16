from telebot.async_telebot import AsyncTeleBot
from telebot.types import Message
from static.dictionary import greeting_text
from utils.requests_pack import this_day, this_month
from utils.calendar_worker import day_status, mounts_bundle
from keyboard.inline import gen_mount_markup

# TODO write state and middleware

async def start_message(message: Message, bot: AsyncTeleBot) -> None:
    """"Хендлер приветственное соообщение с описанием возможностей:
        # TODO заполнить
        """
    user_name = message.from_user.full_name
    text = await greeting_text(user_name)
    await bot.send_message(message.from_user.id, text=text)


async def this_day_is_message(message: Message, bot: AsyncTeleBot) -> None:
    status: str = await day_status(await this_day())
    await bot.send_message(message.from_user.id, text=status)


async def echo_message(message, bot: AsyncTeleBot) -> None:
    await bot.reply_to(message, message.text)


def register_custom_message_handlers(bot: AsyncTeleBot):
    bot.register_message_handler(start_message, commands=["start"], pass_bot=True)
    bot.register_message_handler(this_day_is_message, commands=["this_day"], pass_bot=True)
    bot.register_message_handler(echo_message, func=lambda message: True, pass_bot=True)
