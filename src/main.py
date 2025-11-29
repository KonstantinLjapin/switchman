
import ssl
import asyncio
from aiohttp import web
import telebot

from core.bot import bot
from core.config import env_bot, bot_settings
from core.log_config import loger

from custom_handlers.group.message import register_chat_custom_message_handlers
from custom_handlers.private.message import register_custom_message_handlers
from custom_handlers.private.callback import register_custom_private_callback_query_handlers
from custom_handlers.group.callback import register_custom_group_callback_query_handlers

from telebot.types import BotCommand
from middleware.logging_middleware import register_log_middleware
from filters.chat_type import register_message_filters
from filters.call import register_callback_filters
from core.aiohttp_web_hook import run_bot_hooks
from core.config import bot_settings
async def register_handlers(bot):
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


async def registration(bot, loger):
    loger.info("Starting bot")
    #await register_middleware(bot)
    await register_log_middleware(bot, loger)
    await register_message_filters(bot, loger)
    await register_callback_filters(bot, loger)
    await register_handlers(bot)


if __name__ == '__main__':
    asyncio.run(registration(bot, loger))
    asyncio.run(run_bot_hooks(bot, loger, bot_settings))
