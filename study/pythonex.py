import pandas as pd
import numpy as np
import FinanceDataReader as fdr
from dateutil.relativedelta import relativedelta
import datetime as dt
import momentum as mt


Offensive_assets = np.array(['QQQM' , 'SPY' , 'IWM' , 'VGK' , 'EWJ' , 'VNQ' , 'DBC' , 'IAU' , 'TLT' , 'HYG'])
Diffensive_assets = np.array(['BND' , 'SHV' , 'IEF'])
Canaria_assets = np.array(['VWO' , 'BND'])

list_Offensive = []
for i in Offensive_assets:
    list_Offensive.append(mt.momentum_ticker(i))

list_Diffensive = []
for i in Diffensive_assets:
    list_Diffensive.append(mt.momentum_ticker(i))

list_Canaria = []
for i in Canaria_assets:
    list_Canaria.append(mt.momentum_ticker(i))

ad = 0
for i in list_Canaria:
    if i > 0:
        ad = ad + 1

df_offensive = pd.DataFrame(list_Offensive , index = ['QQQM' , 'SPY' , 'IWM' , 'VGK' , 'EWJ' , 'VNQ' , 'DBC' , 'IAU' , 'TLT' , 'HYG'] , columns= ['momentum score'])
df_diffensive = pd.DataFrame(list_Diffensive , index = ['BND' , 'SHV' , 'IEF'] , columns= ['momentum score']) 
df_Canaria = pd.DataFrame(list_Canaria , index = ['VWO' , 'BND'] , columns= ['momentum score']) 

def we_can(ad):
    if ad == 2:
        offense = 1
        diffense = 0  
    elif ad == 1:
        offense = 0.5
        diffense = 0.5
    elif ad == 0:
        offense = 0
        diffense = 1
    return offense , diffense

offense , diffense = we_can(ad)

