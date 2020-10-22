import pyttsx3
import datetime
import speech_recognition as sr
import random
import magichue

light = magichue.Light('192.168.1.47')
light.rgb = [0, 0, 0]

engine = pyttsx3.init()
engine.setProperty('rate', 120)
engine.setProperty('voice', engine.getProperty('voices')[2].id)
previousRequest = ""


def latest_messages():
    newRequest = open("Requests.txt", "r").read()
    global previousRequest
    if newRequest != previousRequest:
        newText = newRequest.replace(previousRequest, "")
        previousRequest = newRequest
        return newText.split(" -:- ")[1].replace("[", "").replace("]", "").replace("\"", "").replace("\'", "").replace("\n", "").split(",")
    return []


def requests(text):
    with open("Requests.txt", "a") as file:
        file.write(f"{datetime.datetime.now().strftime('%Y:%b:%D-%H:%M:%S')} -:- {text}\n")
    return None


def response(text):
    with open("Responses.txt", "a") as file:
        file.write(f"{datetime.datetime.now().strftime('%Y:%b:%d-%H:%M:%S')} -:- {text}\n")
    return None


def say(text):
    set_light(100, 255, 255)
    engine.say(text)
    engine.runAndWait()
    response(text)
    set_light(0, 0, 0)
    return None


def multi_say(list_of_text):
    return say(list_of_text[random.randint(0, len(list_of_text)-1)])

    
def get_audio(log=True, lights=True):
    r = sr.Recognizer()
    if lights:
        set_light(0, 255, 0)
    with sr.Microphone() as source:
        print("Listening...", end="")
        audio = r.listen(source)
        text = ""
        print("Done!")
        try:
            text = list([i["transcript"].lower() for i in r.recognize_google(audio, language="en-UK", show_all=True)["alternative"]])
        except Exception as e:
            print("Exception: " + str(e) + str(r.recognize_google(audio, language="en-UK", show_all=True)))

    if log:
        requests(text)
    if lights:
        set_light(0, 0, 0)
    return text


def set_light(r,g,b):
    light.rgb = [r,g,b]


def refreshLightConnection():
    global light
    light = magichue.Light('192.168.1.47')
