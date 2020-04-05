from blackmaria import *
from blackmariaplayers import *

import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

scores = []
for m in range(0,1000):
    players = [DuckAndDumpAgressive(0), RandomPlayer(1), RandomPlayer(2), RandomPlayer(3)]
    table = Table(players)
    table.play_match()
    scores.append(table.get_scores())

player0scores = []
player1scores = []
player2scores = []
player3scores = []

for i in scores:
    player0scores.append(i[0])
    player1scores.append(i[1])
    player2scores.append(i[2])
    player3scores.append(i[3])

#print("mean score: " + str(np.mean(scores)))
#print("std score: " + str(np.std(scores)))

fig, axs = plt.subplots(ncols=4)

sns.distplot(player0scores, ax=axs[0])
sns.distplot(player1scores, ax=axs[1])
sns.distplot(player2scores, ax=axs[2])
sns.distplot(player3scores, ax=axs[3])

plt.show()
