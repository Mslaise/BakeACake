from PIL import Image, ImageDraw, ImageFont
from Globals.game_info import *
from Globals.sprite_info import *
from Globals.resources import *


W = UI_screen_width
H = UI_screen_width
for spr in medication_sbs:
    new_image = Image.new('RGBA',(W,H),(0,0,0,0))
    myImage = ImageDraw.Draw(new_image)
    _, _, w, h = myImage.textbbox((0,0),spr.Char,font=Font_UiScreenContent)
    
    myImage.text(((W-w)/2,(H-h)/2),spr.Char,font=Font_UiScreenContent,fill='black')
    new_image.save(ui_is_medications+'/'+spr.Name+'.png','PNG')