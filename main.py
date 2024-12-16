import datetime

import pyttsx3
import requests
import speech_recognition as sr
import pyaudio
import bs4
from bs4 import BeautifulSoup


# Initialize Text-to-Speech Engine
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)  # Set voice
engine.setProperty("rate", 170)  # Set speaking rate

def speak(audio):
    """Speak out the given text."""
    engine.say(audio)
    engine.runAndWait()

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

if __name__ == '__main__':
    while True:
        query = take_command()
        if "wake up" in query:
            try:
                from GreetMe import greetMe  # Ensure GreetMe module exists
                greetMe()
            except ImportError:
                speak("GreetMe module not found.")
                break
            while True:
                query = take_command()
                if "go to sleep" in query:
                    speak("Okay, you can call me anytime!")
                    break
                elif "hello" in query:
                    speak("hello honey, how are you")
                elif "I am fine" in query:
                    speak("That's great honey")
                elif "how are you" in query:
                    speak("I am perfect")
                elif "Thank you" in query:
                    speak("Welcome ,honey")
                elif "open" in query:

                elif "google" in query:
                    from searchnow import searchGoogle
                    searchGoogle(query)
                elif "youtube" in query:
                    from searchnow import searchYoutube
                    searchYoutube(query)
                elif "wikipedia" in query:
                    from  searchnow import searchWikipedia
                    searchWikipedia(query)
                elif "temperature" in query:
                    search="temperature in delhi"
                    url=f"https://www.google.com/search?q={search}"
                    r=requests.get(url)
                    data=BeautifulSoup(r.text,"html.parser")
                    temp=data.find("div",class_ ="BNeawe").text
                    speak(f"current{search} is {temp}")
                elif "weather" in query:
                    search = "weather in delhi"
                    url = f"https://www.google.com/search?q={search}"
                    r = requests.get(url)
                    data = BeautifulSoup(r.text, "html.parser")
                    temp = data.find("div", class_="BNeawe").text
                    speak(f"current{search} is {temp}")
                elif "the time" in query:
                    strTime=datetime.datetime.now().strftime("%H:%M")
                    speak(f"Honey,the time is{strTime}")

                elif "see you later" in query:
                    speak("Goodbye!")
                    exit()
