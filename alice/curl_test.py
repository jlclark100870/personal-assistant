import requests
import json
from speakpy import *
from ollama import Client
def ollama_fun(query):

    url = "http://192.168.68.72:11434/api/generate"
    payload = {"model": "rejekts/pug", "system":'respond with text only so it can be read by a speech synthesizer.',"prompt": query}
    response = requests.post(url, json=payload, stream=True)
    think = ""
    respond = ""
    for line in response.iter_lines():
        data_dict = json.loads(line)
        #print(data_dict)
        for key in data_dict:
            item = key
            if 'thinking' in item:
                val = data_dict["thinking"]
                think = think + " " + val
                print(think)
            if 'response' in item:
                val1 = data_dict["response"]
                respond +=" " + val1
    print(respond)
    speak(think)  
    speak(respond)
#print(data_dict["thinking"])
    # if line:
    #     print(line.decode("utf-8"))
def main():
    ollama_fun("explain special relativity")
if __name__ == "__main__":
    # Call the main function
    main()