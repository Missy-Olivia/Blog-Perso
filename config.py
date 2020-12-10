import os

class Config:


class TestConfig(Config):


class ProdConfig(Config):
    pass

class DevConfig(Config):

    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}