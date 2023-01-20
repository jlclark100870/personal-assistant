import json, requests
url_room = requests.get("http://192.168.1.181/enviro.json")
url_outside = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=37.48&lon=-86.29&appid=472bd080e8719f66f75bf94fe4954e0f")

def room_temp():
    
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
