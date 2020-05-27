import pymysql
import connectvars

def database_connection(connectvars):
	localhost, user, password, db = connectvars
	try:
		conn = pymysql.connect(host = localhost, database = db, user = user, password = password)
	except:
		conn.rollback()

	return conn

def insert_prof_standard(name_standard, url_standard, general_information):
	con = database_connection(connectvars.connection())
	cur = con.cursor()
	try:
		if not found_id_standard(url_standard):
			cur.execute('INSERT prof_standard(name, url, activity) VALUES ("%s", "%s", "%s")' % (name_standard, url_standard, general_information))
			con.commit()
		else:
			print ("such a standard exists")
	except:
		con.rollback()

	con.close()

def found_id_standard(url_standard):
	con = database_connection(connectvars.connection())
	cur = con.cursor()
	try:
		cur.execute('SELECT id FROM prof_standard WHERE url = "%s"' % url_standard)
		results = cur.fetchone()
	except:
		print ("Error: unable to fetch data")

	con.close()
	return results

def insert_information(name, id_information, function, text):
	con = database_connection(connectvars.connection())
	cur = con.cursor()
	try:
		if function == "labor_function" and text == "Требования к образованию и обучению":
			cur.execute('INSERT education_requirement(name, id_function) VALUES ("%s", "%d")' % (name, id_information))
			con.commit() 
		elif function == "labor_function" and text == "Требования к опыту практической работы":
			cur.execute('INSERT experience(name, id_function) VALUES ("%s", "%d")' % (name, id_information))
			con.commit()
		elif function == "subfunction" and text == "Трудовые действия":
			cur.execute('INSERT labor_action(name, id_subfunctions) VALUES ("%s", "%d")' % (name, id_information))
			con.commit()
		elif function == "subfunction" and  text == "Требования к образованию и обучению":
			cur.execute('INSERT necessary_knowledge(name, id_subfunctions) VALUES ("%s", "%d")' % (name, id_information))
			con.commit()
		elif function == "subfunction" and  text == "Требования к опыту практической работы":
			cur.execute('INSERT necessary_skills(name, id_subfunctions) VALUES ("%s", "%d")' % (name, id_information))
			con.commit()
		elif function == "labor_function" and text == "Особые условия допуска к работе":
			print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
		elif function == "labor_function":
			cur.execute('INSERT labor_function(name, id_prof_standard) VALUES ("%s", "%d")' % (name, id_information))
			con.commit() 
		elif function == "subfunction":
			cur.execute('INSERT subfunctions(name, id_function) VALUES ("%s", "%d")' % (name, id_information))
			con.commit() 
	except:
		con.rollback()

	con.close()

def found_id_information(name, id_standard, function):
	con = database_connection(connectvars.connection())
	cur = con.cursor()
	try:
		if function == "labor_function":
			cur.execute('SELECT id FROM labor_function WHERE name = "%s" and id_prof_standard = "%d"' % (name, id_standard))
			results = cur.fetchone()
		elif function == "subfunction":
			cur.execute('SELECT id FROM subfunctions WHERE name = "%s" and id_function = "%d"' % (name, id_standard))
			results = cur.fetchone()
	except:
		print ("Error: unable to fetch data")

	con.close()
	return results

def url_prof():
	con = database_connection(connectvars.connection())
	cur = con.cursor()
	try:
		cur.execute('SELECT id, url FROM prof_standard')
		results = cur.fetchall()
	except:
		print ("Error: unable to fetch data")

	con.close()
	return results
