from telebot.async_telebot import AsyncTeleBot
from core.config import bot_settings


bot = AsyncTeleBot(token=bot_settings.bot_token)
