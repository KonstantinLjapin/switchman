from pydantic_settings import BaseSettings


class SettingsBot(BaseSettings):
    bot_token: str


bot_settings: SettingsBot = SettingsBot()

