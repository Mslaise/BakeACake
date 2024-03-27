#Run this once to generate the inventory sprites.

from PIL import Image, ImageDraw, ImageFont
from Globals.game_info import *
from Globals.sprite_info import *
from Globals.resources import *

W = UI_inventory_grid_width
H = UI_inventory_grid_width

for item in ui:
    new_image = Image.new('RGBA',(W,H),(0,0,0,0))
    myImage = ImageDraw.Draw(new_image)
    _, _, w, h = myImage.textbbox((0,0),item['Char'],font=Font_UiSprite)
    
    myImage.text(((W-w)/2,(H-h)/2),item['Char'],font=Font_UiSprite,fill='black')
    new_image.save(ui_is_items+'/'+item['Name']+'.png','PNG')