from bs4 import BeautifulSoup
import requests
import re
from datetime import datetime
import time
import db_standard
import csv

def get_html(url): 
	response = requests.get(url)
	soup = BeautifulSoup(response.text, "html.parser")
	return soup

def insert_db(language, id_activity):
	db_standard.insert_language(language)
	id_language = db_standard.select_language(language)
	db_standard.activity_language(id_language[0], id_activity)

def language_extraction():
	activity = db_standard.select_activity()

	for i in activity:
		if i[2] is not None and re.match(r'https://ru.wikipedia.org', i[2]):
			soup = get_html(i[2])
			for j in soup.find_all("div", style="padding:0em 0.25em"):
				for k in j.find_all("li"):
					insert_db(k.get_text(), i[0])
		elif i[2] is not None and re.match(r'https://scand.com', i[2]):
			soup = get_html(i[2])
			for t in soup.find_all('div', class_="technologies-search-list__item-inner-list__item-text"):
				for q in t.find_all("li"):
					item = re.sub(r'\([^()]*\)', '', q.get_text())
					item = item.split(',')
					for q1 in item:
						insert_db(q1.strip(), i[0])
		else: 
			continue

def read_tsv():
	data = []

	with open("skills.tsv", encoding='utf-8') as f:
	    for row in csv.reader(f, delimiter='\t'):
	    	if int(row[1]) >= 190:
	    		data.append({"skills": row[0], "quantity": row[1]})
	    		db_standard.skills_vacancy(row[0], int(row[1]))
	    	else:
	    		continue

	return data