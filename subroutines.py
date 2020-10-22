import pyttsx3
import datetime
engine = pyttsx3.init()


def requests(text):
    with open("Requests.txt", "a") as file:
        file.write(f"{datetime.datetime.now().strftime('%Y:%b:%D-%H:%M:%S')} -:- {text}\n")
    return None


def response(text):
    with open("Responses.txt", "a") as file:
        file.write(f"{datetime.datetime.now().strftime('%Y:%b:%d-%H:%M:%S')} -:- {text}\n")
    return None

requests("Tests")
def say(text):
    engine.say(text)
    engine.runAndWait()
