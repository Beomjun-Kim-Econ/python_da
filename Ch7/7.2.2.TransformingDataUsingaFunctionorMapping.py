import numpy as np
import pandas as pd

            ### 7.2.2.Transforming Data Using a Function or Mapping ###

data = pd.DataFrame({"food": ["bacon", "pulled pork", "bacon", "pastrami", "corned beef", "bacon",
                              "pastrami", "honey ham", "nova lox"],
                     "ounces": [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})
print(data)
"""
Let me suppose that I want to add a column like the below.
Then we can map the below one to the 'data' by using .map, which I discussed in 5.2.5.
It modifies the original data.
"""
meat_to_animal = {
  "bacon": "pig",
  "pulled pork": "pig",
  "pastrami": "cow",
  "corned beef": "cow",
  "honey ham": "pig",
  "nova lox": "salmon"
}
data['animal'] = data['food'].map(meat_to_animal)
print(data)

"""
Or we are able to do that by defining new function.
"""
def get_animal(x) :
    return meat_to_animal[x]
print(data['food'].map(get_animal))


            ### 7.2.3. Replacing Values ###

"""
In companies, people sometimes use wired number as sentinel values.
We can replace these with NA values aht pandas understands.
"""
data2 = pd.Series([1., -999., 2., -999., -1000., 3.])
print(data2)
data2_replaced = data2.replace(-999, np.nan)
print(data2_replaced)       # still -1000 remains as sentinel number.
data2_fully = data2.replace([-999, -1000], np.nan)
print(data2_fully)
data2_fully_dic = data2.replace({-999: np.nan, -1000: 10000000})
print(data2_fully_dic)


            ### 7.2.4. Remaining Axis Indexes ###
"""
We can transform axis labels like values in Series, 
by a function or mapping of some form to produce new, differently labeled objects.
"""
data3 = pd.DataFrame(np.arange(12).reshape((3, 4)),
                    index=["Ohio", "Colorado", "New York"],
                    columns=["one", "two", "three", "four"])
def transform(x) :
    return x[:4].upper()
data3_upper = data3.index.map(transform)        # Making new object
print(data3_upper)
# data3_index_modfied = data3.index = data3_upper
# print(data3)

"""
The above case modifed the original data. by rename, I can make new object.
"""
data3_new = data3.rename(index = str.title, columns = str.upper)
print(data3_new)
data3_final = data3.rename(index = {'Ohio': 'INDIANA'},
                           columns = {'three': 'peekaboo'})
print(data3_final)

            ### 7.2.5. Discretization and Binning ###

"""
Countinuous data sometimes needs to be discretized,
or otherwise separated into 'bins' for analysis.
"""
ages = [20, 22, 25, 27, 21, 23, 37, 31, 61, 45, 41, 32]
bins = [18,25,35,60,100]
age_categories = pd.cut(ages, bins)
print(age_categories)

"""
The returned pandas object is Categorical. 
Each bin is identifed by as special interval value type 
containing the lower and upper limit of each bin. 
"""
print(age_categories.codes)     # age의 각 value가 bin의 어디 소속인지?
print(age_categories.categories)    # showing interval
print(age_categories.categories[0])     # show the interval in the bracket.
print(pd.Series(age_categories).value_counts())     # counting each frequency of each bin.

"""
In the string representation of an interval, 
a parenthesis(()) means that the side is open, while the square bracket([]) means it is closed.
I can change which side is closed by passing 'right = False'.
"""
print(pd.cut(ages, bins, right=False))
"""
Also I can override the default interval-based bin labeling
by passing a list or array to the labels option
"""
group_names = ["Youth", "YoungAdult", "MiddleAged", "Senior"]
print(pd.cut(ages, bins, labels=group_names))       # 이름이 붙었다.
"""
If I pass an interger number of bin to pd.cut instead of explict bin,
than pandas will automatically compute same-length bins based on the min and max value in the data. 
"""
data4 = np.random.uniform(size =20)
data4_equal = pd.cut(data4, 4, precision=2)     #precision argument limits the deciaml precision.
print(data4_equal)

"""
A closely related function, pd.qcut, bins the data based on ample quantiles.
It uses sample quartiles.
"""
data5 = np.random.standard_normal(1000)
quartiles = pd.qcut(data5, 4, precision=2)
print(quartiles)
print(pd.Series(quartiles).value_counts())