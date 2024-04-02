from Classes.player import Player
import time

#Activates game events and contains all game elements
#BWA WA WA WA WAW AWAWAAWAWAWAWAWAWAW WAWAWAWAAWAWAW WA   WA  WA  WA  AW  WAWAWAWAWAWAW
class Clock:
    def __init__(self,cocosPipe):
        self.cocos_pipe = cocosPipe
        self.player = Player(cocosPipe)
        self.day = 0
        self.hour = 0
        self.minute = 0
        self.second = 0
 
    #Add what happens every day
    def CycleDay(self):
        self.player.CycleDay()
        
    #Add what happens every hour
    def CycleHour(self):
        self.player.CycleHour()

    #Add what happens every minute
    def CycleMinute(self):
        self.player.CycleMinute()
        
    #Add what happens every second
    def CycleSecond(self):
        self.player.CycleSecond()

    #the cycle arg in the following jump functions are there if you want to choose whether the passing
    #time effects other game elements.
    def JumpDay(self,cycle=True):
        self.day += 1
        if cycle:
            self.player.CycleDay()

    def JumpHour(self,cycle=True):
        self.hour += 1
        if cycle:
            self.player.CycleHour()
        if self.hour == 24:
            self.hour = 0
            self.day += 1

    def JumpMinute(self,cycle=True):
        self.minute += 1
        if cycle:
            self.player.CycleMinute()
        if self.minute == 60:
            self.minute = 0
            self.JumpHour()

    def JumpSecond(self,cycle=True):
        self.second += 1
        if cycle:
            self.player.CycleSecond()
        if self.second == 60:
            self.second = 0
            self.JumpMinute()

    def Tick(self):
        self.JumpSecond()
        
    def RelayGfiPackages(self):
        playerData = self.player.RelayGfiPackages()
        return playerData
    
    def SetDay(self):
        pass
    def SetHour(self):
        pass
    def SetMinute(self):
        pass
    def SetSecond(self):
        pass
        
        
        


    