import logging
import ssl
import asyncio
from aiohttp import web
import telebot
from .config import SettingsBot


async def setup(settings, shutdown, handle):
    # Remove webhook, it fails sometimes the set if there is a previous webhook
    app = web.Application()
    app.router.add_post('/{}/'.format(settings.bot_token), handle)
    app.on_cleanup.append(shutdown)
    return app
