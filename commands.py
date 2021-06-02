import import_file as f
import threading
import time

def get_commands():
#    return f.ser.ser_read().decode('UTF-8')
     return f.sprc.recog_speech(30)    
  

