# app/database.py
from pymongo import MongoClient
from config import MONGO_URI, MONGO_DB

client = MongoClient(MONGO_URI)
db = client[MONGO_DB]

def add_url(name, url, action, time, date):
    db.ActiveURL.insert_one({"Name": name, "URL": url, "Action": action, "Time": time, "Date": date})

def get_all_history():
    return list(db.ActiveURL.find())

def get_active_urls():
    return list(db.ActiveURL.find({"Action": "Added"}))
