from configlib import BaseConfig


class Config(BaseConfig):
    name: str
    password: str
    channel: str


config = Config.get_instance()
