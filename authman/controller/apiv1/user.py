from authman.authman import db
from authman.model import User
from authman.schema.apiv1 import UserSchema
from authman.util import jsonify


class UserController:
    def get_users():
        users_schema = UserSchema(many=True)
        users = User.query.all()
        return jsonify({"Users": users_schema.dump(users)})
        return jsonify(status=501) # Not Implemented.

    def get_user(user_id):
        return jsonify(status=501) # Not Implementedu.

    def create_user():
        return jsonify(status=501) # Not Implementedu. 

    def update_user(user_id):
        return jsonify(status=501) # Not Implemented.

    def delete_user(user_id):
        return jsonify(status=501) # Not Implemented.
