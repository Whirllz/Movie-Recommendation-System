"""
	This module takes input the title extended dataset, named dataset_with_titleEng.csv and gives
	the extended dataset with acto(s),character(s),storyline etc.(dataset.csv)
	For web scraping : BeautifulSoup was used 
	For cleaning data and NLP : nltk library was used
"""

import requests
import bs4
import numpy as np
import re
import csv 
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
from nltk.tokenize import RegexpTokenizer
from nltk.stem import PorterStemmer 

## using stemming in python library
ps = PorterStemmer()

## stop word removal
stop_words = set(stopwords.words('english'))

## url column in dataset_with_titleEng.csv
url_column = 4

'''
new extended dataset with added columns => dataset.csv
Columns added :  
actor(s)
character(s)
story line
'''

final_dataset = open('dataset.csv','w')
firstline=True
comma=','

## dataset extended with English title  
with open('dataset_with_titleEng.csv') as csvfile:
	readCSV = csv.reader(csvfile, delimiter=',')
	for row in readCSV:
		## skip the first line, as it is a header
		if firstline:
			firstline=False
			continue
		## fetch the url of dataset_with_titleEng.csv, one at a time
		res = requests.get(row[url_column])
		soup = bs4.BeautifulSoup(res.text,'lxml')
		act=[] 				# actor list
		ch=[]				# character list


		# add all actor(s) and character(s) in act, ch list :
		for table in soup.find_all('table', attrs={'class': 'cast_list'}):
			for table_data in table.find_all('td'):
				for actor in table_data.find_all('a',href=re.compile('.*name/.*')):
					act.append(actor.text)
			for chars in table.find_all('td',attrs={'class':'character'}):
				ch.append(chars.text)


		# clean the actor list 		
		act = list(map(lambda s: s.strip(), act))		# remove spaces at ends 
		act = list(map(lambda s:s.replace("\n", ""),act)) # remove extra next lines
		act = list(filter(None,act))	# remove null values from list
		act = list(map(lambda s:' '.join(s.split()),act)) # split by spaces
		actor_string = ' | '.join(map(str,act))		# join actors by |
		actor_string.replace(",", " ")	# since csv with comma as separator
		actor_string = actor_string.lower()		
		actor_string +=comma


		# clean the character list
		ch = list(map(lambda s: s.strip(), ch))
		ch = list(map(lambda s:s.replace("\n", ""),ch))
		ch = list(filter(None,ch))
		ch = list(map(lambda s:' '.join(s.split()),ch))
		character_string = ' | '.join(map(str,ch))
		character_string.replace(","," ")
		character_string = character_string.lower()		
		character_string+=comma
		old_row = ','.join(map(str,row))
		old_row+=comma 
		final_dataset.write(old_row)
		final_dataset.write(actor_string)
		final_dataset.write(character_string)

		## take storyline from the url  
		for story in soup.find_all('div', attrs={'class': 'inline canwrap'}):
			summary = story.text
			
			## make all characters small
			summary = summary.lower()
			
			## remove "written by" at the end of each storyline
			sep = 'written'
			summary = summary.split(sep, 1)[0]

			## to remove  punctutations
			tokenizer = RegexpTokenizer(r'\w+')
			li = tokenizer.tokenize(summary)

			## stop word removal
			filtered_sentence = [w for w in li if not w in stop_words]   
			filtered_sentence = [] 
			  
			for w in li: 
				if w not in stop_words: 
					filtered_sentence.append(w)
			
			## stemming in python
			final_dataset_str=[]
			for w in filtered_sentence: 
				final_dataset_str.append(ps.stem(w))
			story_clean = ' '.join(final_dataset_str)			
			print(story_clean)
			final_dataset.write(story_clean)
			final_dataset.write('\n')