import numpy as np
import pandas as pd

            ### 7.1. Handling Missing Data ###

"""
Pandas handles missing data automatically well.
It represents missing data as NaN.
And we call this NaN a 'sentinel value'.
The 'isna' method gives us a Boolean Seires with True where values are null.
"""
float_data = pd.Series([1.2, -3.5, np.nan, 0])
print(float_data)
print(float_data.isna())

"""
Pandas have adopted a convention used in R by referrring to missing data as NA, which stands for 'Not Available'.
NA may either be data that does not exist or data that exist but not is not be able to observed.
To identify missing value can prevent potential bias and data collection problems.
The bulit-in Python 'None' is also treated as NA.
"""
string_data = pd.Series(["aardvark", np.nan, None, "avocado"])
print(string_data)
print(string_data.isna())

float_data = pd.Series([1, 2, None], dtype='float64')
print(float_data)
print(float_data.isna())
