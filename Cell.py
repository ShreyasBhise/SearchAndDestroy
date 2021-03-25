from random import random
class Cell:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.terrain_type = None
        self.false_negative_rate = 0
        self.prob_dict = {'flat':0.1, 'hill':0.3, 'forest':0.7, 'cave':0.9}
        self.is_target = False
        
    def set_terrain(self, terrain):
        self.terrain_type = terrain
        self.false_negative_rate = self.prob_dict[terrain]

    def set_target(self):
        self.is_target = True
        print('target is :')
        print(self.__repr__())

    def get_target(self):
        if not self.is_target:
            return False
        return random() > self.false_negative_rate
    def __repr__(self):
        return '({self.x}, {self.y}) is {self.terrain_type}'.format(self=self)