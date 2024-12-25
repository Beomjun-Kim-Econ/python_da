import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

            ### 9.2.2. Bar plots ###

"""
The 'plot.bar()' and 'plot.barh()' make vertical and horizontal bar plots, respectively.
In this case, the Series or DataFrame index will be used as the x-axis(.bar) or y-axis(.barh) ticks.
"""
# with Series
fig, axes = plt.subplots(2,1)
data = pd.Series(np.random.uniform(size = 16), index = list('abcdefghijklmnop'))
data.plot.bar(ax = axes[0], color = 'black', alpha = 0.7 )
data.plot.barh(ax = axes[1], color = 'black', alpha = 0.7)
plt.show()

# with DataFrame
df = pd.DataFrame(np.random.uniform(size = (6,4)),
                  index = ['one', 'two', 'three', 'four', 'five', 'six'],
                  columns = pd.Index(['A', 'B', 'C', 'D'],
                                     name = 'Genus')) # the options 'name' is about legend.
print(df)
df.plot.bar()
plt.show()
df.plot.barh(stacked = True, alpha = 0.5)
plt.show()

"""
Let's see more specific case.
"""
tips = pd.read_csv('/Users/beomjunkim/Programming/python_da_datas/examples/tips.csv')
print(tips.head())
party_counts = pd.crosstab(tips['day'], tips['size'])
party_counts = party_counts.reindex(index=['Thur', 'Fri', 'Sat', 'Sun'])
print(party_counts)
party_counts = party_counts.loc[:, 2:5]
print(party_counts)

# Normalizing to make each summation of columns 1.
party_pcts = party_counts.div(party_counts.sum(axis='columns'),
                              axis = 'index')
print(party_pcts)
party_pcts.plot.bar(stacked=True)
plt.show()

"""
Let me see seaborn to aggregate of summarize with above example.
"""
tips['tip_pct'] = tips['tip'] / (tips['total_bill'] - tips['tip'])
print(tips.head())
sns.barplot(x = 'tip_pct', y = 'day', data = tips, orient = 'h')
plt.show()
# the black lines on the graphs express 95% confident level, which is able to adjust.

"""
with 'hue' option, I can split by an additional categorical value.
"""
sns.barplot(x='tip_pct', y='day', hue='time', data = tips, orient = 'h')
plt.show()
# 그래프로 이해하면 된다.

"""
seaborn automatically change the aesthetics of plots.
But I can manually switch it using... 
'sns.set_style'..
"""
