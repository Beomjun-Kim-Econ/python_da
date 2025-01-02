import pandas as pd

            ### 8.2.1.Database-Style DataFrame Joins ###

"""
We can operate 'merge' or 'join' by linking rows using one or more keys.
It is important for relational databases. 
'on =' sets that which column I will use as key 
"""

df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
                    'data1': pd.Series(range(7), dtype = 'Int64')})
df2 = pd.DataFrame({'key': ['a', 'b', 'd'],
                    'data2': pd.Series(range(3), dtype = 'Int64')})
print(df1)
print(df2)

merged = pd.merge(df1, df2, on = 'key')
print(merged)

"""
'left_on' and 'right_on' options set which columns I will use as keys.
And 'merge' doesn't ensure the order of rows.
"""
df3 = pd.DataFrame({"lkey": ["b", "b", "a", "c", "a", "a", "b"],
                    "data1": pd.Series(range(7), dtype="Int64")})

df4 = pd.DataFrame({"rkey": ["a", "b", "d"],
                    "data2": pd.Series(range(3), dtype="Int64")})
merged_2 = pd.merge(df3, df4, left_on = 'lkey', right_on = 'rkey')
print(merged_2)

"""
'how = ' sets whether I use left table key or right table key, or the intersection or union.
"""
df1 = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],
                    'data1': pd.Series(range(6), dtype = 'Int64')})
df2 = pd.DataFrame({'key': ['a', 'b', 'a', 'b', 'd'],
                    'data2': pd.Series(range(5), dtype='Int64')})
merged_3 = pd.merge(df1, df2, how = 'left', on = 'key')
print(merged_3)