import ssl
import asyncio
from aiohttp import web
import logging
import telebot
from telebot.async_telebot import AsyncTeleBot

from core.bot import bot
from core.log_config import loger
from core.config import SettingsBot, bot_settings
from core.aiohttp_web_hook import setup

from custom_handlers.group.message import register_chat_custom_message_handlers
from custom_handlers.private.message import register_custom_message_handlers
from custom_handlers.private.callback import register_custom_private_callback_query_handlers
from custom_handlers.group.callback import register_custom_group_callback_query_handlers

from telebot.types import BotCommand
from middleware.logging_middleware import register_log_middleware
from filters.chat_type import register_message_filters
from filters.call import register_callback_filters


async def register_handlers(bot: AsyncTeleBot) -> None:
    register_chat_custom_message_handlers(bot)
    register_custom_message_handlers(bot)
    register_custom_private_callback_query_handlers(bot)
    register_custom_group_callback_query_handlers(bot)
    await bot.set_my_commands(
        commands=[
            BotCommand("start", "начало работы с ботом вызывает описание проекта"),
            BotCommand("this_day_is",
                       "даёт ответ на вопрос: рабочий ли день по рабочему календарю?"),
            BotCommand("this_mount_is",
                       "даёт ответ на вопрос: какие дни в текущим месяце 🟢 рабочие, какие 🔴 выходные?"),
            BotCommand("this_year_is",
                       "даёт информацию на выбор 12 месяцев текущего года ")
        ],
    )


async def registration(bot_instance: AsyncTeleBot, loger: logging, settings: SettingsBot):
    loger.info("Starting bot")
    # await register_middleware(bot_instance)
    await register_log_middleware(bot_instance, loger)
    await register_message_filters(bot_instance, loger)
    await register_callback_filters(bot_instance, loger)
    await register_handlers(bot_instance)


if __name__ == '__main__':
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.load_cert_chain(bot_settings.webhook_ssl_cert, bot_settings.webhook_ssl_priv)
    asyncio.run(registration(bot_instance=bot, loger=loger, settings=bot_settings))
    web.run_app(
        setup(bot_instance=bot, settings=bot_settings),
        host=bot_settings.webhook_listen,
        port=bot_settings.webhook_port,
        ssl_context=context,
    )
