from bs4 import BeautifulSoup
import requests
import re
from datetime import datetime
import time
import json
import memory_profiler
import database

def get_html(url):
	response = requests.get(url)
	soup = BeautifulSoup(response.text, "html.parser")
	return soup

def function_requirements(url):
	soup = get_html('https://ppt.ru' + url)

	array_competencies = {}

	for i in soup.find_all('tr'):
		line_name = i.find('td')
		line_name = line_name.get_text()

		competencies = clear_text(soup, line_name)
		if competencies:
			array_competencies[line_name] = competencies

	return array_competencies

def clear_text(soup, text):
	array = []
	set_point = soup.find(text=text)
	if set_point is not None:
		for i in set_point.findNext().find_all("li"):
			array.append(i.get_text())
	else: array = "Не указано требований"
	
	return array

def get_url_function(url, id_standard):
	subfunction_information, standard_information = [], []
	item = 0

	soup = get_html(url)

	for i in soup.find_all("tr"):
		if i.find("td"):
			if i.find("table"):
				labor_function = i.find("a")
				function = 'labor_function'
				text =''
				database.insert_information(labor_function.get_text(), id_standard, function, text)
				subfunction_quantity = len(i.findAll("a")) - 1
				id_labor_function = database.found_id_information(labor_function.get_text(), id_standard, function)
				function_requirement = function_requirements(labor_function.get('href'))
				for key, value in function_requirement.items():
					print(key)
					for text in value:
						database.insert_information(text, id_labor_function[0], function, key)
				subfunction_information = []
			else:
				item += 1
				labor_subfunction = i.find("a")
				function = "subfunction"
				text =''
				subfunction_competencies = function_requirements(labor_subfunction.get('href'))
				subfunction_information.append({'name_labor_subfunction': labor_subfunction.get_text(), 'labor_subfunction': subfunction_competencies})
				if subfunction_quantity == item:
					standard_information.append({'name_labor_function': labor_function.get_text(), 'function_requirements': function_requirement, 'labor_subfunction': subfunction_information})
					for k in subfunction_information:
						database.insert_information(k['name_labor_subfunction'], id_labor_function[0], function, text)
						id_labor_subfunction = database.found_id_information(k['name_labor_subfunction'], id_labor_function[0], function)
						labor_subfunction = k['labor_subfunction']
						for key, value in labor_subfunction.items():
							print(key)
							for text in value:
								database.insert_information(text, id_labor_subfunction[0], function, key)
					del subfunction_information
					item = 0

	return standard_information

def specialty_in_labor_function(url, specialty):
	empty = 0 
	soup = get_html(url)
	for i in soup.find_all("div", class_="prof-item"):
		text = re.sub('[%s]' % re.escape('-'), ' ', i.get_text())
		if re.findall(specialty.lower(), text.lower()):
			empty = 1
			break
		else: 
			empty = 0
	return empty

def specialty_in_standard(url, specialty):
	empty = 0 
	soup = get_html(url)

	for i in soup.find_all("div", class_="name"):
		pattern = re.compile(specialty)
		result2 = pattern.findall(i.get_text())
		if result2:
			empty = 1
			break
		else: 
			empty = 0

	return empty

def next_page(url):
	array_profstandarts_page = []
	soup = get_html(url)

	for i in soup.find_all("a"):
		if i.get("href") is not None:
			if re.match(r'profstandarts/page', i.get("href")) is not None:
				if array_profstandarts_page and array_profstandarts_page[0] == i.get("href"):
					break
				else:
					array_profstandarts_page.append(i.get("href"))

	return array_profstandarts_page

def prof_standard(url, specialty):
	array_specialty_standard, array_found_standard = [], []
	array_profstandarts_page = next_page(url)
	k = 0
	for x in array_profstandarts_page:
		soup = get_html("https://ppt.ru/docs/"+ x)

		for i in soup.find_all("a"):
			if i.get("href") is not None and re.match(r'/docs/profstandarts', i.get("href")) is not None:
				if i.get_text() == specialty:
					array_specialty_standard.append({'name_standard': i.get_text(), 'url_standard': "https://ppt.ru"+ i.get("href") })

	for item in array_specialty_standard:
		soup = get_html(item["url_standard"])
		general_information = soup.find(class_="description")
		array_found_standard.append({'name_standard': item["name_standard"], 'url_standard': item["url_standard"], 'general_information': general_information.get_text()})
		database.insert_prof_standard(item["name_standard"], item["url_standard"], general_information.get_text())
						

	return array_found_standard

def get_html_1(url):
	headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36 OPR/68.0.3618.63"}
	response = requests.get(url, headers=headers)
	soup = BeautifulSoup(response.text, 'html.parser')
	return soup

def fses_of_hpe(id_fses, url):
	soup = get_html_1(url)

	for i in soup.find_all("div", style="text-indent:5.05mm;"):
		text = re.findall('"(.*?)"', i.get_text())
		if text != []:
			database.insert_fses(text[0], id_fses)
			print(text[0])

# @profile
def main():
	start_time = datetime.now()
	print(start_time)

	# for i in database.found_fses():

	# 	fses_of_hpe(i[0], i[1])

	url = "https://ppt.ru/docs/profstandarts"

	k = 0
	for i in database.found_standard():
		array_standard = prof_standard(url, i[0])
		for j in array_standard:
			k += 1
			url_standard = j["url_standard"]
			print(url_standard)
			id_standard = database.found_id_standard(url_standard)
			standard_information = get_url_function(url_standard, id_standard[0])

	print("PROGRAM TIME: ", datetime.now() - start_time)

if __name__ == '__main__':
	main()