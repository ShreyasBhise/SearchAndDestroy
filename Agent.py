from Environment import Grid
from Cell import Cell
from pprint import pprint
from random import randint
class agent:

    #Travel to the cell with the highest belief that the target is in the 
    def basic_agent1(self, grid):
        return True


    def move(self, new_x, new_y):
        self.environment.field[self.agent_x][self.agent_y].curr_agent = False
        self.agent_x = new_x
        self.agent_y = new_y
        self.environment.field[self.agent_x][self.agent_y].curr_agent = True
        self.time += 1

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
            for j in range(self.dim):
                self.belief[i].append(1/(self.environment.dim ** 2))
    
        pprint(self.environment.field)
        pprint(self.belief)