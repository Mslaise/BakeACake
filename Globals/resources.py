#This file is for storing complex objects that are used by game elements


from PIL import ImageFont
from Globals.game_info import *

from Classes.clock import Clock
from Classes.action_handlers import ActionHandler

import math                
import pyglet               
from multiprocessing import Process, Pipe




act_handle = ActionHandler()
Font_UiSprite = ImageFont.truetype('seguisym.ttf',size=math.floor(UI_inventory_grid_height*0.97),encoding="unic")
Font_UiContentLabel = ImageFont.truetype('seguisym.ttf',size=UI_screen_display_sprite_fontsize, encoding="unic")
Font_UiScreenContent = ImageFont.truetype('seguisym.ttf',size=UI_screen_display_content_fontsize,encoding="unic")



        

