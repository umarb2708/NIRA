import os
import psutil

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

def server_details():
    values["temp"]=str(get_cpu_temp())
    values["cpu_load"]=str(get_cpu_load())
    values["used_ram"]=str(get_ram_usage())
    values["used_mem"]=str(get_mem_usage())
    values["up_time"]=str(get_uptime())
    return values
    
def display_info():
    print("Temperature:"+str(get_cpu_temp()))
    print("Load:"+str(get_cpu_load())+"%")
    print("RAM:"+str(get_ram_usage())+"%")
    print("Memory:"+str(get_mem_usage())+"%")
    print("Uptime:"+str(get_uptime()))


display_info()
