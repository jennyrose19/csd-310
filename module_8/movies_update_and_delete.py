#Jenny Rosero
#Module 7.2 Assignment

import mysql.connector
from mysql.connector import errorcode

mydb = mysql.connector.connect(
	user="movies_user",
	password="popcorn",
	host="127.0.0.1",
	database="movies",
)


def show_films(cursor, title):
    
    print("\n-- DISPLAYING FILMS AFTER DELETE")

    mycursor = mydb.cursor()

    mycursor.execute("""SELECT film_name AS Name, film_director AS Director, genre_name AS Genre, studio_name AS 'Studio name'
    FROM film
    INNER JOIN genre
    ON film.genre_id = genre.genre_id
    INNER JOIN studio
    ON film.studio_id = studio.studio_id""")

    myresult = mycursor.fetchall()

    for film in myresult:
        print("Film: {}\nDirector: {}\nGenre Name: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))

show_films("mycursor", "DISPLAYING FILMS")

#mycursor = mydb.cursor()

#mycursor.execute("""INSERT INTO film (film_name, film_director, film_releaseDate, film_runtime, studio_id, genre_id)
    #VALUES('Star Wars', 'George Lucas', 1978, 142, 4, 4)""")

#mycursor.execute("""UPDATE genre
#SET genre_name = 'Horror'
#WHERE genre_name = 'SciFi'""")

#mycursor.execute("""DELETE FROM film
#WHERE film_name = 'Gladiator'""")


#mydb.commit()

#show_films("mycursor", "DISPLAYING FILMS")




