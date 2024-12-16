import pyttsx3
import datetime
import speech_recognition
from wikipedia import languages

engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty("voice",voices[0].id)
engine.setProperty("rate",170)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning ,Honey")
    elif hour>12 and hour<=18:
        speak("Good Afternoon , Honey")
    else:
        speak("Good Evening,Honey")

    speak("Please tell me, How can i help you?")
