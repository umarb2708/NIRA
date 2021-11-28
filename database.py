import mysql.connector


#---------LOCAL DATABASE CREDENTIAL-------------------
mydb = mysql.connector.connect(
  host="localhost",
  user="db_admin",
  password="Admin@HIRA123#",
  database="hira_db"
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

#Insert Login Info 
def insert_login_details(values):
    sql = "INSERT INTO user_log (user_name,ip_address,pid) VALUES (%s, %s, %s)"
    val = (values["user"],values["ip_address"],values["pid"])
    mycursor.execute(sql, val)
    mydb.commit()
    return "Login details USER:"+values["user"]+" IP:"+values["ip_address"]+" PID:"+values["pid"]

#insert Training commands
def insert_training_commands(values):
    sql = "INSERT INTO command_centre (main_kw,action_file) VALUES (%s, %s)"
    val = (values["main_kw"],values["action_file"])
    mycursor.execute(sql, val)
    mydb.commit()

def insert_commands(values):
    sql = "INSERT INTO commands (command,priority,frm) VALUES (%s, %s,%s)"
    val = (values["command"],values["priority"],values["from"])
    mycursor.execute(sql, val)
    mydb.commit()
  
#update server details
def insert_raspi_info(values):
    sql="UPDATE `raspi_info` SET `temp` = '"+values["temp"]+"', `cpu_load` = '"+values["cpu_load"]+"', `used_ram` = '"+values["used_ram"]+"', `used_mem` = '"+values["used_mem"]+"', `up_time` = '"+values["up_time"]+"' WHERE `raspi_info`.`id` = 1;"
    mycursor.execute(sql)
    mydb.commit()
    return "Raspberry Info inserted"

#Seach commands from command centr
def search_cmd(st):
    lis={
            "cmd":"not found",
            "kw" :"err.cmd_not_found"
            }
    mycursor.execute("SELECT * FROM command_centre")
    myresult = mycursor.fetchall()
    mydb.commit()
    for x in myresult:
        if(x[1] in st):
            lis["cmd"]=x[2]
            lis["kw"]=x[1]
            break

    return lis

def get_commands():
    n=0
    lis=[]
    l={}
    lis.append({
            "id"    :0,
            "cmd"   :"null",
            "priority":"low",
            "frm"   : "hira",
            "exec"  : 0
            })
    mycursor.execute("SELECT * FROM commands WHERE exec = 0")
    myresult = mycursor.fetchall()
    mydb.commit()
    for x in myresult:
        if n==0:
            lis.pop(0)
        l["id"]=x[0]
        l["cmd"]=x[1]
        l["priority"]=x[2]
        l["frm"]=x[3]
        l["exec"]=x[4]
        n=n+1
        lis.append(l)

    return lis

def get_contact(person):
    val={
            "found":0
            }
    mycursor.execute("SELECT * FROM contacts")
    myresult = mycursor.fetchall()
    mydb.commit()
    for res in  myresult:
        if res[1] in person:
            val["found"]=1
            val["name"]=res[1]
            val["phone"]=res[2]
            val["email"]=res[3]
            val["Address"]=res[4]
    return val



def insert_cmd_executed(cmd,status):
    sql = "INSERT INTO commands_executed (command,status) VALUES (%s, %s)"
    val = (cmd,status)
    mycursor.execute(sql, val)
    mydb.commit()
    #print(mycursor.rowcount, "record inserted.")
def update_automation_table(dev_id,status):
    sql="UPDATE home_automation SET status = '"+str(status)+"' WHERE id="+str(dev_id)+";"
    mycursor.execute(sql)
    mydb.commit()
    return "ok"
def update_cmd_table(n):
    sql="UPDATE commands SET exec = 1 WHERE id="+str(n)+";"
    mycursor.execute(sql)
    mydb.commit()


def del_cmd_entries():
    sql="DELETE FROM commands_executed"
    mycursor.execute(sql)
    mydb.commit()
    return "ok"
