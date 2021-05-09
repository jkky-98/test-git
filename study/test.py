import pandas as pd
import numpy as np
import openpyxl

df = pd.read_csv('/Users/jkky/Documents/aparttradedata.csv' , encoding= 'euc-kr')
df = df.rename(columns={'기준년도' : 'year' , '기준월' : 'month' , '기준일' : 'day' , '시군명' : 'name1' , '법정동명' : 'name2' , '아파트명' : 
'brendname' , '층수': 'floor' , '거래금액(만원)' : 'price' , '전용면적(㎡)': 'Area'})
df = df.sort_values(['price'] , ascending = False)
bins = [1000 , 10000 , 30000 , 50000 , 70000 , 100000 , 150000 , 200000 , 300000]
labels = [1,2,3,4,5,6,7,8]
price_cuts = pd.cut(df['price'] , bins = bins, labels = labels )
df['price_score'] = price_cuts
print(df['price_score'].value_counts())
print('------'*20)

hwasung = (df['name1'] == '화성시')
df.loc[:,'hwasung'] = hwasung
hwasum = df['hwasung'].sum()
df['hwasung'] = df['hwasung'] * df['price']
hwatotal = df['hwasung'].sum()
hwasung_mean=hwatotal/hwasum
print(hwasung_mean)

suwon = (df['name1'] == '수원시')
df.loc[:,'suwon'] = suwon
susum = df['suwon'].sum()
df['suwon'] = df['suwon'] * df['price']
sutotal = df['suwon'].sum()
suwon_mean=hwatotal/susum
print(suwon_mean)


sungnam = (df['name1'] == '성남시')
df.loc[:,'sungnam'] = sungnam
sungsum = df['sungnam'].sum()
df['sungnam'] = df['sungnam'] * df['price']
sutotal = df['sungnam'].sum()
sungnam_mean=sutotal/sungsum
print(sungnam_mean)
print('------'*20)
print(df['name2'].value_counts())
print('------'*20)
g_df = df.copy()
g_df_area = g_df.groupby('price_score')['Area'].agg('mean')#시리즈값으로 뱉게됨
# g_df_area = g_df.groupby('price_score').agg({'area' : 'mean'}) #으로 하여금 데이터프레임으로도 뱉을 수 있다.
# g_df에서 'price_score'로 그룹바이한 후['Area']를 통해 area를 해당그룹 기준으로 나눈후 .agg를 통해 해당 그룹의 area평균값을 구한다.
# area가 클수록 땅값이 비싼 점수에 속한다는 통계적 특성을 확보가능하다.
print(g_df_area)
g_df1 = g_df.groupby('price_score').agg({'Area' : ['mean' , 'std' , 'min' , 'max'] , 'price' : ['mean' , 'size' , 'nunique']})
print(g_df1)
df.to_excel('REtrade.xlsx')