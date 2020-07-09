# _*_ coding: utf-8 _*_

#Python
from os import getenv

class Config:
    SECRET_KEY = getenv("SECRET_KEY")
    APP_PORT = int(getenv("APP_PORT"))
    DEBUG = eval(getenv("DEBUG").title())

class DevelopmentConfig(Config):
    FLASK_ENV = "development"
    DEBUG = True

class TestingConfig(Config):
    FLASK_ENV = "testing"
    TESTING = True

config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "default": DevelopmentConfig
}
