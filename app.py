from flask import Flask, request, render_template, redirect, url_for, flash
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'cfef3ad9918b30369b7999ddd28a55d6'

@app.route('/')
def welcome():
	return render_template('welcome.html')

@app.route("/register", methods = ['GET', 'POST'])
def register():
	form = RegistrationForm()
	if (form.validate_on_submit()):
		flash('Account created for {}!'.format(form.username.data), 'success')
		return redirect(url_for('welcome'))
	return render_template('register.html', form = form, title = 'Register')

@app.route("/login", methods = ['GET', 'POST'])
def login():
	form = LoginForm()
	if (form.validate_on_submit()):
		if (form.email.data == 'admin@blog.com' and form.password.data == 'admin'):
			flash('You have been logged in!', 'success')
			return redirect(url_for('home'))
		else:
			flash('Login Unsuccessful. Check username and password', 'danger')
	return render_template('login.html', form = form, title = 'Login')

@app.route("/home")
def home():
	return render_template('home.html', title = 'Home')

@app.route("/about")
def about():
	return render_template('about.html')

@app.route('/makeforms')
def makeforms():
	return render_template("make.html", title = "Create a form")

@app.route("/make", methods = ["POST"])
def Add():
	question = request.form.get("question")
	return question

if __name__ == '__main__':
	app.run(host= '10.0.0.50', port=9000, debug=True)
