import cocos
from _gfi import MainGfi
from G_GameInfo import *


def InitCocos():
	cocos.director.director.init(width=CO_director_width,height=CO_director_height)
    main_layer = MainGfi(int(CO_director_width/2),int(CO_director_height/2))
    main_scene = cocos.scene.Scene(main_layer)
    cocos.director.director.run(main_scene)