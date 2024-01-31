import random
import numpy as np

class Item:
    def __init__(self):
        self.Name = ''
        self.Rarity = ''

class Inventory:
    def __init__(self):
        self.edge_length_ = 5
        self.cube_layers_ = ['Item','Occlusion','Link']
        self.dynamics_ = {'Submissive':0,'Dominant':1,'Vanilla':2}
        self.id_interval_ = 10

        self.ids = {'Occlusion':{i*self.id_interval_ for i in range(1,100)},
                    'Link':{i*self.id_interval_ for i in range(1,100)}}
        self.cubes = {}
        self.cubes['Item'] = np.full((5,5,5),None,dtype=object)
        for key in self.cube_layers_:
            if key != 'Item':
                self.cubes[key] = np.zeros((5,5,5),dtype=int)

    def CheckRelationByItem(self,specItem):
        #Check to see if the item has any related behavior to other items
        icor = self.GetItemCoordinate(specItem)
        return self.CheckRelationByCoordinate(icor)

    def CheckRelationByCoordinate(self,coor):
        #Check to see if the item at a coordinate has any related behavior to other items
        for key in self.cubes:
            if key != 'Item':
                if self.cubes[key][coor] != 0:
                    return True
        return False
    
    def FlashLayer(self,per,lay,dyn = ('Submissive','Dominant')):
        #Randomly assigns relations between objects.

        #Per: chance of any item being changed (<1)
        #Lay: relationship layer
        #Dyn: dynamic between the two items

        for i in range(self.edge_length_**3):
            p = random.random()
            if p <= per:
                coorA = self.GenerateRandomCoordinateNoRelation()
                coorB = self.GenerateRandomCoordinateNoRelation()
                while coorB == coorA:
                    coorB = self.GenerateRandomCoordinateNoRelation()
                self.RomanceByCoordinate(coorA,coorB,lay,dyn)

    def GenerateRandomCoordinate(self):
        #Picks a random, valid item coordinate.
        return (random.randint(0,self.edge_length_-1),
                random.randint(0,self.edge_length_-1),
                random.randint(0,self.edge_length_-1))

    def GenerateRandomCoordinateNoRelation(self):
        #Picks a random coordinate where the item stored at said coordinate has no relations.
        rCor = self.GenerateRandomCoordinate()
        while self.CheckRelationByCoordinate(rCor) == True:
            rCor = self.GenerateRandomCoordinate()
        return rCor

    def GetItemCoordinate(self,specItem):
        #Gets the coordinate of a passed item.
        for i in range(self.edge_length_):
            for ii in range(self.edge_length_):
                for iii in range(self.edge_length_):
                    if self.cubes['Item'][i][ii][iii] == specItem:
                        return (i,ii,iii)
        return (None,None,None)
    
    def RomanceByItem(self,specItemA,specItemB,lay='Occlusion',dyn=('Submissive','Dominant')):
        #Establishes a relationship between two passed items.
        icorA = self.GetItemCoordinate(specItemA)
        icorB = self.GetItemCoordinate(specItemB)
        self.RomanceByCoordinate(icorA,icorB,lay,dyn)

    def RomanceByCoordinate(self,coorA,coorB,lay,dyn=('Submissive','Dominant')):
        #Establishes a relatinship between items stored at two passed coordinates.
        if self.CheckRelationByCoordinate(coorA) == False and self.CheckRelationByCoordinate(coorB) == False:
            self.cubes[lay][coorA] = self.ids[lay].pop()
            self.cubes[lay][coorB] = self.cubes[lay][coorA] + self.dynamics_[dyn[1]]
            self.cubes[lay][coorA] += self.dynamics_[dyn[0]]

    def DivorceByItem(self,specItemA,specItemB,lay):
        #Removes the relationship between two items.
        icorA = self.GetItemCoordinate(specItemA)
        icorB = self.GetItemCoordinate(specItemB)
        self.DivorceByCoordinate(icorA,icorB,lay)

    def DivorceByCoordinate(self,coorA,coorB,lay):
        #Removes the relationship between two items stored at passed coordinates.
        if self.CheckRelationByCoordinate(coorA) and self.CheckRelationByCoordinate(coorB):
            self.cubes[lay][coorA] -= self.cubes[lay][coorA] % self.id_interval_
            self.ids[lay].add(self.cubes[lay][coorA])
            self.cubes[lay][coorA] = 0
            self.cubes[lay][coorB] = 0
    

    

