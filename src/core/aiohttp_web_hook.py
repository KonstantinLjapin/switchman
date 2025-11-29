import logging
import ssl
import asyncio
from aiohttp import web
import telebot
from config import SettingsBot


async def run_bot_hooks(bot, logger: logging, settings: SettingsBot):
    async def handle(request):
        if request.match_info.get('token') == bot.token:
            request_body_dict = await request.json()
            update = telebot.types.Update.de_json(request_body_dict)
            asyncio.ensure_future(bot.process_new_updates([update]))
            return web.Response()
        else:
            return web.Response(status=403)

    async def shutdown(app):
        logger.info('Shutting down: removing webhook')
        await bot.remove_webhook()
        logger.info('Shutting down: closing session')
        await bot.close_session()

    async def setup():
        # Remove webhook, it fails sometimes the set if there is a previous webhook
        logger.info('Starting up: removing old webhook')
        await bot.remove_webhook()
        # Set webhook
        logger.info('Starting up: setting webhook')
        await bot.set_webhook(url=settings.webhook_url_base + settings.webhook_url_path,
                              certificate=open(settings.webhook_ssl_cert, 'r'))
        app = web.Application()
        app.router.add_post('/{}/'.format(settings.bot_token), handle)
        app.on_cleanup.append(shutdown)
        return app

    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    context.load_cert_chain(settings.webhook_ssl_cert, settings.webhook_ssl_priv)
    # Start aiohttp server
    web.run_app(
        setup(),
        host=settings.webhook_listen,
        port=settings.webhook_port,
        ssl_context=context,
    )
