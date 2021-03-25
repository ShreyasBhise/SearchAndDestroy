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

        neighbors = ((-1, 0), (1, 0), (0, -1), (0,1))
        max_belief = 0
        max_cells = list()
        for nb in neighbors:
            tx = self.agent_x + nb[0]
            ty = self.agent_y + nb[1]
            if tx < 0 or ty < 0 or tx >= self.dim or ty >= self.dim:
                continue
            to_check = self.environment.field[tx][ty]
            if self.belief[to_check.x][to_check.y] > max_belief:
                max_belief = self.belief[to_check.x][to_check.y]
                max_cells.clear()
                max_cells.append(to_check)
            elif self.belief[to_check.x][to_check.y]  == max_belief:
                max_cells.append(to_check)
            print(max_cells)
        choice = randint(0, len(max_cells) - 1)
        to_move = max_cells[choice]
        self.move(to_move.x, to_move.y)

    def update_belief(self):
        #TODO: actually update the belief
        pass
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
            for _ in range(self.dim):
                self.belief[i].append(1/(self.environment.dim ** 2))
    
        pprint(self.environment.field)
        pprint(self.belief)