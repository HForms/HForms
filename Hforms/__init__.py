"""
	Initialisation of app
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from os import environ
app = Flask(__name__)

app.config['SECRET_KEY'] = environ.get("CSRF_KEY")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from Hforms import routes

from Hforms.dbModels import User
db.create_all()