from flask import Flask
from flask_restful import Api
from authman.config import Config
print(Config.ENV)
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config) #Load application configs.
    return app