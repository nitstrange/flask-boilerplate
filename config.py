import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_hashing import Hashing

basedir = os.path.abspath(os.path.dirname(__file__))

# Create the Connexion application instance
connex_app = connexion.App(__name__, specification_dir=basedir)


# Get the underlying Flask app instance
app = connex_app.app
JWTManager(app)
CORS(app)
hashing = Hashing(app)


# Configure the SQLAlchemy part of the app instance
app.config['SECRET_KEY'] = "hoursofme"
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////' + os.path.join(basedir, 'people.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

# Create the SQLAlchemy db instance
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#use of flask script manager
manager = Manager(app)
manager.add_command('db', MigrateCommand)

# Initialize Marshmallow
ma = Marshmallow(app)

#running flask in standalone mode
