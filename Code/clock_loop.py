from Classes.clock import Clock

import time 
def ClockLoop(lock,cocosPipe):
    clock = Clock()
    while True:
        time.sleep(1)
        clock.Tick()
        if cocosPipe:
            cocosPipe.send(['Second Passed'])
        