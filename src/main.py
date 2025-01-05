from core.bot import bot
import asyncio
from custom_handlers.message import register_custom_message_handlers
from custom_handlers.callback import register_custom_callback_query_handlers
from filters.calendar import bind_calendar_filters
from filters.simpl import bind_filters

bind_calendar_filters(bot)
bind_filters(bot)
register_custom_message_handlers(bot)
register_custom_callback_query_handlers(bot)
print("Starting bot")
asyncio.run(bot.polling())
