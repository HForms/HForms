from flask import render_template, url_for, flash, redirect, request
from Hforms import app, db, bcrypt
from Hforms.forms import RegistrationForm, LoginForm
from Hforms.dbModels import User
from flask_login import login_user, current_user, logout_user, login_required
from Hforms.dbHandler import Create

@app.route('/')
def welcome():
	return render_template('welcome.html')

@app.route("/register", methods = ['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = RegistrationForm()
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username = form.username.data, email = form.email.data, password = hashed_password)
		db.session.add(user)
		db.session.commit()
		flash('Account created for {}! You shall now be able to login'.format(form.username.data), 'success')
		return redirect(url_for('login'))
	return render_template('register.html', form = form, title = 'Register')

@app.route("/login", methods = ['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email = form.email.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember = form.remember.data)
			next_page  = request.args.get('next')
			return redirect(next_page) if next_page else redirect(url_for('home'))
		else:
			flash('Login Unsuccessful. Check email and password', 'danger')
	return render_template('login.html', form = form, title = 'Login')

@app.route("/logout")
def logout():
	logout_user()
	return redirect(url_for('home'))

@app.route("/about")
def about():
	return render_template('about.html')

@app.route("/home")
@login_required
def home():
	return render_template('home.html', title = 'Home')

@app.route("/account")
@login_required
def account():
	return render_template('account.html', title = 'Account')

@app.route('/makeforms')
@login_required
def makeforms():
	return render_template("make.html", title = "Create a form")

@app.route("/make", methods = ["POST"])
@login_required
def Add():
  questions = []
  dt = []
  is_req = []
  i = 1
  title = request.form.get("title")
  question = request.form.get("question")
  data_type = request.form.get("data_type")
  is_required = request.form.get("is_req")
  while(question):
    questions.append(question)
    dt.append(data_type)
    is_req.append(is_required)
    question = request.form.get("question"+str(i))
    data_type = request.form.get("data_type"+str(i))
    is_required = request.form.get("is_req"+str(i))
    i += 1
  Create(title,questions,is_req,dt,current_user.username)
  return "Thank You!"
