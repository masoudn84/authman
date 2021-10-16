from werkzeug.datastructures import Headers
from authman.authman import db
from authman.model import User
from authman.schema.apiv1 import UserSchema
from authman.util import jsonify

from flask import request


class UserController:
    def get_users():
        users_schema = UserSchema(many=True)
        users = User.query.all()
        return jsonify({"users": users_schema.dump(users)})#return list of users
        #return jsonify(status=501) # Not Implemented.

    def get_user(user_id):
        user_schema = UserSchema()
        user = User.query.get(user_id)
        if user is None:
            return jsonify(status=404,code=103) #user not found
        return jsonify({"user": user_schema.dump(user)}) #return single user   

    def create_user():
        if not request.is_json:
            jsonify(status=415,code=101)
        user_schema = UserSchema(only=["username","password"])
        try:
            data = user_schema.load(request.get_json())#json validation
        except:
            return jsonify(status=400,code=104)
        if not data["username"] or not data["password"]:
            return jsonify(status=400, code=105)#empty data
        user = User.query.filter_by(username=data["username"]).first()
        if user is not None:
            return jsonify(status=400,code=106)#user is already found
        user = User(username=data["username"], password=data["password"])
        db.session.add(user)
        db.session.commit()
        user_schema = UserSchema()
        return jsonify({"user": user_schema.dump(user)}, status=201)  
         

    def update_user(user_id):
        if not request.is_json:
            return jsonify(status=415,code=101)
        user_schema = UserSchema(only=["password"])
        try:
            data = user_schema.load(request.get_json())
        except:
            return jsonify(status=400,code=104)
        if not data["password"]:
            return jsonify(status=400,code=105 )
        user = User.query.get(user_id)
        if user is None:
            return jsonify(status=404,code=103)
        user.password = data["password"]
        db.session.commit()
        user_schema = UserSchema()
        return jsonify({"user":user_schema.dump(user)})
    def delete_user(user_id):
        user = User.query.get(user_id)
        if user is None:
            return jsonify(status=404,code=103)
        db.session.delete(user)
        db.session.commit()
        return jsonify()
