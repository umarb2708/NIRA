import os
import time
import import_file as f
remote_dash=1
connected=0
from pyngrok import ngrok


def connect_ngrok():
    url="NACK"
    ng=os.popen("./ngrok http 1880 --log=stdout > ngrok.log &").read()[:-1]
    time.sleep(10)
    #os.system("head ngrok.log > ng.txt")
    f=open("/home/pi/HIRA/ngrok.log","r")
    for lane in f:
        if "https" in lane:
            l=lane.split()
            url=l[7].replace("url=https://","")
            print (l[7])
    return url

def check_connected():
    connected=0
    tunnels = ngrok.get_tunnels()
    print (tunnels)
    return connected

def connect_remote_dash(en_dash):
    connected=0
    en_remote_dash=en_dash
    connected=check_connected()
    if en_remote_dash and not connected:
        print("DEBUG Creating new connection:EN:"+str(en_remote_dash)+" CON:"+str(connected))
        query_args = { 
                'api_key':'tPmAT5Ab3j7F9',
                'url':'f730-2409-4073-30d-ca9-d69c-81df-39fe-e334.ngrok.io'
                }
        website='https://hirarobot.innovize.in/get-rpi-data.php'
        query_args['url']=connect_ngrok()
        if "successfully" in f.http.post(website,query_args):
            connected=1
        #Add Log Error
    else :
        connected=0 
    return connected




if connect_remote_dash(1) == 1:
    print ("DONE")
