from pydoc import text
import requests

def Speak(string):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(string)

url = "https://newsapi.org/v2/top-headlines?country=us&apiKey=b040e749dd8242028e8612b84d6715c5"
r = requests.get(url)
TotalHeadlines = r.json()["totalResults"]
CurrentHeadline = 1
print(f"Total Headlines are : {TotalHeadlines}")
while(CurrentHeadline <= TotalHeadlines):
    articles = r.json()["articles"][CurrentHeadline]["description"]
    print(f"HeadLine Number: {CurrentHeadline}\n>>> {articles}")
    Speak(f"Head Line Number {CurrentHeadline}: {articles}")
    CurrentHeadline +=1