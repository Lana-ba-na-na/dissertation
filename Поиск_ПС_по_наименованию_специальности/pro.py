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
		print(x)
		soup = get_html("https://ppt.ru/docs/"+ x)

		for i in soup.find_all("a"):
			if i.get("href") is not None and re.match(r'/docs/profstandarts', i.get("href")) is not None:
				url = "https://ppt.ru"+ i.get("href")
				k += 1
				print(k)
				found_standard = specialty_in_standard(url, specialty)

				if found_standard != 0:
					array_specialty_standard.append({'name_standard': i.get_text(), 'url_standard': url })

	for item in array_specialty_standard:
		soup = get_html(item["url_standard"])
		found_standard = ''
		general_information = soup.find(class_="description")

		for i in soup.find_all("tr"):
			if i.find("td"):
				if i.find("table"):
					labor_function = i.find("a")
					found_standard = specialty_in_labor_function("https://ppt.ru" + labor_function.get('href'), specialty)
					if found_standard:
						array_found_standard.append({'name_standard': item["name_standard"], 'url_standard': item["url_standard"], 'general_information': general_information.get_text()})
						database.insert_prof_standard(item["name_standard"], item["url_standard"], general_information.get_text())
						break

	return array_found_standard

def write_to_json(data):
	with open("data_file.json", "w", encoding="utf-8") as write_file:
		json.dump(data, write_file, ensure_ascii=False, sort_keys=True, indent=4)

# @profile
def main():
	start_time = datetime.now()

	specialty = "Программист"
	url_standard = "https://ppt.ru/docs/profstandarts"

	array_standard = prof_standard(url_standard, specialty)
	print(array_standard)
	data = {}
	k = 0
	for i in array_standard:
		k += 1
		url_standard = i["url_standard"]
		id_standard = database.found_id_standard(url_standard)
		standard_information = get_url_function(url_standard, id_standard[0])
		data[k] = {"name_standard": i["name_standard"],"description": {"type_of_professional_activity": i["general_information"], "labor_function": standard_information}}

	write_to_json(data)

	print("PROGRAM TIME: ", datetime.now() - start_time)

if __name__ == '__main__':
	main()