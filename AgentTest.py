from Agent import agent
from Environment import Grid
from Cell import Cell
from time import time
score = [[],[],[]]

flat = [[],[],[]]
hill = [[],[],[]]
frst = [[],[],[]]
cave = [[],[],[]]


outer_loop = 15
inner_loop = 30
start = time()
for i in range(outer_loop):
    env = Grid(50)
    sum1 = 0
    sum2 = 0
    sum3 = 0
    print(i)
    for j in range(inner_loop):
        agent1 = agent(env)
        agent2 = agent(env)
        agent3 = agent(env)

        temp1 = None
        temp2 = None
        temp3 = None

        while temp1 == None:
            temp1 = agent1.basic_agent(1)
        
        while temp2 == None:
            temp2 = agent2.basic_agent(2)
        
        while temp3 == None:
            temp3 = agent3.advanced_agent(2)

        sum1 += temp1
        sum2 += temp2
        sum3 += temp3

    score[0].append(sum1/inner_loop)
    score[1].append(sum2/inner_loop)
    score[2].append(sum3/inner_loop)

    if env.field[env.target[0]][env.target[1]].terrain_type == 0.1:
        flat[0].append(sum1/inner_loop)
        flat[1].append(sum2/inner_loop)
        flat[2].append(sum3/inner_loop)

    elif env.field[env.target[0]][env.target[1]].terrain_type == 0.3:
        hill[0].append(sum1/inner_loop)
        hill[1].append(sum2/inner_loop)
        hill[2].append(sum3/inner_loop)

    elif env.field[env.target[0]][env.target[1]].terrain_type == 0.7:
        frst[0].append(sum1/inner_loop)
        frst[1].append(sum2/inner_loop)
        frst[2].append(sum3/inner_loop)

    elif env.field[env.target[0]][env.target[1]].terrain_type == 0.9:
        cave[0].append(sum1/inner_loop)
        cave[1].append(sum2/inner_loop)
        cave[2].append(sum3/inner_loop)

    env.set_target()

a1 = 'Basic Agent 1:  '
a2 = 'Basic Agent 2:  '
a3 = 'Advanced Agent: '

total_time_secs = time() - start
total_time_mins = total_time_secs / 60
average_solve_time = total_time_secs / (inner_loop * outer_loop) /3

print('Total time: {s:.4f} mins'.format(s=total_time_mins))
print('Average solve time: {s:.4f}s'.format(s=average_solve_time))

print('______TOTAL______')
print(a1 + '{s:.3f}'.format(s=sum(score[0])/len(score[0])))
print(a2 + '{s:.3f}'.format(s=sum(score[1])/len(score[1])))
print(a3 + '{s:.3f}'.format(s=sum(score[2])/len(score[2])))

if len(flat[0]) == 0:
    print('FLAT not found')
else:
    print('______FLAT_______')
    print(a1 + '{s:.3f}'.format(s=sum(flat[0])/len(flat[0])))
    print(a2 + '{s:.3f}'.format(s=sum(flat[1])/len(flat[1])))
    print(a3 + '{s:.3f}'.format(s=sum(flat[2])/len(flat[2])))

if len(hill[0]) == 0:
    print('HILL not found')
else:
    print('______HILL_______')
    print(a1 + '{s:.3f}'.format(s=sum(hill[0])/len(hill[0])))
    print(a2 + '{s:.3f}'.format(s=sum(hill[1])/len(hill[1])))
    print(a3 + '{s:.3f}'.format(s=sum(hill[2])/len(hill[2])))

if len(frst[0]) == 0:
    print('FOREST not found')
else:
    print('______FOREST_______')
    print(a1 + '{s:.3f}'.format(s=sum(frst[0])/len(frst[0])))
    print(a2 + '{s:.3f}'.format(s=sum(frst[1])/len(frst[1])))
    print(a3 + '{s:.3f}'.format(s=sum(frst[2])/len(frst[2])))

if len(cave[0]) == 0:
    print('CAVE not found')
else:
    print('______CAVE_______')
    print(a1 + '{s:.3f}'.format(s=sum(cave[0])/len(cave[0])))
    print(a2 + '{s:.3f}'.format(s=sum(cave[1])/len(cave[1])))
    print(a3 + '{s:.3f}'.format(s=sum(cave[2])/len(cave[2])))