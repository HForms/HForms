from flask import Flask
import psycopg2

def Create(title,questions,is_required,data_type,username):
	i=0

	try:
		DB_PATH = 'CREATE DATABASE "{}"'.format(username)
		conn = psycopg2.connect(user = '_username_', password = '_password_', host = '127.0.0.1', port = '5432')	#replace _string_ with actual username/password
		conn.autocommit = True
		cur = conn.cursor()
		cur.execute(DB_PATH)
		conn.close()
	except psycopg2.errors.DuplicateDatabase:
		conn = psycopg2.connect(database = '{}'.format(username), user = '_username_', password = '_password_', host = '127.0.0.1', port = '5432')		#replace _string_ with actual username/password
		conn.autocommit = True
		cur = conn.cursor()

	addColumn = 'CREATE TABLE "{}" (id SERIAL PRIMARY KEY NOT NULL);'.format(title)
	cur.execute(addColumn)
	for ques in questions:
		ques = ques.replace('"',"'")
		if data_type[i] == 'Text':
			if is_required == 'True':
				addColumn = 'ALTER TABLE "{}" ADD COLUMN "{}" TEXT NOT NULL DEFAULT 0'.format(title,ques)
			else:
				addColumn = 'ALTER TABLE "{}" ADD COLUMN "{}" TEXT'.format(title,ques)
		elif data_type[i] == 'Number':
			if is_required == 'True':
				addColumn = 'ALTER TABLE "{}" ADD COLUMN "{}" REAL NOT NULL DEFULAT 0'.format(title,ques)
			else:
				addColumn = 'ALTER TABLE "{}" ADD COLUMN "{}" REAL'.format(title,ques)
		i+=1
		
		cur.execute(addColumn)
	
	conn.close()
