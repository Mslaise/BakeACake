import random
import math
import _item
"""You start the game on between 4 and 10 medications. Each medication has a random dosage
(pill amount), and is either taken in the morning, evening, or both. Medications will have
random side effects that occur for a random duration at a random interval after you take
the pill. Medications can have overlapping side effects"""


#H = 0  (represents time, in hours, since hour 0)
#Dc = 0 (arbitrary value from 1 to 15.
#Db = random number between 1 and 23.

#When H = 0, Dc = 0.
#When H = Db, Dc = D. 
#When H = 24, Dc = 0. 

#While H < Db, H should increase by Ra every cycle.
#While H > Db, H should decrease by Rb every cycle.

#Ra and Rb should only be set once, when they have the minimum required information to be calculated.

#Given this information, could you write this python function?
#Cycle() - Moves time forward by 1 hour.
 




class Medication:
    def __init__(self):
        #Medications are procedurally generated upon instantiation.

        self.refresh_ = False
        self.refresh_amount_ = 0

        self.name = ""
        self.item = _item.Item()

        #When this is 0, mood penalty is 0.
        self.ideal_dose = random.randint(1,24)

        #Amount in mg of medication in each pill
        self.dose = self.ideal_dose * 2
        
        #Amount of the medication in your system
        self.active_dose = 0

        

        self.mood_multiplier_ = 0

        self.max_mood_reduction_ = random.randint(1,15)

        self.hours_since_taken_ = 0

        self.SetHoursToAbsorb()





    def SetName(self,name):
        self.name = name
        self.item.SetName(name)
 
    def Absorb(self):
        self.active_dose += self.absorb
        self.SetMoodMultiplier()

    def Decay(self):
        if self.active_dose - self.decay > 0:
            self.active_dose -= self.decay
        else:
            self.active_dose = 0
        self.SetMoodMultiplier()

    def Cycle(self):
        #Advances or recedes the effects of medication depending on how long ago you took it.
        if self.hours_since_taken_ >= self.hours_to_absorb_:
            #Medication has been fully absorbed, the effects are wearing off.
            self.hours_since_taken_ += 1
            self.Decay()
        else:
            #Medication has yet to be fully absorbed, advance the effects.
            self.hours_since_taken_ += 1
            self.Absorb()

    #Should only be called when the player takes the given medication
    def Refresh(self):
        self.active_dose += self.dose

    def SetMoodMultiplier(self):
        self.mood_multiplier = abs(self.active_dose-self.ideal_dose)/self.ideal_dose

    def GetMoodReduction(self):
        return self.mood_multiplier * self.max_mood_reduction_
    
    def SetDecay(self):
        self.decay = self.dose / self.hours_to_purge_

    def SetAbsorbtion(self):
        self.absorb = self.dose / self.hours_to_absorb_

    def SetHoursToAbsorb(self):
        hours = 24
        self.hours_to_absorb_ = random.randint(1,hours-1)
        self.hours_to_purge_ = hours - self.hours_to_absorb_
        self.SetAbsorbtion()
        self.SetDecay()


