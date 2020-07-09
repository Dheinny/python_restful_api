# _*_ coding: utf-8 _*_

import pytest
from dotenv import load_dotenv
load_dotenv()

@pytest.fixture(scope="session")
def client():
    from apps import create_app
    flask_app = create_app("testing")

    testing_client = flask_app.test_client()

    ctx = flask_app.app_context()
    ctx.push()

    yield testing_client

    ctx.pop()
