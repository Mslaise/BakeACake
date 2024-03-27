from Globals.game_info import *
from Globals.resources import *

from Classes.gfi import Gfi

import Code.print_dumps as print_dumps
from Code.terminal_loop import TerminalLoop
from Code.init_cocos import InitCocos
from Code.clock_loop import ClockLoop

from multiprocessing import Process, Lock, Pipe




if __name__ == "__main__":
    act_handle.ACT_Clear() #clear the screen
                
    #Intro
    print_dumps.Intro()
    #This will execute as long as cocos has not been initialized    
   
    #Setting up communication between the terminal and cocos threads
    lock = Lock()
    act_handle.Lock = lock
    cocosIn, cocosOut = Pipe()
    clockIn, clockOut = Pipe()
    
    #Actual creation of he cocos thread
    cocosProcess = Process(target=InitCocos,args=(lock,cocosOut))
    clockProcess = Process(target=ClockLoop,args=(lock,cocosIn))
    lock.acquire()
    
    clockProcess.start()
    while act_handle.Go and not act_handle.Gfi:
        #there's probably a better way to handle this but honestly idgaf right now
        TerminalLoop(lock, cocosIn)
        
    cocosProcess.start()
    
    while act_handle.Go:
        TerminalLoop(lock)
        
    cocosProcess.kill()
    
    
    
        
        
