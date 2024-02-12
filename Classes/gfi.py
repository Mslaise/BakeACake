#The interface between the terminal and COCOS. Is the gateway for all graphical operations, runs on the COCOS process.



import cocos
from cocos.actions import *
from Globals.game_info import *
from Globals.resources import *
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
        self.ui.scale = 1.5        
        self.ui_screen_display_sprites = [None,None,None,None]
        self.ui_screen_display_index = 0
        
        #After instantiation, release the lock back to the terminal thread.
        self.ui.do(CallFunc(self.ReleaseLock))
        
        #The lock will release before this function is called, so it'll be skipped
        #Until this instance regains control
        self.ui.do(Repeat(CallFunc(self.HearTerminalEvents)))
                
        self.add(self.ui)
        
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

        if event == 'Screen Popped':
            pass
        
                
            
        
 