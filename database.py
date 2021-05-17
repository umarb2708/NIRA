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


def insert_training_commands(values):
    sql = "INSERT INTO commands (main_kw,action_file) VALUES (%s, %s)"
    val = (values["main_kw"],values["action_file"])
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")




def get_commands(st):
    lis=""
    mycursor.execute("SELECT * FROM commands")
    myresult = mycursor.fetchall()
    for x in myresult:
        if(x[1] in st):
            lis=x[2]
            break
            
    return lis
