import mysql.connector
import import_file as pkg

#---------LOCAL DATABASE CREDENTIAL-------------------
mydb = mysql.connector.connect(
  host="localhost",
  user="db_admin",
  password="Admin@MDB123#",
  database="hira_main"
)
#----------------------------------------------------

#---------REMOTE DATABASE CREDENTIAL-------------------
#mydb = mysql.connector.connect(
#  host="51.210.156.16",
#  user="innovize_wp823",
#  password="-7S(e8g12p",
#  database="innovize_wp823"
#    )
#----------------------------------------------------


if mydb:
    print("Successfully Conected to Database")
else:
    print(mydb)
mycursor = mydb.cursor()
#Function to Insert data to DB
def insertData(tableName,values):
    col=pkg.parser.getKeys(values)
    Datatype=pkg.parser.getDataType(values)
    val=pkg.parser.getData(values)
    sql= "INSERT INTO "+tableName+" ("+col+") VALUES ("+Datatype+")"
    values="("+val+")"
    mycursor.execute(sql, val)
    mydb.commit()
    return 1
#Function for UPDATE query
def UpdateData(tableName,values,condition):
    setval=""
    for key in values:
        if("int" in str(type(values[key]))):
            setval=setval+key+"="+"%d,"
        elif("str" in str(type(values[key]))):
            setval=setval+key+"="+"%s,"
        elif("float" in str(type(values[key]))):
            setval=setval+key+"="+"%f,"
    setval=setval[:-1]

    sql = "UPDATE "+tableName+" SET "+setval+" WHERE "+condition
    val = "("+pkg.parser.getData(values)+")"
    mycursor.execute(sql)
    mydb.commit()

#Function for UPDATE query
def SelectData(tableName,rowNames,condition):
    query="SELECT "+rowNames+" FROM "+tableName+" "+condition
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    mydb.commit()
    return myresult



#-----------------------------------INSERT INTO QUERY---------------------------------------


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

def insert_cmd_executed(cmd,status):
    sql = "INSERT INTO commands_executed (command,status) VALUES (%s, %s)"
    val = (cmd,status)
    mycursor.execute(sql, val)
    mydb.commit()





#-----------------------------------SELECT QUERY---------------------------------------
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
    lis.append({
            "id"    :0,
            "cmd"   :"null",
            "priority":"na",
            "frm"   : "hira",
            "exec"  : 0
            })
    mycursor.execute("SELECT * FROM commands WHERE exec = 0")
    myresult = mycursor.fetchall()
    mydb.commit()
    if len(myresult)>0:
        lis.pop(0)
    for x in myresult:
        l={}
        l["id"]=x[0]
        l["cmd"]=x[1]
        l["priority"]=x[2]
        l["frm"]=x[3]
        l["exec"]=x[4]
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

def get_hira_info():
    val={}
    mycursor.execute("SELECT * FROM hira_info WHERE id=1")
    myresult = mycursor.fetchall()
    mydb.commit()
    for res in myresult:
        val["pid"]=res[1]
        val["tty"]=res[2]
        val["status"]=res[3]
        val["init"]=res[4]
        val["adb"]=res[5]
        val["sleep"]=res[6]
    return val




#-----------------------------------UPDATE QUERY---------------------------------------
def update_dev_status(dev_id,status):
    sql="UPDATE home_automation SET status = '"+str(status)+"' WHERE id="+str(dev_id)+";"
    mycursor.execute(sql)
    mydb.commit()
    return "ok"

def update_dev_param(dev_id,param):
    sql="UPDATE home_automation SET param = '"+str(param)+"' WHERE id="+str(dev_id)+";"
    mycursor.execute(sql)
    mydb.commit()
    return "ok"

def update_cmd_table(n):
    sql="UPDATE commands SET exec = 1 WHERE id="+str(n)+";"
    mycursor.execute(sql)
    mydb.commit()

def update_hira_info(val):
    sql="UPDATE hira_info SET pid = '"+str(val["pid"])+"',tty = '"+str(val["tty"])+"',status ="+str(val["status"])+",init="+str(val["init"])+" ,adb="+str(val["adb"])+",sleep="+str(val["sleep"])+" WHERE id=1"
    mycursor.execute(sql)
    mydb.commit()


#-----------------------------------DELETE QUERY---------------------------------------
def del_cmd_entries():
    sql="DELETE FROM commands_executed"
    mycursor.execute(sql)
    mydb.commit()
    return "ok"

def del_cmd():
    sql="DELETE FROM commands"
    mycursor.execute(sql)
    mydb.commit()
    return 1
