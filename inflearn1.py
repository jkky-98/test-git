import pandas as pd
import numpy as np
import math as m
df = pd.read_csv('Documents/2019_12.csv')

#분석 순서
# 1. 칼럼 첫번째 이름인 ticker 를 종목명으로 바꿔보자
df = df.rename(columns = {'ticker' : '종목명'})

# 1. 디스크라이브를 먼저 해봐서 특성을 보자. include = [np.number]은 넘파이에서 지원하는 숫자만 포함시켜라는 뜻!
# 트랜스포스는 많아질 수 있는 각 금융지표를 가로로 보지말고 세로로 보기 편하게 셋팅하기위함.
# percentiles 는 상위 10% (50%) 70% 95%의 수치를 보여주기 위해 따로 셋팅함.
print(df.describe(percentiles = [0.1 , 0.7 , 0.95] , include = [np.number]).T)
# 중복도 확인가능 , 오브젝트만 설정해서 종목명의 특성을 특정하여 카테고리컬로 수,유니크,탑(가장많이중복)을 가져옴
print(df.describe(include = [np.object , pd.Categorical]))
# per 의 상위 10% 30% 50% 값을 보자.
print(df['PER(배)'].quantile([.1,.3,.5]))
# 데이터의 유니크한 수 파악하기


