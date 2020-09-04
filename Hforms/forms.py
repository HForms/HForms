from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from Hforms.dbModels import User
import re

class RegistrationForm(FlaskForm):
	username = StringField('Username', validators = [DataRequired()])
	password = PasswordField('Password', validators = [DataRequired()])
	cnf_password = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password')])
	submit = SubmitField('Sign Up!')
	def validate_username(self,username):
		regex="^(?=.{8,20}$)(?![_. ])(?!.*[_.]{2})(?!.*[ ])[a-zA-Z0-9._]+(?<![_. ])$"
		user=re.match(regex,username)
		if user:
			raise ValidationError('Sorry your username contains invalid charecters for username.')
	def validate_username(self, username):

		user = User.query.filter_by(username = username.data).first()
		if user:
			raise ValidationError('Sorry! Thats username is already taken. Try another one.')

	def validate_password(self, password):
		password_length = len(password.data)
		if(password_length < 8 or password_length > 32):
			raise ValidationError("Password length must be between 8 and 32 characters")

class LoginForm(FlaskForm):
	username = StringField('Username', validators = [DataRequired()])
	password = PasswordField('Password', validators = [DataRequired()])
	remember = BooleanField('Remember me')
	submit = SubmitField('Login')
