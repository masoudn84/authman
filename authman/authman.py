from flask import Flask,Blueprint
from flask_restful import Api
from authman.config import Config

apiv1_bp = Blueprint("apiv1",__name__,url_prefix="/api/v1")
apiv1= Api(apiv1_bp)
#print(Config.ENV)# just for test

from authman import resource
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config) #Load application configs.
    app.register_blueprint(apiv1_bp)#Load Api v1
    return app