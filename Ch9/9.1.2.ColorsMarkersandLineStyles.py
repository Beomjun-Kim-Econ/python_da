import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

            ### 9.1.2. Colors, Markers, and Line Styles ###

"""
"plot" of matplotlib's line accepts arrays of x and y coordinates and optional color styling options.
i.e. to plot x versus y with green dashes, I would execute...
ax.plot(x,y, linestyle = '--', solor = 'green')
matplotlib supports a variety of colours, not only preset colours, but also hex code(#CECECE)
 
Line plots has the feature "markers" to highlight the actual data points.
The original dataset is discrete, but as must be continuous, 
and matplotlib intellectually draw a apt line. so sometimes the markers are needed.   
"""
fig = plt.figure()
ax = fig.add_subplot()
ax.plot(np.random.standard_normal(30).cumsum(), color = 'black',
        linestyle = 'dashed', marker = 'o')
plt.show()

"""
I can make steps-post line also.
"""
fig = plt.figure()
ax = fig.add_subplot()
data = np.random.standard_normal(30).cumsum()
ax.plot(data, color = 'black', linestyle='dashed', label = 'hi')
ax.plot(data, color = 'black', drawstyle = 'steps-post', label = 'hello')
ax.legend()     # legend: '범례'
plt.show()