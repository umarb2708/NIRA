#==============================================================================================================
#                          HIRA Human Intelligent Robo Assistance
#                                     ---------------
#                                 Innovize Electro Solutions
#--------------------------------------------------------------------------------------------------------------
#                                Design and Developed by UMAR B
#--------------------------------------------------------------------------------------------------------------
# module name: remoteFtp.py
# To perform SFTP file transfer to a server in remote. 
#==============================================================================================================
import os
import sys
from ftplib import FTP
#debugModule-> 1: To debug only this module
debugModule=0
moduleLogPriority=1
for x in sys.argv:
    if x == "--debug":
        debugModule=1

if debugModule == 0:
    from modules import modulePkg as mPkg
#function to upload file 
def ftpupload(host,username,passwrd,filename,serverPath,localPath="media/" ):
    #domain name or server ip:
    ret = ""
    try:
        ftp = FTP(host)
        ftp.login(user=username, passwd =passwrd )
        ftp.storbinary('STOR '+serverPath+filename, open(localPath+filename, 'rb'))
        ret = "SUCCESS: FTP ulpload"
    except:
        ret = "ERROR: FTP ulpload"
    return ret

    
if debugModule ==1 :
    host='hira.innovize.in'
    user='RpiFtpUser@hira.innovize.in'
    pswd='RpiFtp@HIRA123#'
    filename='nothing.txt'
    serverPath='/FaceRecog/images/newface/'
    print(ftpupload(host,user,pswd,filename,serverPath))
