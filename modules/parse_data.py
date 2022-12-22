#==============================================================================================================
#                          HIRA Human Intelligent Robo Assistance
#                                     ---------------
#                                 Innovize Electro Solutions
#--------------------------------------------------------------------------------------------------------------
#                                Design and Developed by UMAR B
#--------------------------------------------------------------------------------------------------------------
# This modules parses the data
#==============================================================================================================

DebugModule=0
myDataDict={}

#To get type of elements in dictionary
def getDataType(MyDict):
    out=""   # temperory data
    retData=""    # Function return data
    for key in MyDict:
        if("int" in str(type(MyDict[key]))):
            out=out+"%s,"
        elif("str" in str(type(MyDict[key]))):
            out=out+"%s,"
        elif("float" in str(type(MyDict[key]))):
            out=out+"%s,"
    retData=out[:-1]
    return retData
#To get the keys
def getKeys(MyDict):
    retData=""    # Function return data
    for key in MyDict:
        retData=retData+key+","
    retData=retData[:-1]
    return retData
# To return datas of Dictionary
def getData(MyDict):
    retData=[]   # Function return data
    for key in MyDict:
        retData.append(MyDict[key])
    return retData   


if DebugModule==1 :
    MyDataDict={
        "Brand": "Peter England",
        "size":  2.5,
        "Name": "Umar",
        "cost": 199
    }
    sql= "INSERT INTO user_log ("+getKeys(MyDataDict)+") VALUES ("+getDataType(MyDataDict)+")"
    values=getData(MyDataDict)

    print(sql)
    print(values)

