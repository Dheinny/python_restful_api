# _*_ coding: utf-8 _*_

from math import ceil

from flask import request

from flask_restful import Resource
from mongoengine.errors import (
    NotUniqueError, ValidationError, FieldDoesNotExist,
    DoesNotExist
)
from marshmallow.exceptions import ValidationError as ValidationErrorMarshmallow
import werkzeug.exceptions as wzg

from apps.responses import (
    resp_already_exists, resp_exception, resp_does_not_exist,
    resp_data_invalid, resp_ok
)

from apps.messages import(
    MSG_NO_DATA, MSG_RESOURCE_CREATED, MSG_INVALID_DATA,
    MSG_RESOURCE_FETCHED_PAGINATED, MSG_RESOURCE_FETCHED,
    MSG_RESOURCE_DELETED, MSG_NO_RESOURCE_REGISTERED
)

# Local
from .models import Client
from .schemas import ClientSchema, ProductSchema

class ClientCollection(Resource):
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
                "Client", MSG_RESOURCE_CREATED.format("Client"), data=result)

    def get(self):
        schema = ClientSchema(many=True)
        args = request.args
        page_id = int(args["page"]) if args.get("page") else 1
        page_size = 10
        if "page_size" in request.args:
            page_size = int(request.args.get("page_size"))
            page_size = 10 if page_size < 1 else page_size

        try: 
            clients = Client.objects()
            count = clients.count() 
            if count == 0:
                return resp_does_not_exist("Client", "client", msg=MSG_NO_RESOURCE_REGISTERED)

            if count <= ((page_id-1)*page_size):
                page_id = ceil(count/page_size)

            clients = clients.paginate(page_id, page_size)

        except FieldDoesNotExist as e:
            return resp_exception("Client", description=e.__str__())

        except wzg.NotFound:
            return resp_does_not_exist("Client", "pagination")

        except Exception as e:
            return resp_exception("Client", description=e.__str__())

        extra = {
            "page": clients.page, "pages": clients.pages, "total":clients.total,
            "params": {"page_size": page_size}
        }

        result = schema.dump(clients.items)

        return resp_ok(
            "Clients", MSG_RESOURCE_FETCHED_PAGINATED.format("Clients"),
            data=result, **extra
        )


class ClientItem(Resource):    
    def get(self, user_id):
        schema = ClientSchema()
        try:
            client = Client.objects.get(id=user_id)
    
        except DoesNotExist as e:
            return resp_does_not_exist("Client", "client id {}".format(user_id))

        except Exception as e:
            print(e)
            return resp_exception("Client", description=e.__str__())

        result = schema.dump(client)
        return resp_ok(
            "Clients", MSG_RESOURCE_FETCHED.format("Clients", user_id),
            data=result
        )

    def delete(self, user_id):
        schema = ClientSchema()
        try:
            client = Client.objects.get(id=user_id).delete()

        except DoesNotExist as e:
            return resp_does_not_exist("Client", "client id {}".format(user_id))
        
        except Exception as e:
            return resp_exception("Client", description=e.__str__())

        from apps.responses import resp_ok_no_content

        return resp_ok_no_content()

