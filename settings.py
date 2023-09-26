from pydantic_settings import BaseSettings


class BotSettings(BaseSettings):
    TOKEN_TG: str
    TOKEN_DIS: str


bot_settings = BotSettings()

