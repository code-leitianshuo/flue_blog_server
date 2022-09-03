# powered by github:code-leitianshuo
from flask import Blueprint
from flask import request, session, abort, Response
from sql import *

users = Blueprint("user", __name__)


@users.route("/user/login", methods=["POST"])
async def user_login():
    username = request.form.get("username")
    password = request.form.get("password")
    req_key = int(request.form.get("key"))
    _key = int(list(key.find({}, {"_id": 0}))[-1]["key"])
    if req_key == _key:
        _user = user.find_one({username: password})
        if _user is not None:
            session["users_key"] = "1"
            return "ok"
        else:
            return abort(403, Response("username||password error"))
    else:
        return abort(403, Response("key error"))


@users.route("/user/register", methods=["POST"])
async def user_register():
    req_key = int(request.form.get("key"))
    username = request.form.get("username")
    password = request.form.get("password")
    _key = int(list(key.find({}, {"_id": 0}))[-1]["key"])
    if req_key == _key:
        user.insert_one({username: password})
        session["users_key"] = "1"
        return "ok"
    else:
        return abort(403, Response("key error"))


@users.route("/user/relogin", methods=["POST"])
async def relogin():
    req_key = int(request.form.get("key"))
    _key = int(list(key.find({}, {"_id": 0}))[-1]["key"])
    if req_key == _key:
        session["users_key"] = "0"
    else:
        return abort(403, Response("key error"))
