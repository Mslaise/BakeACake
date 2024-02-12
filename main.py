from G_GameInfo import *
from G_Resources import *

from _gfi import MainGfi

import F_PrintDumps
from F_TerminalLoop import TerminalLoop
from F_InitCocos import InitCocos

from multiprocessing import Process, Lock, Pipe




if __name__ == "__main__":
    act_handle.ACT_Clear() #clear the screen
                
    #Intro
    F_PrintDumps.Intro()
    #This will execute as long as cocos has not been initialized    
   
    #Setting up communication between the terminal and cocos threads
    lock = Lock()
    act_handle.Lock = lock
    cocosIn, cocosOut = Pipe()
    
    #Actual creation of he cocos thread
    cocosProcess = Process(target=InitCocos,args=(lock,cocosOut))
    
    lock.acquire()
    while act_handle.Go and not act_handle.Gfi:
        #there's probably a better way to handle this but honestly idgaf right now
        TerminalLoop(lock, cocosIn)
        
    cocosProcess.start()
    
    while act_handle.Go:
        TerminalLoop(lock)
        
    cocosProcess.kill()
    
    
    
        
        
