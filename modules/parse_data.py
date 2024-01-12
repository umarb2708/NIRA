DebugModule=0
myDataDict={}
numDict={
    'one':      1,
    'two':      2,
    'three':    3,
    'four':     4,
    'five':     5,
    'six':      6,
    'seven':    7,
    'eight':    8,
    'nine':     9,
    'ten':      10,
    'twenty':   20,
    'thirty':   30,
    'fourty':   40,
    'fifty':    50,
    'sixty':    60,
    'seventy':  70,
    'eighty':   80,
    'ninety':   90,
    'hundred':  100
}
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
#Function to convert word numbers to intiger
def toInt(str):
    words=str.split(" ")
    num=0
    for x in words:
        for y in numDict:
            if x ==y:
                num=num+int(numDict[y])
    return num




if DebugModule==1 :
    st = 'hundred and twenty five'
    print(toInt(st))