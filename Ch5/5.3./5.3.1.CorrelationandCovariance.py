import numpy as np
import pandas as pd

            ### 5.3.1.Correlation and Covariance ###

"""
cor, cov는 당연히 두 쌍의 인수가 필요하다. 우선 이 책의 데이터셋을 기준으로 생각해보자.
"""
price = pd.read_pickle('/Users/beomjunkim/Programming/Python_for_Data_Analysis/examples/yahoo_price.pkl')
volume = pd.read_pickle('/Users/beomjunkim/Programming/Python_for_Data_Analysis/examples/yahoo_volume.pkl')

print(price.head())

"""
이제 각 주식의 가격 변화를 백분율로 계산해보자.
"""
returns = price.pct_change()
print(returns.tail())

"""
corr 과 cov 매서드의 사용방법을 보라.
"""
cor_of_returns = returns["MSFT"].corr(returns["IBM"])   # MSFT 변동률과 IBM 변동률 사이의 상관계수
cov_of_returns = returns["MSFT"].cov(returns["IBM"])    # MSFT 변동률과 IBM 변동률 사이의 공분산
print(cor_of_returns)
print(cov_of_returns)

"""
데이터프레임에서 cov, cor은 어떨까? 직접 보자.
"""
print(returns.corr())
print(returns.cov())

"""
특정 열과 다른 여러 열들 사이의 cor을 알고 싶다면 corrwith 를 쓸 수 있다.
"""
print(returns.corrwith(returns['IBM']))

"""
만약 한 데이터프레임(여기서는 returns)에 딱 맞아 떨어지는 열 이름을 가진 데이터프레임(여기서는 volume)을 넘기면
각 열 이름에 대한 상관계수를 구한다.
"""
print(returns.corrwith(volume))

"""
만약 axis = 'column'를 넘기면 각 열에 대한 상관관계와 공분산을 계산한다.


참고로 위에 서술된 모든 경우, 상관계수를 구하기 전 데이터는 계산 전에 색인 이름 기준으로 정렬된다. 
"""