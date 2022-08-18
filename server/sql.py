import pymongo
# from bson import ObjectId

# powered by github:code-leitianshuo

"""

!!!!除"github:code-leitianshuo"以外所有人严禁对数据库代码修改，如需修改请报备，非本人禁止使用语法2.和删除集合(删除)。任何人禁止对数据库代码进行修改，或备份后修改，禁止提交修改后分支。{{{{修改后出现任何问题本人不负责}}}}!!!!

根据《刑法》第二百八十六条【破坏计算机信息系统罪】违反国家规定，对计算机信息系统功能进行删除、修改、增加、干扰，
造成计算机信息系统不能正常运行，后果严重的，处五年以下有期徒刑或者拘役；后果特别严重的，处五年以上有期徒刑。"""

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
"""
mongo = pymongo.MongoClient("mongodb://127.0.0.1:27017/")
#markdown所见即所得
# 用户，博客名，博客内容，博客评论，全部博客，全部博客日期，个人简介，作者关于，网站首页，博客资源，外部资源
# 内部备份代码
def backup(set):
    set=sql[str(set)+"backup"]
    a=set.find()
    set.insert_many({"backup":a})
sql=mongo["blog"]#创建数据库
user=sql["user"]#用户名、密码 {"username":"password"}
blogname=sql["blogname"]#所有博客名称 {"blogname":["a","b"]}
blogcontent=sql["blogcontent"]#博客内容 {"blogname":"# 一级 ## 二级 ###markdown {{img}}"} {"blogname":{"blogname":"111111"}} {"blogname":{"aaa":"11111"}} blogcontent.delete_one({"nlogname":"aaa"})
comments=sql["comments"]#评论 {"blogname":"blogname","cmt":["name","content"]} {"blogname":["aaa",cmt[name,content]]}
date=sql["date"]#所有博客的创建日期，修改日期 {"a":datetime(type)}
intro=sql["intro"]#作者简介 {"intro":"11111"}
# resource=sql["resource"]#博客内资源 {"blogname":[blogname,{"res":["img","file"]}]} {"aaa":{"res":["aacweffew","asrfe44"]}}
about=sql["about"]#关于作者 {"about":"aaa"}
home=sql["home"]#首页信息 {"home":"aaabbb"}
images=sql["images"]#除博客以外的所有资源（小图标，背景图等）{"bg":["imaegs","img2"],"xitongguanli":["img","img"]}
basic=sql["basic"]#网站后台基本定义信息 {""}
key=sql["key"]#密钥 {"key":""}
# ==>1.txt=1  ==>1.docx=uf894hf9w34h a=1.jpg==>二进制打开，b=a.b64加密
# json{"filename":a,"content":b}