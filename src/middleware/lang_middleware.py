import telebot
from telebot.async_telebot import AsyncTeleBot
from telebot import asyncio_handler_backends
import logging

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)  # Outputs debug messages to console.

TRANSLATIONS = {
    'hello': {
        'en': 'hello',
        'ru': 'привет',
        'uz': 'salom'
    }
}


class LanguageMiddleware(asyncio_handler_backends.BaseMiddleware):
    def __init__(self):
        self.update_types = ['message']  # Update types that will be handled by this middleware.

    async def pre_process(self, message, data):
        data['response'] = TRANSLATIONS['hello'][message.from_user.language_code]

    async def post_process(self, message, data, exception):
        if exception:  # You can get exception occured in handler.
            logger.exception(str(exception))


async def register_middleware(bot: AsyncTeleBot):
    bot.setup_middleware(LanguageMiddleware())
