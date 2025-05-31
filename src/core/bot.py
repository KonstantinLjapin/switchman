from telebot.async_telebot import AsyncTeleBot
from core.config import bot_settings
from telebot.asyncio_storage import StateMemoryStorage

state_storage = StateMemoryStorage()

bot = AsyncTeleBot(token=bot_settings.bot_token, state_storage=state_storage)
