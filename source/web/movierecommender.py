#!/usr/bin/python
print("Content-type:text/html\r\n\r\n")
print('''
<!DOCTYPE html>
<html>
<head>
	<title style="font-family:verdana;">Movie Recommandation</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">

	<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">

<style>
* {box-sizing: border-box;}

body {
  margin: 0;
  font-family: Arial, Helvetica, sans-serif;
}

.topnav {
  overflow: hidden;
  background-color: #e9e9e9;
}

.topnav a {
  float: left;
  display: block;
  color: black;
  text-align: center;
  padding: 14px 16px;
  text-decoration: none;
  font-size: 17px;
}

.topnav a:hover {
  background-color: #ddd;
  color: black;
}

.topnav a.active {
  background-color: #2196F3;
  color: white;
}

.topnav .search-container {
  float: right;
}

.topnav input[type=text] {
  padding: 6px;
  margin-top: 8px;
  font-size: 17px;
  border: none;
}

.topnav .search-container button {
  float: right;
  padding: 6px 10px;
  margin-top: 8px;
  margin-right: 16px;
  background: #ddd;
  font-size: 17px;
  border: none;
  cursor: pointer;
}

.topnav .search-container button:hover {
  background: #ccc;
}

@media screen and (max-width: 600px) {
  .topnav .search-container {
    float: none;
  }
  .topnav a, .topnav input[type=text], .topnav .search-container button {
    float: none;
    display: block;
    text-align: left;
    width: 100%;
    margin: 0;
    padding: 14px;
  }
  .topnav input[type=text] {
    border: 1px solid #ccc;  
  }
}
.carousel-inner img {
      width: 100%;
      height: 600px;
  }

</style>
</head>
<body>

<div class="topnav">
  <a class="active" href="#home">Home</a>
  <a href="#about">About</a>
  <a href="#contact">Contact</a>
  <div class="search-container">
    <form name = "search" action="getmovie.py">
      <input type="text" placeholder="Search..." name="search">
      <button type="submit"><i class="fa fa-search"></i></button>
    </form>
  </div>
</div>

<div id="demo" class="carousel slide" data-ride="carousel">

  <!-- Indicators -->
  <ul class="carousel-indicators">
    <li data-target="#demo" data-slide-to="0" class="active"></li>
    <li data-target="#demo" data-slide-to="1"></li>
    <li data-target="#demo" data-slide-to="2"></li>
  </ul>
 
  <!-- The slideshow -->
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="Images/movie2.jpg" alt="Icon1">
    </div>
    <div class="carousel-item">
      <img src="Images/movie1.jpg" alt="Icon2">
    </div>
    <div class="carousel-item">
      <img src="Images/movie.jpg" alt="Icon3">
    </div>
  </div>
 
  <!-- Left and right controls -->
  <a class="carousel-control-prev" href="#demo" data-slide="prev">
    <span class="carousel-control-prev-icon"></span>
  </a>
  <a class="carousel-control-next" href="#demo" data-slide="next">
    <span class="carousel-control-next-icon"></span>
  </a>
</div>

<section>

	<a name = "about">
        <div class="container-fluid">
                <h1 class="text-center text-capitalize pt-5">About</h1>
                <hr class="w-25 mx-auto pt-5">

                <div class ="row mb-5">
                        <div class ="col-lg-4 col-md-4 col-12">
                                <img src="Images/icon.png" class="img-fluid">
                        </div>
                        <div class="col-lg-8 col-md-8 col-12">
                                <h1 class="text-center text-captialize pt-3">How it Works?</h1>
                                <hr class="w-25 mx-auto pt-3>
                                <p class="pt-4">Go to the search box and enter keywords
                                                relevent to movie that you want to find,
                                                you will get your movie name along with 
						IMDB Rating, link to IMDb
						and year of release.</p>
			</div>
                </div>
        </div>
</section>

<section>
	<a name="contact">
<div class="container-fluid">
        <h1 class="text-center text-capitalize pt-5">Developed By</h1>
        <hr class="w-25 mx-auto pt-5">
        
   <div class ="row text-center mb-5">
        <div class="col-lg-2 col-md-2 col-12 mx-auto">
            <div class="card">
                <img class="card-img-top img-fluid" src="Images/rohit.jpg" alt="Card image">
                <div class="card-body">
                        <h4 class="card-title">Rohit Kumar</h4>
                        <p class="card-text">rohit98077@gmail.com<br>+917497923874</p>
                </div>
            </div>
        </div>

        <div class="col-lg-2 col-md-2 col-12 mx-auto">
            <div class="card">
                <img class="card-img-top" src="Images/rajershi.jpg" alt="Card image">
                <div class="card-body">
                        <h4 class="card-title">Rajershi Gupta</h4>
                        <p class="card-text">rajershigupta@gmail.com<br>+917705826370</p>
                </div>
            </div>
        </div>

	<div class="col-lg-2 col-md-2 col-12 mx-auto">
           <div class="card">
                <img class="card-img-top" src="Images/suraj.jpg" alt="Card image">
                <div class="card-body">
                        <h4 class="card-title">Suraj Kumar</h4>
                        <p class="card-text">surajsharma@iitb.ac.in<br>+917497923874</p>
                </div>
           </div>
        </div>

   </div>
</div>
</section>

<section class="bg-primary">
        <article class ="py-4 text-center text-white">
                <div>
                        <h3 class="display-4">Our mission is to predict the right movie for you.</h3><hr>
			<p class="pt-2">This website is a registered trademark of the Unknown.<p>
			<p class="pt-2">Copyright: IIT Bombay, CS699</p>
		</div>
	</article>
</section>

<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>

</body>
</html>
''')
