# Project name - JARVIS


# Modules
import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclib


# Initialize the recognizer
r = sr.Recognizer()
engine = pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()

def process_command(c):
        if "youtube" in c.lower():
            webbrowser.open("https://youtube.com")
            speak("Opening YouTube boss")

        elif "google" in c.lower():
            webbrowser.open("https://google.com")
            speak("Opening Google boss")

        elif "github" in c.lower():
            webbrowser.open("https://github.com")
            speak("Opening GitHub boss")
        elif c.lower().startswith("play"):
             song = " ".join(c.lower().split(" ")[1:])
             link = musiclib.music[song]
             webbrowser.open(link)
        elif "news" in c.lower():
             webbrowser.open("https://www.ndtv.com/")
             speak("opening the latest news, boss")
             
 
if __name__ == "__main__":
    r = sr.Recognizer()
    speak("jarvis Initializing")
while True:
    try:
    # listen for the wake word "Jarvis"
        with sr.Microphone() as source:
               print("listening...")
               audio = r.listen(source, timeout=5, phrase_time_limit=4)
        word = r.recognize_google(audio)
        if (word.lower() == "jarvis"):
            speak("Yes boss")
            # listen for c
            with sr.Microphone() as source:
                audio = r.listen(source, timeout=5, phrase_time_limit=4)
                c = r.recognize_google(audio)
                process_command(c)
    except Exception as e:
        print("Somthing went wrong!")
