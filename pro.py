from bs4 import BeautifulSoup
import requests
import re
from datetime import datetime
import time
import json
import memory_profiler

def get_html(url):
	response = requests.get(url)
	soup = BeautifulSoup(response.text, "html.parser")
	return soup

def labor_subfunction_competencies(url):
	soup = get_html('https://ppt.ru' + url)

	array_competencies = {}

	for i in soup.find_all('tr'):
		line_name = i.find('td')
		line_name = line_name.get_text()

		competencies = clear_text(soup, line_name)
		array_competencies[line_name] = competencies

	return array_competencies

def clear_text(soup, text):
	array = []
	text = soup.find(text=text)
	if text is not None:
		for i in text.findNext().find_all("li"):
			array.append(i.get_text())
	else: array = "Не указано требований"
	
	return array

def function_requirements(url):
	soup = get_html(url)

	education_title = "Требования к образованию и обучению"
	experience_title = "Требования к опыту практической работы"

	array_requirements = {
	education_title: clear_text(soup, education_title),
	experience_title: clear_text(soup, experience_title)
	}

	return array_requirements 

def get_url_function(url):
	subfunction_information, standard_information = [], []
	item = 0

	soup = get_html(url)
	general_information = soup.find(class_="description")

	for i in soup.find_all("tr"):
		if i.find("td"):
			if i.find("table"):
				labor_function = i.find("a")
				subfunction_quantity = len(i.findAll("a")) - 1
				function_requirement = function_requirements("https://ppt.ru" + labor_function.get('href'))
				subfunction_information = []
			else:
				item += 1
				labor_subfunction = i.find("a")
				subfunction_competencies = labor_subfunction_competencies(labor_subfunction.get('href'))
				subfunction_information.append({'name_labor_subfunction': labor_subfunction.get_text(), 'labor_subfunction': subfunction_competencies})
				if subfunction_quantity == item:
					standard_information.append({'name_labor_function': labor_function.get_text(), 'function_requirements': function_requirement, 'labor_subfunction': subfunction_information})
					del subfunction_information
					item = 0

	return general_information.get_text(), standard_information

def specialty_in_labor_function(url, specialty):
	empty = 0 
	soup = get_html(url)
	for i in soup.find_all("div", class_="prof-item"):
		text = re.sub('[%s]' % re.escape('-'), ' ', i.get_text())
		# result2 = re.findall(specialty.lower(), text.lower())
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

	for x in array_profstandarts_page:
		soup = get_html("https://ppt.ru/docs/"+ x)

		for i in soup.find_all("a"):
			if i.get("href") is not None and re.match(r'/docs/profstandarts', i.get("href")) is not None:
				url = "https://ppt.ru"+ i.get("href")
				found_standard = specialty_in_standard(url, specialty)
				if found_standard != 0:
					array_specialty_standard.append({'name_standard': i.get_text(), 'url_standard': url})

	for item in array_specialty_standard:
		soup = soup = get_html(item["url_standard"])
		found_standard = []
		for i in soup.find_all("tr"):
			if i.find("td"):
				if i.find("table"):
					labor_function = i.find("a")
					found_standard = specialty_in_labor_function("https://ppt.ru" + labor_function.get('href'), specialty)
					if found_standard != 0:
						array_found_standard.append({'name_standard': item["name_standard"], 'url_standard': item["url_standard"]})
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
		general_information, standard_information = get_url_function(i["url_standard"])
		data[k] = {"name_standard": i["name_standard"],"description": {"type_of_professional_activity": general_information, "labor_function": standard_information}}
		k += 1

	write_to_json(data)

	print("PROGRAM TIME: ", datetime.now() - start_time)

if __name__ == '__main__':
	main()