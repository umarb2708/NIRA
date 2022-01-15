import os
import psutil
import mysql.connector
import time
import requests


#---------LOCAL DATABASE CREDENTIAL-------------------
mydb = mysql.connector.connect(
  host="localhost",
  user="db_admin",
  password="Admin@HIRA123#",
  database="hira_db"
)

mycursor = mydb.cursor()

url="https://www.google.com/"
timeout=5
connected=0;

values={
        "SNO":1
        }
hira={
        "id":1
    }
init_dne=0
def get_cpu_temp():
    cmd="vcgencmd measure_temp"
    temp=os.popen(cmd).read()[:-1]
    temp=temp.replace("temp=","").replace("'C","")
    return temp

def get_cpu_load():
    load=psutil.cpu_percent(interval=1)
    return load

def get_ram_usage():
    ram=psutil.virtual_memory()[2]
    return ram


def get_mem_usage():
    mem=psutil.disk_usage('/')[3]
    return mem
def get_uptime():
    cmd="uptime -p"
    uptime=os.popen(cmd).read()[:-1].replace("up ","").replace("weeks","w").replace("days","d").replace("hour","h").replace("minutes","m")
    return uptime

def check_connectivity():
    try:
        request = requests.get(url, timeout=timeout)
        connected=1
    except (requests.ConnectionError, requests.Timeout) as exception :
        connected=0
    return connected


def server_details():
    values["temp"]=str(get_cpu_temp())
    values["cpu_load"]=str(get_cpu_load())
    values["used_ram"]=str(get_ram_usage())
    values["used_mem"]=str(get_mem_usage())
    values["up_time"]=str(get_uptime())
    values["connection"]=str(check_connectivity())
    #return values

def get_hira_details():
    global init_dne
    cmd="ps -aux | grep hira.py | grep 's+\|S+'"
    out=os.popen(cmd).readline()[:-1]
    if "/home/pi/HIRA/hira.py" in out:
        t=out.split()
        hira["user"]=str(t[0])
        hira["pid"]=str(t[1])
        hira["tty"]=str(t[6])
        hira["status"]=str(1)
        hira["init"]=str(1) if init_dne else str(0)
        init_dne=1
    else:
        hira["pid"]=str(0)
        hira["tty"]="pts/0"
        hira["status"]=str(0)
        hira["init"]=str(init_dne)
def display_info():
    print("Temperature:"+str(get_cpu_temp()))
    print("Load:"+str(get_cpu_load())+"%")
    print("RAM:"+str(get_ram_usage())+"%")
    print("Memory:"+str(get_mem_usage())+"%")
    print("Uptime:"+str(get_uptime()))

def insert_raspi_info():
    sql="UPDATE `raspi_info` SET `temp` = '"+values["temp"]+"', `cpu_load` = '"+values["cpu_load"]+"', `used_ram` = '"+values["used_ram"]+"', `used_mem` = '"+values["used_mem"]+"', `up_time` = '"+values["up_time"]+"', `connection` = '"+values["connection"]+"' WHERE `raspi_info`.`id` = 1;"
    mycursor.execute(sql)
    mydb.commit()
    print("Server info inserted->"+str(sql))

def insert_hira_info():
        sql="UPDATE `hira_info` SET `pid` = '"+hira["pid"]+"', `tty` = '"+hira["tty"]+"', `status` = '"+hira["status"]+"', `init` = '"+hira["init"]+"' WHERE `hira_info`.`id` = 1;"
        mycursor.execute(sql)
        mydb.commit()
        print("Hira info inserted->"+str(sql))

while 1:
    server_details()
    insert_raspi_info()
    #get_hira_details()
    #insert_hira_info()
    time.sleep(10)


