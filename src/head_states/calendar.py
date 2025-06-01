from telebot.states import State, StatesGroup


class Calendar(StatesGroup):
    month = State()

