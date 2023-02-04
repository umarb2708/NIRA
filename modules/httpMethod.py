#==============================================================================================================
#                          HIRA Human Intelligent Robo Assistance
#                                     ---------------
#                                 Innovize Electro Solutions
#--------------------------------------------------------------------------------------------------------------
#                                Design and Developed by UMAR B
#--------------------------------------------------------------------------------------------------------------
#Module Name: httpMethod.py
#Module description: To do http methods like get post
#==============================================================================================================
import requests
#from modules import modulePkg as mPkg
moduleLogPriority=1

def post(url,query_args):
    x = requests.post(url, data = query_args,timeout=60)
    return x.text

def doRequest(url,timeout):
    x=""
    try:
        x=request = requests.get(url, timeout=timeout)
        x=x.text
    except (requests.ConnectionError, requests.Timeout) as exception :
        x="Fail"
    return x
print(post("https://hira.innovize.in/FaceRecog/index.php",{}))
