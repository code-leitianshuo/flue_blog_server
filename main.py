from flask import *
from sql import *
from bp import comment
from bp import blog
import random
key1=str(random.randint(10000,99999))
key.insert_one({"key":key1})
# key.create_index([("key",-1)],unique=True)
app=Flask(__name__)
@app.route("/captcha")
def captcha():
    return str(list(key.find({},{"_id":0}))[-1])
app.register_blueprint(comment.cmt)
app.register_blueprint(blog.blg)
# 9113
app.run(port=1025,debug=True)