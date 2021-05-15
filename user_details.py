import getpass
import socket


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
