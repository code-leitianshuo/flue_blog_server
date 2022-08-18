from flask import Blueprint
from flask import request,render_template,send_file,jsonify
from sql import *
cmt=Blueprint("comment",__name__)
@cmt.route("/comment",methods=["POST"])
def comment():
    # {"passkey":"121er32rc","blogname":"aaa","cmt":["un","cmt"]}
    # try:
    # comment=request.form.get("comment")
    passkey=int(request.form.get("passkey"))#i/o F1l9u2e837.46
    blog=request.form.get("blog")#i/o blogname
    cmt1=request.form.get("cmt")#i ["111","111"]
    io=request.form.get("io")#i o d
    # print(blog)
    key1=int(list(key.find({},{"_id":0}))[-1]["key"])
    print(key1)
    if passkey==key1 and io=="i" and blog!=None and cmt1!=None:
        comments.insert_one({"blogname":blog,"cmt":cmt1})
        return jsonify({"error_key":"200","error":"ok"})
    elif passkey==key1 and io=="o":# and blog!=None and cmt1!=None
        a=list(comments.find({"blogname":blog},{"_id":0}))
        return jsonify(a)
    elif passkey==key1 and io=="d" and blog!=None and cmt1!=None:
        comments.delete_one({"blogname":blog,"cmt":cmt1})
        return jsonify({"error_key":"200","error":"ok"})
    else:
        return jsonify({"error_key":"405","error":"key error"})
    # except Exception:
    #     comment=request.form.get("blogname")
    #     # return list(comments.find({"blogname":comment}))
    #     return comment