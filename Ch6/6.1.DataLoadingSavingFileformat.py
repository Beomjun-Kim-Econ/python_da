import numpy as np
import pandas as pd

            ### 6.1.Reading and Writing Data in Text Format ###

"""
Pandas features a number of functions to read various files from txt to pickle.
Its names are read_*** (i.e. read_csv, read_spss, etc)

Ok, then let's load a csv file.
"""
with open('/Users/beomjunkim/Programming/Python_for_Data_Analysis/examples/ex1.csv', 'r') as tmp :
    content = tmp.read()
    # print(content)
"""
In the book, the author used !cat. But the syntax is only for Google Colab or Jupyter. So I used 'with'.
As I checked, the file is divided by comma. There I can read it as csv file.
"""
df = pd.read_csv('/Users/beomjunkim/Programming/Python_for_Data_Analysis/examples/ex1.csv')
print(df)

"""
ex1.csv has header row. But not all case have headers.
Let's see the next case.
"""
with open('/Users/beomjunkim/Programming/Python_for_Data_Analysis/examples/ex2.csv', 'r') as tmp :
    content2 = tmp.read()
    # print(content2)

"""
Like the above example, some files don't have header.
Then we can set it manually.
In the below case, I set header of df2 as None, so the header row was set as integer.
And in df3, I set its header manually made list.
Please be careful that if you want to set header as str like df3, 
then the name of argument is names, not header.  
"""
df2 = pd.read_csv('/Users/beomjunkim/Programming/Python_for_Data_Analysis/examples/ex2.csv',
                  header = None)
print(df2)
df3 = pd.read_csv('/Users/beomjunkim/Programming/Python_for_Data_Analysis/examples/ex2.csv',
                  names = ['a', 'b', 'c', 'd', 'message'])
print(df3)

"""
Let's see df3 again. There are still no index. 
I want to make the most right column(to say message col) as index. 
"""
namelist = ['a', 'b', 'c', 'd', 'message']
df4 = pd.read_csv('/Users/beomjunkim/Programming/Python_for_Data_Analysis/examples/ex2.csv',
                  names = ['a', 'b', 'c', 'd', 'message'],
                  index_col= 'message')

"""
If I want to form hierarchical index, I just pass a list of column numbers or names.
"""
parsed = pd.read_csv('/Users/beomjunkim/Programming/Python_for_Data_Analysis/examples/csv_mindex.csv',
                     index_col=['key1', 'key2'])
print(parsed)

"""
So far we've seen files separated by comma.
But some files use other delimiter, or just use blank.  
"""
with open('/Users/beomjunkim/Programming/Python_for_Data_Analysis/examples/ex3.txt',
          'r') as tmp :
    hi  = tmp.read()
    print(hi)

"""
In this case, firstly we need to do modify this file because the whitespaces are not one.
So we will change the blanks as one, by using regular expression. (정규 표현식)
"""
result = pd.read_csv('/Users/beomjunkim/Programming/Python_for_Data_Analysis/examples/ex3.txt',
                     sep = '\s+')
print(result)
"""
During that pandas recognize ex3.txt, 
it automatically think that the first row is header as the is has one less component.

The file parsing function has a variety of arguments to help you handle datasets.
For example, with skiprow, I can skip first, third, fourth rows.
"""
with open('/Users/beomjunkim/Programming/Python_for_Data_Analysis/examples/ex4.csv',
          'r') as tmp :
    hi  = tmp.read()
    print(hi)
"""
In the above file, there are some fun rows.
"""
df5 = pd.read_csv('/Users/beomjunkim/Programming/Python_for_Data_Analysis/examples/ex4.csv',
                  skiprows=[0,2,3])
print(df5)

"""
Ok. From now let's see missing values. 
By default, pandas uses a set of commonly occurring sentinels, such as NULL or NA.
"""
with open('/Users/beomjunkim/Programming/Python_for_Data_Analysis/examples/ex5.csv',
          'r') as tmp :
    hi  = tmp.read()
    print(hi)
result2 = pd.read_csv('/Users/beomjunkim/Programming/Python_for_Data_Analysis/examples/ex5.csv')
print(pd.isna(result2))

"""
Two NaN exist. Let's handle it.
"""
result2_na = pd.read_csv('/Users/beomjunkim/Programming/Python_for_Data_Analysis/examples/ex5.csv',
                      na_values='NULL')
print(result2_na)

"""
pandas.read_csv has a list of many default NA value representations, 
but these defaults can be disabled with the keep_default_na option.
"""
result2_tmp = pd.read_csv('/Users/beomjunkim/Programming/Python_for_Data_Analysis/examples/ex5.csv',
                      keep_default_na=False)
print(result2_tmp)
print(result2_tmp.isna())   # All of NA became non-NA

result2_tmp2 = pd.read_csv('/Users/beomjunkim/Programming/Python_for_Data_Analysis/examples/ex5.csv',
                           keep_default_na=False,
                           na_values='NA')
print(result2_tmp2)
print(result2_tmp2.isna())      # the real NA is NA, but just blank isn't NA.