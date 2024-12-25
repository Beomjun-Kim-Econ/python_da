import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

            ### Facet Grids and Categorical Data ###

"""
Facet grid is good at expressing to visualize data with many categorical variables.
seaborn has a useful built-in function 'catplot', which enable me to make many kind of faceted plots.
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

sns.catplot(x='day', y = 'tip_pct', hue = 'time', col = 'smoker',
            kind = 'bar', data = tips[tips.tip_pct < 1])

plt.show()

"""
I can adjust those options.
"""
sns.catplot(x = 'day', y= 'tip_pct', row = 'time', col = 'smoker', kind = 'bar',
            data = tips[tips.tip_pct < 1])
plt.show()

"""
'catplot' also can make boxplot by setting kind = 'box'
"""
sns.catplot(x = 'tip_pct', y = 'day', kind = 'box',
            data = tips[tips.tip_pct < 0.5 ])
plt.show()