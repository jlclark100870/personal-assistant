import speaktime
import roomtemp
from jarvis import *
import wemocontrol
import switchcase
import schedule
import datetime

speak('Hello I am the office A I here to improve your life')


roomtemp.checkt()


while True:
    
    schedule.run_pending()
    
    query = take_user_input().lower()
    query = switchcase.switch(query)
    print (query)

    

    if 'turn off computer light' in query:
        speak(choice(opening_text))
        wemocontrol.latte(0,'latte')
    elif 'turn on computer light' in query:
        speak(choice(opening_text))
        wemocontrol.latte(1,'latte')

    elif 'turn off porch light' in query:
        speak(choice(opening_text))
        wemocontrol.latte(0,'porch')
    elif 'turn on porch light' in query:
        speak(choice(opening_text))
        wemocontrol.latte(1,'porch')

    elif 'turn off living room light' in query:
        speak(choice(opening_text))
        wemocontrol.latte(0,'living room over head light')
            
    elif 'turn on living room light' in query:
        speak(choice(opening_text))
        wemocontrol.latte(1,'living room over head light')

    elif 'room temperature' in query:
        speak(choice(opening_text))
        speak("current tempature in the office is")
        speak(roomtemp.room_t())
        speak('degrees Fahrenheit ')

    elif 'outside temperature' in query:
        speak(choice(opening_text))
        speak("current tempature outside is")
        speak(roomtemp.outside_temp())
        speak('Fahrenheit ')

    elif 'time' in query:
        speak(choice(opening_text))
        now = datetime.datetime.now()
        date_string = now.strftime('%H:%M')
        speak('the current time is')
        speak(date_string)

    elif 'date' in query:
        speak(choice(opening_text))
        now = datetime.datetime.now()
        date_string = now.strftime('%m-%d-%Y')
        speak('the current date is')
        speak(date_string)

    roomtemp.checkt()
    speaktime.alarm()
    print('active')