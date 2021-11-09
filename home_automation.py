import import_file as f
dev_num=0
bulb_list=["bulb","light","lamp"]


def turn_on_device(command):
    print("Turning on light")
    f.db.update_automation_table(find_device(command),1)
    return "Device:"+str(find_device(command))+" turned on::OK"

def turn_off_dev(command):
    print("Turning off Device")
    f.db.update_automation_table(find_device(command),0)
    return "Device:"+str(find_device(command))+" turned off::OK"


def find_device(command):

    if "light" in command:
        dev_num=4
    elif "fan" in command:
            dev_num=5
    elif "lamp" in command:
            dev_num=6
    else :
            dev_num=7
    return dev_num

