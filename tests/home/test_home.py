# _*_ coding: utf-8 _*_

import json

def test_index_response_200(client):

    response = client.get("/")

    assert response.status_code == 200

def test_home_response_hello(client):

    response = client.get("/")

    data = json.loads(response.data.decode("utf-8"))

    assert data.get("hello")
    assert data["hello"] == "world by apps"
    
