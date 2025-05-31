from telebot.async_telebot import AsyncTeleBot
from telebot import asyncio_handler_backends
from telebot.types import Message, CallbackQuery
import time


class LoggingMiddleware(asyncio_handler_backends.BaseMiddleware):

    def __init__(self, logger):
        self.logger = logger
        self.update_types = ['message', 'callback_query']

    async def pre_process(self, message: Message | CallbackQuery, data: dict):
        data['logger'] = self.logger
        data['start_time'] = time.time()

    async def post_process(self, message: Message | CallbackQuery, data: dict, exception):
        execution_time = time.time() - data['start_time']

        if exception:
            self.logger.exception(f"Exception after {execution_time:.3f} seconds: {str(exception)}")
        else:
            if isinstance(message, CallbackQuery):
                # Логирование для CallbackQuery
                self.logger.info(f" || {message.__class__.__name__}"
                                 f" || user {message.from_user.full_name}"
                                 f" || id {str(message.from_user.id)}"
                                 f" || data {message.data}"
                                 f" || execution {execution_time:.3f} sec")
            elif int(message.chat.id) > 0:
                # Логирование для личных сообщений
                self.logger.info(f" || {message.__class__.__name__}"
                                 f" || user {message.from_user.full_name}"
                                 f" || id {str(message.from_user.id)}"
                                 f" || chat_id {str(message.chat.id)}"
                                 f" || execution {execution_time:.3f} sec")
            else:
                # Логирование для групповых чатов
                self.logger.info(f" || {message.__class__.__name__}"
                                 f" || group_name {message.chat.username}"
                                 f" || user {message.from_user.full_name}"
                                 f" || id {str(message.from_user.id)}"
                                 f" || chat_id {str(message.chat.id)}"
                                 f" || execution {execution_time:.3f} sec")


async def register_log_middleware(bot: AsyncTeleBot, logger):
    bot.setup_middleware(LoggingMiddleware(logger))
