import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

            ### 9.2.1. Line Plots ###

"""
matplotlib can be a fairly low-level tool. I need to set from the low-level components 
like data display, legend, title, tick label, and other annotations.

In pandas, we may have multiple columns of data, along with row and column labels.
pandas itself has built-in methods that simplify creating visualizations 
from DataFrame, and Series objects.
But there is another library, 'seaborn', 
which is high-level statistical graphics library built on matplotlib.
seaborn implifyes creating many common visualization types.
"""

# Line Plots
"""
We can draw line plots based on Series and DataFrame.
By default, '.plot()'  makes line plots. 
"""
s = pd.Series(np.random.standard_normal(10).cumsum(),
              index = np.arange(0, 100, 10))
# index is passed to be its x-axis.
# I can also disable it by passing use_index = False
s.plot()
plt.show()

"""
I can also adjust 'ax' parameter to placement of subplots in a grid layout.
DataFrame's 'plot' method plots each of its columns as a different line on the same subplot,
creating legend automatically.
"""
df = pd.DataFrame(np.random.standard_normal((10, 4)).cumsum(0),
                  columns = ["A", "B", "C", "D"],
                  index = np.arange(0 , 100, 10))
plt.style.use('grayscale')
df.plot()
plt.show()