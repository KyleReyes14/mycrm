import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'Kanny0102*_*@@'
	
	)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE ndb")

print("yey")