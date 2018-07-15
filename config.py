from pymongo import MongoClient

WTF_CSRF_ENABLED = True
SECRET_KEY = 'hogehoge'
DB_NAME = 'your_db'

DATABASE = MongoClient(
    host='your_db_info', port='your_db_port')[DB_NAME]
POSTS_COLLECTION = DATABASE.posts
USERS_COLLECTION = DATABASE.users
SETTINGS_COLLECTION = DATABASE.settings

DEBUG = True
