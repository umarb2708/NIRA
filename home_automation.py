

bulb_list=["bulb","light","lamp"]


def turn_on_device(command):
    for x in bulb_list:
        if x in command:
            print("Turning on light")
            return "Turning on light"
            break

def turn_off_dev(command):
    for x in bulb_list:
        if x in command:
            print("Turning off light")
            return "Turning off light"
            break

