from werkzeug.datastructures import Headers
from authman.authman import db
from authman.model import User
from authman.schema.apiv1 import UserSchema
from authman.util import jsonify,now ,user_expires_at

from flask import request


class UserController:
    def get_users():
        users_schema = UserSchema(many=True)
        try:
            users = User.query.all()
        except:
            return jsonify(status=500,code=102)
        return jsonify({"users": users_schema.dump(users)})#return list of users
        #return jsonify(status=501) # Not Implemented.

    def get_user(user_id):
        user_schema = UserSchema()
        try:
            user = User.query.get(user_id)
        except:
            return jsonify(status=500,code=102)
        if user is None:
            return jsonify(status=404,code=103) #user not found
        return jsonify({"user": user_schema.dump(user)}) #return single user   

    def create_user():
        if not request.is_json:
            return jsonify(status=415,code=101)
        user_schema = UserSchema(only=["username","password"])
        try:
            data = user_schema.load(request.get_json())#request validation
        except:
            return jsonify(status=400,code=104)
        if not data["username"] or not data["password"]:
            return jsonify(status=400, code=105)#empty data
        try:    
            user = User.query.filter_by(username=data["username"]).first()
        except:
            return jsonify(status=500,code=102)
        if user is not None:
            return jsonify(status=409,code=106)#user is already found
        user = User(username=data["username"], password=data["password"])
        db.session.add(user)
        try:
            db.session.commit()
        except:
            db.sessio.rollback()
            return jsonify(status=500,code=102)
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
            return jsonify(status=400,code=105)
        try:
            user = User.query.get(user_id)
        except:
            return jsonify(status=500,code=102)
        if user is None:
            return jsonify(status=404,code=103)
        user.password = data["password"]
        user.last_change_at = now()
        user.expires_at = user_expires_at()
        user.failed_auth_at = None
        user.failed_auth_count = 0
        try:
            db.session.commit()
        except:
            db.session.rollback()
            return jsonify(status=500,code=102)
        user_schema = UserSchema()
        return jsonify({"user":user_schema.dump(user)})
    def delete_user(user_id):
        try:
            user = User.query.get(user_id)
        except:
            return jsonify(status=500,code=102)
        if user is None:
            return jsonify(status=404,code=103)
        db.session.delete(user)
        try:
            db.session.commit()
        except:
            db.session.rollback()
            return jsonify(status=500,code=102)
        return jsonify()
