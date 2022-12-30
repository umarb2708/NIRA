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
mode=mPkg.init.inputMode


#Function to get terminal Input
def getTerminalInput(command):
    return str(input(command+":"))



def getInput(command):
    retStr="None"
    if mode==0:
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
    command= formatInput()
    if "hira" in command:
        val={
                "command":command,
                "priority":"high" if "shutdown" in command or "reboot" in command else "med", 
                "frm":"hira",
                "exec":0
                }
        mPkg.db.insertData("commands",val)
    

