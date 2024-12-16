import os
import pyautogui
import webbrowser
import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)  # Set voice
engine.setProperty("rate", 170)  # Set speaking rate

def speak(audio):
    """Speak out the given text."""
    engine.say(audio)
    engine.runAndWait()