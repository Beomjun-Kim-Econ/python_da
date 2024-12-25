import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

            ### 9.2.4. Scatter or Point Plots ###
"""
Scatter plots are useful to examining the relationship between tweo one-dim data series.
let's see the 'macrodata' example.
"""
macro = pd.read_csv('/Users/beomjunkim/Programming/python_da_datas/examples/macrodata.csv')
print(macro.head())
data = macro[['cpi', 'm1', 'tbilrate', 'unemp']]
trans_data = np.log(data).diff().dropna()
print(trans_data.tail())

"""
We use seborn's 'regplot'(regressioin plot) method, 
which makes a scatter plot and fits a linear regressioin line.
"""
ax = sns.regplot(x = 'm1', y = 'unemp', data = trans_data)
ax.set_title('change in log(m1) versus log(unemp)')
plt.show()

"""
In exploratory data analysis, to see scatter plot matrix is helpful.
To make each plots is bothering, so we can use 'pairplot' function,
which make scatter plots and density plots.
"""
sns.pairplot(trans_data, diag_kind = 'kde', plot_kws={'alpha': 0.2})