from subroutines import *
import magichue
import time
light = magichue.Light('192.168.1.47')
light.rgb = [0, 0, 0]

while True:
    text = get_audio(log=False, lights=False)
    print(text)
    if "hey trevor" in " : ".join(text) or "hey trouble" in " : ".join(text) or "stupid c***" in " : ".join(text) or "play trevor" in " : ".join(text):
        multi_say(["Yes sir?", "How can I help squire?", "at your service squire", "Anything I can help you with squire", "Ready to help squire"])
        text = get_audio()
        print(text)