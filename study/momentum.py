import pandas as pd
import numpy as np
import FinanceDataReader as fdr
from dateutil.relativedelta import relativedelta
import datetime as dt

def momentum_ticker(ticker):

    month_1 = relativedelta(months=1)
    month_3 = relativedelta(months=3)
    month_6 = relativedelta(months=6)
    month_12 = relativedelta(months=12)
    today = dt.datetime.now()
    df1 = fdr.DataReader(ticker,today - month_1 , today)
    df1_percent = (df1['Close'][-1] - df1['Close'][0])/df1['Close'][0]

    df3 = fdr.DataReader(ticker,today - month_3 , today)
    df3_percent = (df3['Close'][-1] - df3['Close'][0])/df3['Close'][0]

    df6 = fdr.DataReader(ticker,today - month_6 , today)
    df6_percent = (df6['Close'][-1] - df6['Close'][0])/df6['Close'][0]

    df12 = fdr.DataReader(ticker,today - month_12 , today)
    df12_percent = (df12['Close'][-1] - df12['Close'][0])/df12['Close'][0]  

    momentum1 = df1_percent * 100 * 12
    momentum3 = df3_percent * 100 * 4
    momentum6 = df6_percent * 100 * 2
    momentum12 = df12_percent * 100 * 1
    score = momentum1 + momentum3 + momentum6 + momentum12
    return score

