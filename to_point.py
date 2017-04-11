import pandas as pd
import numpy as np
#posi_data=pd.read_csv("posi_data.csv",low_memory=False)
data=pd.read_csv("nega_part_final.csv",low_memory=False)
data.columns=['User_id','Merchant_id','Coupon_id','Discount_rate','Distance','Date_received','Result']

#nega_data_part=nega_data.loc[0:75000]

def no_null(pandas_data):
    item=pandas_data.Distance
    for idx in range(0,len(item)):
        if item[idx]=='null':
            item[idx]=5
        else:
            item[idx]=item[idx]

def change_format(pandas_data):
    item=pandas_data.Discount_rate
    for idx in range(0,len(item)):
        if item[idx].find('0.'):
            tmp_lst=item[idx].split(':')
            item[idx]=round((int(tmp_lst[0])-int(tmp_lst[1]))/int(tmp_lst[0]),2)
        else:
            item[idx]=item[idx]

no_null(data)
data.to_csv("nega_final.csv")
'''
change_format(data)
no_null(data)
data.to_csv("for_test.csv")
'''
