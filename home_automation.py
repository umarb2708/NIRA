import import_file as f

bulb_list=["bulb","light","lamp"]


def turn_on_device(command):
    for x in bulb_list:
        if x in command:
            print("Turning on light")
            f.db.update_automation_table(4,"1")
            return "Turning on light::OK"
            break

def turn_off_dev(command):
    for x in bulb_list:
        if x in command:
            print("Turning off light")
            f.db.update_automation_table(4,"0")
            return "Turning off light::OK"
            break

