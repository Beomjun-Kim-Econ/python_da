import numpy as np
                ### Function Dictionary ###

# page 101, 137, 158, 160, 161, 168, 172, 174, 199, 202, 213, 222, 233, 237, 238, 244
# 공부해야할 것: page 99(집합), 102(내장 순차 자료형 함수), 114(람다함수), 115(제네레이터), 122(파일 읽고쓰기)
# 그 외 정리: np.where()(4.4.1)

    ### Date and Time ### p.75

"""
파이썬 내장 datetime 모듈은 datetime, date, time 자료형을 지원한다.
datetime은 date와 time 정보를 함께 저장 하며 가장 흔히 쓰인다.
"""
from datetime import datetime, date, time

dt = datetime(2011, 10, 29, 20, 30, 21)
print(dt.day)
print(dt.date())
print(dt.time())
print(dt.minute)

"""
strftime 메서드는 datetime을 문자열로 포맷한다.
"""
dt_str = dt.strftime("%Y-%m-%d %H:%M")
print(dt_str)

"""
시계열 데이터를 집계하거나 그룹화할 때 datetime 의 필드를 치환하는 것이 유용한 경우가 종종 있다.
예컨데, 분과 초 필드를 0으로 치환하여 새로운 객체를 생성할 수 있다. 
분이나 초가 필요 없을 때 얘네를 0으로 만들면 유용할 것이다.
"""
dt_hour = dt.replace(minute=0, second=0)    # datetime 은 변경 불가능한 객체이기에 항상 새로운 객체를 반환한다.
print(dt_hour)

"""
두 datetime 객체의 차가 datetime.timedelta 객체가 된다.
"""
dt2 = datetime(2011, 11, 15, 22, 30)
delta = dt2 - dt
print(delta)
print(type(delta))

"""
datetime 은 timedelta 와 더할수도 있다.
"""
print(dt + delta)
print(dt2)      # 바로 윗줄의 결과와 이 줄의 결과가 동일