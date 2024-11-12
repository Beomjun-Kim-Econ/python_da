import numpy as np
import pandas as pd

            ### 5.3.2.Unique value, Counting, and Membership ###

"""
Series 안에 담긴 값의 정보를 추출해보자.
unique 매서드는 중복을 제외한 Series 를 반환한다.
"""
obj = pd.Series(["c", "a", "d", "a", "a", "b", "b", "c", "c"])
unique = obj.unique()
print(unique)
unique.sort()
print(unique)

"""
이번에는 도수 frequency 를 알아보자.
value_counts 를 쓸 수 있다. 기본적으로 내림차순 정렬이 된다.
sort 인수를 설정하여 정렬을 하지 않을 수도 있다.
"""
print(obj.value_counts())
# tmp = pd.value_counts(obj.to_numpy(), sort=False)     #Futurewarning... 그냥 위에꺼 쓰란다.
# print(tmp)

"""
isin 매서드를 통해 특정 값이 Series 에 존재하는 지 알 수 있다.
"""
mask = obj.isin(['b', 'c'])
print(mask)     # b, c가 아닌 곳은 False / 맞으면 True
print(obj[mask])

"""
isin 과 관련있는 Index.get_indexer 매서드는 여러 값이 들어 있는 배열에서 유일한 값의 색인 배열을 구할 수 있다.
"""
to_match = pd.Series(["c", "a", "b", "b", "c", "a"])
unique_vals = pd.Series(["c", "b", "a"])
indices = pd.Index(unique_vals).get_indexer(to_match)
print(indices)


"""
데이터프레임의 여러 열에 대해 히스토그램을 그려야 하는 경우가 종종 있다.
"""
data = pd.DataFrame({"Qu1": [1, 3, 4, 3, 4],
                     "Qu2": [2, 3, 1, 2, 3],
                     "Qu3": [1, 5, 2, 4, 4]})
print(data)
"""
다음과 같이 단일 열에 대한 값 개수를 계산할 수도 있다.
"""
counts = data['Qu1'].value_counts().sort_index()        # Series 이다.
print(counts)

"""
모든 열에 대해 해주고 싶다면 DataFrame의 apply 매서드에 pandas.value_counts 를 넘기자.
"""
# result = data.apply(pd.value_counts).fillna(0)
# FutureWarning - pd.value_counts 는 곧 끝난다. pd.Series(obj).value_counts()
# print(result)
