from modules import parse_data as parser
DebugModule=1
if DebugModule==1 :
    MyDataDict={
        "Brand": "Peter England",
        "size":  2.5,
        "Name": "Umar",
        "cost": 199
    }
    sql= "INSERT INTO user_log ("+parser.getKeys(MyDataDict)+") VALUES ("+parser.getDataType(MyDataDict)+")"
    values=parser.getData(MyDataDict)

    print(sql)
    print(values)