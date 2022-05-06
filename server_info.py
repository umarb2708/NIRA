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

web="https://hirarobot.innovize.in/"
timeout=5
connected=0;
ngrok_started=0
pubIP="hira.local"

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
        request = requests.get(web, timeout=timeout)
        connected=1
    except (requests.ConnectionError, requests.Timeout) as exception :
        connected=0
    return connected
def get_battery_status():
    return 100

def get_LocalIP():
    ip=os.popen("hostname -I").read()[:-1]
    ips=ip.split()
    return ips[0]

def get_PublicIP():
    #currently using NGROK for public access
    ngrok_started=0
    pubIP="hira.local"  

    cmd="ps -aux | grep ngrok | grep 'sl\|Sl'"
    out=os.popen(cmd).readline()[:-1]
    if "./ngrok http 80 --log=stdout" in out:
        ngrok_started=1
        f=open("/home/pi/HIRA/logs/server.log","r")
        for lane in f:
            lane.replace("\n","")
            if "PublicIP" in lane:
                l=lane.split(':')
                pubIP=l[1]
    else:
        url="NACK"
        os.chdir("/home/pi/HIRA")
        ng=os.popen("./ngrok http 80 --log=stdout > logs/ngrok.log &").read()[:-1]
        time.sleep(10)
        f=open("/home/pi/HIRA/logs/ngrok.log","r")
        for lane in f:
            if "https" in lane:
                l=lane.split()
                url=l[7].replace("url=https://","")
                pubIP=url
    return pubIP

def get_hiraStat():
    disabled=1
    sleep=0
    cmd="ps -aux | grep hira.py | grep 's+\|S+\|Sl+'"
    out=os.popen(cmd).readline()[:-1]
    if "/home/pi/HIRA/hira.py" in out:
        disabled=0
    else:
        disabled=1
    sleep=get_hira_info()["sleep"]

    if disabled :
        return 0
    elif  disabled==0 and sleep:
        return 1
    else :
        return 2



def server_details():
    values["temp"]=str(get_cpu_temp())
    values["cpu_load"]=str(get_cpu_load())
    values["used_ram"]=str(get_ram_usage())
    values["used_mem"]=str(get_mem_usage())
    values["up_time"]=str(get_uptime())
    values["battery"]=str(get_battery_status())
    values["devStat"]=str(check_connectivity())
    values["hiraStat"]=str(get_hiraStat())
    values["LocalIP"]=str(get_LocalIP())
    values["PublicIP"]=str(get_PublicIP())
    values["user"]=str("hira_admin")
    return values

def display_info(values):
    print("Temp:"+values["temp"])
    print("Load:"+values["cpu_load"])
    print("RAM :"+values["used_ram"])
    print("Mem :"+values["used_mem"])
    print("Time:"+values["up_time"])
    print("dev :"+values["devStat"])
    print("hira:"+values["hiraStat"])
    print("Local:"+values["LocalIP"])
    print("Public:"+values["PublicIP"])

def storeValues(values):
    out_f=open("/home/pi/HIRA/logs/server.log",'w')
    out_f.write("Temperature:"+values["temp"]+"\n")
    out_f.write("CPU Load:"+values["cpu_load"]+"\n")
    out_f.write("RAM Usage:"+values["used_ram"]+"\n")
    out_f.write("Memory Use :"+values["used_mem"]+"\n")
    out_f.write("Up Time:"+values["up_time"]+"\n")
    out_f.write("dev Status :"+values["devStat"]+"\n")
    out_f.write("hira Status:"+values["hiraStat"]+"\n")
    out_f.write("LocalIP:"+values["LocalIP"]+"\n")
    out_f.write("PublicIP:"+values["PublicIP"]+"\n")

def send_to_website(args):
    global web
    x = requests.post(web+"/get-rpi-data.php", data = args)
    return x.text    


#Database Access
def insert_raspi_info(values):
    sql="UPDATE `raspi_info` SET `temp` = '"+values["temp"]+"', `cpu_load` = '"+values["cpu_load"]+"', `used_ram` = '"+values["used_ram"]+"', `used_mem` = '"+values["used_mem"]+"', `up_time` = '"+values["up_time"]+"', `devStat` = '"+values["devStat"]+"', `hiraStat` = '"+values["hiraStat"]+"', `LocalIP` = '"+values["LocalIP"]+"', `PublicIP` = '"+values["PublicIP"]+"' WHERE `raspi_info`.`id` = 1;"
    mycursor.execute(sql)
    mydb.commit()
    #print("Server info inserted->"+str(sql))
        
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

while 1:
    val=server_details()
    #display_info(val)
    storeValues(val)
    insert_raspi_info(val)
    res=send_to_website(val)
    if "Error:" in res:
        print(str(res))
    #insert_raspi_info()
    #get_hira_details()
    #insert_hira_info()
    #time.sleep(10)


