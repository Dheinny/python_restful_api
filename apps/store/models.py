# _*_ coding: utf-8 _*_

from datetime import datetime

from mongoengine import (
    DateTimeField,
    EmailField,
    EmbeddedDocument,
    EmbeddedDocumentField,
    StringField,
    URLField
)

from apps.db import db


class UserMixin(db.Document):
    """
    Default implementation for User fields
    """
    meta = {
        "abstract": True,
        "ordering": ["email"]
    }

    email = EmailField(required=True, unique=True)
    created = DateTimeField(default=datetime.now)

class User(UserMixin):
    """
    Users
    """
    meta = {"collection": "users"}

    name = StringField(required=True) 
    address = StringField(default="")

