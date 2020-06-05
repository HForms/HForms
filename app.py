from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
  return render_template("make.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if(request.method == 'POST'):
		if(request.form['username'] != 'admin' or request.form['password'] != 'admin'):
			error = 'Login failed, invalid credentials'
		else:
			return redirect(url_for('home'))
	return render_template('login.html', error = error)

@app.route("/make", methods = ["POST"])
def Add():    
	question = request.form.get("question")
	return question

if __name__ == '__main__':
	app.run(host= '10.0.0.40', port=9000, debug=True)
