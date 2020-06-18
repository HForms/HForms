from flask import Flask, render_template, request
from database import Create

app=Flask(__name__)

@app.route("/")
def index():
	return render_template("make.html")

@app.route("/make", methods = ["POST"])
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
	Create(title,questions,is_req,dt)
	return "Thank You!"

if __name__ == "__main__":
	app.run(debug=True)