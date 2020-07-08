# _*_ coding: utf-8 _*_

from flask import Flask
from config import config

def create_app(config_name="default"):
    app = Flask('api-ecomm')

    app.config.from_object(config[config_name])

    return app 
