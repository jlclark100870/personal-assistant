import requests
from functions.os_ops import open_calculator, open_camera, open_cmd, open_notepad, open_discord
#from pprint import pprint
from jarvis import *
import datetime
from roomtemp import *
from wemocontrol import *
from switchcase import switch


p=0
greet_user()
if __name__ == '__main__':

    
    
    while p != 5:
        query = take_user_input().lower()
        query = switch(query)
        print (query)

        

        if 'open notepad' in query:
            speak(choice(opening_text))
            open_notepad()



       # elif 'open discord' in query:
           # open_discord()

        elif 'open command prompt' in query or 'open cmd' in query:
            speak(choice(opening_text))
            open_cmd()

        elif 'open camera' in query:
            speak(choice(opening_text))
            open_camera()

        elif 'open calculator' in query:
            speak(choice(opening_text))
            open_calculator()

        
##        elif 'search on google' in query:
##            speak('What do you want to search on Google, sir?')
##            query = take_user_input().lower()
##            search_on_google(query)

##        elif "send an email" in query:
##            speak("On what email address do I send sir? Please enter in the console: ")
##            receiver_address = input("Enter email address: ")
##            speak("What should be the subject sir?")
##            subject = take_user_input().capitalize()
##            speak("What is the message sir?")
##            message = take_user_input().capitalize()
##            if send_email(receiver_address, subject, message):
##                speak("I've sent the email sir.")
##            else:
##                speak("Something went wrong while I was sending the mail. Please check the error logs sir.")
##
##        elif 'joke' in query:
##            speak(f"Hope you like this one sir")
##            joke = get_random_joke()
##            speak(joke)
##            speak("For your convenience, I am printing it on the screen sir.")
##            pprint(joke)
##
##        elif 'search on google' in query:
##            speak('What do you want to search on Google, sir?')
##            query = take_user_input().lower()
##            search_on_google(query)
##
##        elif "send whatsapp message" in query:
##            speak('On what number should I send the message sir? Please enter in the console: ')
##            number = input("Enter the number: ")
##            speak("What is the message sir?")
##            message = take_user_input().lower()
##            send_whatsapp_message(number, message)
##            speak("I've sent the message sir.")

##        elif 'news' in query:
##            speak(f"I'm reading out the latest news headlines, sir")
##            speak(get_latest_news())
##            speak("For your convenience, I am printing it on the screen sir.")
##            print(*get_latest_news(), sep='\n')
##
##        elif 'weather' in query:
##            ip_address = find_my_ip()
##            city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
##            speak(f"Getting weather report for your city {city}")
##            weather, temperature, feels_like = get_weather_report(city)
##            speak(f"The current temperature is {temperature}, but it feels like {feels_like}")
##            speak(f"Also, the weather report talks about {weather}")
##            speak("For your convenience, I am
##
##        elif "trending movies" in query:
##            speak(f"Some of the trending movies are: {get_trending_movies()}")
##            speak("For your convenience, I am printing it on the screen sir.")
##            print(*get_trending_movies(), sep='\n')
##
##        elif 'news' in query:
##            speak(f"I'm reading out the latest news headlines, sir")
##            speak(get_latest_news())
##            speak("For your convenience, I am printing it on the screen sir.")
##            print(*get_latest_news(), sep='\n')
##
##        elif 'weather' in query:
##
##            city = requests.get(f"https://ipapi.co/68.17.17.17/city/").text
##            speak(f"Getting weather report for your city {city}")
##            weather, temperature, feels_like = get_weather_report(city)
##            speak(f"The current temperature is {temperature}, but it feels like {feels_like}")
##            speak(f"Also, the weather report talks about {weather}")
##            speak("For your convenience, I am printing it on the screen sir.")
##            print(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")
##
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
 
        elif 'room temperature' in query:
            speak(choice(opening_text))
            speak("current tempature in the office is")
            speak(room_temp())
            speak('degrees Fahrenheit ')

        elif 'outside temperature' in query:
            speak(choice(opening_text))
            speak("current tempature outside is")
            speak(outside_temp())
            speak('Fahrenheit ')

        elif 'room humidity' in query:
            speak(choice(opening_text))
            speak("current humidity in the office is")
            speak(roomh())
            speak('percent')

        elif 'good morning' in query:
            speak(choice(opening_text))
            greet_user()

        elif 'good afternoon' in query:
            speak(choice(opening_text))
            greet_user()

        elif 'good night' in query:
            speak(choice(opening_text))
            speak('Good night would you like me to set and alarm for you')
            query = take_user_input().lower()
            if 'no' in query:
                speak('ok sleep well')
            elif 'yes' in query:
                speak('what time would you like me to set it for')
                query = take_user_input().lower()
                respond = alarm(query)
                speak('i set an alarm for ')
                speak(respond)
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
       
