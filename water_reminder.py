import time
import pyttsx3

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    
while True:
    speak("Reminder! Please drink some water and stay hydrated.")
    print("Reminder given")
    time.sleep(3600)