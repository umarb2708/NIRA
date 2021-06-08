import mysql.connector


#---------LOCAL DATABASE CREDENTIAL-------------------
mydb = mysql.connector.connect(
  host="localhost",
  user="pi",
  password="Pi@REX123#",
  database="rex_db"
)
#----------------------------------------------------

#---------REMOTE DATABASE CREDENTIAL-------------------
#mydb = mysql.connector.connect(
#  host="151.106.117.51",
#  user="u556004652_rex_admin",
#  password="Rex@HOSTING123#",
#  database="u556004652_rex_db",
#  connection_timeout=31536000
#    )
#----------------------------------------------------


print(mydb)

mycursor = mydb.cursor()


def insert_login_details(values):
    sql = "INSERT INTO user_log (user_name,ip_address,pid) VALUES (%s, %s, %s)"
    val = (values["user"],values["ip_address"],values["pid"])
    mycursor.execute(sql, val)
    mydb.commit()
    return "Login details USER:"+values["user"]+" IP:"+values["ip_address"]+" PID:"+values["pid"]


def insert_training_commands(values):
    sql = "INSERT INTO commands (main_kw,action_file) VALUES (%s, %s)"
    val = (values["main_kw"],values["action_file"])
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")




def search_cmd(st):
    lis=""
    mycursor.execute("SELECT * FROM commands")
    myresult = mycursor.fetchall()
    mydb.commit()
    for x in myresult:
        if(x[1] in st):
            lis=x[2]
            break

    return lis



def insert_cmd_executed(cmd,status):
    sql = "INSERT INTO commands_executed (command,status) VALUES (%s, %s)"
    val = (cmd,status)
    mycursor.execute(sql, val)
    mydb.commit()
    #print(mycursor.rowcount, "record inserted.")
def update_automation_table(dev_id,status):
    sql="UPDATE home_automation SET status = '"+status+"' WHERE id="+str(dev_id)+";"
    mycursor.execute(sql)
    mydb.commit()
    return "ok"
def del_cmd_entries():
    sql="DELETE FROM commands_executed"
    mycursor.execute(sql)
    mydb.commit()
    return "ok"
