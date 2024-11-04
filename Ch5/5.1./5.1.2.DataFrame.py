import numpy as np
import pandas as pd

            ### 5.1.2. DataFrame ###

"""
DataFrame 은 스프레드시트 형식의 자료구조이다.
여러개의 열이 있고, 서로 다른 값(숫자, 문자열, 불리안 등) 을 담을 수 있다.
각 행과 열에 대한 색인을 가지며, 색인의 모양이 같은 Seires 객체를 여러개 담고 있는 파이썬 딕셔너리 정도 된다.
"""
data = {"state": ["Ohio", "Ohio", "Ohio", "Nevada", "Nevada", "Nevada"],
        "year": [2000, 2001, 2002, 2001, 2002, 2003],
        "pop": [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)          ### 새로운 객체를 생성!! 고로 frame 을 건드려도 data 에는 영향X
print(frame)

"""
R과 비슷하게, 최초/마지막 5개의 행만을 출력할 수도 있다.
"""
print(frame.head())
print(frame.tail())

"""
columns 를 원하는 순서대로 지정하여 해당 순서로 정렬된 DataFrame 객체를 얻을 수도 있다.
그리고 딕셔너리에 없는 값(열 인덱스) 를 넘기면 NaN이 나온다.
"""
frame_tmp = pd.DataFrame(data, columns=['year', 'state', 'pop'])
print(frame_tmp)
frame2 = pd.DataFrame(data, columns = ['year', 'state', 'pop', 'debt'])
print(frame2)

"""
반환된 Series 객체가 DataFrame 과 같은 색인을 가지면 알맞은 값으로 name 속성이 채워진다.
iloc, loc 을 통해 위치나 이름으로 행에 접근할 수도 있다.(5.2.3)
"""
print(frame2.loc[1])
print(frame2.iloc[1])

"""
대입으로 열을 수정해보자. 예컨데 frame2 에서 debt 는 NaN으로 채워진 열이다. 
여기에 스칼라값이다 배열의 값을 대입할 수도 있다.
"""
frame2['debt'] = 16.5
print(frame2)
frame2['debt'] = np.arange(6.)
print(frame2)

"""
리스트나 배열을 열에 대입하려할 때에는 그 길이가 DataFrame 의 길이와 같아야한다.
그리고 Series 를 대입하면 DataFrame 의 색인에 따라 값이 대입되며, 존재하지 않는 색인에는 결측치가 대입된다.
"""
val = pd.Series([-1.2, -1.5, -1.7], index = ['two', 'four', 'five'])
val2 = pd.Series([4,7,8,3])
frame2['debt'] = val
print(frame2)   # 해당하는 인덱스가 없어서 대입이 안됨
frame2['debt'] = val2
print(frame2)   # 길이의 부족한 부분은 여전히 결측치로 남아있음

"""
DataFrame 역시 del 예약어로 열을 삭제할 수 있다.
예시로, state 열이 'Ohio' 인지 검사한 결과를 불리언으로 나타내는 새 열을 만들어보자.
"""
frame2['eastern'] = frame2['state'] == 'Ohio'
print(frame2)
del frame2['eastern']
print(frame2)

"""
이중 딕셔너리의 사례를 보자. 바깥 딕셔너리의 키가 열, 안쪽 딕셔너리의 키가 인덱스가 된다.
여기서 transpose 도 가능하다.
이때, 전치하는 경우 열 내부의 자료형(int, float, str 등) 이 다르다면 정보가 유실될 수 있으니 주의할 것!
"""
population = {"Ohio": {2000: 1.5, 2001: 1.7, 2002: 3.6},
               "Nevada": {2001: 2.4, 2002: 2.9}}
frame3 = pd.DataFrame(population)
print(frame3)
print(frame3.T)

"""
이중 딕셔너리에서 안쪽이 인덱스가 된다고 했는데, 색인을 직접 지정하면 지정된 색인으로 DataFrame 을 생성한다.
"""
frame4 = pd.DataFrame(population, index=[2001,2002,2003])
print(frame4)

"""
Series 를 담고 있는 딕셔너리 데이터 역시 동일하게 취급된다.
"""

pdata = {'Ohio': frame3['Ohio'][:-1],
         'Nevada': frame3['Nevada'][:2]}
frame5 = pd.DataFrame(pdata)
print('\n',frame5)

"""
DataFrame 의 색인과 열에 name 속성이 설정되어 있다며 이 정보도 함께 출력된다.
"""
frame3.index.name = 'year'
frame3.columns.name = 'state'
print(frame3)

"""
DataFrame 을 넘파이 2차원 배열로 넘길수도 있다.
"""
tmp = frame3.to_numpy()     # 새로운 객체 생성
print(tmp)

"""
열이 서로 다른 자료형을 갖는다면 모든 열을 수용하기 위해 반롼된 배열의 자료형이 선택된다.
"""
print(frame2)
tmp_frame2 = frame2.to_numpy()
print(tmp_frame2)