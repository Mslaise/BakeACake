#TODO:
#Implement error handling


import cocos

class GfiPackage:
    def __init__(self,screen,spritePath):
        #Contains all sprites to be presented (string of the path, not on actual cocos sprite object)
        self.screen = screen
        self.sprites = spritePath
        
        #The screen that the sprites will be shown on
       
        
        
        
class GfiFreight:
    #This is just a container for a list of GfiPackages
    def __init__(self,packages):
        self.gfi_packages = [package for package in packages]   
        self.screen = self.gfi_packages[-1].screen
        
        