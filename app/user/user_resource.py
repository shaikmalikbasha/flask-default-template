from app.user.user_service import UserService
from flask import request
from flask_restful import Resource

user_service = UserService()


class UserResource(Resource):
    pass


class UserResourceList(Resource):
    def get(self):
        db_users = user_service.get_all_users()
        return {"success": True, "users": db_users, "status_code": 200}, 200

    def post(self):
        input_body = request.get_json()
        new_user = user_service.add_new_user(input_body)

        return {
            "msg": "New user was successfully created...",
            "created_user": new_user,
            "status_code": 201,
        }, 201
