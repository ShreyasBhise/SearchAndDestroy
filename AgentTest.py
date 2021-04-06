from Agent import agent
from Environment import Grid
from Cell import Cell

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

for i in range(10):
    env = Grid(10)
    sum1 = 0
    sum2 = 0
    print(i)
    for j in range(10):
        agent1 = agent(env)
        agent2 = agent(env)
        temp1 = None
        temp2 = None
        while temp1 == None:
            temp1 = agent1.basic_agent(1)
        
        while temp2 == None:
            temp2 = agent2.basic_agent(2)
        
        sum1 += temp1
        sum2 += temp2
        
    score1.append(sum1/10)
    score2.append(sum2/10)
    if env.field[env.target[0]][env.target[1]].terrain_type == 0.1:
        flat1.append(sum1/10)
        flat2.append(sum2/10)
    elif env.field[env.target[0]][env.target[1]].terrain_type == 0.3:
        hill1.append(sum1/10)
        hill2.append(sum2/10)
    elif env.field[env.target[0]][env.target[1]].terrain_type == 0.7:
        forest1.append(sum1/10)
        forest2.append(sum2/10)
    elif env.field[env.target[0]][env.target[1]].terrain_type == 0.9:
        cave1.append(sum1/10)
        cave2.append(sum2/10)

    env.set_target()

print(score1)
print(score2)
print("FLAT")
print(flat1,flat2)
print("HILL")
print(hill1,hill2)
print("FOREST")
print(forest1, forest2)
print("CAVE")
print(cave1, cave2)
