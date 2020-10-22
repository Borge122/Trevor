import pyttsx3
import datetime
import speech_recognition as sr
import random

engine = pyttsx3.init()
engine.setProperty('rate', 120)
engine.setProperty('voice', engine.getProperty('voices')[2].id)


def requests(text):
    with open("Requests.txt", "a") as file:
        file.write(f"{datetime.datetime.now().strftime('%Y:%b:%D-%H:%M:%S')} -:- {text}\n")
    return None


def response(text):
    with open("Responses.txt", "a") as file:
        file.write(f"{datetime.datetime.now().strftime('%Y:%b:%d-%H:%M:%S')} -:- {text}\n")
    return None


def say(text):
    engine.say(text)
    engine.runAndWait()
    response(text)
    return None


def multi_say(list_of_text):
    return say(list_of_text[random.randint(0, len(list_of_text)-1)])

    
def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...", end="")
        audio = r.listen(source)
        text = ""
        print("Done!")
        try:
            text = list([i["transcript"].lower() for i in r.recognize_google(audio, language="en-UK", show_all=True)["alternative"]])
        except Exception as e:
            print("Exception: " + str(e) + str(r.recognize_google(audio, language="en-UK", show_all=True)))
    requests(text)
    return text