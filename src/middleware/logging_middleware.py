from telebot.async_telebot import AsyncTeleBot
from telebot import asyncio_handler_backends

#TODO add sech the time

class LoggingMiddleware(asyncio_handler_backends.BaseMiddleware):
    def __init__(self, logger):
        self.logger = logger
        self.update_types = ['message']  # Update types that will be handled by this middleware.
    async def pre_process(self, message, data):
        data['logger'] = self.logger
    async def post_process(self, message, data, exception):
        if exception:  # You can get exception occured in handler.
            self.logger.exception(str(exception))


async def register_log_middleware(bot: AsyncTeleBot, logger):
    bot.setup_middleware(LoggingMiddleware(logger))
