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
    mPkg.db.deleteData("commands_executed")
    mPkg.db.deleteData("commands")
    if log_en==1:
        mPkg.logs.createLogFile()
    mPkg.db.insertData("commands_executed",dvVal)
    mPkg.db.UpdateData("hira_info",getHiraInfo(),"id = 1")
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

    
        



