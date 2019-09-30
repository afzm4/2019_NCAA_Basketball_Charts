# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 17:19:21 2019

@author: Andrew
"""
import matplotlib.pyplot as plt
import pandas as pd
from math import pi

team1 = 'Syracuse'
team2 = 'Baylor'
color1 = 'orange'
color2 = 'darkgreen'

df = pd.DataFrame({
        'group': [team1, team2],
        'S': [8.3, 6.1],
        'PD': [4, 4.5],
        'FG%D': [2.7, 1.8],
        'RM': [0, 6.3],
        'TM': [3.2, 0]
})

categories=list(df)[1:]
N = len(categories)

angles = [n / float(N) * 2 * pi for n in range(N)]
angles += angles[:1]

ax = plt.subplot(111, polar=True)

ax.set_theta_offset(pi / 2)
ax.set_theta_direction(-1)

plt.xticks(angles[:-1], categories)
 
# Draw ylabels
ax.set_rlabel_position(0)
plt.yticks([3.5,7], ["3.5","7"], color="grey", size=7)
plt.ylim(0,10)

values=df.loc[0].drop('group').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label=team1, color=color1)
ax.fill(angles, values, 'b', alpha=0.1, color=color1)

values=df.loc[1].drop('group').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label=team2, color=color2)
ax.fill(angles, values, 'r', alpha=0.1, color=color2)
 
# Add legend
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

plt.savefig('syracuse_baylor.png')