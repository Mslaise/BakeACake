from G_GameInfo import *
from G_Resources import *

from _gfi import MainGfi

import F_PrintDumps
from F_ThreadingProcesses import MainLoop
from F_ThreadingProcesses import TerminalLoop
from F_InitCocos import InitCocos





if __name__ == "__main__":
    act_handle.ACT_Clear() #clear the screen
                
    #Intro
    F_PrintDumps.Intro()

    #This will execute as long as cocos has not been initialized
    while act_handle.Go and act_handle.Gfi == False:
        TerminalLoop()
        
    #Once cocos has been initialized
    if act_handle.Go:
        InitCocos()
