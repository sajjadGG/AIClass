"""
@author sajjadGG
this code is used to work with 8 puzzle

"""
import random

SIZE = 9
ROW = int(SIZE**0.5)
class Tile:

    def __init__(self , rep , pos=None):
        self.rep = rep #representation
        if pos == None:
            pos = (rep/ROW , rep%ROW)
        else:
            self.pos = (pos/ROW , pos%ROW)
        self.pos = pos

    def represent(self):
        """return a representation"""
        return self.rep

    def __str__(self):
        return str(self.rep)

def generate_tiles(l):
    return [Tile(e , i) for i,e in enumerate(l)]

def random_world():
    world = generate_tiles(random.sample(list(range(SIZE)),SIZE)) # zero represent empty tile
    return world
        


def show_game(world):
    """world is array of tiles"""
    for i ,t in enumerate(world):
        if(i%3==0):
            print()
        print(" {} ".format(t) , end="")
    

show_game(random_world())    
