import mysql.connector

db=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="msit"
)

mysql_query=db.cursor()
mysql_query.execute("CREATE TABLE customers_2(id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255),address VARCHAR(255),email VARCHAR(100), gender TEXT(50))")
print("TABLE CREATED SUCCESSFULLY")
