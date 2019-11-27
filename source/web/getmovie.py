#!/usr/bin/python
print("Content-type:text/html\r\n\r\n")
import sqlite3
import cgi,cgitb
import csv,sys
from itertools import combinations
cgitb.enable()
form = cgi.FieldStorage()
value = form.getvalue('search')
print("<html>")
print("<head>")
print('''<title style="font-family:verdana;">Movie Recommandation</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">

        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">''')
print('''<style>
	body {
  		margin: 0;
  		font-family: Arial, Helvetica, sans-serif;
		}
	p.pad {
  	padding-right: 500px;
		}
	.button {
 		 background-color: #4CAF50;
 		 border: none;
 		 color: white;
 		 padding: 15px 32px;
  		text-align: center;
  		text-decoration: none;
  		display: inline-block;
  		font-size: 16px;
  		margin: 4px 2px;
  		cursor: pointer;
		}
	</style>''')
print("</head>")

print("<body>")
print('''<section class="bg-primary">
        <article class ="pt-3 pb-2 text-center text-white">
                <div>
                        <h1 class="display-5" style = "color:black">Searched: %s</h1><hr>
                </div>
        </article>
</section>''' % (value))

con = sqlite3.connect("IMDB.db")
cur = con.cursor()

stop_words = {'has', 'by', 'll', 'wouldn', 'shan', 'some', 'a', 'how', 'theirs', 'should', 'do', 'through', "don't", 'where', 'from', 'too', 'hasn', 'who', 'haven', 'the', 'is', 'more', 'yourself', 'no', "needn't", 'ourselves', "should've", 'them', 'because', 'into', 'y', 'until', 'in', 'under', 'my', 'our', 'herself', 'against', 'of', 'there', 'with', 'between', 'we', "that'll", 'here', "it's", 'shouldn', 'they', 'this', 'itself', 'he', 'before', 'same', "wasn't", 'been', "wouldn't", 'both', 'him', "mightn't", 'but', 'during', "you'll", "shouldn't", 'won', 'her', 't', 're', 'after', 'had', 'his', 'd', 'couldn', 'myself', 'if', 'yourselves', 'to', 'whom', 'very', 'can', 'off', 'be', 'mustn', 'so', 'it', "you've", 'on', 'hers', 'ours', 'nor', 'further', 'these', 'have', 'doing', 'down', "doesn't", 'all', 'each', 'did', 'about', "didn't", "hadn't", 'being', 'again', 'just', 'your', 'not', 'ain', "aren't", 'm', 'wasn', 'those', 'when', "haven't", 'will', 'was', 'o', "isn't", 've', 'needn', 'as', "won't", 'few', 'having', "you'd", 'you', 'own', 'does', 'didn', 'up', 'out', 'its', 'why', 'once', 'which', 'himself', 'she', 'don', 'at', 'isn', "weren't", 'ma', 'above', 'now', "you're", "hasn't", 'what', 'mightn', 'are', 'hadn', 'any', 's', "couldn't", 'while', 'other', 'that', 'am', 'weren', 'themselves', 'most', 'me', 'an', 'doesn', "shan't", 'and', 'below', "she's", 'yours', 'i', 'were', 'over', "mustn't", 'for', 'their', 'such', 'then', 'aren', 'only', 'than', 'or'}

#stop_words = set(stopwords.words('english')) 
word_tokens = (value.lower()).split()
words = [w for w in word_tokens if not w in stop_words]

genre = ["action", "adventure", "animation", "biography", "comedy", "crime", "documentry", "drama", "family", "fantasy", "filmnoir", "gameshow", "history", "horror", "music","musical", "mystry", "news", "realitytv", "rimance", "scifi", "short", "sport", "talkshow", "thiller", "war", "western"]

def root_word(word):
        ps = PorterStemmer()
        rooted_word=[]
        for w in words:
                rooted_word.append(ps.stem(w))
        return rooted_word


def search_story(rooted_word):
        story=[]
        for w in rooted_word:
                tmp=cur.execute(''' select title,url,rating,year from MoviesData where storyline like '%'||?||'%';''',(w+' ',)).fetchall()
                print("<br>")
		#print(tmp)
		if story:
                        tmp2=[v for v in story if v in tmp]
                        if tmp2:
                                story=tmp2
                        else:
                                story.extend(tmp)
                else:
                        story=tmp
	return story


def search_across_token(lst):
        res=lst[0]
        for i in range(1,len(lst)):
                if lst[i]:
                        temp=[v for v in res if v in lst[i]]
                        if temp:
                                res=temp
                        else:
                                res.extend(lst[i])
        return res


def search_title_actor_char(lst):
        title,actor,char=[],[],[]
        title=cur.execute(''' select title,url,rating,year from MoviesData where title like '%'||?||'%';''',(words[i],)).fetchall()
        actor=cur.execute(''' select title,url,rating,year from MoviesData where actor like '%'||?||'%';''',(words[i]+' ',)).fetchall()
        char=cur.execute(''' select title,url,rating,year from MoviesData where character like '%'||?||'%';''',(words[i]+' ',)).fetchall()
        return title,actor,char


lst = []
flag = 0
lst = cur.execute(''' select title,url,rating,year from MoviesData where title =?;''',(value,)).fetchall()
if lst:
        flag = 1

if (len(words)>5 and (flag == 0)):
	#rooted_word = root_word(words)
	lst = search_story(words)
	flag = 1

query='select title,url,rating,year from MoviesData where ('
l,l2,l3,l4,=[],[],[],[]
target_list=[[],[],[],[],[]]

if(flag==0):
	for i in range(len(words)):
        	if words[i].isdigit():
        	        word=int(words[i])
        	        l=cur.execute(''' select title,url,rating,year from MoviesData where (year =? );''',(word,)).fetchall()
        	        target_list[i]=l

        	elif words[i] in genre:
                	finalquery=query+words[i]+'=?)'
                	l=cur.execute(finalquery,(1,)).fetchall()
                	target_list[i]=l

        	else :
        	        title,actor,char=[],[],[]
        	        title,actor,char=search_title_actor_char(words[i])
        	        target_list[i]=list(set(title)|set(actor)|set(char))


if(flag == 0):
	lst=search_across_token(target_list)

print('''<section><article class ="py-4 text-center text-white<div>''')
print('''<p align="center"><font color = "blue" size = "5"><b>Predicted Result</font></p>''')
print("<hr>")
print('''<p style="margin-left:20%"> <img src = "imdb.png" align ="left" style="width=20%" height="30%"></p>''')
print("<br>")
if(len(lst)):
	MovieDetail = lst[0]
	moviename = MovieDetail[0].encode('utf-8')
	predictedMovie = ""
	temp = moviename.split()
	for eachword in temp:
		predictedMovie += eachword.capitalize() + " "
	url = MovieDetail[1]
	rating = MovieDetail[2]
	year = MovieDetail[3]
	print('''<p class = "pad"><font size = "4"<b>Movie Name: %s </font></p>''' % (predictedMovie))
	print('''<p class = "pad"><b>Year of Release: %s </p>''' % (year))
	print('''<p class = "pad"><b>Rating: %s </p>''' % (rating))
	print('''<p class = "pad"><a href = %s>IMDb link</a></p>''' % (url))
	print('''<br><br><p class = "pad"><form action="http://localhost/movierecommender.py">
    				<input class = "button" type="submit" value="Search Next Movie"/></p>''')
	print("<br><br><br><br><hr>")

	print('''<p align = "center" style="background-color:cyan;"><font size = "4"<b>Other Results</font></p><hr>''')
	count = 1
	for i in range(len(lst)-1):	
		print("<br><hr>")
		row = lst[i+1]
		print('''<p align ="center"><font size = "3"<b>Movie Name: %s </font></p>''' % (row[0].encode('utf-8')))
		print('''<p align ="center"><a href = %s>IMDb link</a></p>''' % (row[1]))
		print("<hr>")
		count+=1
	print('''<p align ="center"><font size = "3"<b>Total: %d </font></p>''' % (count))
	

else:
	print('''<p class = "pad"><font size = "6"<b>Movie Not Found</font></p>''')
	print('''<br><br><br><br><br><br><br><p class = "pad"><form action="http://localhost/movierecommender.py">
    				<input class = "button" type="submit" value="Search Again"/></p>''')
	
print('''</div>
	</article>
	</section>''')
#print("<br>")
cur.close()
con.close()
print("</body>")
print("</html>")
