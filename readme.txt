

**************************************************
CS699 : Software Lab, Project, 2019
**************************************************

**************************************************
Git Link : https://github.com/Whirllz/Movie-Recommendation-System.git
**************************************************



**************************************************
Project : Movie Recommendation System
**************************************************

**************************************************
Roll numbers and Contributions:- 
193050071 : Rohit Kumar     :  Database implementation, search query and Documentation
193050003 : Suraj Kumar     :  Website and search query optimisation
193059002 : Rajershi Gupta  :  Web scraping, Report and Presentation
**************************************************


**************************************************
Motivation : 
At times when we want to recommend a movie to one of our friends we somehow do not remember the name of the movie. Rather, something sticks with us about the movie, be it the actor or character etc. Therefore, we thought if the user queries the actor(s) or character(s) or title or story of the movie, then we can output the most probable movie from the dataset, with all its details in the dataset to the user.Adding to that, movies that are still relevant to the search query are also given with their names.
Furthermore, this tool can also be used to recommend the movie to the user query according to the relevant search the user makes, to reccomend user certain similar kind of movies.(by Genre, Actor(s), Character(s), StoryLine etc.)
**************************************************


**************************************************
How to host : 
1. Clone the repositry from the git link given in readme.txt
2. Fetch the preprocessed csv file from the path: ../../web/preprocessing/dataset.csv
3. Clean the file or take the final MoviesData.csv file from ../../web/moviesData.csv
4. Install XAMPP and set the path to the source code ”../web/”
5. Make the database from the given file createMovieDB.py, using the fol-
lowing command:
python3 createMovieDB.py
(prerequisite : python3 and SQLite are already installed)
6. Launch XAMPP and start the server
7. open your favourite browser and put the following url : localhost/moviePrediction.py
8. In the search query given at the top-right corner of the website opened,
   the user can give the query. Note that the following few assumptions are
   made for the query:
   (a) If query length <6, then the search is made on all attributes of
       the extended dataset except storyline.
   (b) If query length >5, then the search is made on the storyline only.
	   The best matched entry is returned.
9. The webpage would redirect to the output page where the results can be
seen
**************************************************

