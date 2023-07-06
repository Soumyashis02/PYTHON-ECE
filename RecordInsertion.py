import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="msit"
)

mycursor=mydb.cursor()
sql="INSERT INTO customers(name,address) VALUES(%s,%s)"
val=("SOUMYASHIS","ICHAPUR")
mycursor.execute(sql,val)
sql_2="INSERT INTO customers_2(name,address,email,gender)VALUES(%s,%s,%s,%s)"
val_2=("test1","address1","abc@gmail.com","male")
mycursor.execute(sql_2,val_2)
mydb.commit()
print(mycursor.rowcount,"record inserted.")
