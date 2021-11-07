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
    print("Server info inserted")
while 1:
    server_details()
    insert_raspi_info()
    time.sleep(10)


