import mysql.connector
from modules import modulePkg as mPkg

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
    col=mPkg.parser.getKeys(values)
    Datatype=mPkg.parser.getDataType(values)
    val=mPkg.parser.getData(values)
    sql= "INSERT INTO "+tableName+" ("+col+") VALUES ("+Datatype+")"
    values=mPkg.parser.getData(values)
    #print(sql)
    #print(values)
    mycursor.execute(sql, val)
    mydb.commit()
    return 1
#Function for UPDATE query
def UpdateData(tableName,values,condition):
    setval=""
    for key in values:
        if("int" in str(type(values[key]))):
            setval=setval+key+"="+"%s,"
        elif("str" in str(type(values[key]))):
            setval=setval+key+"="+"%s,"
        elif("float" in str(type(values[key]))):
            setval=setval+key+"="+"%s,"
    setval=setval[:-1]

    sql = "UPDATE "+tableName+" SET "+setval+" WHERE "+condition
    val = mPkg.parser.getData(values)
    #print(sql)
    #print(val)    
    mycursor.execute(sql,val)
    mydb.commit()
#Function for SELECT query
def SelectData(tableName,rowNames,condition):
    query="SELECT "+rowNames+" FROM "+tableName+" "+condition
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    mydb.commit()
    return myresult

#Function for DELETE command




