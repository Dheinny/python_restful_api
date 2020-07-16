# _*_ coding: utf-8 _*_

from datetime import datetime

from mongoengine import (
    DateTimeField,
    EmailField,
    EmbeddedDocument,
    EmbeddedDocumentField,
    StringField,
    URLField,
    DecimalField,
    ReferenceField,
    ListField
)

from apps.db import db


class ClientMixin(db.Document):
    """
    Default implementation for User fields
    """
    meta = {
        "abstract": True,
        "ordering": ["email"]
    }

    email = EmailField(required=True, unique=True)
    created = DateTimeField(default=datetime.now)

class ProductMixin(db.Document):
    """
    Default implementation for Product fiels
    """

    meta = { 
        "abstract": True,
        "ordering": ["cod_prod"]
    }

    cod_prod = StringField(required=True, unique=True)
    created = DateTimeField(default=datetime.now)

class Client(ClientMixin):
    """
    Client
    """
    meta = {"collection": "clients"}

    name = StringField(required=True) 
    address = StringField(default="")


class Product(ProductMixin):
    """
    Product
    """
    meta = {"collection": "products"}

    name = StringField(required=True)
    desc = StringField(default="")
    price = DecimalField(default=0.0) 

class Order(db.Document):
    """
    Order
    """
    meta = {"collection": "orders"}

    client = ReferenceField(Client)
    products_cart = ListField(StringField())
    data_order = DateTimeField(default=datetime.now)
    created = DateTimeField(default=datetime.now)
