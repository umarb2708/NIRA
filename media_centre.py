
import import_file as f





def play_pause(cmd):
    adb_cmd="keyevent 85"
    f.adb.exec_adb_input_shell(adb_cmd)
    return 1

def next(cmd):
    adb_cmd="keyevent 87"
    f.adb.exec_adb_input_shell(adb_cmd)
    return 1

def previous(cmd):
    adb_cmd="keyevent 88"
    f.adb.exec_adb_input_shell(adb_cmd)
    return 1

def stop(cmd):
    adb_cmd="keyevent 86"
    f.adb.exec_adb_input_shell(adb_cmd)
    return 1

def mute(cmd):
    adb_cmd="keyevent 91"
    f.adb.exec_adb_input_shell(adb_cmd)
    return 1

def volume(cmd):
    if 'increase' in cmd or 'up' in cmd:
        adb_cmd="keyevent 24"
    elif 'decrease' in cmd or 'down' in cmd:
        adb_cmd="keyevent 25"
    f.adb.exec_adb_input_shell(adb_cmd)
    return 1


