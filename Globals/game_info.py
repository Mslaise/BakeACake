#Basic information needed to construct game objects or resource objects
import math

CO_director_width = 600
CO_director_height = 400

UI_inventory_grid_width = 27
UI_inventory_grid_height = 21

UI_content_width = 147
UI_content_height = 157
UI_content_border_width = 2
UI_content_display_width = 48
UI_content_display_height = 48
UI_content_display_border_width = 2
UI_content_display_thick_border_width = UI_content_display_border_width * 3
UI_content_display_sprite_fontsize = (math.floor(UI_inventory_grid_height * 1.35))
UI_content_display_medicine_fontsize = ()
UI_content_display_fontsize = int(UI_content_width * 0.75)


xoff = int(UI_content_display_width * 0.5) + int(UI_content_display_sprite_fontsize * 0.25)
xint = UI_content_display_border_width + int(UI_content_display_border_width * 0.5)
ypos = CO_director_height - int(UI_content_display_height * 0.5)
start = 91
UI_content_label_coordinates = [(start+xoff+xint,ypos),
                                (start+xoff+xint * 2 + UI_content_width + UI_content_border_width,ypos),
                                (start+xoff+xint * 3 + UI_content_width * 2 + UI_content_border_width,ypos),
                                (start+xoff+xint * 4 + UI_content_width * 3 + UI_content_border_width,ypos)]


ypos = CO_director_height - int(UI_content_height / 2)
UI_content_screen_coordinates = [(0,ypos),
                                 (UI_content_width+UI_content_border_width,ypos),
                                 (UI_content_width+UI_content_border_width+UI_content_display_thick_border_width,ypos),
                                 (UI_content_width*3+UI_content_border_width*2+UI_content_display_thick_border_width,ypos)]





UI_content_label_west_regions = []
UI_content_label_south_regions = []
UI_content_main_regions = []

