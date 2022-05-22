from flask import Flask
from flask_restful import Api

from app.db import db, ma
from app.user.user_resource import UserResourceList

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object("config")

api = Api(app)
db.init_app(app)
ma.init_app(app)


@app.before_request
def create_tables():
    """
    Initialise the tables before the first request
    """
    db.create_all()


# Register the resources here
api.add_resource(UserResourceList, "/api/users")
