import import_file as f


def get_commands():
    #Commands from speech recognisation comes here
    serial_cmd=f.ser.ser_read().decode('UTF-8')#commands from serial interface
    return serial_cmd
