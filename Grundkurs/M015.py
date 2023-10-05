# Datenbanken

# Datenbanktreiber haben generell zwei benötigte Klassen
# - Connection
# - Cursor

from M015b import User

db = "pyodbc"

if db == "sqlite3":
	import sqlite3

	with sqlite3.connect("../Test.db") as conn:

		cursor = conn.cursor()

		cursor.execute("DROP TABLE IF EXISTS Users")
		cursor.execute("CREATE TABLE Users (int id auto increment, vorname varchar(30))")
		cursor.execute("INSERT INTO Users VALUES(0, 'Lukas')")

		conn.commit()  # Änderungen schreiben

		print(cursor.execute("SELECT * FROM Users").fetchall())

elif db == "pyodbc":
	import pyodbc

	with pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                          "Server=WIN10-LK3;"
                          "Database=PythonKurs;"
                          "Trusted_Connection=yes;") as conn:

		cursor = conn.cursor()

		cursor.execute("DROP TABLE IF EXISTS Users")
		cursor.execute("CREATE TABLE Users (id int identity, vorname varchar(30))")
		cursor.execute("INSERT INTO Users VALUES('Lukas')")

		conn.commit()  # Änderungen schreiben

		rows = cursor.execute("SELECT * FROM Users").fetchall()

		users = list()
		for row in rows:
			users.append(User(row))
		print(users)