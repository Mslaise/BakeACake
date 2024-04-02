#The interface between the terminal and COCOS. Is the gateway for all graphical operations, runs on the COCOS process.


#Changes: 
#PopIcon renamed to ShowScreenDisplayLabel
#ShowScreenDisplaySprite prototype created to present medication sprites

#Todo:
#Implement error handling


import cocos
from cocos.actions import *
from Globals.macrory import *
from Globals.game_info import *
from Globals.resources import *
from Globals.sprite_info import mood_content_coordinates
from Classes.player import Player as player
from Classes.gfi_package import GfiFreight
import time
import multiprocessing




class Gfi(cocos.layer.Layer):
    def __init__(self,x,y,lock,cocosPipeOut): #lock and pipe are for communicating with action_handlers
        #Starts the COCOS application
        super(Gfi,self).__init__()
        self.event = True
        self.lock = lock
        self.cocos_pipe_out = cocosPipeOut

        self.ui = cocos.sprite.Sprite('Sprites/UI/InfoScreen/UiCurrent.png')
        self.ui.position = (x,y)
        self.ui.scale = 1      
        self.ui_content_label_sprites = [None,None,None,None]
        self.ui_content_label_sprites_order = ['','','','']
        self.ui_content_label_index = 0
        
        self.content_display_sprites = []
        
        self.mood_content = cocos.sprite.Sprite(ui_is_content+'/moodHappy.png')
        self.mood_content.position = mood_content_coordinates
        
        self.general_content_sprites = []
        
        #After instantiation, release the lock back to the terminal thread.
        self.ui.do(CallFunc(self.ReleaseLock))
        
        #The lock will release before this function is called, so it'll be skipped
        #Until this instance regains control
        self.ui.do(Repeat(CallFunc(self.HearTerminalEvents)))
               
        self.add(self.ui)
        self.add(self.mood_content)
        

    def e_PopScreen(self,screen):
        pass
        
        
    def e_Exit(self):
        #Ends the scene
        cocos.director.director.scene.end(0)
    
    def HearPygletEvents(self):
        pass
        
    def HearTerminalEvents(self):
        self.lock.acquire()
        
        
        if self.cocos_pipe_out.poll():
            event = self.cocos_pipe_out.recv()
            self.ProcessTerminalEvent(event)
        
        
        self.lock.release()
        pass
        
    def ReleaseLock(self):
        self.lock.release()
    
    def ProcessTerminalEvent(self,event):
        if type(event[0]) == str:
            if event[0] == 'Screen Popped':
            
                self.ui_content_label_sprites_order[-1] = ''
                self.ui_content_label_sprites_order = [''] + self.ui_content_label_sprites_order[:-1]
                self.ui_content_label_sprites_order[0] = event[1][1]

                self.ShowScreenDisplayLabel(event)
            if event[0] == 'Second Passed':
                self.ShowScreenDisplaySprite(event)
            if event[0] == 'Player Data':
                self.PresentPlayerData(event)
        else:
            #Implement error handling
            pass
                
    def ShowScreenDisplayLabel(self,event):
    
        #Remove the final sprite in ui_content_label_sprites
        if self.ui_content_label_sprites[-1] != None:
            self.remove(self.ui_content_label_sprites[-1])
            self.ui_content_label_sprites[-1] = None
            
        #Rotate the list
        self.ui_content_label_sprites = [self.ui_content_label_sprites[-1]] + self.ui_content_label_sprites[:-1]
        
        self.ui_content_label_sprites[0] = cocos.sprite.Sprite('Sprites/UI/InfoScreen/ContentLabels/'+event[1][1]+'.png')
        self.ui_content_label_sprites[0].position = (UI_content_label_coordinates[0])
        self.add(self.ui_content_label_sprites[0])
    
        for i in range(1,len(UI_content_label_coordinates)):
            if self.ui_content_label_sprites[i] != None:
                self.ui_content_label_sprites[i].position = UI_content_label_coordinates[i]
                
                
                
    def ShowScreenDisplaySprite(self,event):
        if type(event[1]) == GfiFreight:
            for package in event[1].gfi_packages:
                if event[1].screen in self.ui_content_label_sprites_order:
                    pos = self.ui_content_label_sprites_order.index(event[1].screen)
                    starting_coordinates = UI_content_screen_coordinates[pos]   
                    if event[1].screen == screen_medications:
                        #Display medic
                        pass
        else:
            #implement error handling
            pass
        
        
    def PresentPlayerData(self,event):
        print('graphics data succesfully relayed')
        pass
                
            
        
 