import mysql.connector
from mysql.connector import errorcode

mydb = mysql.connector.connect(
	user="movies_user",
	password="popcorn",
	host="127.0.0.1",
	database="movies",
)

try:
    print("\n-- DISPLAYING Studio RECORDS --")
    
    mycursor = mydb.cursor()
	
    mycursor.execute("SELECT * FROM studio")

    myresult = mycursor.fetchall()

    for row in myresult:
        print("Studio ID:", row[0])
        print("Studio Name:", row[1], "\n")

    print("\n-- DISPLAYING Genre RECORDS --")   
	
    mycursor.execute("SELECT * FROM genre")

    myresult = mycursor.fetchall()

    for row in myresult:
        print("Genre ID:", row[0])
        print("Genre Name:", row[1], "\n")

    print("\n-- DISPLAYING Short Film RECORDS --")

    mycursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime <=120")

    myresult = mycursor.fetchall()

    for row in myresult:
        print("Film Name:", row [0])
        print("Runtime:", row [1], "\n")
    
    print("\n-- DISPLAYING Director RECORDS in Order --")

    mycursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director")

    myresult = mycursor.fetchall()

    for row in myresult:
        print("Film Name:", row [0])
        print("Director:", row [1], "\n")

        
except mysql.connector.Error as err:
	if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print(" The supplied username or passoword are invalid")

	elif err.errno == errorcode.ER_BAD_DB_ERROR:
		print(" The specified database does not exist")

	else:
		print(err)

finally:
	mydb.close()
