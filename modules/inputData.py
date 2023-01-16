#==============================================================================================================
#                          HIRA Human Intelligent Robo Assistance
#                                     ---------------
#                                 Innovize Electro Solutions
#--------------------------------------------------------------------------------------------------------------
#                                Design and Developed by UMAR B
#--------------------------------------------------------------------------------------------------------------
#Module Name: input.py
#Module description: To get input to HIRA via terminal or serial monitor or voice input
# MODE:0->Terminal(by default) 1:voice input 2:serial monitor input
#==============================================================================================================
from modules import modulePkg as mPkg
from pytimedinput import timedInput
moduleLogPriority=2

#Function to get terminal Input
def getTerminalInput(command):
    returnData=''
    #mode=mPkg.config.getConfiguration()['inputMode']
    termCmd,timeOut=timedInput(command+":",5)
    if timeOut :
        print("Input Timeout")
        returnData='do nothong'
    else:
        returnData=termCmd
    return str(returnData)



def getInput(command):
    retStr=''
    while retStr=='':
        retStr=getTerminalInput(command)
    return retStr
def formatInput():
    cmd=getInput("command")
    if len(cmd) <= 7 and "hira" in cmd :
        mPkg.out.putOutput("What can I do for you")
        cmd=getInput("command")
        cmd="hira "+cmd
    #print(cmd)
    return cmd
def insertCmd():
    if mPkg.config.ExecutionInProgress == 0:
        command= formatInput()
        if "hira" in command:
            val={
                    "command":command,
                    "priority":"high" if "shutdown" in command or "reboot" in command else "med", 
                    "frm":"hira",
                    "exec":0
                    }
            mPkg.db.insertData("commands",val)
    

