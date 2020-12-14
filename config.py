import os

class Config:
    SECRET_KEY = '12345'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://missy:yeet@localhost/test_blog'


class ProdConfig(Config):
    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://missy:yeet@localhost/blog'
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}