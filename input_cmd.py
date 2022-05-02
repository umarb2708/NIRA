import import_file as f
mode=1#0:voice input 1:Terminal input 2:Serial input--> Get this mode from GUI
high_cmd=["sleep","wake up","wakeup","restart","reboot","shutdown","power off"]

def get_term_cmd(st):
    try:
        inp=input(st+":")
    except:
        inp='dont process'
    return inp

def get_vce_cmd():
     return str(f.sprc.takeCommand())
 
def get_ser_cmd():
    return f.ser.ser_read()

def get_cmd(st):
    in_cmd=""
    if mode==0:
        in_cmd=get_vce_cmd()
    elif mode==1:
        in_cmd=get_term_cmd(st)
    elif mode ==2:
        in_cmd=get_ser_cmd()
    
    return in_cmd



def format_cmd():
    values={}
    values["command"]=get_cmd("Command")
    if values["command"].lower() == "hira":
        st="Yes sir"
        f.out.txt_out(st,'100')
        values["command"]="hira "+get_cmd("Command")
    values["priority"]="med"
    for x in high_cmd:
        if x in values["command"]:
            values["priority"]="high"
            break
    values["from"]="hira"
    return values
def insert_cmd():
    val=format_cmd()
    if val["command"] !='dont process':
        f.db.insert_commands(val)

