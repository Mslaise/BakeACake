#Since the sprites are used to create game resources they get their own file


#Assigned spriteboxes instead of explicitly defined dictionaries

from Globals.macrory import *
from Globals.game_info import *
from Classes.spritebox import *

#Font is segoe ui symbol 
Medicine_ui = SpriteBox(u"\u2665",'Medicine')               #medicine
Butter_ui = SpriteBox( u"\u2e19",'Food')                    #butter
Sugar_ui = SpriteBox( u"\ue1a1",'Sugar')                    #sugar
Egg_ui = SpriteBox( u"\u2b2f",'Egg')                        #egg
Plate_ui = SpriteBox(u"\u2b56",'Plate')                     #plate
Bowl_ui = SpriteBox(u"\u2b57",'Bowl')                       #bowl
Flour_ui = SpriteBox(u"\ue1a1",'Flour')                     #flour
Salt_ui = SpriteBox(u"\ue1a1",'Salt')                       #salt
BakingPowder_ui = SpriteBox(u"\ue1a1",'Baking Powder')      #baking powder
Milk_ui = SpriteBox(u"\u2649",'Milk')                       #milk
VanillaExtract_ui = SpriteBox(u"\u29b0",'Vanilla Extract')  #vanilla extract
Mixer_ui = SpriteBox(u"\u2e0e",'Mixer')                     #mixer
Whisk_ui = SpriteBox(u"\u27b0",'Whisk')                     #whisk

ui_sbs = [Medicine_ui,Butter_ui,Sugar_ui,
                  Egg_ui,Plate_ui,Bowl_ui,
                  Flour_ui,BakingPowder_ui,Milk_ui,
                  VanillaExtract_ui,Mixer_ui,Whisk_ui]
                  
                  
Elated_mood_content = SpriteBox(u"\ue11d",'moodElated')
Happy_mood_content = SpriteBox(u"\u263a",'moodHappy')
Sad_mood_content =   SpriteBox(u"\u2639",'moodSad')

mood_content_sbs = [Elated_mood_content,Happy_mood_content,Sad_mood_content]
mood_content_coordinates = (int(CO_director_width) * 0.75,int(CO_director_height)*0.25)


LeftHand_content_label = SpriteBox(u"\u270b",screen_left_hand)
RightHand_content_label = SpriteBox(u"\u270b",screen_right_hand,condition = 'Flip')
Time_content_label = SpriteBox(u"\u231a",screen_time)
Relationships_content_label = SpriteBox(u"\u2766",screen_relationships)
Medications_content_label = SpriteBox(u"\u211e",screen_medications)

display_screens_sbs = [LeftHand_content_label,RightHand_content_label,Time_content_label,Relationships_content_label,Medications_content_label]
display_sprite_fontsize = (math.floor(UI_inventory_grid_height * 1.1))



medications = [u"\u2596",u"\u2597",u"\u2598",u"\u2599",u"\u259a",u"\u259b",u"\u259c",u"\u259d",u"\u259e",u"\u259f",
               u"\u25a0"]
medication_sbs = [SpriteBox(medications[i],'medication'+str(i)) for i in range(len(medications))]








