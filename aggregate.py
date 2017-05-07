import os
import numpy as np
import pandas as pd
import csv
import datetime

import time
from time import mktime
from datetime import datetime
from datetime import timedelta
from types import *
from openpyxl import Workbook
import openpyxl
from datetime import date


#df = pd.read_csv("reduced/amasya_reduced.csv",low_memory=False , delimiter =',',parse_dates={'Datetime':['Date','Time']},index_col='Datetime')
df= pd.read_csv("reduced/Hatay_reduced.csv",delimiter=',', parse_dates={'Datetime':['Date','Time']},low_memory=False)
df= df.dropna(axis=0)

df['Temp.'] = df['Temp.'].astype(int)
df['Holiday'] = df['Holiday'].astype(int)
df['weekDay'] = df['weekDay'].astype(int)

df['Datetime']=pd.to_datetime(df['Datetime'], format='%B %d %Y %H:%M:%S')
df= df.set_index(pd.DatetimeIndex(df['Datetime']))
del df['Datetime']



f = {'Temp.':['mean'], 'Holiday':['mean'],'weekDay':['mean']}
agg_df = df.groupby(pd.TimeGrouper('H',closed = 'left')).agg(f)

#closed = 'left'
print(agg_df)
agg_df.to_csv("reduced/final_reduced/hatay_final.csv")












# df=df.set_index(df['Time'])

# agg_df=df.groupby([pd.TimeGrouper('H')]).aggregate(numpy.sum)

# print(agg_df)