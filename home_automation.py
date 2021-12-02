import import_file as f

bulb_list=["bulb","light"]
lamp_list=["lamp","led","L E D", "LED"]
fan_list=["fan","FAN","F A N"]
clr_list=["red","blue","green"]

clr_param={
        "red":0,
        "green":1,
        "blue":2
        }


def turn_on_device(command):
    dev=find_device(command)
    f.db.update_dev_status(dev["dev_num"],1)

    term_out="dev:"+dev["dev_name"]+"st:ON room:"+dev["room"]+" floor:"+dev["floor"]
    f.out.txt_out(term_out,'011')

    say=dev["dev_name"]+" turned on ."
    f.out.txt_out(say,'100')
    
    f.db.insert_cmd_executed("turn on the "+dev["dev_name"],"1")
    return 1

def turn_off_device(command):
    dev=find_device(command)
    f.db.update_dev_status(dev["dev_num"],0)

    term_out="dev:"+dev["dev_name"]+"st:OFF room:"+dev["room"]+" floor:"+dev["floor"]
    f.out.txt_out(term_out,'011')

    say=dev["dev_name"]+" turned off ."
    f.out.txt_out(say,'100')

    f.db.insert_cmd_executed("turn off the "+dev["dev_name"],"1")
    return 1

def change_colour(command):
    param=0
    dev=6
    for cl in clr_list:
        if cl in command:
            param= clr_param[cl]
            break

    f.db.update_dev_param(dev,param)
    say="colour changed."
    f.out.txt_out(say,'100')

    f.db.insert_cmd_executed("change LED colour","1")
    return 1


        

def find_device(command):
    dev_det={
            "dev_num"   :0,
            "dev_name"  :"no device",
            "room"      :"master bedroom",
            "floor"     :"first"
            }
    #Checking bulb list in commands
    for dev in bulb_list:
        if dev in command and dev_det["dev_num"] == 0:
            dev_det["dev_num"]  =4
            dev_det["dev_name"] ="light"
            break

    for dev in fan_list :
        if dev in command and dev_det["dev_num"] == 0:
            dev_det["dev_num"]  =5
            dev_det["dev_name"] ="fan"
            break

    for dev in lamp_list :
        if dev in command and dev_det["dev_num"] == 0:
            dev_det["dev_num"]  =6
            dev_det["dev_name"] ="night lamp"
            break
    return dev_det

