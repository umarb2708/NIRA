import import_file as f
import threading
import time
mode=2#1:voice input 2:Terminal input 3:Serial input--> Get this mode from GUI

def get_voice_cmd():
#   return f.ser.ser_read().decode('UTF-8')
    return str(f.sprc.takeCommand())  
def get_term_cmd():
    return input("Command:")
def get_dash_cmd():
    db_val=f.db.get_dash_cmd()
    return db_val["cmd"]
  
def get_input():
    #voice=threading.Thread(target=get_voice_cmd)
    #term =threading.Thread(target=get_term_cmd)
    #dash =threading.Thread(target=get_dash_cmd)
    #print (get_dash_cmd().lower())
    return get_term_cmd().lower()
#def get_input():
#    global mode
#    if mode==1:
#        return get_voice_cmd().lower()
#    elif mode==2:
#        return get_term_cmd().lower()
    
