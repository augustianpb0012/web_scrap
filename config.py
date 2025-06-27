import os

class Config:
    # General Configurations
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'mysecretkey'
    
    # LDAP Server Configurations
    LDAP_HOST = os.environ.get('LDAP_HOST') or 'ldap://192.168.0.120'
    LDAP_BASE_DN = os.environ.get('LDAP_BASE_DN') or 'dc=example,dc=com'
    LDAP_USER_DN = os.environ.get('LDAP_USER_DN') or 'cn=admin,dc=example,dc=com'
    LDAP_PASSWORD = os.environ.get('LDAP_PASSWORD') or 'password'

    # MongoDB Configuration
    MONGO_URI = os.environ.get('MONGO_URI') or 'mongodb://localhost:27017/your_database'
