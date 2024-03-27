import ctypes
ui_is = "Sprites/UI/InfoScreen"
ui_is_content_labels = "Sprites/UI/InfoScreen/ContentLabels"
ui_is_content = "Sprites/UI/InfoScreen/Content"
ui_is_items = "Sprites/UI/InfoScreen/Items"
ui_is_medications = "Sprites/UI/InfoScreen/medications"



#Useful constants
user_screen_width = ctypes.windll.user32.GetSystemMetrics(0)
user_scren_height = ctypes.windll.user32.GetSystemMetrics(1)

#Actions
action_help = 'help'
action_wait = 'wait'
action_list = 'list'
action_exit = 'exit'
action_egfi = 'egfi'
action_pops = 'pops'
action_goto = 'goto'
action_clear = 'clear'
valid_actions = [action_help,action_wait,action_list,action_exit,action_egfi,action_pops,action_goto,action_clear]


#Screens
screen_left_hand = 'left-hand'
screen_right_hand = 'right-hand'
screen_time = 'time'
screen_relationships = 'relationships'
screen_medications = 'medications'

valid_screens = [screen_left_hand,screen_right_hand,screen_time,screen_relationships,screen_medications]

#Terms
term_formatter = 'formatter'
term_screen = 'fcreen'
term_action = 'action'
term_time = 'time'
term_description = 'description'
term_room = 'room'
term_gfi = 'GFI'
valid_terms = [term_formatter,term_screen,term_action,term_time,term_description,
               term_room,term_gfi]


#Formatters
form_formatter = 'FORM'
form_screen = 'SCRN'
form_action = 'ACT'
form_time = 'TIME'
form_desc = 'DESC'
form_room = 'ROOM'
form_gfi = 'GFI'
valid_formatters = [form_formatter,form_screen,form_action,form_time,form_room,
                    form_gfi]

term_form_convert = {}
term_form_convert[term_formatter] = form_formatter
term_form_convert[term_screen] = form_screen
term_form_convert[term_action] = form_action
term_form_convert[term_time] = form_time
term_form_convert[term_description] = form_desc
term_form_convert[term_room] = form_room
term_form_convert[term_gfi] = form_gfi

form_term_convert = {}
for item in valid_terms:
    form_term_convert[term_form_convert[item]] = item


#Lists
list_formatters = 'formatters'
list_actions = 'actions'
list_terms = 'terms'
list_screens = 'screens'
list_lists = 'lists'
valid_lists = [list_formatters,list_actions,list_terms,list_screens,list_lists]
list_map = {list_formatters:[item for item in valid_formatters],
            list_actions:[item for item in valid_actions],
            list_terms:[item for item in valid_terms],
            list_screens:[item for item in valid_screens],
            list_lists:[item for item in valid_lists]}