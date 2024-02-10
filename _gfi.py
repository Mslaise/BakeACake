import cocos
from G_Resources import act_handle
import threading
from F_ThreadingProcesses import MainLoop
from F_ThreadingProcesses import TerminalLoop

class MainGfi(cocos.layer.Layer):
    def __init__(self,x,y):
    
        #Starts the COCOS application
        super(MainGfi,self).__init__()
        act_handle.push_handlers(self)
        
        ui = cocos.sprite.Sprite('Sprites/UI/InfoScreen/UiCurrent.png')
        ui.position = (x,y)
        ui.scale = 1.5
        self.add(ui,z=0)
        
        insist = threading.Thread(target = MainLoop)
        insist.start()
        
    def e_PopScreen(self,screen):
        pass
        
    def e_Exit(self):
        #Ends the scene
        cocos.director.director.scene.end(0)
        
    def UpdateVisuals(self):
        #Updates visuals before giving back control to the main thread
        
        insist = threading.Thread(target=MainLoop)
        insist.start()
        
        
 