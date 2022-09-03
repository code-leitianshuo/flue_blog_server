# powered by github:code-leitianshuo
from flask import Blueprint
from flask import request, abort, Response, session, jsonify
from bson import ObjectId
from sql import *
from jinja2 import filters
import datetime

cmt = Blueprint("comment", __name__)


# filters.do_mark_safe()

@cmt.route("/comment/insert", methods=["POST"])
async def insert():
    if session.get("users_key") == "1":
        req_key = int(request.form.get("key"))
        req_blogname = request.form.get("name")
        req_nickname = request.form.get("nickname")
        req_icon = request.form.get("icon")
        req_email = request.form.get("email")
        req_content = request.form.get("content")
        _key = int(list(key.find({}, {"_id": 0}))[-1]["key"])
        if req_key == _key:
            time = datetime.datetime.now().strftime("%Y-%m-%d:%H-%M-%S")
            comments.insert_one({req_blogname: [time, req_nickname, req_icon, req_email, req_content]})
            id = comments.find_one({req_blogname: [time, req_nickname, req_icon, req_email, req_content]})["_id"]
            comment_id.insert_one({req_nickname: req_email})
            return "ok"
        else:
            return abort(403, Response("key error"))
    else:
        return abort(403, Response("key error"))


@cmt.route("/comment/find", methods=["POST"])
async def find():
    req_key = int(request.form.get("key"))
    req_id = request.form.get("id")
    req_sort = request.form.get("sort")
    _key = int(list(key.find({}, {"_id": 0}))[-1]["key"])
    if len(req_id) == 24:
        req_id = ObjectId(req_id)
        if req_key == _key:
            ret = list(comments.find({"_id": req_id}).limit(int(req_sort)))
            for i in ret:
                i["_id"] = str(i["_id"])
            return jsonify(ret)
        else:
            return abort(403, Response("key error"))
    else:
        if req_key == _key:
            ret = list(comments.find({}).limit(int(req_sort)))
            for i in ret:
                i["_id"] = str(i["_id"])
            return jsonify(ret)
        else:
            return abort(403, Response("key error"))


@cmt.route("/comment/delete", methods=["POST"])
async def delete():
    if session.get("users_key") == "1":
        req_key = int(request.form.get("key"))
        req_id = request.form.get("id")
        req_email = request.form.get("email")
        req_id = ObjectId(req_id)
        _key = int(list(key.find({}, {"_id": 0}))[-1]["key"])
        if req_key == _key:
            comments.delete_one({req_email: req_id})
            return "ok"
        else:
            return abort(403, Response("key error"))
    else:
        return abort(403, Response("key error"))


@cmt.route("/comment/id", methods=["POST"])
async def _id():
    req_email = request.form.get("email")
    req_nickname = request.form.get("nickname")
    content = str(list(comment_id.find({req_nickname: req_email})))
    return content
