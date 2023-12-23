from pymongo import MongoClient
import bcrypt


mongo = MongoClient('mongodb://localhost:27017', connect=False)
database = mongo.get_database('UserAuthentication')
users_collection = database.get_collection('Users')


def encrypt_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')


def insert_user(username, password):
    users_collection.insert_one({'username': username, 'password': encrypt_password(password)})


def check_password(password, encrypted):
    return bcrypt.checkpw(password.encode('utf-8'), encrypted.encode('utf-8'))


def get_user(user):
    return users_collection.find_one({'username': user})
