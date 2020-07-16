# _*_ coding: utf-8 _*_

from math import ceil

from flask import request

from flask_restful import Resource
from mongoengine.errors import (
    NotUniqueError, ValidationError, FieldDoesNotExist,
)
from marshmallow.exceptions import ValidationError as ValidationErrorMarshmallow
import werkzeug.exceptions as wzg

from apps.responses import (
    resp_already_exists, resp_exception, resp_does_not_exist,
    resp_data_invalid, resp_ok, resp_ok_no_content
)

from apps.messages import(
    MSG_NO_DATA, MSG_RESOURCE_CREATED, MSG_INVALID_DATA,
    MSG_RESOURCE_FETCHED_PAGINATED, MSG_RESOURCE_FETCHED,
    MSG_NO_RESOURCE_REGISTERED
)

from apps.decorators.methods_decorator import GetDecorator, DeleteDecorator

# Local
from apps.store.models import Product
from apps.store.schemas import ProductSchema

class ProductCollection(Resource):
    def post(self, *args, **kwargs):
        req_data = request.get_json() or None
        data, errors, result = None, None, None
        schema = ProductSchema()

        if req_data is None:
            return resp_data_invalid("Product", [], msg=MSG_NO_DATA)
        
        try:
            data = schema.load(req_data)
        except ValidationErrorMarshmallow as err:
            return resp_data_invalid("Product", err.messages)

        try:
            data["name"] = data["name"].title()
            data["cod_prod"] = data["cod_prod"].upper()

            model = Product(**data)
            model.save()

        except NotUniqueError:
            return resp_already_exists("Product", "product")

        except ValidationError as e:
            return resp_exception("Product", msg=MSG_INVALID_DATA, description=e)

        except Exception as e:
            return resp_exception("Product", description=e)

        result = schema.dump(model)
        return resp_ok(
                "Product", MSG_RESOURCE_CREATED.format("Product"), data=result)

    def get(self):
        schema = ProductSchema(many=True)
        args = request.args
        page_id = int(args["page"]) if args.get("page") else 1
        page_size = 10
        if "page_size" in request.args:
            page_size = int(request.args.get("page_size"))
            page_size = 10 if page_size < 1 else page_size

        try: 
            products = Product.objects()
            count = products.count()
            if count == 0:
                return resp_does_not_exist("Product", "product", msg=MSG_NO_RESOURCE_REGISTERED)

            if count <= ((page_id-1)*page_size):
                page_id = ceil(count/page_size)

            products = products.paginate(page_id, page_size)

        except FieldDoesNotExist as e:
            return resp_exception("Product", description=e.__str__())

        except wzg.NotFound:
            return resp_does_not_exist("Product", "pagination")

        except Exception as e:
            return resp_exception("Product", description=e.__str__())

        extra = {
            "page": products.page, "pages": products.pages, "total":products.total,
            "params": {"page_size": page_size}
        }

        result = schema.dump(products.items)

        return resp_ok(
            "Products", MSG_RESOURCE_FETCHED_PAGINATED.format("Products"),
            data=result, **extra
        )


class ProductItem(Resource):
    @staticmethod
    @GetDecorator
    def get(cod_prod):
        schema = ProductSchema()
        product = Product.objects.get(cod_prod=cod_prod)
        result = schema.dump(product)

        return resp_ok(
            "Products", MSG_RESOURCE_FETCHED.format("Products", cod_prod),
            data=result
        )

    @staticmethod
    @DeleteDecorator
    def delete(cod_prod):
        product = Product.objects.get(cod_prod=cod_prod).delete()

        return resp_ok_no_content()

