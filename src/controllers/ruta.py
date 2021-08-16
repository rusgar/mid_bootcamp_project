from app import app
from flask import request
from utils.json_response import json_response, str_to_json
from utils.mongo_connection import mongo_read
from utils.type import cast_types
from utils.handle_error import handle_error



@app.get("/Paises")
@handle_error
def read_mongo():
    q= cast_types(**dict(request.args))
    if "mongo_query" in q.keys():
        q = str_to_json(q["mongo_query"])
    print(q)
    return json_response(list(mongo_read("core","euro",q)))



