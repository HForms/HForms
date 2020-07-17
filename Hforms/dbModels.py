from Hforms import db, login_manager
from datetime import datetime
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key = True)
	username = db.Column(db.String(20), unique = True, nullable = False)
	password = db.Column(db.String(60), nullable = False)

	def __repr__(self):
		return "User('{}', '{}')".format(self.id, self.username)