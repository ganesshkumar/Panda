import os
from pymongo import MongoClient, errors
from datetime import datetime

class MongoDBClient:
    def __init__(self):
        try:
            self.client = MongoClient('mongodb://save-the-hacker:backstroke@troup.mongohq.com:10075/app22534615')
        except errors.ConnectionFailure:
            self.client = MongoClient('localhost',27017)
        self.db = self.client.app22534615
        self.reviews = self.db.reviews

    @staticmethod
    def get_empty_data():
        dict = {
            'title': '',
            'title_ws': '',
            'amzn_url': '',
            'flip_url': '',
            'amzn_hash': '',
            'flip_hash': '',
            'amzn_senti': {
                'positive': 0,
                'negative': 0,
                'neutral': 0
            },
            'amzn_rating': 0.0,
            'flip_rating': {
                'positive': 0,
                'negative': 0,
                'neutral': 0
            },
            'flip_rating': 0.0,
            'twitter_tags': [],
            'lastUpdated': datetime.now()
        }
        return dict

    def get(self, title):
        return self.reviews.find_one({'title_ws': ''.join(e for e in title if e.isalnum()).lower()})

    def save(self, data):
        data['title_ws'] = ''.join(e for e in data['title'] if e.isalnum()).lower()
        self.reviews.save(data)

    def insert(self, data):
        try:
            self.reviews.insert(data)
            return "Post added successfully"
        except errors.DuplicateKeyError:
            return  "Post already added"

if __name__ == "__main__":
    client = MongoDBClient()
    print client.get('Moto U')
