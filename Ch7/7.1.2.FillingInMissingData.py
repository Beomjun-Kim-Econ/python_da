import numpy as np
import pandas as pd

            ### 7.1.2.Filling In Missing Data ###

"""
In previous chapter we saw how to 'remove' somethings.
In this chapter we are going to see how to 'cover up' the holes.
The first one is fillna method, which is workhorse function to use.
It can cover up NA with the value I input.
"""
df = pd.DataFrame(np.random.standard_normal((7, 3)))
df.iloc[:4, 1] = np.nan
df.iloc[:2, 2] = np.nan
print(df.fillna(0))

"""
Calling 'fillna' with a dictionalry, I can use a different fill value for each column.
"""
print(df.fillna({1: 0.5, 2: 0}))    # missing values in column 1 are filled with 0.5, and in column 2 are filled with 0.

"""
ffill and bfill method can be used in reindexing. See the below case.
"""
df2 = pd.DataFrame(np.random.standard_normal((6, 3)))
df2.iloc[2:, 1] = np.nan
df2.iloc[4:, 2] = np.nan
print(df2)
print(df2.ffill())
print(df2.bfill())