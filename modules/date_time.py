import datetime
moduleLogPriority=3
def get_date():
    return int(datetime.datetime.now().day)

def get_month():
    return int(datetime.datetime.now().month)

def get_year():
    return int(datetime.datetime.now().year)

def get_time():
    return datetime.datetime.now().strftime("%I:%M:%S")

def get_hour():
    return int(datetime.datetime.now().hour)
def getAlldateTime():
    return datetime.datetime.now().strftime("%d:%m:%Y::%I:%M:%S")

def wishme():
    hour=get_hour()
    if hour>=6 and hour<12:
        return "Good Morning"

    elif hour>=12 and hour<18:
        return "Good Afternoon"

    elif hour>=18 and hour<24:
        return "Good Evening"

    else:
        return "Good Night"
