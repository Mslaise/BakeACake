from PIL import Image, ImageDraw, ImageFont
from G_GameInfo import *
from G_SpriteInfo import *


W = UI_inventory_grid_width
H = UI_inventory_grid_height

GD_UiSpriteFont = ImageFont.truetype('seguisym.ttf',size=math.floor(H*0.97),encoding="unic")


for item in ui_sprite_info:
    new_image = Image.new('RGBA',(W,H),(0,0,0,0))
    myImage = ImageDraw.Draw(new_image)
    _, _, w, h = myImage.textbbox((0,0),item['Char'],font=GD_UiSpriteFont)
    
    myImage.text(((W-w)/2,(H-h)/2-5),item['Char'],font=GD_UiSpriteFont,fill='black')
    new_image.save('Sprites/UI/Items/'+item['Name']+'.png','PNG')