'''
@date 10.28
@author qixuxiang

'''
import numpy as np
import pandas as pd
from pandas import Series, DataFrame

data1=pd.read_csv("nega_part_final.csv",low_memory=False);#offline test
'''
data2=pd.read_csv("ccf_offline_stage1_train.csv",low_memory=False);#offline train
data3=pd.read_csv("ccf_online_stage1_train.csv",low_memory=False);#online train



'''
print("total rows:{0}".format(len(data1)))
data1.columns=[['User_id','Merchant_id','Coupon_id','Discount_rate','Distance','Date_received','Date','Result']]
#ascend=data1.sort(columns=['Coupon_id'], ascending=[True])#排序Coupon_id
'''
coupon_arr=np.array(ascend['Coupon_id'])#提取出所有的Coupon_id并放在一个ndarray

coupon_lst=coupon_arr.tolist()
print(type(coupon_lst),len(coupon_lst))

print(coupon_lst)
#print(coupon_arr)
'''
num1=data1[u'Coupon_id'].value_counts()
num1.to_csv("nega_count.csv")





'''
print(type(coupon_lst))
tmpset=set(coupon_lst)
for item in tmpset:
    print(coupon_lst.count(item),"of",item,"in list")

print("total rows:{0}".format(len(data2)))
print("total rows:{0}".format(len(data3)))
print(list(data1))
print(list(data2))
print(list(data3))
'''
