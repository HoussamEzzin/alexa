import pyttsx3
import speech_recognition as sr 
import wikipedia
import webbrowser
import pywhatkit
import pyjokes



engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

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

if __name__ == "__main__":
    while True:
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            speak('Searching Wikipedia')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)    
        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")
        elif 'open google' in query:
            webbrowser.open("https://www.google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("https://www.stackoverflow.com")    
        elif 'alexa' in query:
            speak('Hi user how are you ?')
        elif 'play' in query:
            song = query.replace('play','')
            speak('Playing '+song)
            pywhatkit.playonyt(song)
        elif 'joke' in query:
            speak(pyjokes.get_joke())
            
