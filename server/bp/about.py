# powered by github:code-leitianshuo
from flask import Blueprint
from flask import jsonify, request, session, abort, Response
from sql import *

about_bp = Blueprint("about", __name__)


@about_bp.route("/about/find", methods=["POST"])
async def about_find():
    about = list(author_about.find({}))
    print(about)
    about["_id"] = str(about["_id"])
    return jsonify(about)


@about_bp.route("/about/insert", methods=["POST"])
async def about_insert():
    req_about = request.form.get("about")
    req_key = int(request.form.get("key"))
    _key = int(list(key.find({}, {"_id": 0}))[-1]["key"])
    print(_key)
    if session.get("users_key") == "1":
        if req_key == _key:
            author_about.insert_one({"about": req_about})
            return "ok"
        else:
            return abort(403, Response("key error"))
    else:
        return abort(403, Response("key error"))


@about_bp.route("/about/delete", methods=["POST"])
async def about_delete():
    req_id = request.form.get("id")
    req_key = int(request.form.get("key"))
    _key = int(list(key.find({}, {"_id": 0}))[-1]["key"])
    print(_key)
    if session.get("users_key") == "1":
        if req_key == _key:
            author_about.delete_one({"_id": req_id})
            return "ok"
        else:
            return abort(403, Response("key error"))
    else:
        return abort(403, Response("key error"))
