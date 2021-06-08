import import_file as f
import threading
import time
mode=2#1:voice input 2:Terminal input 3:Serial input--> Get this mode from GUI

def get_voice_cmd():
#   return f.ser.ser_read().decode('UTF-8')
    return str(f.sprc.takeCommand())  
def get_term_cmd():
    return input("Command:")
  

def get_input():
    global mode
    if mode==1:
        return get_voice_cmd()
    elif mode==2:
        return get_term_cmd()
    
