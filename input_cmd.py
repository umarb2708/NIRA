import import_file as f
mode=1

def get_term_cmd():
    inp=input("command:")
    return inp

def get_vce_cmd():
     return str(f.sprc.takeCommand())
 
def get_ser_cmd():
    return f.ser.ser_read()

def get_cmd():
    in_cmd=""
    if mode==0:
        in_cmd=get_vce_cmd()
    elif mode==1:
        in_cmd=get_term_cmd()
    elif mode ==2:
        in_cmd=get_ser_cmd()

    return in_cmd



def format_cmd():
    values={}
    values["command"]=get_cmd()
    values["priority"]="med"
    values["from"]="hira"
    return values
def insert_cmd():
    print("Getting input from terminal")
    f.db.insert_commands(format_cmd())

