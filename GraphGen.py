import matplotlib.pyplot as plt
import numpy as np



labels = ['Flat', 'Hill', 'Forest', 'Cave']

basic1 = [20563.056, 35945.786, 54992.200, 65010.433]
basic2 = [7972.722, 10032.586, 33474.417, 118707.900]
advanced = [1761.622, 4666.090, 13468.517, 26291.100]


x = np.arange(len(labels))
width = 0.2
fig, ax = plt.subplots()
rects1 = ax.bar(x-width, basic1, width, label='Basic Agent 1')
rects3 = ax.bar(x, basic2, width, label='Basic Agent 2')
rects2 = ax.bar(x+width, advanced, width, label='Advanced Agent')

ax.set_ylabel('Average Score')
ax.set_title('Scores over Various Terrains, num_tests = 450')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

ax.bar_label(rects1, padding=3)
ax.bar_label(rects2, padding=3)
ax.bar_label(rects3, padding=3)

fig.tight_layout()

plt.show()

