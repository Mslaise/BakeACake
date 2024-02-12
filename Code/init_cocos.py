import cocos
from Classes.gfi import Gfi
from Globals.game_info import *
from Globals.resources import *
import math

def InitCocos(lock,pipe):
    #Initializes COCOS for the COCOS process
    
    cocos.director.director.init(width=CO_director_width,height=CO_director_height)
    
    #The GFI will handle all transfers of power between the terminal and cocos
    main_layer = Gfi(math.floor(CO_director_width/2),math.floor(CO_director_height/2),lock,pipe) 
    
    main_scene = cocos.scene.Scene(main_layer)
    cocos.director.director.run(main_scene)

    #The road ends here