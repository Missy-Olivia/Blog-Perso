import os

class Config:
    SECRET_KEY = '12345'
    UPLOADED_PHOTOS_DEST ='app/static/pics'
    #  email config
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    # simple mde  config
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://missy:yeet@localhost/test_blog'


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://missy:yeet@localhost/blog'
    DEBUG = True

config_options = {
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}