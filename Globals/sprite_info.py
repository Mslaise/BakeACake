#Since the sprites are used to create game resources they get their own file

from Globals.macrory import *

#Font is segoe ui symbol 
Medicine_ui = {'Char':u"\u2665",'Name':'Medicine'}               #medicine
Butter_ui = {'Char': u"\u2e19",'Name':'Food'}                    #butter
Sugar_ui = {'Char': u"\ue1a1",'Name':'Sugar'}                    #sugar
Egg_ui = {'Char': u"\u2b2f",'Name':'Egg'}                        #egg
Plate_ui = {'Char':u"\u2b56",'Name':'Plate'}                     #plate
Bowl_ui = {'Char':u"\u2b57",'Name':'Bowl'}                       #bowl
Flour_ui = {'Char':u"\ue1a1",'Name':'Flour'}                     #flour
Salt_ui = {'Char':u"\ue1a1",'Name':'Salt'}                       #salt
BakingPowder_ui = {'Char':u"\ue1a1",'Name':'Baking Powder'}      #baking powder
Milk_ui = {'Char':u"\u2649",'Name':'Milk'}                       #milk
VanillaExtract_ui = {'Char':u"\u29b0",'Name':'Vanilla Extract'}  #vanilla extract
Mixer_ui = {'Char':u"\u2e0e",'Name':'Mixer'}                     #mixer
Whisk_ui = {'Char':u"\u27b0",'Name':'Whisk'}                     #whisk

ui = [Medicine_ui,Butter_ui,Sugar_ui,
                  Egg_ui,Plate_ui,Bowl_ui,
                  Flour_ui,BakingPowder_ui,Milk_ui,
                  VanillaExtract_ui,Mixer_ui,Whisk_ui]
                  
                  
                  


#Font is segoe ui emoji
LeftHand_display = {'Char':u"\u270b",'Name':screen_left_hand}
RightHand_display = {'Char':u"\u270b",'Name':screen_right_hand,'Condition':'Flip'}

display_screens = [LeftHand_display,RightHand_display]