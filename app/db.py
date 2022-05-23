from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initiate the SQLAlchemy object
db = SQLAlchemy()

# Initiate the Marshmallow object
ma = Marshmallow()

# Initiate
migrate = Migrate()
