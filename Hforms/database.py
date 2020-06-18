from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import sqlite3

def Create(title,questions,is_required,data_type):
	i=0
	app = Flask(__name__)
	with app.app_context():

		DB_PATH = 'sqlite:///../test.db'
		app.config['SQLALCHEMY_DATABASE_URI'] = DB_PATH
		db = SQLAlchemy(app)
		class Question(db.Model):
			__tablename__ = title
			id = db.Column(db.Integer, primary_key = True)
		db.init_app(app)
		db.create_all()	

	conn = sqlite3.connect("test.db")
	c = conn.cursor()
	for ques in questions:
		if data_type[i] == 'Text':
			if is_required == 'True':
				addColumn = "ALTER TABLE '{}' ADD COLUMN '{}' VARCHAR NOT NULL DEFAULT 0".format(title,ques)
			else:
				addColumn = "ALTER TABLE '{}' ADD COLUMN '{}' VARCHAR".format(title,ques)
		elif data_type[i] == 'Number':
			if is_required == 'True':
				addColumn = "ALTER TABLE '{}' ADD COLUMN '{}' REAL NOT NULL DEFULAT 0".format(title,ques)
			else:
				addColumn = "ALTER TABLE '{}' ADD COLUMN '{}' REAL".format(title,ques)
		i+=1
		
		conn.execute(addColumn)
