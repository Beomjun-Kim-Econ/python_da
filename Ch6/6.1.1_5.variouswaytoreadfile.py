import numpy as np
import pandas as pd

            ### 6.1.1_5.Various way to read file

"""
When I tried to read very large file, I may want to read only small piece of the file to see
or iterate smaller chunks.

Before to start to handle a large file, let me modify printing option of pandas.
"""
# pd.options.display.max_rows = 10

result = pd.read_csv('/Users/beomjunkim/Programming/Python_for_Data_Analysis/examples/ex6.csv')
print(result)

"""
In above case, result read the file entirely.
By nrow I can read only few rows.
"""
result2 = pd.read_csv('/Users/beomjunkim/Programming/Python_for_Data_Analysis/examples/ex6.csv',
                      nrows=10)
print(result2)
"""
I can check that result2 read only 10 rows as there's no elipsis.

Then let's see how to explore the dataset file with dividing as chunks.
Firstly I need to see its datatype
"""
chunker = pd.read_csv('/Users/beomjunkim/Programming/Python_for_Data_Analysis/examples/ex6.csv',
                     chunksize = 1000)
print(type(chunker))    # TextFileReader

"""
The type of chunker is TextFileReader, 
which allows me to iterate over the parts of the file according to the chuncksize.
The below case shows aggrregating the value of 'keys' by iterating over the file.
"""
tot = pd.Series([], dtype = 'int64')
for piece in chunker :
    tot = tot.add(piece['key'].value_counts(), fill_value=0)
print(tot)