from app.user.user_model import User
from app.user.user_schema import UserSchema
from flask import request

user_schema = UserSchema()
users_schema = UserSchema(many=True)


class UserService:
    def get_all_users(self):
        users = users_schema.dump(User.find_all())
        print(users)
        return users

    def add_new_user(self, input_body):
        input_body = request.get_json()
        new_user = User(
            input_body["name"],
            input_body["email"],
            input_body["password"],
            input_body["age"],
        )
        new_user.save()
        print(new_user)
        return user_schema.dump(new_user)
