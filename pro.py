from bs4 import BeautifulSoup
import requests
import re
from datetime import datetime
import time

def get_html(link):
	response = requests.get(link)
	soup = BeautifulSoup(response.text, "html.parser")
	return soup

def specialty_in_standard(url, specialty):
	not_empty = 0 
	soup = get_html(url)

	for i in soup.find_all("div", class_="name"):
		pattern = re.compile(specialty)
		result2 = pattern.findall(i.get_text())
		if not result2:
			not_empty = 0
		else: 
			not_empty = soup
			break

	return not_empty

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
	array_specialty_standard = []
	array_profstandarts_page = next_page(url)

	for x in array_profstandarts_page:
		soup = get_html("https://ppt.ru/docs/"+ x)

		for i in soup.find_all("a"):
			if i.get("href") is not None and re.match(r'/docs/profstandarts', i.get("href")) is not None:
				url = "https://ppt.ru"+ i.get("href")
				found_standard = specialty_in_standard(url, specialty)
				if found_standard != 0:
					array_specialty_standard.append({'name': i.get_text(), 'url': url})

	return array_specialty_standard

def main():
	start_time = datetime.now()

	specialty = "Программист"
	url_standard = "https://ppt.ru/docs/profstandarts"

	print(prof_standard(url_standard, specialty))

	print("PROGRAM TIME: ", datetime.now() - start_time)

if __name__ == '__main__':
	main()