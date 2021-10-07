from flask import Flask,Blueprint
from flask_restful import Api
#from flask_restx import Api  ##replace restx with restfull to document apis
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

from authman.config import Config

db = SQLAlchemy()
mg = Migrate()
ma = Marshmallow()

apiv1_bp = Blueprint("apiv1",__name__,url_prefix="/api/v1")
apiv1= Api(apiv1_bp)
#print(Config.ENV)# just for test

from authman import resource
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config) #Load application configs.
    db.init_app(app) # initialize sqlalchemy instance.
    mg.init_app(app, db) #initialize database migrate instance.
    ma.init_app(app) #initialize marshmallow serialize and validation instance.
    app.register_blueprint(apiv1_bp)#Load Api v1
    return app