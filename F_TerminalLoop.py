from G_Resources import act_handle
from G_Resources import clock
from G_GameInfo import *

    
def TerminalLoop(lock,pipe=None):
    #Input loop   
    USER_INPUT = input("> ")
    print()
    
    if lock.acquire(False):
        lock.release()
    
    if pipe:
        act_handle.pipe = pipe
        
    act_handle.ResolveAction(USER_INPUT,lock)
                                                          #Lock 2
    print()
    
    if lock.acquire(False):
        lock.release()                                    #Release 2
        
    clock.Tick()
    
    

    
    
