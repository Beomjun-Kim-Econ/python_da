import numpy as np
import pandas as pd

            ### 7.1.1.Filtering Out Missing Data ###

"""
Let's see some few ways to filter out missing data.
The method 'isna' checked whether each value is NaN or not.
notna method is conversed version of isna. 
The method 'dropna' and 'notna' can be helpful to achieve our purpose-filtering out-.
"""

data = pd.Series([1, np.nan, 3.5, np.nan, 7])
print(data.dropna())
print(data.notna())

"""
Let's focus on DataFrame. 
I would want to drop rows when all of its components are NA or when there's even one NA.
we use dropna for the latter, and we add how='all' for the formal.

These functions and methods make new object by default.
"""
data = pd.DataFrame([[1., 6.5, 3.], [1., np.nan, np.nan],
                     [np.nan, np.nan, np.nan], [np.nan, 6.5, 3.]])
print(data)
print(data.dropna())
print(data.dropna(how='all'))

"""
We dropped rows in the above case.
We can also drop columns by same way, adding the argument axis = 'columns'
"""
data[4] = np.nan
print(data)
print(data.dropna(axis='columns'))
print(data.dropna(how='all', axis='columns'))

"""
Sometimes, I might want to drop a row only when it has fewer than a certain number of NAs.
“I can use the argument ‘thresh’. If thresh = 2, rows that have fewer than 2 non-NA values will be dropped. 
In other words, rows need at least 2 non-NA values to be kept.
"""
df = pd.DataFrame(np.random.standard_normal((7, 3)))
df.iloc[:4, 1] = np.nan
df.iloc[:2, 2] = np.nan
print(df)
print(df.dropna())
print(df.dropna(thresh=2))