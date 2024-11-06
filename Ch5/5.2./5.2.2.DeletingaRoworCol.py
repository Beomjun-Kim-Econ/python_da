import numpy as np
import pandas as pd

                ### 5.2.2.Deleting a Row or Column ###

"""
삭제하려눈 축이 제외된 리스트를 이미 갖고 있거나 색인 배열을 갖고 있다면 
5.2.1. 과 같이 reindex 나 loc 로 삭제할 수 있다.  하지만 이 방법은 데이터의 모양을 직접 변경해야 한다.
하지만 drop 메서드를 쓰면 선택한 값이 사라져있는 새로운 객체를 얻을 수 있다.
"""
obj = pd.Series(np.arange(5.), index=["a", "b", "c", "d", "e"])
new_obj = obj.drop('c')
print(new_obj)
print(obj.drop(['d', 'e']))

"""
DataFrame 에서는 행, 열 모두에서 색인값을 삭제할 수 있다.
인덱스로 행 삭제때는 인수로 index=, 열 삭제 때는 columns= 을 사용한다.
"""
data = pd.DataFrame(np.arange(16).reshape((4,4)),
                    index = ['Ohio', 'Colorado', 'Utah', 'New York'],
                    columns=['one', 'two', 'three', 'four'])
print(data)
data_1 = data.drop(index=['Colorado', 'Utah'], columns=['one'])
print(data_1)

"""
열 삭제 방법으로 다음의 문법도 있다.
"""
data_2 = data.drop('two', axis=1)
print(data_2)
