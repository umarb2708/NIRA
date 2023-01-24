#==============================================================================================================
#                          HIRA Human Intelligent Robo Assistance
#                                     ---------------
#                                 Innovize Electro Solutions
#--------------------------------------------------------------------------------------------------------------
#                                Design and Developed by UMAR B
#--------------------------------------------------------------------------------------------------------------
#Module Name: executeCommands.py
#Module description: To execute the commands to HIRA with priority
#==============================================================================================================
from modules import modulePkg as mPkg
moduleLogPriority=1
def startExecution():
    lis_h=mPkg.db.SelectData("commands","*","WHERE priority = 'high' AND exec = 0")#high priority list
    lis_m=mPkg.db.SelectData("commands","*","WHERE priority = 'med' AND exec = 0")#Medium priority list
    lis_l=mPkg.db.SelectData("commands","*","WHERE priority = 'low' AND exec = 0")#Low Priority List

    #print("High Priority List")
    #print(lis_h)
    #print("Med Priority List")
    #print(lis_m)
    #print("Low Priority List")
    #print(lis_l)
    mPkg.config.ExecutionInProgress=1
    for row in lis_h:#Running High Priority list first
        executeCmd(row)
    for row in lis_m:#Running Medium Priority list then
        executeCmd(row)
    for row in lis_l:#Running Low Priority list last
        executeCmd(row)
    mPkg.config.ExecutionInProgress=0


    return 0

def executeCmd(cmdDetails):
    module=SearchKeyWord(cmdDetails[1])
    #print("Command:"+cmdDetails[1])
    result=eval("mPkg."+module+"('"+cmdDetails[1]+"')") 
    UpdateCmdStatus(cmdDetails,0)
    if mPkg.config.log_en ==1 and moduleLogPriority <= mPkg.config.log_priority :
        mPkg.log.writeLog("exe Command:"+cmdDetails[1]+"-->Done")



def SearchKeyWord(command):
    moduleFound=""
    CCdata=mPkg.db.SelectData("command_centre","*","")
    for row in CCdata:
        if row[2] in command:
            moduleFound=row[3]
            break

    return moduleFound
def UpdateCmdStatus(cmdDetails,ErrStatus):
    val={
            "exec":1
            }
    CmdID=cmdDetails[0]
    mPkg.db.UpdateData("commands",val,"id = "+str(CmdID))


