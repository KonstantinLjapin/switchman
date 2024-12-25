from telebot import types
from telebot.async_telebot import AsyncTeleBot
from telebot.asyncio_filters import AdvancedCustomFilter
from telebot.callback_data import CallbackData, CallbackDataFilter


calendar_factory = CallbackData("year", "month", prefix="calendar")


class CalendarCallbackFilter(AdvancedCustomFilter):
    key = 'calendar'

    async def check(self, call: types.CallbackQuery, config: CallbackDataFilter):
        return config.check(query=call)


def bind_filters(bot: AsyncTeleBot):
    bot.add_custom_filter(CalendarCallbackFilter())
