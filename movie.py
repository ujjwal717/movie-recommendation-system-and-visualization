import psycopg2
import pandas as pd
from bokeh.plotting import figure, output_file, save, show
from bokeh.models import HoverTool
from bokeh.models import NumeralTickFormatter
import webbrowser

db_link = psycopg2.connect(
    database="your database",
    user="your database username",
    password="your database password",
    host="your host",
    port="your port",
)

c = db_link.cursor()
sql_query = """SELECT * FROM movie_data """
pd.set_option("display.max_colwidth", None)
df = pd.read_sql_query(sql_query, db_link)


def recommend(genre):
    desired_genre = genre
    df_genre = df[df["genre"].str.contains(desired_genre)]
    df_filter = df_genre[
        [
            "name",
            "year",
            "rating",
            "genre",
            "certificate",
            "run_time",
            "budget",
            "box_office",
            "profit",
            "directors",
        ]
    ]

    def create_p_rating():
        TOOLTIPS = HoverTool(
            tooltips=[
                ("Rank", "$index"),
                ("Movie Name", "@name"),
                ("Genres", "@genre"),
                ("Run Time", "@run_time"),
                ("Certificate", "@certificate"),
                ("IMDB Rating", "@rating"),
                ("Year Released", "@year"),
            ]
        )

        p = figure(
            title="Your genre sorted according to IMDB Rating ",
            x_axis_label="IMDB RATING",
            y_axis_label="YEAR RELEASED",
            tools=[TOOLTIPS],
        )
        circle = p.circle("rating", "year", fill_color="red", size=10, source=df_filter)
        output_file("p.html")
        save(p)
        webbrowser.open("p.html")

    def create_p_collection():
        TOOLTIPS_NEW = HoverTool(
            tooltips=[
                ("Rank", "$index"),
                ("Movie Name", "@name"),
                ("Budget", "@budget"),
                ("Box Office Collection", "@box_office"),
                ("Profit", "@profit"),
                ("Runtime", "@run_time"),
                ("Year Released", "@year"),
            ]
        )
        p_collection = figure(
            width=1000,
            height=1000,
            title="Your genre's Box office collection and Budget",
            x_axis_label="Budget",
            y_axis_label="Box Office Collection",
            tools=[TOOLTIPS_NEW],
        )
        p_collection.xaxis[0].formatter = NumeralTickFormatter(format="0")
        p_collection.yaxis[0].formatter = NumeralTickFormatter(format="0")
        circle_new = p_collection.circle(
            "budget", "box_office", fill_color="maroon", size=10, source=df_filter
        )

        output_file("p_collection.html")
        save(p_collection)
        webbrowser.open("p_collection.html")

    def cert_rating():
        cert = df_filter["certificate"]
        rate = df_filter["rating"]

        TOOLTIPS_CERT = HoverTool(
            tooltips=[
                ("Movie Name", "@name"),
                ("certificate", "@certificate"),
                ("rating", "@rating"),
            ]
        )

        p_cert = figure(
            x_range=cert.unique(),
            height=700,
            width=800,
            x_axis_label="CERTIFICATE",
            y_axis_label="IMDB RATING",
            title="Rating vs Certification of Movies based on your selected Genre",
            toolbar_location=None,
            tools=[TOOLTIPS_CERT],
        )
        p_cert.vbar(
            x="certificate",
            top="rating",
            width=0.5,
            fill_color="green",
            source=df_filter,
        )
        p_cert.xgrid.grid_line_color = "black"
        p_cert.y_range.start = 0.5

        output_file("p_cert.html")
        save(p_cert)
        webbrowser.open("p_cert.html")

    def cert_profit():
        name = df_filter["name"]
        profit = df_filter["profit"]

        TOOLTIPS_PROFIT = HoverTool(
            tooltips=[
                ("Movie Name", "@name"),
                ("Genre", "@genre"),
                ("Profit", "@profit"),
                ("IMDB Rating", "@rating"),
                ("Year Released", "@year"),
            ]
        )

        p_profit = figure(
            x_range=name.unique(),
            height=800,
            width=4000,
            x_axis_label="MOVIE NAME",
            y_axis_label="PROFIT",
            title="Movie profit according to your genre",
            toolbar_location=None,
            tools=[TOOLTIPS_PROFIT],
        )
        p_profit.yaxis[0].formatter = NumeralTickFormatter(format="0")
        p_profit.xaxis.major_label_orientation = "vertical"
        p_profit.vbar(x="name", top="profit", width=0.4, source=df_filter)
        p_profit.xgrid.grid_line_color = "black"
        p_profit.y_range.start = 0

        output_file("p_profit.html")
        save(p_profit)
        webbrowser.open("p_profit.html")

    def cert_director():
        name = df_filter["directors"]
        profit = df_filter["profit"]

        TOOLTIPS_DIRECTOR = HoverTool(
            tooltips=[
                ("Movie Name", "@name"),
                ("Profit", "@profit"),
                ("Directors", "@directors"),
            ]
        )

        p_director = figure(
            x_range=name.unique(),
            height=800,
            width=4000,
            x_axis_label="DIRECTOR NAME",
            y_axis_label="PROFIT",
            title="List of Directors having movies with highest profits",
            toolbar_location=None,
            tools=[TOOLTIPS_DIRECTOR],
        )
        p_director.yaxis[0].formatter = NumeralTickFormatter(format="0")
        p_director.xaxis.major_label_orientation = "vertical"
        p_director.vbar(
            x="directors", top="profit", width=0.4, color="orange", source=df_filter
        )
        p_director.xgrid.grid_line_color = "black"
        p_director.y_range.start = 0

        output_file("p_director.html")
        save(p_director)
        webbrowser.open("p_director.html")

    def cert_director_rating():
        name = df_filter["directors"]
        profit = df_filter["rating"]

        TOOLTIPS_DIRECTOR_RATING = HoverTool(
            tooltips=[
                ("Movie Name", "@name"),
                ("IMDB Rating", "@rating"),
                ("Directors", "@directors"),
            ]
        )

        p_director_rating = figure(
            x_range=name.unique(),
            height=800,
            width=4000,
            x_axis_label="DIRECTOR NAME",
            y_axis_label="IMDB RATING",
            title="List of Directors having movies with highest IMDB Ratings",
            toolbar_location=None,
            tools=[TOOLTIPS_DIRECTOR_RATING],
        )
        p_director_rating.yaxis[0].formatter = NumeralTickFormatter(format="0")
        p_director_rating.xaxis.major_label_orientation = "vertical"
        p_director_rating.vbar(
            x="directors", top="rating", width=0.4, color="brown", source=df_filter
        )
        p_director_rating.xgrid.grid_line_color = "black"
        p_director_rating.y_range.start = 0

        output_file("p_director_rating.html")
        save(p_director_rating)
        webbrowser.open("p_director_rating.html")

    create_p_collection()
    create_p_rating()
    cert_rating()
    cert_profit()
    cert_director()
    cert_director_rating()


movies = [
    "Drama",
    "drama",
    "Crime",
    "crime",
    "Action",
    "action",
    "Biography",
    "biography",
    "History",
    "history",
    "Adventure",
    "adventure",
    "Western",
    "western",
    "Romance",
    "romance",
    "Sci-fi",
    "sci-fi",
    "Mystery",
    "mystery",
    "Family",
    "family",
    "Fantasy",
    "fantasy",
    "Thriller",
    "thriller",
    "War",
    "war",
    "Animation",
    "animation",
    "Music",
    "music",
    "Horror",
    "horror",
    "Comedy",
    "comedy",
    "Film-Noir",
    "film-noir",
]

print(
    """Welcome to Movie Recommendation System.

This system shows you the various details and Visualizations relating to IMDB Rating, Movie Release Year, Profit etc.

You need to provide the Genre for which you want to see various details.

The various Genres supported are :- 

1)  Drama
2)  Crime
3)  Action
4)  Biography
5)  History
6)  Adventure
7)  Western
8)  Romance
9)  Sci-fi
10) Mystery
11) Family
12) Fantasy
13) Thriller
14) War
15) Animation
16) Music
17) Horror
18) Comedy


Kindly select Genre from the given genres only :) """
)

user_input = input("Enter the genre : ")

if user_input in movies:
    genre = user_input.capitalize()
    recommend(genre)
else:
    print("Wrong input, Enter the genre correctly")

c.close()
db_link.close()
