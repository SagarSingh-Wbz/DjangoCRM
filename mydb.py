import mysql.connector

dataBase=mysql.connector.connect(
    host='WBZ-IN-PG02QY7X',
    user='',
    passwd=''
)

cursorobj=dataBase.cursor()

cursorobj.execute("CREATE DATABASE testDjango")

print("Connection Established!")