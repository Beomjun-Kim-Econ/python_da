import numpy as np
import pandas as pd

            ### 5.3.Numerical Descriptive Computation and Summary

"""
판다스 객체는 일반적인 수학/통계학 매서드를 갖고 있다. 
이들은 Series, DataFrame의 행이나 열에서 단일 값(합, 평균 등)을 구하는 축소(reduction), 
요약 통계(summary statistics) 범주에 속한다.

순수 넘파이 어레이에 제공되는 동일한 매서드와 다르게 판다스의 매서드는 처음부터 누락된 데이터를 제외토록 설계되었다. 
"""
df = pd.DataFrame([[1.4, np.nan], [7.1, -4.5], [np.nan, np.nan], [0.75, -1.3]],
                  index=["a", "b", "c", "d"],
                  columns=["one", "two"])
print(df)
"""
DataFrame의 sum은 각 열의 합을 담은 Series 를 반환한다.
sum에서 인수로 axis = 1 or axis = 'columns'를 넣으면 행의 합을 담은 Series를 반환한다.
즉 디폴트는 axis = 'index' 인 것
기본적으로 NaN은 자동으로 건너뛴다. 
그런데 하나라도 결측치가 있는 경우 합도 NaN 처리고 하고 싶다면 skipna = False 로 두면 된다.
즉 디폴트는 skipna = True 라는 것
"""
print(df.sum())
print(df.sum(axis = 1))     # or axis = 'columns'
print(df.sum(skipna = False))

"""
평균과 같은 일부 집계에서는 결과값 생성을 위해 최소 하나 이상의 non-NA value 가 필요하다.
"""
print(df.mean(axis=1))  # c행은 둘 다 NaN 이라서 평균도 NaN 으로 나왔다.

"""
idxmin, idxmax 같은 매서드는 최소/최대값을 가진 '색인값'을 반환한다.
이렇게 색인값과 같이 간접적인 요소를 통하는 것을 간접 통계(indirect satistics)라 한다.
"""
print(df.idxmax())

"""
누산 매서드 accumulation 도 있다.
"""
print(df.cumsum())
"""
describe 매서드도 있다. 요약 통계량을 쭉 나열해버린다.
"""
print(df.describe())

"""
describe 의 대상이 수치 데이터가 아니면 다른 요약 통계량을 만든다.
"""
df2 = pd.Series(['a', 'a', 'b', 'c'] * 4)
print(df2.describe())

