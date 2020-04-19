from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("make.html")

@app.route("/make", methods = ["POST"])
def Add():    
    question = request.form.get("question")
    return question