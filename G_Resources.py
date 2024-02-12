#This file is for storing complex objects that are used by game elements


from PIL import ImageFont
from G_GameInfo import *

import _clock               #For creating clock
import _action_handlers     #For creating act_handle

import math                 #Used math.floor
import pyglet               
from multiprocessing import Process, Pipe




clock = _clock.Clock()
act_handle = _action_handlers.ActionHandler()
Font_UiSprite = ImageFont.truetype('seguisym.ttf',size=math.floor(UI_inventory_grid_height*0.97),encoding="unic")
Font_UiScreenDisplay = ImageFont.truetype('seguisym.ttf',size=math.floor(UI_screen_display_width * 0.97), encoding="unic")



        

