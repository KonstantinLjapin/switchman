from telebot import types
from telebot.asyncio_filters import AdvancedCustomFilter


class IsGroupCallback(AdvancedCustomFilter):
    """
    Фильтр для проверки callback-запросов из групповых чатов.
    """
    key = 'is_group_callback'

    def __init__(self, logger=None):
        self.logger = logger

    async def check(self, callback: types.CallbackQuery, text: str) -> bool:
        """
        Проверяет, пришел ли callback из группового чата.

        Args:
            callback: Объект callback-запроса Telegram
            text: Дополнительный текст (не используется)

        Returns:
            bool: True если callback из группы/супергруппы
        """
        if self.logger:
            self.logger.debug(f"Group callback check for chat {callback.message.chat.id}")
        return callback.message.chat.type in ['group', 'supergroup']


class IsPrivateCallback(AdvancedCustomFilter):
    """
    Фильтр для проверки callback-запросов из личных сообщений.
    """
    key = 'is_private_callback'

    def __init__(self, logger=None):
        self.logger = logger

    async def check(self, callback: types.CallbackQuery, text: str) -> bool:
        """
        Проверяет, пришел ли callback из личного чата.

        Args:
            callback: Объект callback-запроса
            text: Дополнительный текст (не используется)

        Returns:
            bool: True если callback из личного чата
        """
        if self.logger:
            self.logger.debug(f"Private callback check for user {callback.from_user.id}")
        return callback.message.chat.type == 'private'


async def register_callback_filters(bot, logger):
    bot.add_custom_filter(IsGroupCallback(logger))
    bot.add_custom_filter(IsPrivateCallback(logger))


