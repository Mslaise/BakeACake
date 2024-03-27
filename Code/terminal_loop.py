from Globals.resources import act_handle
from Globals.game_info import *

    
def TerminalLoop(lock,cocosPipe=None,clockPipe=None):
    #Input loop   
    USER_INPUT = input("> ")
    
    if lock.acquire(False):
        lock.release()
    
    if cocosPipe:
        act_handle.cocosPipe = cocosPipe

    act_handle.ResolveAction(USER_INPUT,lock)
                                                          #Lock 2    
    if lock.acquire(False):
        lock.release()                                    #Release 2
        
    
    

    
    
