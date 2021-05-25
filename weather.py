import requests, json
url = 'https://api.openweathermap.org/data/2.5/weather?q=thrissur&appid=77bd683c4059c1ba2f440bf32d6c3b31'#Open api link here
values={
        "SNO":1
        }

def get_weather_info():
    res = requests.get(url)
    data = res.json()
    weather = data['weather'] [0] ['main'] 
    temp = data['main']['temp']
    wind_speed = data['wind']['speed']
    latitude = data['coord']['lat']
    longitude = data['coord']['lon']
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    description = data['weather'][0]['description'] 
    #print(str(temp)+" "+str(humidity)+"  "+str(wind_speed)+" "+str(description)+" "+str(weather))
    values["temp"]=str(temp)
    values["humidity"]=str(humidity)
    values["pressure"]=str(pressure)
    values["city"]="Thrissur"
    values["wind"]=str(wind_speed)
    values["overall"]=str(weather)
    values["description"]=str(description)
    return values;
    #print (values)
#get_weather_info()
def speak_weather_info():
    val=get_weather_info()
    speak_str=val["temp"]+" degree temperature and "+val["humidity"]+" percent humidity with "+val["wind"]+" wind speed at "+val["city"]+". Overall the climate is "+val["overall"]+" today."
    return speak_str
