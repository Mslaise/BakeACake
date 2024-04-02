from Classes.clock import Clock

import time 
def ClockLoop(lock,cocosPipe):
    clock = Clock(cocosPipe)
    while True:
        time.sleep(1)
        clock.Tick()
        graphicsData = clock.RelayGfiPackages()
        if cocosPipe:
            cocosPipe.send(['Second Passed',graphicsData])
        