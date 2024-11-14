import numpy as np
import pandas as pd

            ### 6.1.1_5.Various way to read file

"""
When I tried to read very large file, I may want to read only small piece of the file to see
or iterate smaller chunks.

Before to start to handle a large file, let me modify printing option of pandas.
"""
pd.options.display.max_rows = 10

