from Environment import Grid
from Cell import Cell
from pprint import pprint
from random import randint
class agent:

    #Travel to the cell with the highest belief that the target is in the 
    def basic_agent1(self):
        found = self.search(self.agent_x, self.agent_y)
        if found:
            return self.get_score()
        
        self.update_belief()
        to_move = self.find_max_belief(self.belief[self.agent_x][self.agent_y])
        if to_move.x != self.agent_x or to_move.y != self.agent_y:
            self.move(to_move.x, to_move.y)
        
    def find_max_belief(self, curr_max):
        max_cells = [self.environment.field[self.agent_x][self.agent_y]]
        max_belief = curr_max

        for i in range(self.dim):
            for j in range(self.dim):
                if i == self.agent_x and j == self.agent_y or self.belief[i][j] < max_belief: 
                    continue
                if self.belief[i][j] > max_belief:
                    max_belief = self.belief[i][j]
                    max_cells.clear()
                max_cells.append(self.environment.field[i][j])
        
        return max_cells[randint(0, len(max_cells) - 1)]

                

    def update_belief(self):
        (x, y) = (self.agent_x, self.agent_y)
        self.belief[x][y] = self.belief[x][y] * self.environment.field[x][y].terrain_type
        new_list = [(f'{num:.1f}' for num in lst) for lst in self.belief]
        print(new_list)

    def calculate_dist(self, old, new):
        return abs(old[1] - new[1]) + abs(old[0]-new[0])

    def move(self, new_x, new_y):
        cost = self.calculate_dist((self.agent_x, self.agent_y), (new_x, new_y))
        self.environment.field[self.agent_x][self.agent_y].curr_agent = False
        self.agent_x = new_x
        self.agent_y = new_y
        self.environment.field[self.agent_x][self.agent_y].curr_agent = True
        self.time += cost

    def search(self, s_x, s_y):
        self.time += 1
        return self.environment.query_cell(s_x, s_y)

    
    def get_score(self):
        return self.time
    def __init__(self, env):
        self.environment = env
        self.dim = env.dim
        self.time = 0
        self.agent_x = randint(0, self.dim - 1)
        self.agent_y = randint(0, self.dim - 1)
        
        self.environment.field[self.agent_x][self.agent_y].curr_agent = True

        self.belief = list()
        for i in range(self.dim):
            self.belief.append(list())
            for _ in range(self.dim):
                self.belief[i].append(1/(self.environment.dim ** 2))
