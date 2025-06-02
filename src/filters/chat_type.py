from telebot import types
from telebot.asyncio_filters import AdvancedCustomFilter


class IsGroup(AdvancedCustomFilter):
    """
    Фильтр для проверки групповых чатов (обычных и супергрупп).
    При использовании нескольких фильтров они выполняются последовательно в порядке регистрации.

    Пример использования:
    @bot.message_handler(is_group=True)  # Только для групповых чатов
    async def group_handler(message): ...

    Attributes:
        key (str): Ключ фильтра для использования в декораторах
        logger: Логгер для записи событий (опционально)

    Note:
        Фильтры в pyTelegramBotAPI работают как AND условия - все указанные фильтры должны вернуть True
    """
    key = 'is_group'

    def __init__(self, logger):
        """
        Инициализация фильтра с логгером

        Args:
            logger: Объект логгера для записи событий
        """
        self.logger = logger

    async def check(self, message: types.Message, text: str) -> bool:
        """
        Проверяет, является ли чат групповым

        Args:
            message: Объект сообщения Telegram
            text: Текст, переданный в фильтр (не используется)

        Returns:
            bool: True если чат является группой или супергруппой
        """
        if self.logger:
            self.logger.info(f"Group check for chat {message.chat.id}")
        return message.chat.type in ['group', 'supergroup']


class IsPrivate(AdvancedCustomFilter):
    """
    Фильтр для проверки личных сообщений.
    Фильтры выполняются в порядке их указания в декораторе @bot.message_handler.

    Примеры:
    1. Только личные сообщения:
    @bot.message_handler(is_private=True)

    2. Комбинация фильтров (личные сообщения с командой):
    @bot.message_handler(commands=['start'], is_private=True)

    Note:
        Порядок выполнения фильтров:
        1. Сначала проверяются фильтры в декораторе (слева направо)
        2. Затем вызывается обработчик сообщения
    """
    key = 'is_private'

    def __init__(self, logger):
        """
        Инициализация фильтра для личных сообщений

        Args:
            logger: Объект логгера для записи событий
        """
        self.logger = logger

    async def check(self, message: types.Message, text: str) -> bool:
        """
        Проверяет, является ли чат личным сообщением

        Args:
            message: Объект сообщения Telegram
            text: Дополнительный текст для фильтра (не используется)

        Returns:
            bool: True если это личное сообщение
        """
        if self.logger:
            self.logger.info(f"Private chat check for user {message.from_user.id}")
        return message.chat.type == 'private'


async def register_message_filters(bot, logger):
    bot.add_custom_filter(IsPrivate(logger))
    bot.add_custom_filter(IsGroup(logger))
