import json, requests
from jarvis import *
from time import sleep
import datetime

def time_break():
    now = datetime.datetime.now()
    global date_string 
    date_string = now.strftime('%H:%M:%S')
    global hour_string
    hour_string = now.strftime('%H')
    global minute_string
    minute_string = now.strftime('%M')
    global second_string
    second_string = now.strftime('%S')

def spktime():
    
    now = datetime.datetime.now()
    date_string = now.strftime('%H:%M:%S')
    speak('the current time is')
    speak(date_string)
    return date_string


def alarm():
    time_break()
    curhour = int(hour_string)
    curminute = int(minute_string)
    cursecond = int(second_string)
    url_time = requests.get("http://192.168.1.168/dataset.json")
    text = url_time.text
    data = json.loads(text)
    text = data['alarm'].split(':')
    alarm_state = data['alarm_state']
    if alarm_state == "yes":

        if curhour >= int(text[0]) and curminute > int(text[1]) and cursecond > 0 and curhour < 18:
   
            print(spktime())
            print('all done')
    

    