# _*_ coding: utf-8 _*_

from marshmallow import Schema
from marshmallow.fields import Email, Str, Decimal

from apps.messages import MSG_FIELD_REQUIRED

class ClientSchema(Schema):
    name = Str(required=True, 
            error_messages={"required": MSG_FIELD_REQUIRED.format("name")}
           )
    email = Email(required=True, 
                error_message={"required": MSG_FIELD_REQUIRED.format("email")}
            )
    address = Str()

class ProductSchema(Schema):
    cod_prod = Str(required=True,
                    error_message={"required": MSG_FIELD_REQUIRED.format("cod_prod")}
                )
    name = Str(required=True, 
                error_message={"required": MSG_FIELD_REQUIRED.format("name")}
           )
    desc = Str()
    price = Decimal() 
