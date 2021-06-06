import os
import time
yt_watch_url="https://www.youtube.com/watch?v="
yt_search_url="https://www.youtube.com/results?search_query="
yt_param={
        "video_code":"WpOJDaj0MM4",
        "search_code":"IICDC2017 Team 126652 Quarterfinal Submission",
        "search":0,
        "watch":1,
        "stop":0
        
        }

def connect_android():
    connected=0
    os.system("android-adb kill-server")
    while (connected==0):
        reply=os.popen("android-adb connect 192.168.15.36:5555").read()[:-1]
        if "connected to" in reply:
            connected=1
            print("ADB connected successfully")
def open_youtube(yt_param):
    if yt_param["stop"]==1:
        re=os.popen("android-adb shell am force-stop com.google.android.youtube").read()[:-1]
    elif yt_param["watch"]==1:
        re=os.popen("android-adb shell am start  "+yt_watch_url+ yt_param["video_code"]).read()[:-1]
        print("Reply as:"+re)

connect_android()
time.sleep(3)
open_youtube(yt_param)
time.sleep(60)
yt_param["stop"]=1
open_youtube(yt_param)
