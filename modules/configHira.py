
from modules import modulePkg as mPkg
moduleLogPriority=1
#To print the output of each module status according to priority
log_en=0    #0:disable 1:enable
log_priority=1 #1:high 2:medium 3:low (low will print all high,medium,low, medium will print all medium and high, high will print only high)
#To define input/output mode
inputMode=0 #0:Terminal 1:speech 2:serial com
outputMode=0 #0:TTS 1:terminal 2:serial com

#Enabling some features
adb_en=0 # Enable ADB 0:disable 1:enable
serialCom_en=0 #Enable Serial communication 0:disable 1:enable


haltInpThread=0
ExecutionInProgress=0

def getConfiguration():
    cfg={}
    dbData=mPkg.db.SelectData('configuration','*','WHERE id = 1')
    for x in dbData:
        cfg['version']=x[1]
        cfg['test_en']=x[2]
        cfg['inputMode']=x[3]
        cfg['outputMode']=x[4]
        cfg['remoteDash']=x[5]
        cfg['adb_en']=x[6]
        cfg['serialCom_en']=x[7]
        cfg['hiraWheels']=x[8]
        cfg['cam_en']=x[9]
    return cfg
