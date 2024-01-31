from G_Help import *

def ResolveAction(fullInput):
    splitInput = fullInput.split()
    if splitInput[0] in valid_actions:
        if splitInput[0] == action_help:   #Help
            ACT_Help(splitInput[1:])
        elif splitInput[0] == action_wait: #Wait
            ACT_Wait(splitInput[1:])
        elif splitInput[0] == action_list: #List
            ACT_List(splitInput[1:])
        elif splitInput[0] == action_exit: #Exit
            ACT_Exit(splitInput[1:])
        elif splitInput[0] == action_pops: #Pops
            ACT_Pops(splitInput[1:])
        else:
            print('No implementation for',splitInput[0])
    else:
        print('Invalid action. For a list of valid actions, type "help" or "list action"')

def ACT_Help(splitInput):
    if len(splitInput) <= 1:
        for item in valid_actions:
            print(item+':',HELP_DESCRIPTIONS[item][valid_terms[0]])
        print()
        print('For a description of each action, type "help" and then the name of the action.')
    else:
        print(len(splitInput))
        if splitInput[1] in valid_terms:
            print('-Term (TERM)-')
        elif splitInput[1] in valid_actions:
            print('-Action (ACT)-')
        elif splitInput[1] in valid_formatters:
            print('-Formatter (FORM)-')

        print(splitInput[0])
        for entry in HELP_DESCRIPTIONS[splitInput[0]]:
            print(entry+':',HELP_DESCRIPTIONS[splitInput[0]][entry])

def ACT_Wait(splitInput):
    pass

def ACT_List(splitInput):
    if len(splitInput) == 1:
        if splitInput[0] in valid_lists:
            print('-Enumerating '+splitInput[0]+'-')
            for item in list_map[splitInput[0]]:
                print(item)        
    

Go = True
def ACT_Exit(splitInput):
    global Go
    Go = False

def ACT_Pops(splitInput):
    if len(splitInput) == 1:
        if splitInput[0] in valid_screens:
            pass
        else:
            pass
    