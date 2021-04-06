from random import random
class Cell:
    
    def __init__(self, x, y, p):
        self.x = x
        self.y = y
        if p < 0.25:
            self.terrain_type = 0.1 #FLAT
        elif p < 0.5:
            self.terrain_type = 0.3 #HILL
        elif p < 0.75:
            self.terrain_type = 0.7 #FOREST
        else:
            self.terrain_type = 0.9 #CAVE
        self.is_target = False
        self.curr_agent = False
        self.searched = False

    def set_terrain(self, terrain):
        self.terrain_type = terrain

    def set_target(self):
        self.is_target = True

    def search_cell(self):
        self.searched = True
        if not self.is_target:
            return False
        return random() > self.terrain_type
    
    
    def __repr__(self):
       return '{self.terrain_type} {self.is_target}'.format(self=self)