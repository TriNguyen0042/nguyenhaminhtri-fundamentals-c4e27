from pymongo import MongoClient
mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(mongo_uri)
hw = client.c4e
cmt = hw["posts"]
post = {
    "title": "Comment C4E27",
    "author": "Nguyễn Hà Minh Trí",
    "content": "Nhiều bài tập quá reeeeeeeeee",
}
cmt.insert_one(post)
