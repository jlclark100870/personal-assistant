import pyttsx4
from datetime import datetime
import speech_recognition as sr
from random import choice



# Initialize the text-to-speech engine
engine = pyttsx4.init('sapi5')



# Optional: Adjust properties (rate, volume, voice)
# You can adjust the speaking rate (words per minute)
engine.setProperty('rate', 150) 

# You can adjust the volume (0.0 to 1.0)
engine.setProperty('volume', 0.9)

# To see available voices:
voices = engine.getProperty('voices')
# Change voice (e.g., to the second voice in the list, often a female voice)
# Note: voice indices/IDs vary by system
engine.setProperty('voice', voices[2].id) 


def speak(text):
    """Used to speak whatever text is passed to it"""
    
    engine.say(text)
    engine.runAndWait()

def take_user_input():
    """Takes user input, recognizes it using Speech Recognition module and converts it into text"""

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        speak('Listening....')
        
        r.pause_threshold = 1.2
       
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-us')
        if not 'exit' in query or 'stop' in query:
            pass
            
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Good night sir, take care!")
            else:
                speak('Have a good day sir!')
            exit()
    except Exception:
        #speak('Sorry, I could not understand. Could you please say that again?')
        query = 'none'
    return query

