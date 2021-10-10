
from flask_restful import Resource
from authman.controller.apiv1 import UserController

"""
   GET /Users ---> list of users.
   GET /users/<user_id>  ---> Get user info.
   POST /users ---> create new user.
   POST /users/<user_id> not allowd 
   PATCH /users/ ---> Not allowd
   PATCH /users/<user_id> update user
   delete /users/ ---> Not allowd
   delete /users/<user_id> delete user 
"""
class UserResource(Resource):

    def get(self,user_id=None):
        if user_id is None:
            return UserController.get_users()#Get list of users.
#            return {"user": "singleton"}
#        return {"users": "collection"}
        else:
            return UserController.get_user(user_id)#Get user info.

    def post(self):
        return UserController.create_user() #Create new user.

    def patch(self, user_id):
        return UserController.update_user(user_id)

    def delete(self, user_id):
        return UserController.delete_user(user_id)
