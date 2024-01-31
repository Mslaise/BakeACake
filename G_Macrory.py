action_help = 'Help'
action_wait = 'Wait'
action_list = 'List'
action_exit = 'Exit'
action_pops = 'Pops'
action_goto = 'Goto'
valid_actions = [action_help,action_wait,action_list,action_exit,action_pops,action_goto]

screen_inventory = 'Inventory'
screen_mood = 'Mood'
valid_screens = [screen_inventory,screen_mood]

term_formatter = 'Formatter'
term_screen = 'Screen'
term_action = 'Action'
term_time = 'Time'
term_description = 'Description'
term_room = 'Room'
valid_terms = [term_formatter,term_screen,term_action,term_time,term_description,
               term_room]

form_formatter = 'FORM'
form_screen = 'SCRN'
form_action = 'ACT'
form_time = 'TIME'
form_desc = 'DESC'
form_room = 'ROOM'
valid_formatters = [form_formatter,form_screen,form_action,form_time,form_room,
                    ]

term_form_convert = {}
term_form_convert[term_formatter] = form_formatter
term_form_convert[term_screen] = form_screen
term_form_convert[term_action] = form_action
term_form_convert[term_time] = form_time
term_form_convert[term_description] = form_desc
term_form_convert[term_room] = form_room

form_term_convert = {}
for item in valid_terms:
    form_term_convert[term_form_convert[item]] = item


valid_screens = []


list_formatters = 'Formatters'
list_actions = 'Actions'
list_terms = 'Terms'
list_screens = 'Screens'
list_lists = 'Lists'
valid_lists = [list_formatters,list_actions,list_terms,list_screens,list_lists]
list_map = {list_formatters:[item for item in valid_formatters],
            list_actions:[item for item in valid_actions],
            list_terms:[item for item in valid_terms],
            list_screens:[item for item in valid_screens],
            list_lists:[item for item in valid_lists]}