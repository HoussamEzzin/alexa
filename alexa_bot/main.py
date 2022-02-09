import pyttsx3
import speech_recognition as sr 
import wikipedia
import webbrowser
import pywhatkit
import pyjokes
import os
from github import git_add_all, git_commit, git_push

'''
Initializing engine and voices.
'''
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


#function that make alexa speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    """
    takes micro input from the user
    returns string output
    """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing ...")
        query = r.recognize_google(audio, language='en-US')
       
        print(f"You said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query