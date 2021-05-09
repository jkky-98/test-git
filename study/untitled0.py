# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 00:02:15 2021

@author: 준기요
"""

import pandas as pd 
import numpy as np
import time as t
import openpyxl


pd.set_option('display.width', 1000)

df = pd.read_csv('Documents/2016_12.csv')

df = df.rename(columns = {'ticker' : '종목명'})
# ticker를 종목명으로 바꿔주기

df.describe( include = [np.number] , percentiles =[0.03 , 0.05 , 0.8] ).T
# 숫자만 표시하고 하위 3% , 5% , 80%로 수정해서 보여줌

df.nsmallest(5 , 'PER(배)')
# 'per 가장 작은 5종목 골라주기'

df.nsmallest(100 , 'PER(배)').nlargest(5 , '당기순이익(억원)')
# per 가장 낮은놈 100개중에서 당기순이익 가장큰 5개 추출

df.sort_values(['순이익률(%)' , 'EPS(원)' ] , ascending = [True , False] ).head()
# 어센딩(오름차순)은 기본설정 , 순이익율을 오름차순으로 정렬한 상태에서 eps를 내림차순으로 작성.


df[['EPS(원)' , '종목명']]
# 컬럼 두개를 가져오기 ( 데이터 프레임으로 가져와짐 )

df[['종목명']]
# 리스트로 전달할 경우 데이터프레임으로 가져와지므로 대괄호안에 리스트로 작성하여 종목명을 가져오면 시리즈가 아니라 데이터프레임으로 가져와짐

df['종목명']
# 리스트로 종목명을 가져옴

df.filter(like = 'RO')
#RO가 들어가있는 모든 컬럼을 가져와줌

df.filter(regex = 'P\w+R')
#정규표현식으로 표현된 것을 가져와줌(regex) , 크롤링관련해서 필요할거임. 점프투 파이썬에서 흥미로우면 공부해볼 것.
# P로 시작해서 R로 끝나는 것을 가져와줌

df.dtypes.value_counts()
# 칼럼에 대한 데이터 정보를 알려줌 ex) float64 , object...etc 이것으로 판단한 후 셀렉트디타입할것.(아래)

df.select_dtypes(include = ['float'])
# float에 해당하는 데이터 프레임을 보여줌 exclude로 빼고도 가져올 수 있음.

df.iloc[2]  , df.iloc[[2]] 
# 3번째 행을 나타내줌 첫번째는 스칼라값으로 나타내고 두번째 값은 시리즈로 나타내줌

df1 = df.set_index('종목명')
# 인덱스를 종목명으로!

df1.loc[['삼성SDI','삼성전자'],['순이익률(%)' , 'EPS(원)']]
# 삼성sdi 와 삼성전자의 , 순이익률와 eps 를 나타냄.

df1.loc['CJ' : '휴켐스' , ['매출액(억원)' , 'PSR(배)']]
# CJ부터 휴켐스까지 매출액과 psr을 나타내기 (주목할 것은 범위로 표시할때는 리스트형으로 넣어주질 않음!!)

# iloc , loc 은 [ a , b ] 형식으로 a에는 행을 나타내며 , b에는 열을 나타낸다. 범위로 나타낼 경우 먼저요소 : 나중요소 로 나타내던가 , [요소1 , 요소2 , 요소3 ...]로 특정요소들만 선택도 가능

# 스칼라를 뽑을때는 iloc , loc 대신 iat , at 으로 하면 속도가 매우 빠르다!( 버젼상이한 듯 하니 알아볼것...)

con1 = df1['순이익률(%)'] > df1['영업이익률(%)']
# 영업이익률보다 순이익률이 큰 경우를 구하자. ( false & true ) , false = 0 , true = 1 로 취급함

con1.sum() , con1.mean()
# 위의 경우에서 트루인 값만 모두 더했을때의 결과 , 평균의 값을 알려줌

df1[con1]
# 영업이익률보다 순이익률이 높은 df1를 다시 추출하는 방법!

df1.loc[con1]
# 위와 같은 경우임 암기해야함!

con2 = df1['PBR(배)'] < 1
final_con = (con1 & con2)
df1.loc[final_con]
# con2인 피비알이 1보다 작을 조건과 con1인 순이익률이 영업이익률보다 클 경우 동시에 만족하는 final_con을 만들 수 있다.

df[df['종목명'].isin(['삼성전자' ,'휴켐스' , 'CJ'])]
# isin으로 종목명특정해서 정보 빼내는 방법 isin(list) 로 하여금 실현 가능

con1.all()
# 해당 불린시리즈에서 .all()을 찍어주면 모든놈들이 트루냐? 모든놈들이 트루이면 트루를 뱉고 아니면 펄스를 뱉음
con1.any()
# 해당 불린시리즈에서 .any()를 찍어주면 어떤 한놈이라도 트루가 존재하냐? 존재한다면 트루를 뱉고 아니라면 펄스를 뱉음


check = df1['순이익률(%)']
check = np.nan_to_num(check , copy = False)
( check > -10000000 ) .all()
# np.nan_to_num 을 통해 nan값을 0으로 바꾸고 -10000000 보다 모든 값이 큰지 질문하면 True를 뽑아줌 / nan 값을 항상 주의해야함!!

Sector_data = pd.read_csv('Documents/inflearn_pandas_part1_material/my_data/symbol_sector.csv')

Sector_data['Sector'].value_counts()
# sector 별로 소속된 중복값들을 표현해줌 ex) 기타 금융업 110 , 의약품 제조업 44...

top_5_sector_list = Sector_data['Sector'].value_counts().nlargest(5).index

Sector_data[Sector_data.isin(top_5_sector_list)]

(df1['PER(배)'] == np.nan).any()
#피이알에서 난의 존재를 알아보기

df1['PER(배)'].hasnans
#피이알에서 난의 존재 알아보기

df1['PER(배)'].isna().sum()
#난이 몇개인지 true=1을 다합하여 sum을 구하여 숫자을 알아볼 수 있음.

df.isnull()
#데이터프레임에서 nan이 있으면 true로 표시

df.isnull().any(axis = 0)
#각 칼럼들의 난값이 하나라도 있냐라는 질문에 true and false로 대답해줌.

df.isnull().any(axis = 0).any()
# 이 칼럼들중 트루가 하나라도 있냐??
# 이 데이터프레임에 난값이 하나라도 있냐??

df1['PER(배)'] == df1['PER(배)']
# 각 종목마다 지표에 난값이 존재하면 false를 나타냄 이유는 난값과 난값의 같다는 표현은 false를 출력함

df1['PER(배)'].equals(df1['PER(배)'])
# 현재의 칼럼과 equals()속의 칼럼과 정말로 같은 지 비교

df1[df1['PER(배)'].notnull() & df1['당기순이익(억원)'].notnull()]
# per에 널이 없고 당기순이익도 널이 없는 데이터프레임을 달라

df1.notnull().all(axis = 1)
# 가로방향으로 모두가 널인 값인가? 각 로우마다 참거짓 표현

df1.dropna(subset = ['PER(배)'])
# 특정 컬럼중에 nan값이 하나라도 있으면 쳐내라 ( 나머진 살리기 )
df1['PER(배)'] = df1['PER(배)'].fillna(0)

bound1 = df1['PER(배)'] >= 10
bound2 = (df1['PER(배)'] >= 5) & (df1['PER(배)'] < 10)
bound3 = (df1['PER(배)'] >= 0) & (df1['PER(배)'] < 5)
bound4 = df1['PER(배)'] < 0

df1.loc[bound1 , 'PER_score'] = 1
df1.loc[bound2 , 'PER_score'] = 2
df1.loc[bound3 , 'PER_score'] = 3
df1.loc[bound4 , 'PER_score'] = -1
df1['PER_score'].nunique()
df1['PER_score'].value_counts()
df1['PER_score'].head()

#bound1로 하여금 per이 10보다 높으면 true를 뱉는다.
#bound2 loc을 통하여 bound1에서 트루값에 해당하는 놈들만 새로운 칼럼 피비알스코어에 1을 넣는다.
#bound3 loc을 통하여 bound2에서 트루값에 해당하는 놈들만 기존 칼럼 피비알스코어에 2를 넣는다 이때 바운드1과 2는 겹치지않으므로 걱정할필요없다 나머지도 마찬가지로 구현된다.

df1.loc[ :  , 'PER_score1'] = (bound1 * 1) + (bound2 * 2) + (bound3 * 3) + (bound4 * -1)
df1['PER_score'].value_counts()
df1['PER_score1'].value_counts()
df1['PER_score1'].equals([df1['PER_score']])
#두개의 벨류카운트시에 인티저와 플롯으로 다름을 알 수 있다.
df1['PER_score'].dtypes
df1['PER_score1'].dtypes
#dtypes메소드를 통해 정확히 확인가능하다.
df1['PER_score'].astype(int).equals(df1['PER_score1'])
#astype(int)로 하여금 정수로 타입을 바꿔준후 이퀄을 찍어 트루가 됨을 확인 할 수 있다.
per_cuts = pd.cut(df1['PER(배)'] , [-np.inf , 0 , 5 , 10 , np.inf])
#판다스에서 지원하는 cut이란 메소드는 칼럼을 먼저 나타낸후 ,로 구분하고 리스트로 구간을 나누어 나타내면 칼럼으로 잘라서 해당 범위에 속하는 것들을 알 수 있다.
per_cuts.value_counts()

bins = [-np.inf , 0 , 5 , 10 , np.inf]
labels = ['괴상한주' , '저평가주' , '보통주' , '고평가주']

per_cuts2 = pd.cut(df1['PER(배)'] , bins = bins , labels = labels)

#라벨링을 해주기 위함 bins는 자를 범위를 나타내며 , labels는 범위사이에 값이 어떤 라벨을 가질건지 라벨리스트로하여금 넣어준다.
df1.loc[: , 'PER_score3'] = per_cuts2
df1['PER_score4'] = per_cuts2
#loc의 경우 로우의 범위를 전체로 설정한 후 칼럼명을 정한후 해당 칼럼공간에 cut한 리스트를 전해준다.
per_qcuts = pd.qcut(df1['PER(배)'] , 3 , labels = [1,2,3])
#감동적인 로직 , per을 도수분포표로하여금 히스토그램을 나타내었을때 각 도수가 주어진 숫자(3), 즉 3구간으로 나누었을때 구간의 도수가 모두 같게끔 분할한다.
df1 = df1.dropna(subset = ['PER(배)' , 'PBR(배)' , 'PSR(배)'])

# df1의 subset을 per로 설정하고 nan값이 존재하는 row를 모두 쳐내버림
df1['PER(배)'].isna().count()
# per이 난값인것이 존재하는지 확인

df1.drop(['PER_score' , 'PER_score1' ,'PER_score3','PER_score4'] , axis = 'columns' , inplace = True)
# 칼럼 자르기.
pbr_qcuts = pd.qcut(df1['PBR(배)'] , 3 , labels = [1,2,3])
psr_qcuts = pd.qcut(df1['PSR(배)'] , 3 , labels = [1,2,3])
df1['PBR_score'] = pbr_qcuts
df1['PSR_score'] = psr_qcuts
df1['PER_score'] = per_qcuts

g_df = df1.copy()
#새로운 , 그대로의 복사체를 만들때는 그냥 = 으로 하지말고 .copy()를 사용할 것.

g_df_obj = g_df.groupby(['PER_score' , 'PBR_score' , 'PSR_score'])

g_df_obj.size().loc[(1,2)]
#사이즈를 찍었을때 나타나는 형태는 시리즈이다. 이때 록으로 하여금 (튜플형태)로 전달하여 보고싶은 것들을 볼 수 있다.
g_df_obj.ngroups
#그룹의 수를 알려줌
g_df_obj.groups
#그룹들의 요소를 딕셔너리 형태로 나타내줌
g_df_y = g_df.groupby('PER_score')['영업이익률(%)'].agg('mean')
print(g_df_y)
#perscore를 그룹바이해준 후 영업이익률을 그룹바이 기준으로 그룹바이 인덱스마다 평균값을 나오게 해줌.
g_df.groupby('PER_score').agg({'영업이익률(%)' : 'mean' }) # 요 형태를 주로 쓸 것!!!!!!!!
#같은 방식이지만 agg()에 평균값 낼 칼럼을 정해서 표시하는 방법이다.

#------------------------------------------------------------------------------------------------
sorted_df = df.reset_index(drop = True)
sorted_df.rename(columns = {'매출액(억원)' : 'Sales' , '순이익률(%)' : 'Income' ,'영업이익률(%)' : 'Operating_income' , '당기순이익(억원)' : 'Net income',
                            'EPS(원)' : 'EPS' , 'BPS(원)' : 'BPS' , 'SPS(원)' : 'SPS' , 'PER(배)' : 'PER' , 'PBR(배)' : 'PBR' , 'PSR(배)' : 'PSR'} , inplace = True)
co1 = sorted_df['종목명']
sorted_df = sorted_df.drop('종목명' , axis = 1)
print(sorted_df)
#보기 나쁜 한글을 모두 영어로 대체하여 표시 , 종목명같은경우 불가피하므로 오른쪽 끝으로 보내어 정렬함
df1.to_excel('tt.xlsx')

g_df1 = g_df.groupby(['PBR_score' , 'PER_score'])\
            .agg({'영업이익률(%)' : ['mean' , 'std' , 'min' , 'max'] ,
                         'ROE(%)' : ['mean' , 'size' , 'nunique' ] 
                })
# pbr , per 스코어를 통해서 그루핑을 한 후 영업이익률에 대한 다음 리스트의 통계값을 그리고 roe에 대한 다음 통계값을 추출한다

sorted_per_qcuts = pd.qcut(sorted_df['PER'] , 3 , labels = [1,2,3])
sorted_pbr_qcuts = pd.qcut(sorted_df['PBR'] , 3 , labels = [1,2,3])
sorted_psr_qcuts = pd.qcut(sorted_df['PSR'] , 3 , labels = [1,2,3])

sorted_df['PER_score'] = sorted_per_qcuts
sorted_df.loc[: , 'PBR_score'] = sorted_pbr_qcuts
sorted_df['PSR_score'] = sorted_psr_qcuts
sorted_df['종목명'] = co1

g_sorted_df = sorted_df.groupby(['PBR_score' ,'PER_score' , 'PSR_score'])\
                       .agg({'ROE(%)' : ['mean' , 'max' , 'min' , 'std' ,'idxmax'] , 
                       'Operating_income' : ['mean' , 'max' , 'min' , 'std' ,'idxmax']})
level0 = g_sorted_df.columns.get_level_values(0)
level1 = g_sorted_df.columns.get_level_values(1)
g_sorted_df.columns = level0 + '_' + level1
g_sorted_df = g_sorted_df.reset_index()
print(g_sorted_df)

