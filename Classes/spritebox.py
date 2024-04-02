#New class that is responsible for containing information on sprites


class SpriteBox():
    def __init__(self,rchar,name,condition=None):
        self.name = name
        self.char = rchar
        self.condition = condition
		
		