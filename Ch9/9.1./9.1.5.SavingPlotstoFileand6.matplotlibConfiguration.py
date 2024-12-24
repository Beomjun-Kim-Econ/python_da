import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

            ### 9.1.5. Saving Plots to File ###

"""
We learned to make some figures so far.
We can save those figures using 'savefig', which is the figure object. Like...
fig.savefig('figpath.svg') * svg: sort of vector image file
and also I can opt its dpi like...
fig.savefig('figpath.png', dpi = 400)
"""
fig, ax = plt.subplots()
rect = plt.Rectangle((0.2, 0.75), 0.4, 0.15, color = 'black', alpha =0.3)
circ = plt.Circle((0.7, 0.2), 0.15, color = 'blue', alpha =0.3)
pgon = plt.Polygon([[0.15, 0.15], [0.35, 0.4], [0.2, 0.6]],
                   color = 'green', alpha = 0.5)
ax.add_patch(rect)
ax.add_patch(circ)
ax.add_patch(pgon)
# fig.savefig('/Users/beomjunkim/Programming/hello.png', dpi = 400)



            ### 9.1.6. matplotlib Configuration ###
"""
matplotlib comes configured with color schemes and defaults that are geared 
primarily toward preparing figures for publication.
And I can customize via global parameters, 
which can govern figure size, subplot spacing, font size, colour, and so on.
I can adjust these setting through '.rc', like...
plt.rc('figure', figsize = (10, 10)) (runtime configuration)
the above code set the figure size as (10, 10)
All of the current configuration settings are found in the 'plt.reParams'
"""



