
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
    say="which video you want"
    f.out.txt_out(say,'100')
    search_word=f.inp.get_cmd("Search Keyword").replace(" ","+")
    #print("YT DEBUG:Search Command:"+search_word)

    #adb_cmd="start com.google.android.youtube"
    adb_cmd="start "+yt_search_url+search_word
    
    re=f.adb.exec_adb_am_shell(adb_cmd)
    if re:
        
        f.db.insert_cmd_executed("open youtube","1")#insert init done to DB
        return 1
    else:
        f.db.insert_cmd_executed("open youtube","0")#insert init done to DB
        return 0


def close_youtube(command):
    adb_cmd="force-stop com.google.android.youtube"
    re=f.adb.exec_adb_am_shell(adb_cmd)
    if re:
        f.db.insert_cmd_executed("close youtube","1")#insert init done to DB
        return 1
    else:
        f.db.insert_cmd_executed("close youtube","0")#insert init done to DB
        return 0


