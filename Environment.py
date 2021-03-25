from Cell import Cell
import random as rnd

class Grid:
    def set_terrain(self):
        cts = [0, 0, 0, 0]
        for i in range(self.dim):
            for j in range(self.dim):
                terrain = rnd.random()

                if terrain < 0.25:
                    self.field[i][j].set_terrain('flat')
                    cts[0] += 1
                elif terrain < 0.5:
                    self.field[i][j].set_terrain('hill')
                    cts[1] += 1
                elif terrain < 0.75:
                    self.field[i][j].set_terrain('forest')
                    cts[2] += 1
                else:
                    self.field[i][j].set_terrain('cave')
                    cts[3] += 1
        print(cts, str(cts[0] + cts[1] + cts[2] + cts[3]))
    def set_target(self):
        rand_x = rnd.randint(0, self.dim - 1)
        rand_y = rnd.randint(0, self.dim - 1)

        self.field[rand_x][rand_y].set_target()


    def print_field(self):
        for i in range(self.dim):
            for j in range(self.dim):
                print(self.field[i][j])
    def __init__(self, dim):
        self.dim = dim
        
        self.field = list()
        for i in range(dim):
            self.field.append(list())
            for j in range(dim):
                self.field[i].append(Cell(i, j))

        self.set_terrain()
        self.set_target()
        #self.print_field()