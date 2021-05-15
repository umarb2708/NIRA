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
    sql = "INSERT INTO commands (main_kw,opt_kw1,opt_kw2,opt_kw3,opt_kw4,opt_kw5,action_file,param1,param2,param3,param4,param5) VALUES (%s, %s,%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)"
    val = (values["main_kw"],values["opt_kw1"],values["opt_kw2"],values["opt_kw3"],values["opt_kw4"],values["opt_kw5"],values["action_file"],values["param1"],values["param2"],values["param3"],values["param4"],values["param5"])
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
