import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

            ### 9.1.3. Ticks, Labels, and Legends ###

"""
Most of plot decorations can be accessed through methods on matplotlib axes objects.
It includes 'xlim', 'xticks', and 'xticklabels'.
There're two ways to adjust these options.

1. Called with no arguements returns the current parameter value.
i.e. ax.xlim() returns the current x-axis plotting range.
2. Called with parameters sets the parameter value.
i.e. ax.xlim([0, 10]) sets the x-axis range to 0 to 10.
"""

fig, ax = plt.subplots()
ax.plot(np.random.standard_normal(1000).cumsum())
# plt.show()

"""
Let's change the x-axis ticks of the over example.
Let I use 'set_xticks', and 'set_xticklabels'
Addtionally, 'rotation' option sets 
"""
ticks = ax.set_xticks([0, 250, 500, 750, 1000])
labels = ax.set_xticklabels(['one', 'two', 'three', 'four', 'five'],
                            rotation = 30, fontsize = 8)
plt.show()
