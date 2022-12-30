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
def startExecution():
    lis_h=mPkg.db.SelectData("commands","*","WHERE priority = 'high'")
    lis_m=mPkg.db.SelectData("commands","*","WHERE priority = 'med'")
    lis_l=mPkg.db.SelectData("commands","*","WHERE priority = 'low'")

    #print("High Priority List")
    #print(lis_h)
    #print("Med Priority List")
    #print(lis_m)
    #print("Low Priority List")
    #print(lis_l)
    
