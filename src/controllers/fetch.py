# from utils.handle_error import handle_error
from utils.json_response import json_response, str_to_json
from app import app
from flask import request
from utils.mongo_connection import mongo_read
from utils.type_casting import cast_types
from utils.handle_error import handle_error



@app.get("/read")
@handle_error
def read_mongo():
    q= cast_types(**dict(request.args))
    if "mongo_query" in q.keys():
        q = str_to_json(q["mongo_query"])
    print(q)
    return json_response(list(mongo_read("core","euro",q)))


# Función controladora
# @app.route("/")
# @handle_error
# def ejemplo():
#     alumno = {
#         "name":"edu"
#     }
#     return json_response(alumno)


# @app.route("/saludo")
# @handle_error
# def saludo_fn():
#     print("terminal")
#     print(request.args)
#     name = request.args.get("name", "~~~")
#     surname = request.args.get("surname", "~~~")
#     # raise ValueError("Esto no es correcto")
#     return {
#         "name":"EMOJI / " + name,
#         "surname":surname,
#     }
