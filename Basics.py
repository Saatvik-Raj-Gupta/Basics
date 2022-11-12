import pyttsx3
import datetime
import playsound
from datetime import date
import speech_recognition as sr
import subprocess
import webbrowser
from pydictionary import Dictionary as dictionary
#spech
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
#audio
def audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = r.recognize_google(audio)
        print(said)
        return said.lower()
#greeting
def wishme():
    t=int(datetime.datetime.now().hour)
    if t>=0 and t<12:
        speak("Good Morning")
    elif t>=12 and t<16:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
#date_time
def date_time():
    today = date.today()
    t=(datetime.datetime.now())
    speak("Today's date:", today,"Time is",t)
#note making
def take_note(text):
    date=datetime.datetime.now()
    file_name=str((date).replace(":", "-") + "-note.exe")
    with open(file_name, "w") as f:
        f.write(text)
    subprocess.Popen(["notepad.exe", file_name])
#speak("Hello")
#wishme()
#audio()
def main(x): 
    if "take note" in x:
        speak("what would you like me to note")
        text=audio()
        take_note(text)
    elif "youtube" in x:
        webbrowser.open("youtube.com")
    elif "google" in x:
        webbrowser.open("google.com")
    elif "search" in x:
        speak("what do you want me to search")
        query=audio()
        
    elif "open" in x:
        speak("which app")
        app=audio()
        open(app)
    elif "meaning" in x:
        speak("please say  the word to find meaning of")
        word=audio()
        speak(dictionary.meaning(word))
    elif "synonyms" in x:
        speak("please say the word")
        wo=audio()
        speak(dictionary.synonym(wo))
    elif "antonyms" in x:
        speak("please say the word")
        an=audio()
        speak(dictionary.antonym(an))
    elif "translate" in x:
        speak("please say the word")
        word=audio()
        speak("language to be translated in")
        lang=audio()
        speak(dictionary.translate(word,lang))
wishme()
x=audio()        
main(x)
