#==============================================================================================================
#                          HIRA Human Intelligent Robo Assistance
#                                     ---------------
#                                 Innovize Electro Solutions
#--------------------------------------------------------------------------------------------------------------
#                                Design and Developed by UMAR B
#--------------------------------------------------------------------------------------------------------------
# This modules used for initialisation of HIRA at startup
#==============================================================================================================

from modules import modulePkg as mPkg
#Deleting all previous data
log_en=1
def initHira():
    dvVal={
            "command":"Initialisation",
            "status":'1'
            }

    string="Hi Sir "+mPkg.date.wishme()+". Please wait while initialisation going on" #Starting voice output
    mPkg.out.putOutput(string);
    print("Initialising HIRA")
    mPkg.db.deleteData("commands_executed")
    mPkg.db.deleteData("commands")
    print("Deleted old commands:success")
    if log_en==1:
        mPkg.logs.createLogFile()
        print("Log File creation:success")
    checkSubMcuStatus()#Checking sub mcu status
    
    mPkg.db.insertData("commands_executed",dvVal)
    mPkg.db.UpdateData("hira_info",getHiraInfo(),"id = 1")
    string="I am ready. Command me preceeding with HIRA"
    mPkg.out.putOutput(string);
    print("Initialisation completed")
    return 1
def getHiraInfo():
    info={}
    info['pid']=mPkg.mon.curr_pid()
    info['tty']=mPkg.mon.get_tty()
    info['adb']=mPkg.mon.checkAdb()
    info['sleep']=0
    info['init']=1
    info['status']=1

    return info
def checkSubMcuStatus():
    print("Checking sub MCU status.......")
    dbData=mPkg.db.SelectData('hiraSubMCU','*','WHERE id = 1')
    for x in dbData:
        if x[1] == "1":
            print("Hirawheels connection:success")
        else:
            print("Hirawheels connection:failed")
        if x[2] == "1":
            print("Hira Cam connection:success")
        else:
            print("Hira Cam connection:failed")
        if x[3] == "1":
            print("Hira Eyes connection:success")
        else:
            print("Hira Eyes connection:failed")
    
    return 0

    
        



