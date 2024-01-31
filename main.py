import action_handlers
import _clock
import cocos


#MAIN


clock = _clock.Clock()


for item in clock.player.medications: 
    clock.player.TakeMedication(item)


print("You have decided to bake a cake from scratch. It's something you've always wanted to try but never got around to.")
print()
print("How will you begin?")

while action_handlers.Go:
    fullInput = input(">")
    print()
    action_handlers.ResolveAction(fullInput)
    print()
    clock.Tick()
