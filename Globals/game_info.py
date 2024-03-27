#Basic information needed to construct game objects or resource objects
import math

UI_inventory_grid_width = 27
UI_inventory_grid_height = 21

UI_screen_width = 147
UI_screen_border_width = 2
UI_screen_display_width = 48
UI_screen_display_height = 48
UI_screen_display_border_width = 2
UI_screen_display_sprite_fontsize = (math.floor(UI_inventory_grid_height * 1.35))
UI_screen_display_medicine_fontsize = ()
UI_screen_display_content_fontsize = int(UI_screen_width * 0.75)

CO_director_width = 600
CO_director_height = 400

xoff = int(UI_screen_display_width * 0.5) + int(UI_screen_display_sprite_fontsize * 0.25)
xint = UI_screen_display_border_width + int(UI_screen_display_border_width * 0.5)
ypos = CO_director_height - int(UI_screen_display_height * 0.5)
start = 91
UI_screen_display_px_coordinates = [(start+xoff+xint,ypos),
                                    (start+xoff+xint * 2 + UI_screen_width + UI_screen_border_width,ypos),
                                    (start+xoff+xint * 3 + UI_screen_width * 2 + UI_screen_border_width,ypos),
                                    (start+xoff+xint * 4 + UI_screen_width * 3 + UI_screen_border_width,ypos)]







