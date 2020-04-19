from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)
fun_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

@app.route('/')
def home():
	return "Hello world! Click <a href={}>here</a> for some fun XD".format(fun_url)

@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if(request.method == 'POST'):
		if(request.form['username'] != 'admin' or request.form['password'] != 'admin'):
			error = 'Login failed, invalid credentials'
		else:
			return redirect(url_for('home'))
	return render_template('login.html', error = error)

if __name__ == '__main__':
	app.run(debug=True)