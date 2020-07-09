# _*_ coding: utf-8 _*_

from flask import request

from flask_restful import Resource
from mongoengine.errors import NotUniqueError, ValidationError
from marshmallow.exceptions import ValidationError as ValidationErrorMarshmallow

from apps.responses import (
    resp_already_exists, resp_exception,
    resp_data_invalid, resp_ok
)

from apps.messages import(
    MSG_NO_DATA, MSG_RESOURCE_CREATED, MSG_INVALID_DATA
)

# Local
from .models import Client
from .schemas import ClientSchema, ProductSchema

class CreateClient(Resource):
    def post(self, *args, **kwargs):
        req_data = request.get_json() or None
        data, errors, result = None, None, None
        schema = ClientSchema()

        if req_data is None:
            return resp_data_invalid("Client", [], msg=MSG_NO_DATA)
        
        try:
            data = schema.load(req_data)
        except ValidationErrorMarshmallow as err:
            return resp_data_invalid("Client", err.messages)

        try:
            data["name"] = data["name"].title()
            data["email"] = data["email"].lower()

            model = Client(**data)
            model.save()

        except NotUniqueError:
            return resp_already_exists("Client", "client")

        except ValidationError as e:
            return resp_exception("Client", msg=MSG_INVALID_DATA, description=e)

        except Exception as e:
            return resp_exception("Client", description=e)

        result = schema.dump(model)

        return resp_ok(
                "Client", MSG_RESOURCE_CREATED.format("Client"))
