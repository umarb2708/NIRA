import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="pi",
  password="Pi@REX123#",
  database="rex_db"
)
print(mydb)

mycursor = mydb.cursor()


def insert_login_details(user,ip_address):
    sql = "INSERT INTO user_log (user_name,ip_address) VALUES (%s, %s)"
    val = (user,ip_address)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
