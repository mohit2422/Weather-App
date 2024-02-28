import requests
import json
import win32com.client as win
speaker = win.Dispatch("SAPI.SpVoice")

city = input("Enter the name of the city\n")

url = f"https://api.weatherapi.com/v1/current.json?key=f230ec8f8fc241dd9ad145725232512&q={city}"

r = requests.get(url)
print(r.text)
weatherDic = json.loads(r.text)
w = weatherDic["current"]["temp_c"]
s = f"The current weather in {city} is {w} degrees"
speaker.Speak(s)

