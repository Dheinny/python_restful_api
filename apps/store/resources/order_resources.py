# _*_ coding: UTF-8 _*_

import json
from math import ceil

from flask import request
from flask_restful import Resource

from mongoengine.errors import FieldDoesNotExist

import werkzeug.exceptions as wzg

from apps.responses import *

from apps.messages import *

from apps.store.models import (
    Client, Product, Order
)

from apps.store.schemas import (
    ClientSchema, ProductSchema, OrderSchema,
    ReqOrderSchema
)

class OrderCollection(Resource):

    def post(self, *args, **kwargs):
        req_data = request.get_json() or None
        data, errors, result = None, None, None

        if req_data is None:
            return resp_data_invalid("Order", [], msg=MSG_NO_DATA)

        try:
            request_schema = ReqOrderSchema()
            data = request_schema.load(req_data)

            print(data)
            client_id = data["client_id"]
            data.pop("client_id")
            client = Client.objects.get(id=client_id)


            order = Order(**data)
            order.client = client

            order.save()

            order_schema = OrderSchema()
            result = order_schema.dump(order)

            return resp_ok("Order", "Order registred with success!", data=result)

        except Exception as e:
            return resp_exception("Order", "An error occurred: {}".format(e))

    def get(self):
        schema = OrderSchema(many=True)
        args = request.args
        page_id = int(args.get("page", 1))
        page_size = int(args.get("page_size", 10))\
            if int(args.get("page_size", 10)) >= 1 else 10

        try:
            orders = Order.objects()
            count = orders.count()
            print(schema.dump(orders))
            if count == 0:
                return resp_does_not_exist("Order", "order", msg=MSG_NO_RESOURCE_REGISTERED)

            if count <= ((page_id - 1) * page_size):
                page_id = ceil(count / page_size)

            orders = orders.paginate(page_id, page_size)

        except FieldDoesNotExist as e:
            return resp_exception("Order", description=e.__str__())

        except wzg.NotFound:
            return resp_does_not_exist("Order", "pagination")

        except Exception as e:
            return resp_exception("Order", description=e.__str__())

        extra = {
            "page": orders.page, "pages": orders.pages, "total": orders.total,
            "params": {"page_size": page_size}
        }

        result = schema.dump(orders.items)

        return resp_ok(
            "Products", MSG_RESOURCE_FETCHED_PAGINATED.format("Orders"),
            data=result, **extra
        )




