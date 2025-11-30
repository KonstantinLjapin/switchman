import asyncio

from aiohttp import web
from aiohttp.web import Request

import telebot
from telebot.async_telebot import AsyncTeleBot

from core.config import SettingsBot


async def handle(request: Request):
    bot_instance = request.app['bot_instance']
    if request.match_info.get('token') == bot_instance.token:
        request_body_dict = await request.json()
        update = telebot.types.Update.de_json(request_body_dict)
        asyncio.ensure_future(bot_instance.process_new_updates([update]))
        return web.Response()
    else:
        return web.Response(status=403)


async def shutdown(app):
    bot_instance = app['bot_instance']
    await bot_instance.remove_webhook()
    await bot_instance.close_session()


async def setup(bot_instance: AsyncTeleBot, settings: SettingsBot):
    # Remove webhook, it fails sometimes the set if there is a previous webhook
    app = web.Application()
    app.router.add_post('/{token}/', handle)
    app.on_cleanup.append(shutdown)
    app['bot_instance'] = bot_instance
    app['bot_settings'] = settings
    return app
