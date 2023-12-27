from pymongo import MongoClient
from datetime import datetime, timedelta
import bcrypt


mongo = MongoClient('mongodb://localhost:27017', connect=False)
database = mongo.get_database('UserAuthentication')
users_collection = database.get_collection('Users')


def insert_user(username, password, uuid4=None):
    users_collection.insert_one({'username': username, 'password': password, 'session_token': uuid4,
                                 'last_login': str(datetime.now()),
                                 'token_expiry': str(datetime.now() + timedelta(hours=1))})


def get_user_by_username(user):
    return users_collection.find_one({'username': user})


def get_user_by_id(user_id):
    return users_collection.find_one({'_id': user_id})
