import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

            ### 9.1.1. Figures and Subplots ###

"""
Let's start from the scratch
"""
data = np.arange(10)
print(data)
plt.plot(data)
plt.show()

"""
plt.figure() cab set some options for my figures, like the length of x-axis, so on.
i.e. figsize option will set the size and aspect ratio.
And basically I can't make empty figure, but through 'subplot', I can make the empty figures.
"""
fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)

"""
Especially these axis object have various methods to create different types of plots.
And it is preferred to use the axis method over the top-level plotting functions like "plt.plot".
"""
ax3.plot(np.random.standard_normal(50).cumsum(), color = 'black',
         linestyle = 'dashed')
# plt.show()

"""
And the additional options instruct matplotlib to plot a blck dashed line.
The objects returned by "fig.add_subplot" are "AxesSubplt" objects, 
which I can directly plot on the other empty subplots by calling each one's instance method.
at the below, 'bins' sets the # of intervals, and 'alpha' sets the transparency of the overlaid plot.
"""
ax1.hist(np.random.standard_normal(100), bins = 20, color = 'black', alpha = 0.3)
ax2.scatter(np.arange(30), np.arange(30) + 3 * np.random.standard_normal(30))
plt.show()

"""
We can creat a grid of subplots conveniently by use "plt.subplots", 
which create Numpy array containing subplots as components
"""
fig, axes = plt.subplots(2, 3)
print(axes)
plt.show()
# empty 2x3 plots

"""
We can adjust the spacing around subplots,
and this adjustment is relative to the height and width of the full plot.
So if I need to paste the plot to the ppt file or so on, then in fact, I can just take a capture...
Anyway!
"""
fig, axes = plt.subplots(2,2, sharex=True, sharey=True)
for i in range(2) :
    for j in range(2) :
        axes[i, j].hist(np.random.standard_normal(500), bins = 50,
                        color = 'black', alpha = 0.5)
fig.subplots_adjust(wspace = 0, hspace = 0)
plt.show()