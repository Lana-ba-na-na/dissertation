import pymysql
from config import con_standard # модуль с данными для подключения к БД 

def database_connection(connectvars): # Функция подключения к БД
	localhost, user, password, db = connectvars
	try:
		conn = pymysql.connect(host = localhost, database = db, user = user, password = password)
	except:
		conn.rollback()

	return conn

def insert_prof_area(name_area, url_area):
	con = database_connection(con_standard.connection())
	cur = con.cursor()
	try:
		if not found_area(name_area):
			cur.execute('INSERT prof_area(name, url) VALUES ("%s", "%s")' % (name_area, url_area))
			con.commit()
	except:
		con.rollback()

	con.close()

def found_area(name_area):
	con = database_connection(con_standard.connection())
	cur = con.cursor()
	try:
		cur.execute('SELECT id, url FROM prof_area WHERE name = "%s"' % name_area)
		results = cur.fetchone()
	except:
		print ("Error: unable to fetch data")

	con.close()
	return results

def insert_prof_standard(name_standard, url_standard, general_information, id_area):
	con = database_connection(con_standard.connection())
	cur = con.cursor()
	try:
		if not found_id_standard(url_standard):
			cur.execute('INSERT prof_standard(name, url, activity, id_prof_area) VALUES ("%s", "%s", "%s", "%d")' % (name_standard, url_standard, general_information, id_area))
			con.commit()
		else:
			print ("such a standard exists")
	except:
		con.rollback()

	con.close()

def found_id_standard(url_standard):
	con = database_connection(con_standard.connection())
	cur = con.cursor()
	try:
		cur.execute('SELECT id FROM prof_standard WHERE url = "%s"' % url_standard)
		results = cur.fetchone()
	except:
		print ("Error: unable to fetch data")

	con.close()
	return results

def insert_information(name, id_information, function, text):
	con = database_connection(con_standard.connection())
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
	con = database_connection(con_standard.connection())
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

def select_activity():
	con = database_connection(con_standard.connection())
	cur = con.cursor()
	try:
		cur.execute('SELECT id, name, url FROM professional_activity')
		results = cur.fetchall()
	except:
		print ("Error: unable to fetch data")

	con.close()
	return results

def insert_language(name_language):
	con = database_connection(con_standard.connection())
	cur = con.cursor()
	try:
		if not select_language(name_language):
			cur.execute('INSERT programming_languages(name) VALUES ("%s")' % name_language)
			con.commit()
	except:
		con.rollback()

	con.close()

def select_language(name_language):
	con = database_connection(con_standard.connection())
	cur = con.cursor()
	try:
		cur.execute('SELECT id FROM programming_languages WHERE name =("%s")' % name_language)
		results = cur.fetchone()
	except:
		print ("Error: unable to fetch data")

	con.close()
	return results

def activity_language(id_language, id_activity):
	con = database_connection(con_standard.connection())
	cur = con.cursor()
	try:
		if not select_activity_language(id_language, id_activity):
			cur.execute('INSERT activity_language(id_activity, id_language) VALUES ("%d", "%d")' % (id_activity, id_language))
			con.commit()
	except:
		con.rollback()

	con.close()

def select_activity_language(id_language, id_activity):
	con = database_connection(con_standard.connection())
	cur = con.cursor()
	try:
		cur.execute('SELECT id FROM activity_language WHERE id_activity = ("%d") and id_language = ("%d") ' % (id_activity, id_language))
		results = cur.fetchall()
	except:
		print ("Error: unable to fetch data")

	con.close()
	return results

def skills_vacancy(name, quantity):
	con = database_connection(con_standard.connection())
	cur = con.cursor()
	try:
		if not select_skills_vacancy(name):
			cur.execute('INSERT skills_vacancy(name, quantity) VALUES ("%s", "%d")' % (name, quantity))
			con.commit()
		else:
			cur.execute('UPDATE skills_vacancy SET quantity = "%d" WHERE name = "%s"' % (quantity, name))
			con.commit()
	except:
		con.rollback()

	con.close()


def select_skills_vacancy(name):
	con = database_connection(con_standard.connection())
	cur = con.cursor()
	try:
		cur.execute('SELECT id FROM skills_vacancy WHERE name = ("%s")' % name)
		results = cur.fetchone()
	except:
		print ("Error: unable to fetch data")

	con.close()
	return results

def correlation_skills_activity():
	con = database_connection(con_standard.connection())
	cur = con.cursor()
	try:
		cur.execute('SELECT pa.id, sv.id \
					FROM activity_language as al \
					JOIN professional_activity as pa ON al.id_activity = pa.id \
					JOIN programming_languages as pl ON al.id_language = pl.id, \
					skills_vacancy as sv \
					WHERE sv.name = pl.name \
					GROUP BY pl.name')
		results = cur.fetchall()
	except:
		print ("Error: unable to fetch data")

	con.close()
	return results

def insert_correlation_skills_activity(id_activity, id_skills):
	con = database_connection(con_standard.connection())
	cur = con.cursor()
	try:
		cur.execute('INSERT skills_activity(id_activity, id_skills) VALUES ("%d", "%d")' % (id_activity, id_skills))
		con.commit()
	except:
		con.rollback()

	con.close()

def display():
	con = database_connection(con_standard.connection())
	cur = con.cursor()
	try:
		cur.execute('SELECT ps.name, pa.name, sv.name, sv.quantity \
					FROM activity_language as al \
					JOIN professional_activity as pa ON al.id_activity = pa.id \
					JOIN programming_languages as pl ON al.id_language = pl.id, \
					skills_vacancy as sv, activityps_activityvac as aa, prof_standard as ps \
					WHERE sv.name = pl.name and aa.standard_activity = ps.activity and aa.id_prof_activityvac = pa.id \
					GROUP BY pl.name')
		results = cur.fetchall()
	except:
		print ("Error: unable to fetch data")

	con.close()
	return results

def professional_activity():
	con = database_connection(con_standard.connection())
	cur = con.cursor()
	try:
		cur.execute('SELECT name FROM `professional_activity`')
		results = cur.fetchall()
	except:
		print ("Error: unable to fetch data")

	con.close()
	return results