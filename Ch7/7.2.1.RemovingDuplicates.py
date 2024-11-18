import numpy as np
import pandas as pd

            ### 7.2.1.Removing Duplicates ###

"""
We might found some rows for any number of reasons.
Let's see an example.
"""
data = pd.DataFrame({"k1": ["one", "two"] * 3 + ["two"],
                     "k2": [1, 1, 2, 3, 3, 4, 4]})
print(data)
"""
The method 'duplicated' in DataFrame 
returns a Boolean Series indicating whether each row is a duplicated.
And drop_duplicates returns a DataFrame with rows where the duplicated array is False filtered out.
"""
print(data.duplicated())
print(data.drop_duplicates())

"""
Both of the methods consider all of the columns by default.
But I can set the coverage of considering by 'subset'.
"""
data['v1'] = range(7)
print(data)
print(data.drop_duplicates(subset=['k1']))  # k1의 중복이 사라짐

"""
When pandas removes duplicates, it drops from last, in other words it remians first ones, by default.
We can change it by 'keep = 'last''.
"""
print(data.drop_duplicates(['k1', 'k2'], keep = 'last'))    # subset이 자동으로 설정
