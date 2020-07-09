# -*- coding: utf-8 -*-

from flask_restful import Api, Resource

from apps.store.resources import CreateClient

class Index(Resource):

    def get(self):
        return {"hello": "world by apps"}

api = Api()

def configure_api(app):
    api.add_resource(Index, "/")

    api.add_resource(CreateClient, "/clients")

    api.init_app(app)

