import numpy as np
import pandas as pd

                ### 5.1.1. Series ###

"""
Series 는 일련의 객체를 담을 수 있는 1차원 배열 같은 자료구조다. 어떤 넘파이 자료형이라도 담을 수 있다.
또한 index 색인을 갖는다. 간단한 Series 객체를 생성해보자.
"""
obj = pd.Series([4,7,-5,3])
print(obj)

"""
Series 의 배열과 색인 객체는 array, index 를 통해 얻을 수 있다.
일반적으로 .array 는 넘파이 배열을 감사는 PandasArray 이다.
"""
print(obj.array)
print(obj.index)

"""
각 데이터를 지칭하는 색인을 직접 지정해 Series 를 만들 수도 있다.
"""
obj2 = pd.Series([4,7,-5,3], index=["d", "b", "a", "c"])
print(obj2)
print(obj2.index)
print(obj2['a'])

"""
불리언 배열을 통해 값을 걸러내거나, 스칼라 곱, 유니버셜 펑션 등을 써도 색인과 값은 계속 연결된다.
"""
print(obj2[obj2 > 0])
print(obj2*2)
print(np.exp(obj2))

"""
Series 를 이해하는 또 다른 방법은 일종의 고정길이 딕셔너리라고 생각하는 것이다.
색인(키) - 데이터값(밸류) 로 연결되지 않는가?
"""
print('b' in obj2)
print('e' in obj2)

"""
실제로, 파이썬 딕셔너리 객체를 판다스 Series로 변환할 수 있다.
반대로 Series를 딕셔너리로 바꿀 수도 있다.
이 때, 두 방향 모두 원본은 살려두고 새롭게 객체를 만드는 것이다.
"""
sdata = {'Ohio': 35_000, 'Texas': 71_000, 'Oregon': 16_000, 'Utah':5_000}
obj3 = pd.Series(sdata)
print(obj3)
obj2_tmp = obj2.to_dict()
print(obj2_tmp)

"""
딕셔너리를 Series 로 바꿀 때, 색인을 직접 지정할 수도 있다.
"""
states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = pd.Series(sdata, index=states)
print(obj4)     # California 에는 대응 하는 값이 없으니까 NaN으로 나오는 것.
# Utah 는 states 에느느 미포함이니까 실행 결과에서 빠진다.

"""
이렇게 누락된 수를 찾을 때 좋은 함수는 isnull, notnull 이다.
"""
print(pd.isna(obj4))
print(pd.notna(obj4))
print(obj4.isna())

"""
데이터의 병합 등은 뒤에서 살펴보자. 우선은 간단하고 직관적으로 뭔가를 해보자.
"""
print(obj3 + obj4)

"""
Seires 객체 자체와 색인은 모두 name 속성을 갖는다.(데이터값은 안가짐)
"""
obj4.name = 'population'
obj4.index.name = "state"
print(obj4)

"""
색인을 바꿔줄 수도 있다.
"""
obj.index = ['Bob', 'Steve', 'Jeff', "Ryan"]
print(obj)
obj2.index = ['Bob', 'Steve', 'Jeff', "Ryan"]
print(obj2)
