from flask import Blueprint
from flask import request,render_template,send_file,jsonify
from sql import *
blg=Blueprint("blog",__name__)
@blg.route("/blog",methods=["GET"])
def blg1():
    # {"passkey":"121er32rc","blogname":"aaa","cmt":["un","cmt"]}
    # try:
    # comment=request.args.get("comment")
    passkey=int(request.args.get("passkey"))#i/o F1l9u2e837.46
    blog=request.args.get("blog")#i/o blogname 
    bc=request.args.get("blogcontent")#i ["111","111"]
    io=request.args.get("io")#i o d
    # print(blog)
    print(passkey,blog,bc,io)
    key1=int(list(key.find({},{"_id":0}))[-1]["key"])
    print(key1)
    if passkey==key1 and io=="i" and blog!=None and bc!=None:
        # {"blogname":{"aaa":"11111"},"blogname":{"bbb":"11111"}}
        blogname.insert_one({"blogname":blog})
        blogcontent.insert_one({"blogname":{blog:bc}})
        return jsonify({"error_key":"200","error":"ok"})
    elif passkey==key1 and io=="o" and blog!=None and bc!=None:
        bn=list(blogname.find({"blogname":blog}))
        bc=list(blogcontent.find({}))["blogname"]#"aaa":"####1111","bbb":"####2222"
        print(bc)
        return jsonify({bn:bc})
    elif passkey==key1 and io=="d" and blog!=None and bc!=None:
        blogname.delete_one({"blogname":blog})
        blogcontent.delete_one({blog})
        return jsonify({"error_key":"200","error":"ok"})
    else:
        return jsonify({"error_key":"405","error":"key error"})
    # except Exception:
    #     comment=request.args.get("blogname")
    #     # return list(comments.find({"blogname":comment}))
    #     return comment