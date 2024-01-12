#----------------------------------------------------------------
#               HIRA(Human Intelligent Robo Assistant)
#               Developed by : Innovize Tech Solution
#----------------------------------------------------------------
#                       Module: mysql.py 
#       Database handling like insert,delete,update,create
#----------------------------------------------------------------

from modules import modulePkg as mPkg
#---------LOCAL DATABASE CREDENTIAL-------------------
mydb = mPkg.mysql.connector.connect(
  host="localhost",
  user="db_admin",
  password="Admin@MDB123#",
  database="nira"
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
    mycursor.execute(sql,val)
    mydb.commit()
    return 1
#Function for SELECT query
# SELECT Query has two type
#   1. with condition
#   2. without condition
# We are using dispatch to do fundtion over riding

@mPkg.dispatch(str,str,str)
def SelectData(tableName,rowNames,condition):
    query="SELECT "+rowNames+" FROM "+tableName+" WHERE "+condition
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    mydb.commit()
    return myresult

@mPkg.dispatch(str,str)
def SelectData(tableName,rowNames):
    query="SELECT "+rowNames+" FROM "+tableName
    mycursor.execute(query)
    myresult = mycursor.fetchall()
    mydb.commit()
    return myresult
#Function for DELETE command
def deleteData(tableName):
    sql="DELETE FROM "+tableName
    mycursor.execute(sql)
    mydb.commit()
    return 1