import requests
from pprint import pprint
from jarvis import *
import time
import pyttsx3
from decouple import config
import speech_recognition as sr
import main

def call_name(): 
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        if not 'Jarvis' in query:
            print(query)
            
    except Exception:
        query = 'listhold main'

    return query


def listen():
    
    query = call_name()

    if 'Jarvis' in query:
       print(greet_user())
       main.taskd()
            #speak(greet_user())
    else:
        listen()
listen()
