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

"""
Let's add legends by passing the 'label' argument when adding each piece of the plot 
"""
fig, ax = plt.subplots()
ax.plot(np.random.randn(1000).cumsum(), color = 'black', label = 'one')
ax.plot(np.random.randn(1000).cumsum(), color = 'black', linestyle = 'dashed', label = 'two')
ax.plot(np.random.randn(1000).cumsum(), color = 'black', linestyle = 'dotted', label = 'three')
ax.legend()     #adding legend
plt.show()

"""
the 'legend' method(.legend) has several other choices for the location 'loc'(location) arguement.
The 'loc', which is the option for legend, tells matplotlib where to place th plot.
Its default is 'best', which tries to choose a location that is most out of the way.
If I want to exclude some elements, then I can achieve it by passing no label, 
or passing 'label = '_nolegend''.
"""
