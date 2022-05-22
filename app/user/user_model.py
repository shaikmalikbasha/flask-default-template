from app.db import db


# Define a base model for other database tables to inherit
class Base(db.Model):

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(
        db.DateTime,
        default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp(),
    )

    def save(self):
        db.session.add(self)
        db.session.commit()

    def remove(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_all(cls):
        return cls.query.all()


# Define a User model
class User(Base):

    __tablename__ = "users"

    name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(192), nullable=False)

    # New instance instantiation procedure
    def __init__(self, name, email, password):

        self.name = name
        self.email = email
        self.password = password

    @classmethod
    def find_by_id(cls, user_id):
        return cls.query.filter_by(id=user_id).first()

    def __repr__(self):
        return str(self.__dict__)

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "created_at": self.created_at.strftime(r"%Y/%m/%d, %H:%M:%S"),
            "updated_at": self.updated_at.strftime(r"%Y/%m/%d, %H:%M:%S"),
        }
