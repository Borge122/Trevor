from subroutines import *
import time
import magichue
import numpy as np
import spotipy
light = magichue.Light("192.168.1.47")

print(latest_messages())

while True:
    command = latest_messages()
    time.sleep(0.1)
    print(command)
    if not command == []:
        if "party time" in " ".join(command) or "party mode" in " ".join(command):
            say("Initiating party mode squire.")
            light.mode = magichue.RAINBOW_CROSSFADE
        elif "epilepsy mode" in " ".join(command):
            say("Initiating epilepsy mode squire.")
            light.mode = magichue.WHITE_STROBE
        elif "chill vibes" in  " ".join(command):
            say("Initiating chill vibes squire.")
            n = 0
            while True:
                light.rgb = percentblend([107, 15, 204], [229, 0, 134], np.sin(n))
                time.sleep(0.1)
                n += 0.05
                n = n % (2 * 3.1415)

        elif "say" in command[0]:
            say(command[0][command[0].find("say"):])
        elif "repeat" in command[0]:  ##Cause it mistakes say as play
            print(command[0].find("repeat"))
            say(command[0][command[0].find("repeat"):])
        elif "synchronise beat protocol" in " ".join(command):
            print("synchronise hues and stuff to spotify using API")
