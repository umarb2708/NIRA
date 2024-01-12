#----------------------------------------------------------------
#               HIRA(Human Intelligent Robo Assistant)
#               Developed by : Innovize Tech Solution
#----------------------------------------------------------------
#                       Module: modulePkg.py 
#               Contains handle for all modules created
#----------------------------------------------------------------
#outside package
import mysql.connector
from multipledispatch import dispatch


from modules import inputData as inp
from modules import mysql_db as db



#Misc Packages for data process
from modules import parse_data as parser #Parse keys, data, and datatype from dict