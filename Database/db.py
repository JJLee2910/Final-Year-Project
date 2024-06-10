from pymongo import MongoClient

client = MongoClient("mongodb+srv://Lee:kaixin12@cluster0.vmgyyjq.mongodb.net/")

db = client['FYP']
collection = db['user']


class Database:
    def __init__(self):
        self.client = MongoClient('mongodb+srv://Lee:kaixin12@cluster0.vmgyyjq.mongodb.net/')
        self.db = self.client['FYP']
        self.user_collection = self.db['user']
    
    def find_user(self, username, password):
        return self.user_collection.find_one({'_id': username, 'Password': password})
