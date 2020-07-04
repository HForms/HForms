from flask import Flask
import psycopg2

def Create(title,questions,is_required,data_type,username):
	i=0

	try:
		username = username.replace('"',"'")
		DB_PATH = 'CREATE DATABASE "{}"'.format(username)
		conn = psycopg2.connect(user = '_username_', password = '_password_', host = '127.0.0.1', port = '5432')	#replace _string_ with actual username/password
		conn.autocommit = True
		cur = conn.cursor()
		cur.execute(DB_PATH)
	except psycopg2.errors.DuplicateDatabase:
		conn = psycopg2.connect(database = '{}'.format(username), user = '_username_', password = '_password_', host = '127.0.0.1', port = '5432')		#replace _string_ with actual username/password
		conn.autocommit = True
		cur = conn.cursor()

	try:
		title = title.replace('"',"'")
		addColumn = 'CREATE TABLE "{}" (id SERIAL PRIMARY KEY NOT NULL);'.format(title)
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
	except psycopg2.errors.DuplicateTable:
		return 0
	conn.close()
	return 1

def Questions(title,username):
	conn = psycopg2.connect(database = '{}'.format(username), user = '_username_', password = '_password_', host = '127.0.0.1', port = '5432')		#replace _string_ with actual username/password
	cur = conn.cursor()
	cur.execute('SELECT * from "{}"'.format(title))
	questions = next(zip(*cur.description))
	conn.close()
	return questions

def Is_Required(title,username):
	conn = psycopg2.connect(database = '{}'.format(username), user = '_username_', password = '_password_', host = '127.0.0.1', port = '5432')		#replace _string_ with actual username/password
	cur = conn.cursor()
	cur.execute('SELECT is_nullable FROM information_schema.columns WHERE table_name = %s',(title,))
	is_req = cur.fetchall()
	conn.close()
	return is_req

def Data_Type(title,username):
	conn = psycopg2.connect(database = '{}'.format(username), user = '_username_', password = '_password_', host = '127.0.0.1', port = '5432')		#replace _string_ with actual username/password
	cur = conn.cursor()
	cur.execute('SELECT data_type FROM information_schema.columns WHERE table_name = %s',(title,))
	data_type = cur.fetchall()
	conn.close()
	return data_type

def Answers(title,username,questions,answers):
	try:
		conn = psycopg2.connect(database = '{}'.format(username), user = '_username_', password = '_password_', host = '127.0.0.1', port = '5432')		#replace _string_ with actual username/password
		conn.autocommit = True
		cur = conn.cursor()
		questions = list(questions)
		questions.pop(0)
		questions = tuple(questions)
		questions = str(questions).replace("'",'"')
		answers = tuple(answers)
		addAnswer = """INSERT INTO "{}" {} VALUES {}""".format(title,questions,answers)
		cur.execute(addAnswer)
		conn.close()
	except psycopg2.errors.InvalidTextRepresentation:
		return 0
	return 1
