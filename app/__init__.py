from flask import Flask
from flask_pymongo import PyMongo
from flask_ldap3_login import LDAP3LoginManager
from config import Config


# Initialize MongoDB and LDAP Manager
mongo = PyMongo()
ldap_manager = None

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # MongoDB Initialization
    try:
        mongo.init_app(app)
        print("MongoDB connected successfully.")
    except Exception as e:
        print(f"Error while connecting to MongoDB: {e}")

    # LDAP Initialization
    global ldap_manager
    try:
        ldap_manager = LDAP3LoginManager(app)
        print("LDAP Manager initialized successfully.")
    except Exception as e:
        print(f"Error while initializing LDAP: {e}")
    
    return app
