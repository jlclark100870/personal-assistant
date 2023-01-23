import requests
from jarvis import *
import datetime
from wemocontrol import *


p=0
greet_user()
if __name__ == '__main__':

    
    
    while p != 5:
        query = take_user_input().lower()
        query = switch(query)
        print (query)

        

       

        if 'good night' in query:
            speak(choice(opening_text))
            speak('Good night would you like me to set and alarm for you')
            query = take_user_input().lower()
            if 'no' in query:
                speak('ok sleep well')
            elif 'yes' in query:
                speak('what is the name of this event')
                eventname = take_user_input().lower()
                speak('when is the event')
                eventtime = take_user_input().lower()
                
                speak('i set an alarm for ')
                speak(eventname)
                speak('at')
                speak(eventtime)
                speak('sleep well')
            else:
                speak('I did not understand your answer')
                speak('ok sleep well')
        
        elif 'turn off computer light' in query:
            speak(choice(opening_text))
            latte(0,'latte')
        elif 'turn on computer light' in query:
            speak(choice(opening_text))
            latte(1,'latte')

        elif 'turn off porch light' in query:
            speak(choice(opening_text))
            latte(0,'porch')
        elif 'turn on porch light' in query:
            speak(choice(opening_text))
            latte(1,'porch')

        elif 'turn off living room light' in query:
            speak(choice(opening_text))
            latte(0,'living room over head light')
            
        elif 'turn on living room light' in query:
            speak(choice(opening_text))
            latte(1,'living room over head light')
       
