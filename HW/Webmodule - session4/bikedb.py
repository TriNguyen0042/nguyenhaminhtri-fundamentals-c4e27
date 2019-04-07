from pymongo import MongoClient
from bson.objectid import ObjectId
mongo_uri = "mongodb+srv://admin:admin@cluster0-vyheh.mongodb.net/test?retryWrites=true"
client = MongoClient(mongo_uri)
bikedb = client.bike
bikes = bike_db["bikes"]
