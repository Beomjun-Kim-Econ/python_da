import numpy as np
import pandas as pd

            ### 5.2.6.Sorting and Raking ###
"""
어떤 기준에 근거하여 데이터를 정렬하는 것은 아주 중요하다. 
정렬된 새로운 객체를 반환하는 sort_index 를 사용해서 행ㄱ과 열의 색인을 알파벳 순서로 정렬해보자.
"""
obj = pd.Series(np.arange(4), index = ['d', 'a', 'b', 'c'])
print(obj)
obj_test = obj.sort_index()
print(obj_test)

"""
위에서는 Series 를 정렬했다. 이번에는 DataFrame 을 정렬해보자.
여기서는 행과 열 중 하나의 인덱스를 기준으로 정렬할 수 있다.
"""
frame = pd.DataFrame(np.arange(8).reshape((2,4)),
                     index = ['three', 'one'],
                     columns = ['d', 'a', 'b', 'c'])
print(frame)
frame_sort_by_index = frame.sort_index()
print(frame_sort_by_index)
frame_sort_by_columns = frame.sort_index(axis="columns")
print(frame_sort_by_columns)
frame_sort_by_both = frame_sort_by_columns.sort_index()
print(frame_sort_by_both)

"""
데이터는 기본이 오름차순(ascending) 이다. 즉 ascending = True 가 디폴트라는 것.
인수를 변경하며 내림차순도 가능하다.
"""
frame_columns_descending = frame.sort_index(axis='columns', ascending = False)
print(frame_columns_descending)

"""
지금까지는 인덱스를 기준으로 정렬했다.
Series에서 값을 오름차순, 내림차순으로 정렬하려면 sort_value를 쓰면 된다.
"""
obj2 = pd.Series([4,7,-3,2])
obj2_test = obj2.sort_values()
print(obj2_test)

"""
정렬시 결측치는 기본적으로 Seires 객체의 가장 뒤로 간다.
ascending 이 True, False 이든 관계 없다.
다만 na_position 인수를 'first'로 설정하여 먼저 오게 할 수 있다. 즉 기본값이 'last'라는 것
"""
obj3 = pd.Series([4, np.nan, 7, np.nan, -3, 2])
obj3_test = obj3.sort_values()
print(obj3_test)
obj3_first_nan = obj.sort_values(na_position='first')
print(obj3_first_nan)

"""
지금까지는 Series 의 값 기준 정렬을 보았다.
이제는 DataFrame 을 값 기준으로 정렬해보자.
우선 하나 이상의 열에 있는 값으로 정렬할 경우, sort_values 함수에 기준이 될 열을 넘겨주자.
"""
frame2 = pd.DataFrame({'b': [4, 7, -3, 2], 'a': [0, 1, 0, 1]})
print(frame2)
frame2_sort_by_a = frame2.sort_values('b')
print(frame2_sort_by_a)

"""
여러 개의 열을 정렬하려면 열 이름 리스트로 넘겨주면 된다.
여기서는 b로 정렬하고 a로 정렬한다.
"""
frame2_sort_by_two = frame2.sort_values(['b', 'a'])
print(frame2_sort_by_two)

"""
순위에 대해 알아보자. 순위는 가장 낮은 값부터 시작해 배열의 유효한 데이터 개수까지의 순서를 매긴다.
"""
obj = pd.Series([7, -5, 7, 4, 2, 0, 4])
print(obj.rank())
"""
부연설명을 해보자. 우선 위 리스트를 오름차순 정렬해보면
-5, 0,2,4,4,7,7 이다.
-5, 0, 2 는 각각 1,2,3의 순위를 갖는다.
4는 네번째와 다섯번째에 있으므로 (4+5)/2 = 4.5 순위,
7은 여섯번째와 일곱번째에 있으므로 (6+7)/2 = 6.5 순위인 것이다.

그런데 여기서 그냥 4를 두개 다 4.5 처리가 아니라, 하나는 4, 다른 하나는 5 이렇게 처리하고 싶을 수도 있다.
그럴 때는 인수 method = 'first' 를 쓰면 된다.
그리고 내림차순 랭크를 원한다면 ascending = False 로 두면 된다.
또한 여기서는 동률의 경우 average 였는데, 이 외에도 동률 처리 방식은 다양하다.
"""
print(obj.rank(method='first'))
print(obj.rank(ascending=False))

"""
DataFrame 을 랭크로 바꿔보자.
"""
frame = pd.DataFrame({"b": [4.3, 7, -3, 2], "a": [0, 1, 0, 1], "c": [-2, 5, 8, -2.5]})
row_ranked_frame = frame.rank(axis = 'rows')
col_ranked_frame = frame.rank(axis = 'columns')
print(row_ranked_frame)     # 각 열 내의 순위 매기기
print(col_ranked_frame)     # 각 행 내의 순위 매기기
