from app import ma
from app.user.user_model import User


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    id = ma.auto_field()
    name = ma.auto_field()
    email = ma.auto_field()
    password = ma.auto_field()
    age = ma.auto_field()
    created_at = ma.auto_field()
    updated_at = ma.auto_field()
