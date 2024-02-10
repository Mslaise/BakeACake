from G_Help import *
from G_Macrory import *
import cocos
import time
import threading
import pyglet
import os

class ActionHandler(pyglet.event.EventDispatcher):
    def __init__(self):
        super(ActionHandler,self).__init__()
        self.Go = True
        self.Gfi = False
        
    def ResolveAction(self,fullInput):
        splitInput = fullInput.split()
        
        
        if len(splitInput) > 0 and splitInput[0] in valid_actions:
            if splitInput[0] == action_help:   #Help
                self.ACT_Help(splitInput[1:])
            elif splitInput[0] == action_wait: #Wait
                self.ACT_Wait(splitInput[1:])
            elif splitInput[0] == action_list: #List
                self.ACT_List(splitInput[1:])
            elif splitInput[0] == action_exit: #Exit
                self.ACT_Exit(splitInput[1:])
            elif splitInput[0] == action_egui: #Egfi
                self.ACT_Egfi(splitInput[1:])
            elif splitInput[0] == action_pops: #Pops
                self.ACT_Pops(splitInput[1:])
            elif splitInput[0] == action_clear:
                self.ACT_Clear()
            else:
                print('No implementation for',splitInput[0])
        else:
            print('Invalid action. For a list of valid actions, type "help" or "list action"')

    def ACT_Help(self,splitInput):
        if len(splitInput) < 1:
            for item in valid_actions:
                print(item+':',HELP_DESCRIPTIONS[item][valid_terms[0]])
            print()
            print('For a description of each action, type "help" and then the name of the action.')
        else:
            if splitInput[0] in valid_terms:
                print('-Term (TERM)-')
            elif splitInput[0] in valid_actions:
                print('-Action (ACT)-')
            elif splitInput[0] in valid_formatters:
                print('-Formatter (FORM)-')

            print(splitInput[0])
            for entry in HELP_DESCRIPTIONS[splitInput[0]]:
                print(entry+':',HELP_DESCRIPTIONS[splitInput[0]][entry])

    def ACT_Wait(self,splitInput):
        pass

    def ACT_List(self,splitInput):
        if len(splitInput) == 0:
            print('-printing valid lists-')
            for item in valid_lists:
                print(item)
            print()
            print("For more information about what these lists contain, type 'list' and follow it with a valid list name.")
        else:
            if splitInput[0] in valid_lists:
                for item in list_map[splitInput[0]]:
                    print(item)
        

    def ACT_Exit(self,splitInput):
        self.Go = False
        self.dispatch_event('e_Exit')
        
    def ACT_Egfi(self,splitInput):
        if self.Gfi == False:
            self.Gfi = True
            print('You have activated the GFI. Commands will still be entered through the terminal.')
        else:
            print('GFI has already been activated.')
            
    def ACT_Pops(self,splitInput):
        if splitInput[0] in valid_screens:
            #This won't actually handle anything with Cocos, that will be done with MainGFI.
            #All this method serves to do is dispatch the popscreen event.
            self.dispatch_event('e_PopScreen',splitInput[0])
            
            
    def ACT_Clear(self):
        for i in range(100):
            print()
        


#Types of events dispatched by ActionHandler
ActionHandler.register_event_type('e_PopScreen')
ActionHandler.register_event_type('e_Exit')

act_handle = ActionHandler()
