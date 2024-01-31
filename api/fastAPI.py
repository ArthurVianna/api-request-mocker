# fastAPI Preparing and running api

from fastapi import FastAPI, Request
from fastapi.routing import APIRoute


def create_app(config):

    app = FastAPI()

    async def get_response(request: Request):
        endpoint = request.url.path.replace('/', "", 1)
        
        for endpoint_config in config:
            if endpoint_config["endpoint"] == endpoint and endpoint_config["method"].upper() == request.method:
                return endpoint_config["response"]
        return None

    for endpoint_config in config:
        app.add_api_route(
            "/" + endpoint_config["endpoint"],
            get_response,
            methods=[endpoint_config["method"]],
            name=endpoint_config["endpoint"],
        )

    return app