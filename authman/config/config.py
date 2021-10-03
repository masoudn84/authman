from os import environ
class Config:
    #==================Global Configuration================
    ENV = environ.get("FANTOM_AUTHMAN_ENV","production")
    TESTING = int(environ.get("FANTOM_AUTHMAN_TESTING","0"))
    DEBUG = int(environ.get("FANTHOM_AUTHMAN_DEBUG","0"))
    #==================Database Config======================
    SQLALCHEMY_DATABASE_URI = environ.get("FANTOM_AUTHMAN_DATABASE_URI", None)
    SQLALCHEMY_ECHO = DEBUG
    SQLALCHEMY_QUERIES = DEBUG
    SQLALCHEMY_TRACK_MODIFICATIONS = DEBUG