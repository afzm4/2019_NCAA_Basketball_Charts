# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 16:43:58 2019

@author: Andrew
"""

import matplotlib.pyplot as plt
import pandas as pd
from math import pi

df = pd.DataFrame({
        'group': ['UNC', 'Iona'],
        'S': [7.2, 6.8],
        'PD': [13.2, 1.2],
        'FG%D': [5.1, 0.8],
        'RM': [9.7, 0],
        'TM': [1.1, 0.9]
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
plt.yticks([5,10], ["5","10"], color="grey", size=7)
plt.ylim(0,15)

values=df.loc[0].drop('group').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="UNC", color="lightblue")
ax.fill(angles, values, 'b', alpha=0.1, color="lightblue")

values=df.loc[1].drop('group').values.flatten().tolist()
values += values[:1]
ax.plot(angles, values, linewidth=1, linestyle='solid', label="Iona", color="darkred")
ax.fill(angles, values, 'r', alpha=0.1, color="darkred")
 
# Add legend
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

plt.savefig('unc_iona.png')
