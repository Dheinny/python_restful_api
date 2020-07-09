# _*_ coding: utf-8 _*_

from mongoengine import (
    StringField
)

from apps.store.models import User

class TestUser:

    def setup_method(self):
        self.data = {
            "email": "teste1@teste.com",
            "name": "teste1",
            "address": "rua teste1, cidade teste1"
        }

        self.model = User(**self.data)

    def test_email_field_exist(self):
        """
        Check if email field exists
        """
        assert "email" in self.model._fields

    def test_email_field_is_required(self):
        """
        Check if email field is required
        """
        assert self.model._fields["email"].required is True

    def test_email_field_is_unique(self):

        assert self.model._fields["email"].unique is True

    def test_email_field_is_str(self):

        assert isinstance(self.model._fields["email"], StringField)

    def test_all_fields_in_model(self):
        fields_check = ["email", "created", "name", "address"]

        for i in fields_check:
            assert i in self.model._fields

    
    #TODO tests for other fields, following the same idea above

