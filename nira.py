#----------------------------------------------------------------
#               HIRA(Human Intelligent Robo Assistant)
#               Developed by : Innovize Tech Solution
#----------------------------------------------------------------
#                       Module: hira.py 
#                    Main module to start
#--------------------------------------------------------------
import multiprocessing 
import time
from modules import modulePkg as mPkg
val={
        "Name":'Hufsath',
        "age":19,
        "measure":170.3
}
mPkg.db.insertData('test_table',val)
print(mPkg.db.SelectData('test_table','Name, age'))