from flask import Flask, request, render_template, redirect, url_for, session, flash

app = Flask(__name__)

app.secret_key = "secret"

@app.route('/')
def welcome():
	return render_template('welcome.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if(request.method == 'POST'):
		if(request.form['username'] != 'admin' or request.form['password'] != 'admin'):
			error = 'Login failed, invalid credentials'
		else:
			session['logged_in'] = True
			flash('You were just logged in!')
			return redirect(url_for('home'))
	return render_template('login.html', error = error)
	# TODO : add unique users

@app.route('/home')
def home():
	try:
		return render_template('home.html', status = session['logged_in'])
	except:
		flash('You need to login first!')
		return redirect(url_for('login'))

@app.route('/logout')
def logout():
	session.pop('logged_in', None)
	flash('You are logged out!')
	return redirect(url_for('welcome'))

@app.route('/make-forms')
def index():
	return render_template("make.html")

@app.route("/make", methods = ["POST"])
def Add():
	question = request.form.get("question")
	return question

if __name__ == '__main__':
	app.run(host= '10.0.0.40', port=9000, debug=True)