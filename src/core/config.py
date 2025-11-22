from pydantic_settings import BaseSettings, SettingsConfigDict


class SettingsEnvPath(BaseSettings):
    env_path: str


class SettingsBot(BaseSettings):
    bot_token: str         # '<api_token>'
    webhook_host: str      # '<ip/host where the bot is running>'
    webhook_port: int      # 8443  # 443, 80, 88 or 8443 (port need to be 'open')
    webhook_listen: str    # '0.0.0.0'  # in some vps you may need to put here the ip addr
    webhook_ssl_cert: str  # './webhook_cert.pem'  # path to the ssl certificate
    webhook_ssl_priv: str  # './webhook_pkey.pem'  # path to the ssl private key
    webhook_url_base: str  # "https://{}:{}".format(webhook_host, webhook_port)
    webhook_url_path: str  # "/{}/".format(api_token)

    model_config = SettingsConfigDict(env_file=SettingsEnvPath().env_path)


bot_settings: SettingsBot = SettingsBot()
env_bot = SettingsEnvPath()
