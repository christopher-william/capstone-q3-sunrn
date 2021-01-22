from secrets import token_hex

from environs import Env

env = Env()


class Config:
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = token_hex(32)
    SECRET_KEY = token_hex(32)


class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = env.str('DATABASE_DEVELOP_URL')
    DEBUG = True


class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = env.str('DATABASE_TEST_URL')
    TESTING = True


class ProductionConfig(Config):
    ENV = 'production'
    SQLALCHEMY_DATABASE_URI = env.str('DATABASE_URL')
    JWT_SECRET_KEY = env.str('JWT_SECRET_KEY')
    SECRET_KEY = env.str('SECRET_KEY')
