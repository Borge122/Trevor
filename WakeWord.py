from subroutines import *
import magichue

light = magichue.Light('192.168.1.47')
light.rgb = [0, 0, 0]

while True:
    text = get_audio()
    print(text)
    if "hey trevor" in " : ".join(text) or "hey trouble" in " : ".join(text) or "stupid c***" in " : ".join(text):
        light.rgb = [100, 255, 255]
        multi_say(["Yes sir?", "How can I help squire?", "at your service squire", "Anything I can help you with squire", "Ready to help squire"])
        light.rgb = [0, 0, 0]