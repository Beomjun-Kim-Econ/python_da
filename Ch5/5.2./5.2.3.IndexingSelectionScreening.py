import numpy as np
import pandas as pd

        ### 5.2.3.Indexing,Selection, and Screening ###

"""
Series 의 색인(obj[...]) 은 넘파이 배열의 색인과 유사하다.
하지만 정수가 아니어도 된다는 점이 다르다.
"""
obj = pd.Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
print(obj)
print(obj['b'])
# print(obj[1])       # FutureWarning 발생
print(obj[2:4])
print(obj[['b', 'a', 'd']])
# print(obj[[1,3]])   # FutureWarning 발생
print(obj[obj < 2])     # 판다스의 인덱스-값은 일종의 딕셔너리의 키-밸류이다. 그래서 값(밸류)이 2보다 작은 애들만 도출함

"""
하지만 loc 를 사용하는 것이 선호된다. 여기서 loc는 location 이다.
위에서 print(obj[1]), print(obj[2:4]) 와 같은 [] 선택은 앞으로 작동하지 않을 것이다.
이 경우는 iloc(integer-location)로 바꿔야한다.
"""
print(obj.loc[['b', 'a', 'd']])

"""
[] 기반 선택 (i.e. obj[1] 이런 것)의 경우 정수 처리 방식이 다르기에 loc를 선호하는 사람들이 많다.
게다가 앞서 언급했듯 지원도 안할거고.
그래도 우선 한번 알아는 보자.
"""
obj1 = pd.Series([1,2,3], index = ['a','b','c'])
obj2 = pd.Series([1,2,3], index = ['a', 'b', 'c'])
# print(obj1[[0,1,2]])    # FutureWarning 발생
# print(obj2[[0,1,2]])    # FutureWarning 발생

"""
loc 기반의 선택을 배워보자. 우선 안되느느 걸 먼저 보자. loc는 index가 정수가 아닌데 정수 입력을 받으면 안된다.
"""
# print(obj2.loc[[0,1]])    # 에러 발생

"""
loc 연산자는 레이블로만 색인을 취한다. 
반면 iloc는 일관되게 정수로만 색인을 취한다.

즉 .loc는 색인에 따라 내가 선택하는 거고, .iloc는 무조건 첫행은 0, 다음행은 1,... 이런 식이다.
"""
print(obj1.iloc[[0,1]])
print(obj2.iloc[[1,2]])

"""
loc를 통해 슬라이싱도 가능하지만, "엔드포인트가 포함된다"
"""
print(obj2.loc['b':'c'])

"""
loc를 값을 골라 값을 바꿔줄 수도 있다.
"""
obj2.loc['b':'c'] = 5
print(obj2)

"""
DataFrame 에서 여러가지를 해보자.
"""
# 열 고르기
data = pd.DataFrame(np.arange(16).reshape((4, 4)),
                    index=["Ohio", "Colorado", "Utah", "New York"],
                    columns=["one", "two", "three", "four"])
print(data)
print('two')
print(data[['three', 'one']])

# 이번에는 행을 슬라이싱과 불리언으로 해보자
print(data[2:])
print(data[data['three'] > 5])

# 불리안 배열을 만들어보고 이를 응용하자.
print(data<5)
data_tmp = data.copy()
data_tmp[data_tmp < 5] = 0

"""
본격적으로 loc, iloc 선택을 보자.
두 개 모두 행 선택을 위한 도구다.
"""
# 우선 레이블을 이용해 단일 행을 선택해보자
print(data.loc['Colorado'])
# 위의 결과는 단일 행을 가진 Series 이다.

# 여러 행을 선택하면 새로운 DataFrame 으로 생성된다.
data_part = data.loc[['Colorado', 'New York']]
print(data)
print(data_part)

# loc에서 쉼표로 구분해서 행열을 조합해 선택할 수도 있다.
tmp = data.loc['Colorado', ['two', 'three']]
print(tmp)

"""
iloc 도 크게 다르지는 않다. 차이라면 정수색이라는 것.
.iloc[[2,3], [1,4]]: 2, 3번 행의 1,4번 열 데이터를 가져와라 라는 뜻
"""
print(data.iloc[2])
print(data.iloc[[2,1]])
print(data.iloc[2, [3,0,1]])
print(data.iloc[[1,2], [3,0,1]])

"""
loc, iloc 모두 슬라이스도 지원한다.
"""
print(data.loc[:'Utah', 'two'])
print(data.iloc[:, :3][data.three > 5])

# loc는 불리언이 되고 iloc에서는 안된다.
print(data.loc[data.three >= 2])

"""
[]을 이용하는 정수색인을 절대 쓰지좀 말자.
"""
ser = pd.Series(np.arange(3.))
ser_with_label = pd.Series(np.arange(3.), index = ['a', 'b', 'c'])
print(ser_with_label['b'])
print(ser)
# print(ser[-1])    # 에러 발생
"""
리스트라면 문제없이 될 문법인데 왜 여기서는 안되는가?
우선 컴퓨터는 레이블 색인을 찾는데에 실패한다. 앞서보듯 ser_with_label['b'] 이 잘 작동하는데, 레이블을 우선 찾는다.
근데 ser에는 -1 이라는 레이블이 없으므로 정수 색인을 찾는다. 근데 정수 색인에 -1은 없다.
고로 에러가 발생하는 것.

정리해보자. 판다스는 
(1) 색인이 정수값을 담는다면 우선 레이블부터 뒤져보게 되어있다. 
(2) 반면 정수 기반 슬라이싱은 정수 부터 뒤져보게 되어있다.
1번의 특징으로 인해...
"""
# print(ser_with_label[-1])   # futurewarning
"""
이 작동하나, Futurewarning 이 발생한다.
생각하기 힘들면 그냥 무조건 loc, iloc 를 붙혀서 쓰는걸로 하자. 딴 생각 금지.
"""

"""
연쇄색인의 함정을 알아보자.
"""
data.loc[:, 'one'] = 1
print(data)

data.iloc[2] = 5
print(data)

data.loc[data['four'] > 5] =3
print(data)
"""
이렇게 값이 잘 바뀐다. 그런데...
"""
# data.loc[data.three == 5]['three'] = 6
# ‘three’ 열 값이 5인 행을 선택한 뒤, 해당 결과에서 ‘three’ 열만 추출하는 코드임.
# print(data)
"""
얘는 왜 문제지?
저런식으로 .loc[][] 의 형태를 연쇄색인(chained indexing) 이라한다.
이는 의도한대로 data 자체를 건드리는 것이 아니라 임싯값(비어있지 않은 data.loc[data==5] 의 결과를 바꾸려한다.
고로 data가 변하지 않는다.
이 문제를 피하기 위해서는 .loc[] 꼴로, [] 안에 다 집어 넣어야 한다. 두 개의 [] 로 나누지 말고!
즉, 값을 할당할 때에는 연쇄색인을 가급적 피해야 한다는 것이다.
"""