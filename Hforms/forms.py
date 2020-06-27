"""
	Author: Srikar
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from Hforms.dbModels import User

class RegistrationForm(FlaskForm):
	username = StringField('Username', validators = [DataRequired(), Length(min = 2, max = 20)])
	password = PasswordField('Password', validators = [DataRequired()])
	cnf_password = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password')])
	submit = SubmitField('Sign Up!')

	def validate_username(self, username):

		user = User.query.filter_by(username = username.data).first()
		if user:
			raise ValidationError('Sorry! Thats username is already taken. Try another one.')

class LoginForm(FlaskForm):
	username = StringField('Username', validators = [DataRequired(), Email()])
	password = PasswordField('Password', validators = [DataRequired()])
	remember = BooleanField('Remember me')
	submit = SubmitField('Login')