import pandas as pd
import numpy as np
import datetime

data=pd.read_csv("posi_final.csv",low_memory=False);
df1=data.Date
df2=data.Date_received

def no_null(pandas_data):
    item=pandas_data.Distance
    for idx in range(0,len(item)):
        if item[idx]=='null':
            item[idx]=5
        else:
            item[idx]=item[idx]

no_null(data)

data.to_csv("posi_part_final.csv")

'''
count=0
assert len(df1)==len(df2)
for idx in range(0,len(df1)):
    if (datetime.datetime.strptime(str(df1[idx]),'%Y%m%d')-datetime.datetime.strptime(str(df2[idx]),'%Y%m%d')).days<=15:
        count+=1
'''
