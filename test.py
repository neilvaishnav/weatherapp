import requests
import json
import win32com.client as wincom

import time

speak = wincom.Dispatch("SAPI.SpVoice")

text = "Hello! I am your robo speaker. Please enter what you want to know!"
speak.Speak(text)



city = input("Enter the name of the city:\n")
url = f"http://api.weatherapi.com/v1/current.json?key=a25da6dbd3f9466593c132115232803&q={city}"

r = requests.get(url)
# print(r.text)

# To convert to string to dictionary
wdic = json.loads(r.text)

# Enter particular things to know
w = wdic["current"]["temp_c"]


text = f"you are entered city name is  {city} and current temperature is {w}"
speak.Speak(text)
print("Current temp is ",w)