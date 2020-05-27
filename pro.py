from bs4 import BeautifulSoup
import requests
import re
from datetime import datetime
import time
import json
import memory_profiler
import database #модуль работы с БД

def get_html(url): 
	response = requests.get(url)
	soup = BeautifulSoup(response.text, "html.parser")
	return soup

def function_requirements(url):  # Вспомогательная функция извлечения требований из ПС
	soup = get_html('https://ppt.ru' + url)

	array_competencies = {}

	for i in soup.find_all('tr'):
		line_name = i.find('td')
		line_name = line_name.get_text()

		competencies = clear_text(soup, line_name)
		if competencies:
			array_competencies[line_name] = competencies

	return array_competencies

def clear_text(soup, text):  # Вспомогательная функция к функции function_requirements
	array = []
	set_point = soup.find(text=text)
	if set_point is not None:
		for i in set_point.findNext().find_all("li"):
			array.append(i.get_text())
	else: array = "Не указано требований"
	
	return array

def get_url_function(url, id_standard):  # Функция извлечения требований из ПС
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
							for text in value:
								database.insert_information(text, id_labor_subfunction[0], function, key)
					del subfunction_information
					item = 0

	return standard_information

def specialty_in_labor_function(url, specialty): #Функция нахождения наименования специальности ОКЗ в обобщенной трудовой функции
	empty = 0 
	soup = get_html(url)
	for i in soup.find_all("div", class_="description"):
		for j in i.find_all("td", text="ОКЗ"):
			for k in j.findNext():
				for t in k.findNext():
					pattern = re.compile(specialty)
					result2 = pattern.findall(i.get_text())
					if result2:
						empty = 1
						break
					else: 
						empty = 0
	return empty

def specialty_in_standard(url, specialty): #Функция нахождения наименовании специальности в пункте "Группы занятий" в ПС 
	empty = 0 
	soup = get_html(url)

	for i in soup.find_all("div", class_="name"):
		pattern = re.compile(specialty)
		result2 = pattern.findall(i.get_text())
		if result2:
			empty = result2 
			break
		else: 
			empty = 0

	return empty

def next_page(url): # Прохождение пагинации
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

def found_standard(specialty, param): # Функция находит ПС на сайте https://ppt.ru/docs/profstandarts
	array_specialty_standard, array_found_standard = [], 0
	url = "https://ppt.ru/docs/profstandarts"
	array_profstandarts_page = next_page(url)

	for x in array_profstandarts_page:
		soup = get_html("https://ppt.ru/docs/"+ x)

		for i in soup.find_all("a"):
			if i.get("href") is not None and re.match(r'/docs/profstandarts', i.get("href")) is not None:
				if i.get_text() == param:
					array_specialty_standard.append({'name_standard': i.get_text(), 'url_standard': "https://ppt.ru"+ i.get("href") })
	for item in array_specialty_standard:
		url = item["url_standard"]
		soup = get_html(url)
		general_information = soup.find(class_="description")
		found_standard = specialty_in_standard(url, specialty)
		if found_standard != 0:
			for i in soup.find_all("tr"):
				if i.find("td"):
					if i.find("table"):
						labor_function = i.find("a")
						found_standard = specialty_in_labor_function("https://ppt.ru" + labor_function.get('href'), specialty)
						if found_standard != 0:
							array_found_standard = {'name_standard': item["name_standard"], 'url_standard': item["url_standard"], 'general_information': general_information.get_text()}
							database.insert_prof_standard(item["name_standard"], item["url_standard"], general_information.get_text())
						

	return array_found_standard

def get_html_area(url): 
	headers = {'User-Agent':"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36 OPR/68.0.3618.63"}
	response = requests.get(url, headers=headers)
	soup = BeautifulSoup(response.text, 'html.parser')
	return soup

def prof_area(): # Функция извлекает виды профессиональной области ПС
	area = []
	url = "https://classinform.ru/profstandarty.html"
	soup = get_html_area(url)

	for i in soup.find_all("div", class_="four_fifth"):
		param = i.find("a")
		if param is not None:
			area.append({"name_area": param.get_text(), "url_area": param.get("href")})
			database.insert_prof_area(param.get_text(), param.get("href"))

	return area

def area_standard(url): # Функция извлечения наименований ПС выбранной области
	soup = get_html_area(url)
	arr_standard = []

	for i in soup.find_all("div", class_="four_fifth"):
		param = i.find("a")
		if param is not None and re.search(r'\d', param.get("href")):
			arr_standard.append(param.get_text())

	return arr_standard

# @profile
def main(prof_area, specialty): # Основная функция программы
	start_time = datetime.now()
	print(start_time)
	array_standard = []

	url = database.found_area(prof_area)
	url = 'https://classinform.ru/' + url[0]

	for i in area_standard(url):
		standard = found_standard(specialty, i)
		if standard != 0:
			array_standard.append(standard)

	# for j in array_standard:
	# 	url_standard = j["url_standard"]
	# 	id_standard = database.found_id_standard(url_standard)
	# 	standard_information = get_url_function(url_standard, id_standard[0])

	print("PROGRAM TIME: ", datetime.now() - start_time)

	return array_standard

# if __name__ == '__main__':
# 	main()