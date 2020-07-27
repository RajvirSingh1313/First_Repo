import requests
import json
import time
from win32com.client import Dispatch

def speak(s):
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(s)

data = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=49e391e7066c4158937096fb5e55fb5d")

result = data.json()
print(result['status'])
# print(result)

india=data.json()

news = result['articles']

speak("Here are the top ten news of the India")
speak("So our first news is ")
for i  in range(0,10):
    print(i)
    print(news[i]['description'])
    print("for more ",india['articles'][i]['url'])
    speak(news[i]['description'])
    if i>=9:
        break
    time.sleep(1)
    if i == 8:
        speak("So our last news for today is ")
    else:
        speak("Moving To Our next news")


speak("Thanks for listening ! Have a nice day")
speak("Keep coding")
