import numpy as np
import pandas as pd

            ### 5.2.7.DuplicatedIndex ###

"""
지금까지는 색인의 중복은 없었다. 그런데 색인이 중복되면 어쩌나?
"""
obj = pd.Series(np.arange(5), index=['a','a', 'b', 'b', 'c'])
print(obj)
"""
일단은 잘 나온다. is_unique 속성은 해당 값이 유일한지 아닌지를 보여준다.
즉 obj.index 에 is_unique를 검사함으로서 중복 색인이 있는지 없는지를 알 수 있다.
"""
print(obj.index.is_unique)

"""
중복 색인값이 있다면 색인을 이용한 데이터 골라내기 역시 다르게 작동한다.
Series 에서 지금까지의 유일색인의 경우 당연히 스칼라를 반환하였지만
중복색인은 Series 를 반환한다.
"""
print(obj['a'])
"""
레이블이 반복되는지의 여부에 따라 색인을 이용해 선택한 결과가 다를 수도 있으므로
코드가 좀 더 복잡해진다.
"""

df = pd.DataFrame(np.random.standard_normal((5, 3)),
                  index=["a", "a", "b", "b", "c"])
print(df)
print(df.loc['b']) # 중복색인 - 데이터프레임이 반환
print(df.loc['c']) # 유일색인 - 행이 시리즈로 반환