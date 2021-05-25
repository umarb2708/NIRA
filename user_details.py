import getpass
import socket
import psutil
import shutil
import re
import os
from gpiozero import CPUTemperature


path="/root/"
cpu = CPUTemperature()

def get_user():
    return getpass.getuser()

def get_Host_name_IP():
    host_ip=""
    try:
        host_name = socket.gethostname()
        host_ip = socket.gethostbyname(host_name)
        #print("Hostname :  ",host_name)
        #print("IP : ",host_ip)
    except:
        print("Unable to get Hostname and IP")
    return host_ip


def get_cpu_load():
    return psutil.cpu_percent(4)
def get_used_ram():
    return psutil.virtual_memory()[2]

def get_used_disk():
    stat=shutil.disk_usage(path)
    st=str(stat)
    st=st.replace("usage(","")
    st=st.replace(")","")
    st=st.replace("\s+","")
    used=re.split(",",st)
    byte_used=int(used[1].replace(" used=",""))
    gb_used=float(byte_used/1000000000)
    return format(gb_used,".2f")



def get_up_time():
    return os.popen('uptime -p').read()[:-1].replace("up ","").replace("hours","H").replace("minutes","M")

def get_cpu_temp():
    return cpu.temperature
