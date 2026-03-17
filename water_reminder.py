import time
import pyttsx3


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

minutes = float(input("Kitne minutes ke baad reminder chahiye? : "))

seconds = minutes * 60

while True:
    speak("Reminder! Please drink some water and stay hydrated.")
    print("Reminder given")
    time.sleep(seconds)
