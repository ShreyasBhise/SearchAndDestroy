from Environment import Grid
from Cell import Cell
from pprint import pprint
from random import randint
class agent:

    #Travel to the cell with the highest belief that the target is in the 
    def basic_agent(self, search_type):
        found = self.search(self.agent_x, self.agent_y)
        if found:
            return self.get_score()
        
        self.update_belief()
        to_move = self.find_max_belief(search_type)
        if to_move.x != self.agent_x or to_move.y != self.agent_y:
            self.move(to_move.x, to_move.y)
        return None
        
    def find_max_belief(self, search_type):

        max_cells = list() # A list of all cells with maximal belief and then minimal distance from agent.
        max_belief = self.belief[self.agent_x][self.agent_y]  # Current maximum belief
        if search_type == 2:
            max_belief *= (1 - self.environment.field[self.agent_x][self.agent_y].terrain_type)
        min_dist = 0 # Current minimum distance

        if search_type == 1: #Basic agent 1
            for i in range(self.dim):
                for j in range(self.dim):
                    if self.belief[i][j] < max_belief: #This cell is worse than the best cell, skip it
                        continue
                    if self.belief[i][j] > max_belief:  # This cell has a higher belief than the previous max so make it the only entry in the list.
                        max_cells.clear()
                        max_belief = self.belief[i][j]
                        min_dist = self.calculate_dist((self.agent_x, self.agent_y), (i, j))
                        max_cells.append(self.environment.field[i][j])
                    
                    else: # Equal belief
                        dist = self.calculate_dist((self.agent_x, self.agent_y), (i, j)) 
                        if dist < min_dist: # Less distance to agent, make it the only element in list
                            max_cells.clear()
                            min_dist = dist
                            max_cells.append(self.environment.field[i][j])

                        elif dist == min_dist: # Equal distance as the rest, append to list
                            max_cells.append(self.environment.field[i][j])
        else: #Basic Agent 2
            for i in range(self.dim):
                for j in range(self.dim):
                    curr_confidence = self.belief[i][j] * (1 - self.environment.field[i][j].terrain_type)
                    if curr_confidence < max_belief:
                        continue
                    if curr_confidence > max_belief:
                        max_cells.clear()
                        max_belief = curr_confidence
                        min_dist = self.calculate_dist((self.agent_x, self.agent_y), (i, j))
                        max_cells.append(self.environment.field[i][j])
                    else:
                        dist = self.calculate_dist((self.agent_x, self.agent_y), (i, j)) 
                        if dist < min_dist: # Less distance to agent, make it the only element in list
                            max_cells.clear()
                            min_dist = dist
                            max_cells.append(self.environment.field[i][j])

                        elif dist == min_dist: # Equal distance as the rest, append to list
                            max_cells.append(self.environment.field[i][j])

        return max_cells[randint(0, len(max_cells) - 1)]

    def update_belief(self):
        (x, y) = (self.agent_x, self.agent_y)
        target_in_cell = self.belief[x][y]
        target_failed = self.environment.field[x][y].terrain_type
        
        self.belief[x][y] = (target_in_cell*target_failed)/((target_in_cell*target_failed) + (1-target_in_cell))
        pfail = (target_in_cell*target_failed) + (1-target_in_cell)

        # total_belief = self.belief[x][y]
        for i in range(self.dim):
            for j in range(self.dim):
                if (i,j) == (x,y):
                    continue
                self.belief[i][j] /= pfail
                # total_belief += self.belief[i][j]

        # print(total_belief)
        # print(self.belief)
        # new_list = [(f'{num:.1f}' for num in lst) for lst in self.belief]
        # print(new_list)

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

        # print(self.environment.field)
        # print(self.belief)
