# encoding: utf-8
## -*- coding: utf-8 -*-

import datetime
import urllib.request
import re
from bs4 import BeautifulSoup

text_file = open("Output.txt", "w")

CATEGORIES = ["firstpage","rokomari","country","capital","world","capitalcity","bangla","editorial","business","entertainment","sports","lastpage"]

now = datetime.datetime.now()
current_date = str(now.day) + "-" + str(now.month) + "-" + str(now.year)
for news in CATEGORIES:
	with urllib.request.urlopen('http://www.prothom-alo.com/tp-' + news + '/' + current_date) as response:
	   html_doc_1 = response.read()
	soup_1 = BeautifulSoup(html_doc_1, 'html.parser')

	for link in soup_1.find_all('a'):
		article_link = link.get('href')
		if re.search("/article/", article_link):
			with urllib.request.urlopen('http://www.prothom-alo.com' + article_link) as response:
	   			html_doc_2 = response.read()
			soup_2 = BeautifulSoup(html_doc_2, 'html.parser')
			text_file.write(soup_2.get_text())
			#print(link.get('href'))
text_file.close()
#print(soup.prettify())






