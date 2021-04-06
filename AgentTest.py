from Agent import agent
from Environment import Grid
from Cell import Cell

score1 = []
score2 = []

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
    env.set_target()

print(score1)
print(score2)
