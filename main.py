from api.fastAPI import *
import json

with open("config.json", "r") as read_file:
    config = json.load(read_file)

app = create_app(config)