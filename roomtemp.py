import json, requests
import schedule
import jarvis
url_room = requests.get("http://192.168.1.168/enviro.json")
url_outside = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=37.48&lon=-86.29&appid=472bd080e8719f66f75bf94fe4954e0f")
url_therm = requests.get("http://192.168.1.168/dataset.json")
def room_t():
    url_room = requests.get("http://192.168.1.168/enviro.json")
    text = url_room.text
    data = json.loads(text)
    fd = data['fd']
    return int(fd)

def roomh():
    text = url_room.text
    data = json.loads(text)
    h = float(data['h'])
    return int(h)


def alarm(set_time):
    print(set_time)
    return set_time


def outside_temp():
    
    text = url_outside.text
    data = json.loads(text)
    temp_raw = data['main']['temp']
    tempature = (int(temp_raw)-273.15)*1.8+32
    return int(tempature)

def outside_temp_max():
    
    text = url_outside.text
    data = json.loads(text)
    temp_raw = data['main']['temp_max']
    tempature = (int(temp_raw)-273.15)*1.8+32
    return int(tempature)

def outside_temp_min():
    
    text = url_outside.text
    data = json.loads(text)
    temp_raw = data['main']['temp_min']
    tempature = (int(temp_raw)-273.15)*1.8+32
    return int(tempature)

def checkt():
    url_therm = requests.get("http://192.168.1.168/dataset.json")
    text = url_therm.text
    data = json.loads(text)
    room_temp = room_t()
    upper_temp = data['upper_temp']
    lower_temp = data['lower_temp']
    if room_temp > upper_temp or room_temp < lower_temp:
        jarvis.speak(room_temp)
    schedule.every(10).minutes.do(checkt)
    return lower_temp

def outside_temp():
    url_room = requests.get("http://192.168.1.168/enviro.json")
    text = url_outside.text
    data = json.loads(text)
    temp_raw = data['main']['temp']
    tempature = (int(temp_raw)-273.15)*1.8+32
    return int(tempature)