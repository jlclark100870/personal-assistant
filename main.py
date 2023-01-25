import speaktime
import roomtemp
from jarvis import *
import wemocontrol
import switchcase
import schedule
import datetime
import wolframalpha
import wikipedia

speak('Hello I am the office A I here to improve your life')


roomtemp.checkt()


while True:
    
    
    
    query1 = take_user_input().lower()
    query = switchcase.switch(query1)
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
        a,b=roomtemp.outside_temp()
        speak("current tempature outside is")
        speak(b)
        speak('Fahrenheit ')
        speak('as of')
        speak(a)

    elif 'time' in query:
        strTime=datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"the time is {strTime}")

    elif 'date' in query:
        speak(choice(opening_text))
        now = datetime.datetime.now()
        date_string = now.strftime('%m-%d-%Y')
        speak('the current date is')
        speak(date_string)

    elif 'ask a question' in query:
        speak('I can answer to computational and geographical questions and what question do you want to ask now')
        question=take_user_input().lower()
        app_id="R2K75H-7ELALHR35X"
        client = wolframalpha.Client('R2K75H-7ELALHR35X')
        try:
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)
        except:
            speak('I was unable to find any information for '+question)

    elif 'wikipedia' in query:
        speak('what would you like me to search for...')
        question=take_user_input().lower()
        try:
            results = wikipedia.summary(question, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        except:
            speak('I was unable to find any information for '+question+'on wikipedia')
    elif 'who are you' in query or 'what is your name' in query:
        speak('I am a computerized personal assistant capable of answering questions and simple household task ... my name is shiela and I am glad you asked')

    elif 'commands' in query:
        speak('turn on computer light....turn off computer light....turn on porch light....wikipedia....ask a question.... are just some of the things I will respond to the list is growing every day feel free to ask me anything I will answer if I know how')

   

    roomtemp.checkt()
    speaktime.alarm()
    print('active')
