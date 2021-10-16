from os import environ
class Config:
    #==================Global Configuration=================
    ENV = environ.get("FANTOM_AUTHMAN_ENV","production")
    TESTING = int(environ.get("FANTOM_AUTHMAN_TESTING","0"))
    DEBUG = int(environ.get("FANTHOM_AUTHMAN_DEBUG","0"))
    TIMEZONE = environ.get("FANTOM_AUTHMAN_TIMEZONE","Asia/Tehran")
    #==================Database Config======================
    SQLALCHEMY_DATABASE_URI = environ.get("FANTOM_AUTHMAN_DATABASE_URI", None)
    SQLALCHEMY_ECHO = DEBUG
    SQLALCHEMY_QUERIES = DEBUG
    #======================USER CONFIGURATION================
    SQLALCHEMY_TRACK_MODIFICATIONS = DEBUG
    USER_DEFAULT_ROLE = environ.get("FANTOM_AUTHMAN_USER_DEFAULT_ROLE","member")
    USER_DEFAULT_EXPIRY_TIME = int(environ.get("FANTOM_AUTHMAN_USER_DEFAULT_EXPIRY_TIME","365"))
    USER_DEFAULT_STATUS = int(environ.get("FANTOM_AUTHMAN_USER_DEFAULT_STATUS","3")) #activate and enabled