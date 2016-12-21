# encoding: utf-8
## -*- coding: utf-8 -*-

import datetime
import urllib
import re
from bs4 import BeautifulSoup
#from sets import Set

text_file = open("jugantor.txt", "w")





CATEGORIES_PA = ["first-page",																																																																																																																																												"last-page","sports","news","industry-trade","anando-nagar","oneday-everyday","window","bangla-face","city","dristipat","it-world","the-northern-town","our-chittagong","two-leaves-and-a-bud","select-nasik"]

now = datetime.datetime.now()
current_date = str(now.day) + "-" + str(now.month) + "-" + str(now.year)
for news in CATEGORIES_PA:
	with urllib.request.urlopen('http://www.jugantor.com/' + news) as response:
	   html_doc_1 = response.read()
	   print(html_doc_1)
	soup_1 = BeautifulSoup(html_doc_1, 'html.parser')
	link_set = set([])
	for link in soup_1.find_all('a'):
		article_link = link.get('href')
		if re.search("http://www.jugantor.com/"+news, article_link):
			#print(news)
			if(article_link not in link_set):
				link_set.add(article_link)
				print(article_link)
				#article_link = article_link[15:]
				#print(article_link)
				#VALID_TAGS = ['div', 'p']
				#soup = BeautifulSoup(article_link)

				soup = BeautifulSoup(urllib.request.urlopen(article_link))

				tags = soup('p')
				for tag in tags:
					text_file.write(tag.get_text())


				#for tag in soup.findAll('p'):
				#   if tag.name not in VALID_TAGS:
				 #       tag.replaceWith(tag.renderContents())

				#print( soup.renderContents() )
				#with urllib.request.urlopen(article_link) as response:
		   		#	html_doc_2 = response.read()
				#soup_2 = BeautifulSoup(html_doc_2, 'html.parser')
				#text_file.write(soup_2.find('p').get_text())

text_file.write('\n\n')

text_file.close()
#print(soup.prettify())

