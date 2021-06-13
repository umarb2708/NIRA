
import import_file as f
yt_watch_url="https://www.youtube.com/watch?v="
yt_search_url="https://www.youtube.com/results?search_query="
yt_param={
        "video_code":"WpOJDaj0MM4",
        "search_code":"IICDC2017 Team 126652 Quarterfinal Submission",
        "search":0,
        "watch":1,
        "stop":0
        
        }


def open_youtube(command):
    str="which video you want"
    f.tts.speak(str)
    search_word=f.cmd.get_input().replace(" ","+")
    #print("YT DEBUG:Search Command:"+search_word)

    #adb_cmd="start com.google.android.youtube"
    adb_cmd="start "+yt_search_url+search_word
    
    re=f.adb.exec_adb_am_shell(adb_cmd)
    if re:
        return "Youtube opened::OK"
    else:
        return "Error occured while opening youtube::FAIL"


def close_youtube(command):
    adb_cmd="force-stop com.google.android.youtube"
    re=f.adb.exec_adb_am_shell(adb_cmd)
    if re:
        return "Youtube close::OK"
    else:
        return "Error occured while opening youtube::FAIL"


