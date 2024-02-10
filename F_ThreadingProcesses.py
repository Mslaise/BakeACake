from G_Resources import act_handle
import time
import _clock
from G_Resources import clock

def MainLoop():
    #Wait for the main thread to finish its work before you call this
    #time.sleep(0.05)
    while act_handle.Go:
        TerminalLoop()
    
def TerminalLoop():
    #Input loop
    fullInput = input("> ")
    print()
    act_handle.ResolveAction(fullInput)
    print()
    clock.Tick()