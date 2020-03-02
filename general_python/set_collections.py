import mysql.connector

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="db_username",
  passwd="db_password"
)

# print(mydb)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")