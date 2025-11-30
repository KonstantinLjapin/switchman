import asyncio
from aiohttp import web
import telebot
from aiohttp.web import Request


async def handle(request: Request):
    bot_instance = request.app['bot_instance']
    if request.match_info.get('token') == bot_instance.token:
        request_body_dict = await request.json()
        update = telebot.types.Update.de_json(request_body_dict)
        asyncio.ensure_future(bot_instance.process_new_updates([update]))
        return web.Response()
    else:
        return web.Response(status=403)
