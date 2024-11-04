import numpy as np
import pandas as pd

            ### 5.1.3. Index Object ###
"""
판다스의 색인 객체는 축 레이블(DataFrame의 열 이름 포함)과 다른 메타데이터(축의 이름 등)을 저장하는 객체이다.
Series나 DataFrame 객체를 생성하 ㄹ때 사용하는 배열이나 다른 순차적인 레이블은 내부적으로 색인으로 변환된다.
"""
obj = pd.Series(np.arange(3), index=["a", "b", "c"])
index = obj.index
print(index)
print(index[1:])

"""
색인 객체는 변경이 불가능하다.
이러한 불변성 덕분에 자료구조 사이에서 색인을 안전하게 공유할 수 있다.
"""
# index[1] = 'd'  # TypeError
labels = pd.Index(np.arange(3))
labels
obj2 = pd.Series([1.5, -2.5, 0], index=labels)
print(obj2)
print(obj2.index is labels)

"""
배열과 유사하게 Index 객체도 고정된 크기로 작동한다.
"""
population = {"Ohio": {2000: 1.5, 2001: 1.7, 2002: 3.6},
               "Nevada": {2001: 2.4, 2002: 2.9}}
frame3 = pd.DataFrame(population)
print(frame3)
print(frame3.columns)
print("Ohio" in frame3.columns)
print(2003 in frame3.index)

"""
파이썬의 집합과 달리 판다스의 색인은 중복을 허용한다.
"""
tmp = pd.Index(["foo", "foo", "bar", "bar"])
print(tmp)