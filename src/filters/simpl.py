from telebot import types
from telebot.async_telebot import AsyncTeleBot
from telebot.asyncio_filters import AdvancedCustomFilter
from telebot.callback_data import CallbackData, CallbackDataFilter


simpl_factory = CallbackData(prefix="simpl1234")


class SimplCallbackFilter(AdvancedCustomFilter):
    key = 'config'

    async def check(self, call: types.CallbackQuery, config: CallbackDataFilter):
        print("Filter  simpl called")
        return config.check(query=call)


def bind_filters(bot: AsyncTeleBot):
    bot.add_custom_filter(SimplCallbackFilter())
