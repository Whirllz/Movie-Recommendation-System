import sys
import sqlite3
import csv

con = sqlite3.connect("/Users/surajsharma/Code/cs699/Project/MoviePred/IMDB.db")
cur = con.cursor()
cur.execute('''drop table if exists MoviesData''')
cur.execute('''create table if not exists MoviesData (tid TEXT primary key, url TEXT, rating FLOAT, year int, action int, adult int,
								adventure int, animation int, biography int, comedy int, crime int, documentry int,
								drama int, family int, fantasy int, filmnoir int, gameshow int, history int, horror int, music int,
								musical int, mystry int, news int, realitytv int, romance int, scifi int, short int,
								sport int, talkshow int, thiller int, war int, western int, title TEXT, actor TEXT, character TEXT, storyline TEXT)''')
file = "moviesData.csv"
infile = open(file,'r')
dr=csv.reader(infile)
to_db = [ ( i[0], i[1], i[2] , i[3], i[4], i[5],i[6], i[7], i[8] , i[9], i[10], i[11], i[12], i[13], i[14], i[15], i[16], i[17],i[18], i[19], i[20] , i[21], i[22], i[23],i[24], i[25], i[26] , i[27], i[28], i[29],i[30], i[31], i[32], i[33], i[34],i[35])for i in dr]

cur.executemany('''INSERT INTO MoviesData (tid, url, rating, year, action, adult, adventure, animation, biography, comedy, crime,
						documentry, drama, family, fantasy, filmnoir, gameshow, history, horror, music, musical, mystry,
						news,realitytv, romance, scifi, short, sport, talkshow, thiller, war, western, title, actor, character, storyline)
						VALUES (?, ?, ?, ?,?, ?, ?, ?,?, ?, ?, ?,?, ?, ?, ?,?, ?, ?, ?, ?, ?, ?, ?,?, ?, ?, ?,?, ?, ?, ?,?, ?, ?, ?)''', to_db)

con.commit();
con.close()
