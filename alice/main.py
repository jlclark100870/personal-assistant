from speakpy import *
import switchcase as switchcase
from routines import *
from datetime import datetime
from curl_test import *
import random
greetings=[
    "hi",
    "hello",
    "what's up",
]
user = "human"
ai = "alice"

speak("hello my name is alice, I am your personal assistant, you can ask me any thing, I will help you if I can, I am stall learning so please be patient.")
speak("hello what is your name")
query1 = take_user_input().lower()
query = switchcase.switch_name(query1)
user = query
print(user)
speak(f"hello {user} nice to meet you I will remeber your name")

    

def qa_algra():
    speak(f"how may i assist you {user}")
    query1 = take_user_input().lower()
    query = switchcase.switch(query1)
    print (query1)
    print (query)
    if query == "none":
        ollama_fun(query1)
    elif query in greetings:
        random_response = random.choice(greetings)
        speak(random_response)
    elif query == "thank you":
        speak(f"You are welcome {user}")    
    elif query == "what is my name":
        speak(f"Your name is{user}")
    elif query == "what is your name":
        speak(f"my name is{ai}")
    elif query == "time":
        speak(get_time())
    else:
        ollama_fun(query1)

while True:
    query1 = take_user_input().lower()
    query = switchcase.switch_name(query1)
    if query == "hey alice":
        qa_algra()