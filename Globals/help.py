from Globals.macrory import *


HELP_DESCRIPTIONS = {}

for item in valid_actions:
    #Formatter, Description
    HELP_DESCRIPTIONS[item] = {term_formatter:'',
                               term_description:''}

for item in valid_terms:
    #Description
    HELP_DESCRIPTIONS[item] = {term_description:''}


#Terms only have descriptions
    
#Formatter 
HELP_DESCRIPTIONS[term_formatter][term_description] = "An abbreviation of an action or object."

#Screen 
HELP_DESCRIPTIONS[term_description][term_description] = "A pop-up window with a graphical representation of something."

#Action
HELP_DESCRIPTIONS[term_action][term_description] = "Something the player can do."

#Time
HELP_DESCRIPTIONS[term_time][term_description] = "Time passes at a rate of 1 second per second. Even now, time is passing."

HELP_DESCRIPTIONS[term_gfi][term_description] = "Short for 'Graphical Feedback Interface.'"

#Actions have Formatters and Descriptions
#Action 'help'
HELP_DESCRIPTIONS[action_help][term_formatter] = 'ACT ACT1 | FORM1 | TERM1'
HELP_DESCRIPTIONS[action_help][term_description] = 'Explains either an action, formatter, or term to the user.'

#Action 'wait' 
HELP_DESCRIPTIONS[action_wait][term_formatter] = 'ACT TIME1'
HELP_DESCRIPTIONS[action_wait][term_description] = 'Wait for a particular amount of time.'

#Action 'list' 
HELP_DESCRIPTIONS[action_list][term_formatter] = 'ACT TERM1'
HELP_DESCRIPTIONS[action_list][term_description] = 'Display all objects that are defined with TERM1.'

#Action 'exit'
HELP_DESCRIPTIONS[action_exit][term_formatter] = 'ACT'
HELP_DESCRIPTIONS[action_exit][term_description] = 'Exits the program.'

#Action 'pops'
HELP_DESCRIPTIONS[action_pops][term_formatter] = 'ACT SCRN1'
HELP_DESCRIPTIONS[action_pops][term_description] = 'Pops up a specific screen.'

#Action 'clear'
HELP_DESCRIPTIONS[action_clear][term_formatter] = 'ACT'
HELP_DESCRIPTIONS[action_clear][term_description] = 'Clears the screen.'

#Action 'egfi'
HELP_DESCRIPTIONS[action_egfi][term_formatter] = 'ACT'
HELP_DESCRIPTIONS[action_egfi][term_description] = 'Enables the GFI.'

