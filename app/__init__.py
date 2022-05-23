from dotenv import load_dotenv
from flask import Flask
from flask_restful import Api
import os

from app.db import db, ma
from app.user.user_resource import UserResourceList

load_dotenv(".env")


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


@app.route("/")
def index():
    return {"msg": "Hello, World!", "app_name": os.getenv("APP_NAME")}


# Register the resources here
api.add_resource(UserResourceList, "/api/users")
