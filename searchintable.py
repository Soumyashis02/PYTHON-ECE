import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="msit"
)

mycursor=mydb.cursor()

sql="DELETE FROM customers WHERE address=%s"
adr=str(input("Enter your address"))
mycursor.execute(sql,adr)
mydb.commit()
print(myursor.rowcount,"record(S) deleted")
