#==============================================================================================================
#                          HIRA Human Intelligent Robo Assistance
#                                     ---------------
#                                 Innovize Electro Solutions
#--------------------------------------------------------------------------------------------------------------
#                                Design and Developed by UMAR B
#--------------------------------------------------------------------------------------------------------------
#Module:hiraMonitor.py 
# Description:This module used to monitor Following Data(initial check up for before startup)
#               1.User Login, PID, user IP 
#               2.Interface conected like adb,ethernet,wifi,serial com,
#               3.Initial run and sleep status
#==============================================================================================================
import getpass
import os
import time
from modules import modulePkg as mPkg

def checkAdb():
    return 0
def checkSerialCom():

    return 0
def checkEthernet():

    return 0
def checkWifi():

    return 0
def checkHDMI():

    return 0
def checkHDD():

    return

def get_user():
    return getpass.getuser()
def curr_pid():
    return os.getpid()
def getServerStatus():
    serverStat={}
    dbRows=mPkg.db.SelectData('raspi_info','*','WHERE id = 1')
    for eachRow in dbRows:
        serverStat['temp']=eachRow[1]
        serverStat['cpu_load']=eachRow[2]
        serverStat['used_ram']=eachRow[3]
        serverStat['used_mem']=eachRow[4]
        serverStat['battery']=eachRow[6]
    return serverStat


def check_who():
    cmd="zgrep sshd /var/log/auth.log* | grep rhost | sed -re 's/.*rhost=([^ ]+).*/\\1/' | sort -u"
    who=os.popen(cmd).read()[:-1]
    return who
def get_tty():
    cmd="tty"
    tty=os.popen(cmd).read()[:-1]
    return tty  


def checkWarnings():
    serverstat=getServerStatus()
    alertTemperature(serverstat)
    alertBattery(serverstat)
    alertCPUusage(serverstat)
    alertRAMusage(serverstat)
    return 1
def alertTemperature(serverstat):
    val={
        "priority":"high", 
        "frm":"hira",
        "exec":0
            }
    if serverStat['temp'] >= 55 and serverStat['temp'] < 60:
        val["command"]="warn<->Temperature raise detected. Please check"
        mPkg.db.insertData("commands",val)
    elif serverStat['temp'] >= 60:
        val["command"]="warn<->Critical temperature detected. Initiating auto shutdown in 30 seconds"
        mPkg.db.insertData("commands",val)
        time.sleep(30)
        val["command"]="shutdown"
        mPkg.db.insertData("commands",val)
    return 1
def alertBattery(serverstat):
    val={
        "priority":"high", 
        "frm":"hira",
        "exec":0
            }
    if serverStat['battery'] >= 20 and serverStat['battery'] < 30:
        val["command"]="warn<->Low battery. Please charge"
        mPkg.db.insertData("commands",val)
    elif serverStat['battery'] < 20:
        val["command"]="warn<->Critical battery voltage. Initiating auto shutdown in 30 seconds"
        mPkg.db.insertData("commands",val)
        time.sleep(30)
        val["command"]="shutdown"
        mPkg.db.insertData("commands",val)
    return 1
def alertCPUusage(serverstat):
    val={
        "priority":"high", 
        "frm":"hira",
        "exec":0
            }
    if serverStat['cpu_load'] >= 70 and serverStat['cpu_load'] < 90:
        val["command"]="warn<->High CPU load detected. Please check"
        mPkg.db.insertData("commands",val)
    elif serverStat['cpu_load'] >90:
        val["command"]="warn<->Critical CPU load. Initiating auto shutdown in 30 seconds"
        mPkg.db.insertData("commands",val)
        time.sleep(30)
        val["command"]="shutdown"
        mPkg.db.insertData("commands",val)
    return 1
def alertRAMusage(serverstat):
    val={
        "priority":"high", 
        "frm":"hira",
        "exec":0
            }
    if serverStat['used_ram'] >= 70 and serverStat['used_ram'] < 90:
        val["command"]="warn<->High RAM usage detected. Please check"
        mPkg.db.insertData("commands",val)
    elif serverStat['used_ram'] >90:
        val["command"]="warn<->Critical RAM usage. Initiating auto shutdown in 30 seconds"
        mPkg.db.insertData("commands",val)
        time.sleep(30)
        val["command"]="shutdown"
        mPkg.db.insertData("commands",val)
    return 1
def alertMEMusage(serverstat):
    val={
        "priority":"high", 
        "frm":"hira",
        "exec":0
            }
    if serverStat['used_mem'] >= 70 and serverStat['used_mem'] < 90:
        val["command"]="warn<->High memory usage detected. Please check"
        mPkg.db.insertData("commands",val)
    elif serverStat['used_mem'] >90:
        val["command"]="warn<->Critical memory usage. Initiating auto shutdown in 30 seconds"
        mPkg.db.insertData("commands",val)
        time.sleep(30)
        val["command"]="shutdown"
        mPkg.db.insertData("commands",val)
    return 1



    

