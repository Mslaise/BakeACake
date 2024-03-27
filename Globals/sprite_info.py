#Since the sprites are used to create game resources they get their own file

from Globals.macrory import *
from Globals.game_info import *

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
                  
                  
                  
Elated_mood_content = {'Char':u"\ue11d",'Name':'moodElated'}
Happy_mood_content = {'Char':u"\u263a",'Name':'moodHappy'}
Sad_mood_content =   {'Char':u"\u2639",'Name':'moodSad'}

mood_content = [Elated_mood_content,Happy_mood_content,Sad_mood_content]
mood_content_coordinates = (int(CO_director_width) * 0.75,int(CO_director_height)*0.25)


#Font is segoe ui emoji
LeftHand_content_label = {'Char':u"\u270b",'Name':screen_left_hand}
RightHand_content_label = {'Char':u"\u270b",'Name':screen_right_hand,'Condition':'Flip'}
Time_content_label = {'Char':u"\u231a",'Name':screen_time}
Relationships_content_label = {'Char':u"\u2766",'Name':screen_relationships}
Medications_content_label = {'Char':u"\u211e",'Name':screen_medications}

display_screens = [LeftHand_content_label,RightHand_content_label,Time_content_label,Relationships_content_label,Medications_content_label]
display_sprite_fontsize = (math.floor(UI_inventory_grid_height * 1.1))



medications = [u"\u2596",u"\u2597",u"\u2598",u"\u2599",u"\u259a",u"\u259b",u"\u259c",u"\u259d",u"\u259e",u"\u259f",
               u"\u25a0"]
medication_sprites = [{'Char': medications[i], 'Name':'medication'+str(i)} for i in range(len(medications))]








