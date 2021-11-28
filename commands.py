import import_file as f
mode=2#1:voice input 2:Terminal input 3:Serial input--> Get this mode from GUI


def fetch_frm_db():
    return f.db.get_commands()

def get_list_sz(lis):
    return len(lis)

def start_exe():
    lis=fetch_frm_db()
    list_len=get_list_sz(lis)
    if  list_len > 0 and lis[0]["id"] !=0:
        #for High priority 
        for n in range (list_len):
            if lis[n]["priority"]=="high":
                f.exe.exec_commands(lis[n]["cmd"]) #executing high priority command 
                f.db.update_cmd_table(lis[n]["id"]) #making command as executed
                lis.pop(n) #deleting command from fetch list
                list_len=get_list_sz(lis)


        #for MED priority 
        for n in range (list_len):
            if lis[n]["priority"]=="med":
                print("Executing <MED> command with ID->"+str(lis[n]["id"]))
                f.exe.exec_commands(lis[n]["cmd"]) #executing high priority command 
                f.db.update_cmd_table(lis[n]["id"]) #making command as executed
                lis.pop(n) #deleting command from fetch list
                list_len=get_list_sz(lis)


        #for Low priority 
        for n in range (list_len):
            if lis[n]["priority"]=="low":
                print("Executing <LOW> command with ID->"+str(lis[n]["id"]))
                f.exe.exec_commands(lis[n]["cmd"]) #executing high priority command 
                f.db.update_cmd_table(lis[n]["id"]) #making command as executed
                lis.pop(n) #deleting command from fetch list
                list_len=get_list_sz(lis)

            
    


        


#def get_voice_cmd():
##   return f.ser.ser_read().decode('UTF-8')
#    return str(f.sprc.takeCommand())  
#def get_term_cmd():
#    return input("Command:")
#def get_dash_cmd():
#    db_val=f.db.get_dash_cmd()
#    return db_val["cmd"]
#  
##def get_input():
##    #voice=threading.Thread(target=get_voice_cmd)
##    #term =threading.Thread(target=get_term_cmd)
##    #dash =threading.Thread(target=get_dash_cmd)
##    #print (get_dash_cmd().lower())
##    return get_term_cmd().lower()
#def get_input():
#    global mode
#    if mode==1:
#        return get_voice_cmd().lower()
#    elif mode==2:
#        return get_term_cmd().lower()
    
