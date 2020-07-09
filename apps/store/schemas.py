# _*_ coding: utf-8 _*_

from marshmallow import Schema
from marshmallow.fields import Email, Str, Decimal

from apps.messages import MSG_FIELD_REQUIRED

class ClientSchema(Schema):
    name = Str(required=True, 
            error_messages={"required": MGS_FIELD_REQUIRED+"name"}
           )
    email = Email(required=True, 
                error_message={"required": MGS_FIELD_REQUIRED+"email"}
            )
    address = Str()

class ProductSchema(Schema):
    cod_prod = Str(required=True,
                    error_message={"required": MGS_FIELD_REQUIRED+"cod_prod"}
                )
    name = Str(required=True, 
                error_message={"required": MGS_FIELD_REQUIRED+"name"}
           )
    desc = Str()
    price = Decimal() 
