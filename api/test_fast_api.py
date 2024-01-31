import unittest
from fastapi.testclient import TestClient
from fastAPI import create_app

def testCreateTwoEndpoints():
    config = [
        {
            "endpoint":"seasons",
            "method": "get",
            "response":{
                "response":[
                    2015,
                    2016,
                    2017,
                    2018,
                    2019,
                    2020,
                    2021,
                    2022,
                    2023
                ]
            }
        },
        {
            "endpoint":"health",
            "method": "get",
            "response":{
                "response":"api-request-mocker up"
            }
        }
    ]

    app = create_app(config)

    client = TestClient(app)

    response = client.get("/seasons")
    assert response.status_code == 200
    assert response.json() == config[0]["response"]

    secondResponse = client.get("/health")
    assert secondResponse.status_code == 200
    assert secondResponse.json() == config[1]["response"]

