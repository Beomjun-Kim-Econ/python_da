import numpy as np
import pandas as pd

        ### 5.2.4. Calculation Operator and Daty Alignment ###

"""
판다스는 서로 다른 색인을 갖는 객체 간의 산술연산을 간단히 처리할 수 있다.
예컨데 객체를 더할 때 색인이 다르다면 추후 색인이 통합된다. 
"""
s1 = pd.Series([7.3, -2.5, 3.4, 1.5], index=["a", "c", "d", "e"])
s2 = pd.Series([-2.1, 3.6, -1.5, 4, 3.1],
               index=["a", "c", "e", "f", "g"])
print(s1)
print(s2)
s_add = s1 + s2
print(s_add)
# 여기서 f, g는 비록 s2에 있으나 s1에는 없어서 NaN 처리가 되었다. 반면 a, c 는 양자 모두에 있으므로 더해져서 값이 잘 있다.

"""
df끼리 더할 때는 '겹치는 색인'이어야 한다. 그렇지 않으면 결측치가 되어버린다.
"""
df1 = pd.DataFrame(np.arange(9.).reshape((3,3)),
                   columns=list('bcd'), index = ['Ohio', 'Texas', 'Colorado'])

df2 = pd.DataFrame(np.arange(12.).reshape((4,3)),
                   columns=list('bde'), index = ['Utah','Ohio', 'Texas', 'Oregon'])
print(df1 + df2)

"""
이렇게 인덱스가 서로 다른 객체간 연산에서 존재하지 않는 축의 값을 0과 같이 특수한 값으로 지정하고 싶을 수 있다.
우선 np.nan을 대입해 고의적으로 NA를 만들어보자.
"""
df3 = pd.DataFrame(np.arange(12).reshape((3,4)), columns=list('abcd'))
df4 = pd.DataFrame(np.arange(20).reshape((4,5)), columns=list('abcde'))
df4.loc[1, 'b'] = np.nan
print(df3)
print(df4)
print(df3+df4)  # 합에서도 여전히 결측치로 나온다.

"""
그렇다면 앞에서 보았던, 겹치는게 없는 인덱스의 경우에 몽땅 결측치로 처리되어 버리는 문제를 어떻게 해결하지?
add 매서드를 사용하면 된다.
이러면 내가 바라는 그 방식대로 add가 된다.
이 외에도 sub, div, floordiv, mul, pow 등이 있다.(사전 참고)
여기서 fill_value 는 NaN 에 어떤 값을 넣을 것인지를 설정하는 것이다.
"""
df5 = df3.add(df4, fill_value = 0)
print('hi\n',df5)

"""
위에서 add 말고 radd 가 있는데, 이는 reverse이다.
즉 1/df(3) 와 df3.rdiv(1) 이 같다.
sub의 경우면 df1.sub(df2, fill_value = 0) 과 df2.rsub(df1, fill_value = 0) 이 같다.
"""
print(1/df3)
print(df3.rdiv(1))

"""
판다스의 두 데이터구조 DataFrame 과 Series 사이의 연산을 해보자. 
우선 브로드캐스트 Broadcast 를 이해해보자.
"""
arr = np.arange(12.).reshape((3,4))
print(arr - arr[0])

"""
우리가 생각하듯이 행이 쏙 빠지는게 아니라, 각 행에 arr[0] 이 각각 substarct 된다.
이를 브로드캐스트라고 한다.
이제 DataFrame 과 Series 사이의 연산을 해보자.
"""
frame = pd.DataFrame(np.arange(12.).reshape((4,3)),
                     columns=list('bde'), index = ['Utah', 'Ohio', 'Texas', 'Oregon'])
series = frame.iloc[0]
print(frame)
print(series)
print(frame - series)

"""
위의 예에서 frame - series 가 브로드캐스팅으로 연산되었음을 보았다.
그런데 색인값을 DataFrame 의 열이나 Series 의 색인에서 찾을 수 없다면 어떻게 될까?
그렇다면 그 객체는 형식을 맞추기 위해 재색인 (reindexing, reindex)된다.
예시를 보자.
"""
series2 = pd.Series(np.arange(3), index = ['b', 'e', 'f'])  # f는 새롭게 생기고, d가 없다. 색인이 안맞다!
print(frame)
print(series2)
print(frame + series2)
"""
색인이 맞던 b, e는 연산이 되고
d는 프레임에는 원래 잘 있었지만 series2에는 없어서 결측치가 되었다.
그리고 f는 반대로 프레임에는 없었고 series2에는 있는데, 위와 마찬가지로 당연히 결측치가 된다.

이런 방식은 우리가 원하는 방식은 아닌데, 어떻게 해야할까?
바로 앞과 마찬가지다. frame.add(series2) 를 쓰면 된다.
여기에 axis 를 인수로 지정할 수도 있는데, 이는 연산을 적용할 축 번호다.
아래의 예제 코드에서 axis='index' 는 DataFrame 의 열을 따라 연산을 수행하라는 의미다.
"""
series3 = frame['d']
print(frame)
print(series3)
print(frame.sub(series3, axis = 'index'))




