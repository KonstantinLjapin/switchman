from pydantic_settings import BaseSettings, SettingsConfigDict


class SettingsEnvPath(BaseSettings):
    env_path: str



env_bot = SettingsEnvPath()
