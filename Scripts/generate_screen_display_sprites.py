#Run this once to generate the sprites for the displays


from PIL import Image, ImageDraw, ImageFont
from G_GameInfo import *
from G_SpriteInfo import *
from G_Resources import *

W = UI_inventory_grid_width
H = UI_inventory_grid_width

for item in display_screens:
    new_image = Image.new('RGBA',(W,H),(0,0,0,0))
    myImage = ImageDraw.Draw(new_image)
    _, _, w, h = myImage.textbbox((0,0),item['Char'],font=Font_UiScreenDisplay)
    
    myImage.text(((W-w)/2,(H-h)/2-5),item['Char'],font=Font_UiScreenDisplay,fill='black')
    new_image.save('Sprites/UI/InfoScreen/ScreenDisplays/'+item['Name']+'.png','PNG')