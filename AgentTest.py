from Agent import agent
from Environment import Grid
from Cell import Cell
from time import time
score1 = []
score2 = []

flat1 = []
hill1 = []
forest1 = []
cave1= []

flat2 = []
hill2 = []
forest2 = []
cave2= []

<<<<<<< Updated upstream
outer_loop = 15
inner_loop = 30
start = time()
for i in range(outer_loop):
    env = Grid(50)
=======
outer_loop = 10
inner_loop = 10
start = time()
for i in range(outer_loop):
    env = Grid(20)
>>>>>>> Stashed changes
    sum1 = 0
    sum2 = 0
    print(i)
    for j in range(inner_loop):
        agent1 = agent(env)
        agent2 = agent(env)
        temp1 = None
        temp2 = None
        while temp1 == None:
            temp1 = agent1.basic_agent(2)
        
        while temp2 == None:
            temp2 = agent2.advanced_agent(2)
        
        sum1 += temp1
        sum2 += temp2

    score1.append(sum1/inner_loop)
    score2.append(sum2/inner_loop)
    if env.field[env.target[0]][env.target[1]].terrain_type == 0.1:
        flat1.append(sum1/inner_loop)
        flat2.append(sum2/inner_loop)
    elif env.field[env.target[0]][env.target[1]].terrain_type == 0.3:
        hill1.append(sum1/inner_loop)
        hill2.append(sum2/inner_loop)
    elif env.field[env.target[0]][env.target[1]].terrain_type == 0.7:
        forest1.append(sum1/inner_loop)
        forest2.append(sum2/inner_loop)
    elif env.field[env.target[0]][env.target[1]].terrain_type == 0.9:
        cave1.append(sum1/inner_loop)
        cave2.append(sum2/inner_loop)

    env.set_target()

a1 = 'Agent 1: '
a2 = 'Agent 2: '
total_time_secs = time() - start
total_time_mins = total_time_secs / 60
average_solve_time = total_time_secs / (inner_loop * outer_loop)
print('Total time: ' + str(total_time_mins), end=' ')
print('Average solve time: ' + str(average_solve_time))

print('______TOTAL______')
print(a1 + str(sum(score1)/len(score1)))
print(a2 + str(sum(score2)/len(score2)))

print('______FLAT_______')
print(a1 + str(sum(flat1)/len(flat1)))
print(a2 + str(sum(flat2)/len(flat2)))

print('______HILL_______')
print(a1 + str(sum(hill1)/len(hill1)))
print(a2 + str(sum(hill2)/len(hill2)))

print('______FOREST_______')
print(a1 + str(sum(forest1)/len(forest1)))
print(a2 + str(sum(forest2)/len(forest2)))

print('______CAVE_______')
print(a1 + str(sum(cave1)/len(cave1)))
print(a2 + str(sum(cave2)/len(cave2)))