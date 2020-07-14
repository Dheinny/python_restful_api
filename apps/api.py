# -*- coding: utf-8 -*-

from flask_restful import Api, Resource

from apps.store.resources import ClientCollection, ClientItem

class Index(Resource):

    def get(self):
        return {"hello": "world by apps"}

api = Api()

def configure_api(app):
    api.add_resource(Index, "/")

    api.add_resource(ClientCollection, "/clients" )
    api.add_resource(ClientItem, "/clients/<string:user_id>")

    api.init_app(app)

