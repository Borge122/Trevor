from subroutines import *
light = magichue.Light('192.168.1.47')
latestMessages()

while True:
    command = latestMessages()
    print(command)