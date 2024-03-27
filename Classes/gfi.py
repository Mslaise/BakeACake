#The interface between the terminal and COCOS. Is the gateway for all graphical operations, runs on the COCOS process.



import cocos
from cocos.actions import *
from Globals.macrory import *
from Globals.game_info import *
from Globals.resources import *
from Globals.sprite_info import mood_content_coordinates
import time
import multiprocessing




class Gfi(cocos.layer.Layer):
    def __init__(self,x,y,lock,pipe): #lock and pipe are for communicating with action_handlers
        #Starts the COCOS application
        super(Gfi,self).__init__()
        self.event = True
        self.lock = lock
        self.pipe = pipe

        self.ui = cocos.sprite.Sprite('Sprites/UI/InfoScreen/UiCurrent.png')
        self.ui.position = (x,y)
        self.ui.scale = 1      
        self.ui_screen_display_sprites = [None,None,None,None]
        self.ui_screen_display_index = 0
        
        self.mood_content = cocos.sprite.Sprite(ui_is_content+'/moodHappy.png')
        self.mood_content.position = mood_content_coordinates
        
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
        
        
        if self.pipe.poll():
            event = self.pipe.recv()
            self.ProcessTerminalEvent(event)
        
        
        self.lock.release()
        pass
        
    def ReleaseLock(self):
        self.lock.release()
    
    def ProcessTerminalEvent(self,event):
        if event[0] == 'Screen Popped':
            self.PopIcon(event)
        if event[0] == 'Second Passed':
            self.UpdateTimeGraphics(event)
            
    def PopIcon(self,event):
    
        #Remove the final sprite in ui_screen_display_sprites
        if self.ui_screen_display_sprites[-1] != None:
            self.remove(self.ui_screen_display_sprites[-1])
            self.ui_screen_display_sprites[-1] = None
            
        #Rotate the list
        self.ui_screen_display_sprites = [self.ui_screen_display_sprites[-1]] + self.ui_screen_display_sprites[:-1]
        if self.ui_screen_display_sprites[0] == None:
            self.ui_screen_display_sprites[0] = cocos.sprite.Sprite('Sprites/UI/InfoScreen/ContentLabels/'+event[1][1]+'.png')
            self.ui_screen_display_sprites[0].position = (UI_screen_display_px_coordinates[0])
            self.add(self.ui_screen_display_sprites[0])
        
        for i in range(1,len(UI_screen_display_px_coordinates)):
            if self.ui_screen_display_sprites[i] != None:
                self.ui_screen_display_sprites[i].position = UI_screen_display_px_coordinates[i]
                
                
                
    def UpdateTimeGraphics(self,event):
        pass
                
            
        
 