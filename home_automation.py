import import_file as f

bulb_list=["bulb","light"]
lamp_list=["lamp","led","L E D", "LED"]
fan_list=["fan","FAN","F A N"]


def turn_on_device(command):
    dev=find_device(command)
    f.db.update_automation_table(dev["dev_num"],1)

    term_out="dev:"+dev["dev_name"]+"st:ON room:"+dev["room"]+" floor:"+dev["floor"]
    f.out.txt_out(term_out,6)

    say=dev["dev_name"]+" turned on ."
    f.out.txt_out(say,1)
    
    f.db.insert_cmd_executed("turn on the "+dev["dev_name"],"1")

def turn_off_device(command):
    dev=find_device(command)
    f.db.update_automation_table(dev["dev_num"],0)

    term_out="dev:"+dev["dev_name"]+"st:OFF room:"+dev["room"]+" floor:"+dev["floor"]
    f.out.txt_out(term_out,6)

    say=dev["dev_name"]+" turned off ."
    f.out.txt_out(say,1)

    f.db.insert_cmd_executed("turn off the "+dev["dev_name"],"1")


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

