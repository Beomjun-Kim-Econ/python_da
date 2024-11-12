import numpy as np
import pandas as pd

        ### 5.2.5.Appling of Function and Mapping ###

"""
판다스 객체에도 넘파이의 유니버셜 함수 (Universial function)을 적용할 수 있다. (4.3 참고)
"""

frame = pd.DataFrame(np.random.standard_normal((4,3)),
                     columns=list('bde'), index = ['Utah', 'Ohio', 'Texas', 'Oregon'])
print(frame)
print(np.abs(frame))

"""
이러한 넘파이 유니버셜 함수 외에도 각 행이나 열의 1차원 배열에만 한정적으로 함수를 적용ㄹ할 수도 있다.
이는 DataFrame 의 apply 매서드로 가능하다.
"""
def f1(x) :
    return x.max() - x.min()
print(frame.apply(f1))
"""
여기서 f는 각 Series(column)의 substraction between max and min 을 반환한다. 
그리고 자신이 생성된 각 열을 인덱스로 하는 Series 가 반환된다.

위의 예에서 frame.apply(f1, column='column') 으로 인수(Argument)를 추가하면 어떻게 될까?
방향이 반대가 된다. 기본은 aixs = 'index' 임을 유념하자. 아래예시를 보자.
"""
print(frame.apply(f1, axis = 'columns'))

"""
좋다. 이제 apply 를 좀 더 알아보자.
사실 일반적인 통계량(sum, mean 등) 은 이미 DataFrame 의 매서드로 존재하므로 굳이다.

apply 매서드에 전달된 함수는 꼭 스칼라를 반환할 필요 없다. 여러 값을 가진 Series를 반환할 수도 있다. 
"""
def f2(x) :
    return pd.Series([x.min(), x.max()], index = ['min', 'max'])
print(frame.apply(f2))

"""
이런식으로도 가능하다.
여기서 배열의 각 원소에 적용되는 파이썬 함수를 사용할 수도 있다. 
예컨데 frmae 객체에서 부동소수점 문자열 포맷으로 변환하고 싶다면
applymap 을 이용해서 아래와 같이 수행한다.
"""
def my_format(x) :
    return f'{x:.2f}'
# print(frame.applymap(my_format))   applymap 은 곧 지원종료... FutureWaring
"""
applymap 은 FutureWarning! -> map을 씁시다. map은 각 열로 타겟을 좁힌다.
"""
print(frame['e'].map(my_format))
