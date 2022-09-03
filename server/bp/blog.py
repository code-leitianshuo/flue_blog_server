# powered by github:code-leitianshuo
from flask import Blueprint
from flask import request, render_template, jsonify, abort, Response, session
from bson import ObjectId
from sql import *
import datetime

blg = Blueprint("blog", __name__)


@blg.route("/blog/insert", methods=["POST"])
async def insert():
    if session.get("users_key") == "1":
        req_key = int(request.form.get("key"))
        req_blogname = request.form.get("name")
        req_blogsimple = request.form.get("simple")
        req_blogcontent = request.form.get("content")
        _key = int(list(key.find({}, {"_id": 0}))[-1]["key"])
        if req_key == _key:
            time = datetime.datetime.now().strftime("%Y-%m-%d:%H-%M-%S")
            blog.insert_one({req_blogname: [time, req_blogsimple, req_blogcontent]})
            id = blog.find_one({req_blogname: [time, req_blogsimple, req_blogcontent]})["_id"]
            blog_id.insert_one({req_blogname: id})
            return "ok"
        else:
            return abort(403, Response("key error"))


@blg.route("/blog/find", methods=["POST"])
async def find():
    req_key = int(request.form.get("key"))
    req_id = request.form.get("id")
    req_sort = request.form.get("sort")
    _key = int(list(key.find({}, {"_id": 0}))[-1]["key"])
    if len(req_id) == 24:
        req_id = ObjectId(req_id)
        if req_key == _key:
            ret = list(blog.find({"_id": req_id}).limit(int(req_sort)))
            for i in ret:
                i["_id"] = str(i["_id"])
            return jsonify(ret)
        else:
            return abort(403, Response("key error"))
    else:
        if req_key == _key:
            ret = list(blog.find({}).limit(int(req_sort)))
            for i in ret:
                i["_id"] = str(i["_id"])
            return jsonify(ret)
        else:
            return abort(403, Response("key error"))


@blg.route("/blog/delete", methods=["POST"])
async def delete():
    if session.get("users_key") == "1":
        req_key = int(request.form.get("key"))
        req_id = request.form.get("id")
        req_blogname = request.form.get("name")
        req_id = ObjectId(req_id)
        _key = int(list(key.find({}, {"_id": 0}))[-1]["key"])
        if req_key == _key:
            blog.delete_one({req_blogname: req_id})
            return "ok"
        else:
            return abort(403, Response("key error"))


@blg.route("/blog/id", methods=["POST"])
async def _id():
    req_blogname = request.form.get("name")
    content = str(list(blog_id.find())[0][req_blogname])
    return content
