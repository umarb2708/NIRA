import requests, json
import import_file as f
url = 'https://api.openweathermap.org/data/2.5/weather?q=thrissur&appid=753b203a4081430106aa585083e7523f'#Open api link here
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
def weather_info(cmd):
    val=get_weather_info()
    weather=val["temp"]+" degree temperature and "+val["humidity"]+" percent humidity at "+val["city"]+". Overall the climate is "+val["overall"]+" today."
    f.out.txt_out(weather,'111')
    f.db.insert_cmd_executed("weather","1")#insert init done to DB
    return 1
