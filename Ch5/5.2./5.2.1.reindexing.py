import numpy as np
import pandas as pd

        ### 5.2.1. Reindexing ###

"""
판다스 객체의 가장 중요한 기능 중 하나는 reindex 이다. 이는 새로운 색인에 적합하도록 객체를 생성하는 기능이다.
"""
obj = pd.Series([4.5, 7.2, -5.3, 3.6], index = ['d', 'b', 'a', 'c'])
print(obj)

"""
재색인 하는 경우, 색인에 맞춰서 데이터를 재배열한다. 이 때 대응하는 값이 없다면 NaN으로 처리한다.
reindex는 새로운 객체를 생성한다.
"""
obj2 = obj.reindex(['a', 'b', 'c', 'd','e'])
print(obj2)


"""
위와 같이 빈 경우 보간해야한다. 이 때, method 인수를 통해 어떻게 보간할 지 결정할 수 있다.
여기선 ffill 로 보자.
"""
obj3 = pd.Series(['blue', 'purple', 'yellow'], index = [0,2,4])
obj3_tmp = obj3.reindex(np.arange(6), method='ffill')
print(obj3_tmp)

"""
DataFrame 에 대한 reindex 는 행(색인), 열, 또는 둘 다 변경 가능하다. 순서만 전달하면 재색인이 된다.
각각의 색인을 지정하는 방법을 알아보자. 우선 행의 색인을 바꿔보자.
"""
frame = pd.DataFrame(np.arange(9).reshape((3, 3)),
                     index = ['a', 'c', 'b'],
                     columns = ['Ohio', 'Texas', 'California'])
frame2 = frame.reindex(['a', 'c', 'b', 'd'])
print(frame2)

"""
열을 재색인 해보자. 방법은 axis 인수를 추가로 설정해주는 것이다. 원래 axis의 디폴트 값은 index 인 셈이다.
"""
states = ['Texas', 'California', 'Utah']
frame3 = frame.reindex(states, axis='columns')
print(frame3)

"""
사실 일반적인 방법은 loc 연산자를 이용하는 것이다. 이 방법은 모든 새로운 색인 레이블이 DataFrame에 존재할 때만 작동한다. 
"""
frame4 = frame.loc[['a', 'b', 'c'], ['California','Texas']]
print(frame4)