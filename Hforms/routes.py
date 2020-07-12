from flask import render_template, url_for, flash, redirect, request, send_file
from Hforms import app, db, bcrypt
from Hforms.forms import RegistrationForm, LoginForm
from Hforms.dbModels import User
from flask_login import login_user, current_user, logout_user, login_required
from Hforms.dbHandler import Create, Questions, Answers, Is_Required, Data_Type, Table, File
from Hforms.urls import make_url, get_url

@app.route('/')
def welcome():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	return render_template('welcome.html', title = 'Welcome')

@app.route("/register", methods = ['GET', 'POST'])
def register():
	if current_user.is_authenticated:
		return redirect(url_for('home'))
	form = RegistrationForm()
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
		user = User(username = form.username.data, password = hashed_password)
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
		user = User.query.filter_by(username = form.username.data).first()
		if user and bcrypt.check_password_hash(user.password, form.password.data):
			login_user(user, remember = form.remember.data)
			next_page  = request.args.get('next')
			return redirect(next_page) if next_page else redirect(url_for('home'))
		else:
			flash('Login Unsuccessful. Check username and password', 'danger')
	return render_template('login.html', form = form, title = 'Login')

@app.route("/logout")
def logout():
	logout_user()
	return redirect(url_for('welcome'))

@app.route("/about")
def about():
	return render_template('about.html', title = 'About')

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
	if(Create(title,questions,is_req,dt,current_user.username)):
		user = User.query.filter_by(username = current_user.username).first()
		url = make_url(user,title)
		flash('Thank You for making a form! Click <a href="{}/{}" target = "_blank">here</a> to fill the form.'.format('https://hforms.me', url), 'success')
	else:
		flash('A form with the name {} alredy exists. Please create a form with a different name.'.format(title), 'danger')
	
	return redirect(url_for('home'))

@app.route("/<url>", methods = ["GET","POST"])
def An(url):
	try:
		li = get_url(url)
		user = User.query.filter_by(username = li[0]).first()
		questions = Questions(li[1],user.username)
		is_req = Is_Required(li[1],user.username)
		data_type = Data_Type(li[1],user.username)
		return render_template("form_layout.html",questions = questions, is_req = is_req, data_type = data_type, url=url, form_name=li[1])
	except:
		if(url != 'favicon.ico'):
			flash("Error 404 page not found ;-;", 'danger')
			return redirect(url_for('welcome'))
		# return "Error 404 page not found ;-;"
		else:
			return 'favicon.ico not found'

@app.route("/answers", methods = ["POST"])
def Ans():
	url = request.form.get("url")
	li = get_url(url)
	user = User.query.filter_by(username = li[0]).first()
	questions = Questions(li[1],user.username)
	answers = []
	for i in range(1,len(questions)):
		answer = request.form.get("answer"+str(i))
		answers.append(answer)
	if(Answers(li[1],user.username,questions,answers)):
		flash("Your responses have been saved. Thanks for using HForms :)")
	else:
		flash("Please enter correct data in the form")
	return redirect(url_for('welcome'))

@app.route("/download", methods = ['GET','POST'])
@login_required
def Tables():
	user = User.query.filter_by(username = current_user.username).first()
	table = Table(user.username)
	return render_template('download.html', titles = table)

@app.route("/csv", methods = ['POST'])
@login_required
def download():
	table = request.form.get("option")
	user = User.query.filter_by(username = current_user.username).first()
	File(table, user.username)
	return send_file('{}.csv'.format(table), mimetype='text/csv', attachment_filename='{}.csv'.format(table), as_attachment=True)
