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


async def handle(request):
    if request.match_info.get('token') == bot.token:
        request_body_dict = await request.json()
        update = telebot.types.Update.de_json(request_body_dict)
        asyncio.ensure_future(bot.process_new_updates([update]))
        return web.Response()
    else:
        return web.Response(status=403)


async def shutdown(app):
    loger.info('Shutting down: removing webhook')
    await bot.remove_webhook()
    loger.info('Shutting down: closing session')
    await bot.close_session()


async def setup():
    # Remove webhook, it fails sometimes the set if there is a previous webhook
    loger.info('Starting up: removing old webhook')
    await bot.remove_webhook()
    # Set webhook
    loger.info('Starting up: setting webhook')
    await bot.set_webhook(
        url=bot_settings.webhook_url_base.format(bot_settings.webhook_host, bot_settings.webhook_port)
        + bot_settings.webhook_url_path,
        certificate=open(bot_settings.webhook_ssl_cert, 'r')
    )
    app = web.Application()
    app.router.add_post('/{token}/', handle)
    app.on_cleanup.append(shutdown)
    return app


if __name__ == '__main__':
    asyncio.run(registration(bot, loger))
    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.load_cert_chain(bot_settings.webhook_ssl_cert, bot_settings.webhook_ssl_priv)
    # Start aiohttp server
    web.run_app(
        setup(),
        host=bot_settings.webhook_listen,
        port=bot_settings.webhook_port,
        ssl_context=context,
    )
