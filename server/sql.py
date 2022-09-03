# powered by github:code-leitianshuo
import pymongo

"""
根据《刑法》第二百八十六条【破坏计算机信息系统罪】违反国家规定，对计算机信息系统功能进行删除、修改、增加、干扰，
造成计算机信息系统不能正常运行，后果严重的，处五年以下有期徒刑或者拘役；后果特别严重的，处五年以上有期徒刑。
"""

"""
pymongo语法:
1.添加:集合.insert_[one|many]({"名称":内容})
2.###删除:集合.delete_[one|many]({"名称":内容})
3.改动(更新):集合.update_[one|many]({"名称":内容},{"改动方法[$inc(常用)|$set|$push|$pull(常用)]":{"名称":内容}})
4.查询:集合.find_[one|many|]({"名称":内容})
5.索引:集合.create_index([("名称",[1|-1])],unique=([True|False]))
6.删除索引:集合.drop_index([("名称",[1|-1])])
7.limit限定到第()个内容
8.skip跳过第()个内容
9.sort计数
10.count计数
11.嵌入式:a集合某内容==>b集合某内容
12.引用式:a集合某内容objectid==>b集合某内容
13.###删除合集:合集.drop
14.str转objectid:ObjectId(str)
15.$lt小于
16.$lte小于等于
17.$gt大于
18.$gte大于等于
"""
mongo = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
# 用户，博客名，博客内容，博客评论，全部博客，全部博客日期，个人简介，作者关于，网站首页，博客资源，外部资源
sql = mongo["blog"]  # 创建数据库
blog_id = sql["id"]  # id {blogname:_id}
comment_id = sql["cmt_id"]
user = sql["user"]  # 用户名、密码 {username:password}
blog = sql["blog"]  # 博客内容 {blogname:[time,simple_content,content]}
comments = sql["comments"]  # 评论 {blogname:[[time,username,users_icon,users_email,content],[time,username,users_icon,users_email,content]]}
author_about = sql["about"]  # 关于作者 {"about":"aaa"}
basic = sql["basic"]  # 博客基本定义信息 {"title":"111"}
key = sql["key"]  # 密钥 {"key":"10000"}
