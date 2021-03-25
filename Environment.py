from Cell import Cell
from random import randint, random
import random as rnd, pprint

class Grid:
    
    def set_target(self):
        rand_x = randint(0, self.dim - 1)
        rand_y = randint(0, self.dim - 1)

        self.field[rand_x][rand_y].set_target()

    def print_field(self):
        for i in range(self.dim):
            for j in range(self.dim):
                print(self.field[i][j], end=' ')
            print()

    def query_cell(self, row, col):
        return self.field[row][col].search_cell()
        
    def __init__(self, dim):
        self.dim = dim

        self.field = list()
        for i in range(dim):
            self.field.append(list())
            for j in range(dim):
                self.field[i].append(Cell(i, j, random()))
        self.set_target()
        self.print_field()