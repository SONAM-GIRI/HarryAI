import webbrowser

import  speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
from django.db.models.expressions import result
from django.utils.lorem_ipsum import sentence


def take_command():
    """Listen to and recognize the user's voice command."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 300
        try:
            audio = r.listen(source, timeout=7)
        except sr.WaitTimeoutError:
            print("No voice detected within the timeout period.")
            return "None"

    try:
        print("Understanding...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
    except sr.UnknownValueError:
        print("Sorry, I didn't catch that. Please repeat.")
        return "None"
    except sr.RequestError:
        print("Could not request results; check your internet connection.")
        return "None"
    return query.lower()

query = take_command().lower()
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)  # Set voice
engine.setProperty("rate", 170)  # Set speaking rate

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def searchGoogle(query):
    if "google" in query:
        import wikipedia as googleScrap
        query = query.replace("Harry","")
        query = query.replace("Googlesearch","")
        query =query.replace("google","")
        speak("This is what i found on google")

        try:
            pywhatkit.search(query)
            result=googleScrap.summary(query,3)
            speak(result)
        except:
            speak("No speakable output avaiable")

def searchYoutube(query):
    if "Youtube" in query:
        speak("This is what I found for your search")
        query=query.replace("youtube","")
        query=query.replace("Youtube search","")
        query=query.replace("harry","")

        web="https://www.youtube.com/results?search_query=" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        speak("Done,Honey")

def searchWikipedia(query):
    if "wikipedia" in query:
        speak("Searching from wikipedia....")
        query=query.replace("search Wikipedia","")
        query=query.replace("Harry","")
        query=query.replace("wikipedia","")
        results=wikipedia.summary(query,sentence=3)
        speak("According to Wikipedia...")
        print(results)
        speak(results)

