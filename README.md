# movie-recommendation-system-and-visualizatio
It is a movie recommendation and visualization system. The user can select the genre from the 18 genres that are available and the system will show different visualizations with various comparisons such as "year released vs imdb rating", "which directors have movies with highest IMDB ratings and profits" and much more. The visualizations support for hovertool which allows you to see the exact values/data by hovering to the visualization.

It implements the use of SQL and Microsoft Excel for the data cleaning and Data pre-processing.
Then it uses python for the logic of the project and database is also linked using psycopg2 library.
Then pandas is used for the data frame and the manipulation of the data frame.
I have also used bokeh for the visualization of the data.
Along with this, I have also used libraries for saving the output file and then showing it to web browser.

So, all the used libraries are mentioned below :-

1) import psycopg2
2) import pandas as pd
3) from bokeh.plotting import figure, output_file, save, show
4) from bokeh.models import HoverTool
5) from bokeh.models import NumeralTickFormatter
6) import webbrowser


**Working :-** In this project, the user first needs to select the category of the movie from the various available categories(available categories are also displayed to the user). When user select a category, then the system generates various insights/data with visuals which we will discuss one by one.

**Note :- I have taken "Romance" as Movie Category to generate the visuals for this readme to explain the visual and the insight.**


1) **Genre sorted according to IMDB Rating**



![genre sorted according to IMDB rating](https://github.com/ujjwal717/movie-recommendation-system-and-visualization/assets/93403224/8ae47b59-b89d-45eb-86d4-0f493690a8b4)


**Explanation :-** In this, I have used the scatterplot having the IMDB rating at X-Axis and release year of the movie at Y-Axis.

**Insight :-** I found that in "Romance" genre, the highest IMDB rating(obviously from the dataset) is of movie named "Forrest Gump" and has an IMDB Rating of '8.8'and was released in 1994. Also, the visual supports for hovering tool, so you can just hover over each scatterplot to have a detailed information about the movie such as 'Genre','Run-Time','IMDB Rating','Certificate' and more.



2)**IMDB Rating and Certificate of movies according to selected Genre**


![rating vs certification of movies based on selected genre](https://github.com/ujjwal717/movie-recommendation-system-and-visualization/assets/93403224/9cf4b93c-bb88-409d-beaf-bb461fa2967e)



**Explanation :-** This Visual includes certificate at the X-Axis and IMDB Rating at the Y-Axis.

**Insight :-** I found that movies of PG-13 certificate has the highest IMDB Rating and some of such movies are "Forrest Gump" , "Life is Beautiful". This visual also supports for hovering which will provide you the detailed information about the movie, certificate and rating.






