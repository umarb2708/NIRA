import os
import time
def connect_android():
    connected=0
    num_turn=0
    os.system("android-adb kill-server")
    while (connected==0 & num_turn!=3):
        num_turn=num_turn+1;
        reply=os.popen("android-adb connect 192.168.43.198:5555").read()[:-1]
        if "connected to" in reply:
            connected=1
    if connected:
        return "ADB connection successfull"
    else:
        return "ADB connection failed"


def exec_adb_am_shell(cmd):
    adb_cmd="android-adb shell am "+cmd
    re=os.popen("android-adb shell am "+cmd).read()[:-1]
    return 1
def exec_adb_input_shell(cmd):
    re=os.popen("android-adb shell input "+cmd).read()[:-1]
    return 1


#res=connect_android()
#res=exec_adb_am_shell("start  https://www.youtube.com/results?search_query=node+red+and+adb")

