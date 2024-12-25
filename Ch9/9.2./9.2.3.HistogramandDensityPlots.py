import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

            ### 9.2.3.Histogram and Density Plots ###
"""
Histogram is a kind of bar plot, which gives a discretized display of value frequency.
Let's make a histogram of tip percentage of the total bill using 'plot.his' method on Series.
"""
tips = pd.read_csv('/Users/beomjunkim/Programming/python_da_datas/examples/tips.csv')
print(tips.head())
party_counts = pd.crosstab(tips['day'], tips['size'])
party_counts = party_counts.reindex(index=['Thur', 'Fri', 'Sat', 'Sun'])
print(party_counts)
party_counts = party_counts.loc[:, 2:5]
print(party_counts)
party_pcts = party_counts.div(party_counts.sum(axis='columns'), axis = 'index')
tips['tip_pct'] = tips['tip'] / (tips['total_bill'] - tips['tip'])

tips['tip_pct'].plot.hist(bins=50)
plt.show()

"""
We also draw density plot, which is a kind of continuous version of hitogram.
The other name of density plot is KDE plots, kernel density estimate plots,
because the procedure from histogram to density plot is called as 'kernel'.
It needs SciPy.
"""
tips['tip_pct'].plot.density()
plt.show()

"""
seaborn makes histogram and density plots even easier through its 'histplot' method,
which can plot both a histogram and a continuous density estimate simultaneously.
Let's see an example making binmodal distribution. (bimodal distribution: 쌍봉분포)
"""
comp1 = np.random.standard_normal(200)
comp2 = 10 + 2 * np.random.standard_normal(200)
values = pd.Series(np.concatenate([comp1, comp2]))
sns.histplot(values, bins=100, color='black')
plt.show()
