# _*_ coding: utf-8 _*_

from flask import Flask
from config import config

from .api import configure_api

def create_app(config_name="default"):
    app = Flask('api-ecomm')

    app.config.from_object(config[config_name])
    
    configure_api(app)

    return app 
