"""
	This module takes input the Kaggle dataset, named output.csv and gives
	the column extended dataset with English title added(dataset_with_titleEng.csv).
	For web scraping : BeautifulSoup was used 
"""
import requests
import bs4
import numpy as np
import re
import csv

firstline=True
## dataset extended with titles(in English)
title_file = open('dataset_with_titleEng.csv','a+')
comma=','
sep = '('

## url column in kaggle dataset
url_column = 4

## Initial dataset taken from Kaggle
with open('output.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	for row in readCSV:
		## Skip the first line, as it is a header
		if firstline:
			firstline=False
			continue
		## fetch the url of Kaggle dataset, one at a time
		res = requests.get(row[url_column])
		## check if response object is not null 
		if(res):

			## use bs4 to 
			soup = bs4.BeautifulSoup(res.text,'lxml')
			title_text = soup.select('title')
			title =title_text[0].getText()
			title = title.split(sep, 1)[0]

			## write old row entry, then add title column
			old_entry = ','.join(map(str,row))
			title_file.write(old_entry)
			title_file.write(comma)
			title_file.write(title)
			title_file.write('\n')
		else:
			continue