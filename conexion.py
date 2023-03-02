import mysql.connector

cnn = mysql.connector.connect(host="localhost",port="3308", user = "root", password="2707", db="bdejemplopy")
print(cnn)

cur = cnn.cursor()
cur.execute("Select * from countries")
datos=cur.fetchall()

for fila in datos:
    print(fila)