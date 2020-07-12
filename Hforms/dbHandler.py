from flask import Flask
import sqlite3
import csv

def database(username):
	db = "DB/{}.db".format(username)
	conn = sqlite3.connect(db, isolation_level=None)
	return conn

def Create(title,questions,is_required,data_type,username):
	i=0

	username = username.replace('"',"'")
	conn = database(username)
	cur = conn.cursor()

	try:
		title = title.replace('"',"'")
		addColumn = 'CREATE TABLE "{}" (id INTEGER PRIMARY KEY)'.format(title)
		cur.execute(addColumn)
		for ques in questions:
			ques = ques.replace('"',"'")
			if data_type[i] == 'Text':
				if is_required[i] == 'True':
					addColumn = 'ALTER TABLE "{}" ADD COLUMN "{}" TEXT NOT NULL DEFAULT 0'.format(title,ques)
				else:
					addColumn = 'ALTER TABLE "{}" ADD COLUMN "{}" TEXT'.format(title,ques)
			elif data_type[i] == 'Number':
				if is_required[i] == 'True':
					addColumn = 'ALTER TABLE "{}" ADD COLUMN "{}" REAL NOT NULL DEFAULT 0'.format(title,ques)
				else:
					addColumn = 'ALTER TABLE "{}" ADD COLUMN "{}" REAL'.format(title,ques)
			i+=1
			
			cur.execute(addColumn)
	except sqlite3.OperationalError:
		return 0
	conn.close()
	return 1

def Questions(title,username):
	conn = database(username)
	cur = conn.cursor()
	cur.execute('SELECT * from "{}"'.format(title))
	questions = next(zip(*cur.description))
	conn.close()
	return questions

def Is_Required(title,username):
	conn = database(username)
	cur = conn.cursor()
	cur.execute('PRAGMA TABLE_INFO("{}")'.format(title))
	is_req = [info[3] for info in cur.fetchall()]
	conn.close()
	return is_req

def Data_Type(title,username):
	conn = database(username)
	cur = conn.cursor()
	cur.execute('PRAGMA TABLE_INFO("{}")'.format(title))
	data_type = [info[2] for info in cur.fetchall()]
	conn.close()
	return data_type

def Answers(title,username,questions,answers):
	try:
		conn = database(username)
		cur = conn.cursor()
		questions = list(questions)
		questions.pop(0)
		questions = tuple(questions)
		questions = str(questions).replace("'",'"')
		answers = tuple(answers)
		addAnswer = """INSERT INTO "{}" {} VALUES {}""".format(title,questions,answers)
		cur.execute(addAnswer)
		conn.close()
	except:
		return 0
	return 1

def Table(username):
	conn = database(username)
	cur = conn.cursor()
	cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
	tables = cur.fetchall()
	conn.close()
	return tables

def File(title,username):
	conn = database(username)
	cur = conn.cursor()
	exe = 'Select * from "{}"'.format(title)
	cur.execute(exe)
	with open("Hforms/{}.csv".format(title),'w') as file:
		writer = csv.writer(file,delimiter = '\t')
		writer.writerow([row[0] for row in cur.description])
		writer.writerows(cur)
