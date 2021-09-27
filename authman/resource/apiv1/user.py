
from flask_restful import Resource

class UserResource(Resource):

    def get(self,user_id=None):
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
        if user_id is not None:
            return {"user": "singleton"}
        return {"users": "collection"}