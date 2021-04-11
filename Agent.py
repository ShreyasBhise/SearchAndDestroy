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

    def advanced_agent(self, search_type):
        found = self.search(self.agent_x, self.agent_y)
        if found:
            return self.get_score()
        
        self.update_belief()
        if self.optimal_cell is None: 
            self.optimal_cell = self.find_max_belief(search_type)
        if(self.optimal_cell.x==self.agent_x and self.optimal_cell.y==self.agent_y): # best move is to stay in place
            self.optimal_cell = None
            return None
        to_move = self.best_path_move(self.optimal_cell)
        if to_move[0] != self.agent_x or to_move[1] != self.agent_y:
            self.move(to_move[0], to_move[1])
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

        
        for i in range(self.dim):
            for j in range(self.dim):
                if (i,j) == (x,y):
                    continue
                self.belief[i][j] /= pfail

      

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
        self.optimal_cell = None
        
        self.environment.field[self.agent_x][self.agent_y].curr_agent = True

        self.belief = list()
        for i in range(self.dim):
            self.belief.append(list())
            for _ in range(self.dim):
                self.belief[i].append(1/(self.environment.dim ** 2))

        

    def best_path_move(self, optimal_cell):
        x1 = self.agent_x
        y1 = self.agent_y
        x2 = optimal_cell.x
        y2 = optimal_cell.y
        switched = False
        if(x1>x2): # reduce to 2 dp cases, so x1 is always to the right of x2
            switched = True
            temp = x2
            x2 = x1
            x1 = temp
            temp = y2
            y2 = y1
            y1 = temp
        
        dp = list()
        prev = list()

        if y1>y2: # calculating path from top left to bottom right
            for i in range(0, x2-x1+1):
                dp.append(list())
                prev.append(list())
                for j in range(0, y1-y2+1):
                    dp[i].append(0)
                    prev[i].append((0, 0))
                    if(i==0 and j==0): # base case
                        dp[i][j]=self.belief[x1][y1]
                        prev[i][j]=(-1, -1)
                    elif(i==0):
                        dp[i][j]=dp[i][j-1]+self.belief[x1][y1-j]
                        prev[i][j]=(i, j-1)
                    elif(j==0):
                        dp[i][j]=dp[i-1][j]+self.belief[x1+i][y1]
                        prev[i][j]=(i-1, j)
                    else:
                        if(dp[i-1][j]>dp[i][j-1]):
                            dp[i][j]=dp[i-1][j]+self.belief[x1+i][y1-j]
                            prev[i][j]=(i-1, j)
                        else:
                            dp[i][j]=dp[i][j-1]+self.belief[x1+i][y1-j]
                            prev[i][j]=(i, j-1)
                    if(i==x2-x1 and j==y1-y2):
                        if switched:
                            return (x1+prev[i][j][0], y1-prev[i][j][1])
                        else:
                            curr = (i, j)
                            parent = prev[i][j]
                            while parent[0]!=0 or parent[1]!=0:
                                curr = parent
                                parent = prev[curr[0]][curr[1]]
                            return (x1+curr[0], y1-curr[1])

        else: # calculating path from bottom left to top right
            for i in range(0, x2-x1+1):
                dp.append(list())
                prev.append(list())
                for j in range(0, y2-y1+1):
                    dp[i].append(0)
                    prev[i].append((0, 0))
                    if(i==0 and j==0): # base case
                        dp[i][j]=self.belief[x1][y1]
                        prev[i][j]=(-1, -1)
                    elif(i==0):
                        dp[i][j]=dp[i][j-1]+self.belief[x1][y1+j]
                        prev[i][j]=(i, j-1)
                    elif(j==0):
                        dp[i][j]=dp[i-1][j]+self.belief[x1+i][y1]
                        prev[i][j]=(i-1, j)
                    else:
                        if(dp[i-1][j]>dp[i][j-1]):
                            dp[i][j]=dp[i-1][j]+self.belief[x1+i][y1+j]
                            prev[i][j]=(i-1, j)
                        else:
                            dp[i][j]=dp[i][j-1]+self.belief[x1+i][y1+j]
                            prev[i][j]=(i, j-1)
                    if(i==x2-x1 and j==y2-y1):
                        if switched:
                            return (x1+prev[i][j][0], y1+prev[i][j][1])
                        else:
                            curr = (i, j)
                            parent = prev[i][j]
                            while parent[0]!=0 or parent[1]!=0:
                                curr = parent
                                parent = prev[curr[0]][curr[1]]
                            return (x1+curr[0], y1+curr[1])
