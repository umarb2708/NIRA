#==============================================================================================================
#                          HIRA Human Intelligent Robo Assistance
#                                     ---------------
#                                 Innovize Electro Solutions
#--------------------------------------------------------------------------------------------------------------
#                                Design and Developed by UMAR B
#--------------------------------------------------------------------------------------------------------------
# To perform FTP file transfer to a server in remote. 
#==============================================================================================================
#import pysftp
import os
from ftplib import FTP
import import_file as f

#debugModule-> 1: To debug only this module
debugModule=1


#function to download any file from server
#Filename should be path+file
#def sftpgetfile(filename,host,user,psw):
#    sftp = pysftp.Connection(host, username=user, password=psw)
#    try :
#        os.chdir("ftpOut/")
#    except :
#        os.mkdir("ftpOut/")
#        os.chdir("ftpOut/")

#    sftp.get(filename)
#   sftp.close

#function to upload file 
#def sftpputfile(filename,host,user,psw):
#    ret = ""
#    sftp = pysftp.Connection(host, username=user, password=psw)
#    try :
#        os.chdir("FtpIn/")
#        sftp.put(filename)
#        ret = "Success"
#    except :
#        ret = "Error"
#        
#    sftp.close
#    return ret


def ftpupload(host,username,passwrd,filename,ServerPath,LocalPath ):
    #domain name or server ip:
    ret = ""
    try:
        ftp = FTP(host)
        ftp.login(user=username, passwd =passwrd )
        ftp.storbinary('STOR '+ServerPath+filename, open(LocalPath+filename, 'rb'))
        ret = "SUCCESS: FTP ulpload"
    except:
        ret = "ERROR: FTP ulpload"
    return ret

    
if debugModule ==1 :
    host='hira.innovize.in' #Sending to this host
    user='RpiFtpUser@hira.innovize.in' #FTP user name
    pswd='RpiFtp@HIRA123#' #FTP Pass
    filename='file.txt'  #Filename to send
    Spath='/FaceRecog/images/newface/' #path in Server
    Lpath="images/" #Local Path
    print(ftpupload(host,user,pswd,filename,Spath,Lpath))
