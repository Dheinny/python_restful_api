# -*- coding: utf-8 -*-

from flask_restful import Api, Resource

from apps.store.resources.client_resources import ClientCollection, ClientItem
from apps.store.resources.product_resources import ProductCollection, ProductItem
from apps.store.resources.order_resources import OrderCollection, OrderItem

class Index(Resource):

    def get(self):
        return {"hello": "Welcome to our virtual store"}

api = Api()

def configure_api(app):
    api.add_resource(Index, "/")

    api.add_resource(ClientCollection, "/clients" )
    api.add_resource(ClientItem, "/clients/<string:client_id>")

    api.add_resource(ProductCollection, "/products")
    api.add_resource(ProductItem, "/products/<string:cod_prod>")

    api.add_resource(OrderCollection, "/orders")
    api.add_resource(OrderItem, "/orders/<string:order_id>")

    api.init_app(app)

