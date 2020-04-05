from blackmaria import *
from blackmariaplayers import *

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

scores = []
for m in range(0,1000):
    players = [RandomPlayer(0), RandomPlayer(1), RandomPlayer(2), RandomPlayer(3)]
    table = Table(players)
    table.play_match()
    scores.append(table.get_scores())

print("mean score: " + str(np.mean(scores)))
print("std score: " + str(np.std(scores)))

sns.distplot(scores)
plt.show()
