# powered by github:code-leitianshuo
from flask import *
from sql import *
from bp import comment
from bp import blog
from bp import user
from bp import about
import random

key1 = str(random.randint(10000000, 99999999))
key.insert_one({"key": key1})
app = Flask(__name__)
app.secret_key = 'flueblog'


@app.route("/captcha", methods=["POST"])
async def captcha():
    return str(list(key.find({}, {"_id": 0}))[-1])


app.register_blueprint(comment.cmt)
app.register_blueprint(blog.blg)
app.register_blueprint(user.users)
app.register_blueprint(about.about_bp)
# 9113
app.run(port=1026, debug=True)
