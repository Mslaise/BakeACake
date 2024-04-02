import random


from Globals.macrory import *
from Classes.inventory import Inventory
from Classes.item import Item
from Classes.bond import Bond
from Classes.medication import Medication
from Classes.gfi_package import GfiPackage
from Classes.gfi_package import GfiFreight

class Player:
    def __init__(self,cocosPipe):
        self.cocos_pipe = cocosPipe
        self.med_debuff_ = 0
        self.max_mood_ = 100

        #These determine on what interval your mood will be calculated in
        self.valid_mood_types_ = ["Peaceful","Stable","Sensitive","Neurotic"]

        self.name = "Addy"
        self.inventory = Inventory(cocosPipe)
        self.bonds = []
        self.medications = []

        self.mood = self.max_mood_
        self.mood_type = 'Stable'

        self.InitializeMedications()
        self.InitializeBonds()

    def CalculateMood(self):
        self.mood = self.max_mood_

        for med in self.medications:
            self.mood -= med.GetMoodReduction()

        if self.mood < 0:
            self.mood = 0


    def CycleDay(self):
        #Called when 1 day passes
        
        if self.mood_type == 'Peaceful':
            self.CalculateMood()

    def CycleHour(self):
        #Called when 1 hour passes

        #Medications only cycle on the hour
        for med in self.medications:
            med.Cycle()

        #Mood is recalculated if you are stable
        if self.mood_type == 'Stable':
            self.CalculateMood()
            print(self.mood)


    def CycleMinute(self):
        #Called when 1 minute passes
        if self.mood_type == 'Sensitive':
            self.CalculateMood()
        
    def CycleSecond(self):
        #Called when 1 second passes
        if self.mood_type == 'Neurotic':
            self.CalculateMood()

    def TakeMedication(self,medic):
        for med in self.medications:
            if med == medic:
                med.Refresh()

    def AddMedication(self,medic):
        self.medications.append(medic)

    def RemoveMedication(self,medic):
        self.medications.remove(medic)

    def AddBond(self,bond):
        self.bonds.append(bond)

    def RemoveBond(self,bond):
        self.bonds.remove(bond)

    def SetMood(self,mood):
        if mood in self.valid_mood_types_:
            self.mood_type = mood
            
    def GetMaxMood(self):
        return self.max_mood_

    def InitializeMedications(self):
        #You start the game on between 4 and 10 medications
        amount = random.randint(4,10)
        amount = 1
        for i in range(amount):
            self.AddMedication(Medication(ui_is_medications+'/medication'+str(i)+'.png'))
        
    def InitializeBonds(self):
        #3 to 8 bonds
        amount = random.randint(3,8)
        for i in range(amount):
            self.AddBond(Bond())
            
    #any graphical information that needs to be sent to the GFI from the player is done so here
    def RelayGfiPackages(self):
        medicationPackages = self.GatherMedicationPackages()
        freight = GfiFreight(medicationPackages)
        return freight
            
    def GatherMedicationPackages(self):
        medicationPackages = []
        for med in self.medications:
            medicationPackages.append(GfiPackage(screen_medications,med.sprite))
 
        return medicationPackages
        
            
   
        