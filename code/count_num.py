import pandas as pd
data1=pd.read_csv("ccf_offline_stage1_test_revised.csv",low_memory=False);#offline test
data2=pd.read_csv("ccf_offline_stage1_train(table 1).csv.csv",low_memory=False);#offline train
data3=pd.read_csv("ccf_online_stage1_train.csv",low_memory=False);#online train
print("total rows:{0}".format(len(data1)))
print("total rows:{0}".format(len(data2)))
print("total rows:{0}".format(len(data3)))
data1.columns=[['User_id','Merchant_id','Coupon_id','Discount_rate','Distance','Date_received']]
data2.columns=[['User_id','Merchant_id','Coupon_id','Discount_rate','Distance','Date_received','Date']]
#count1=data1[u'Coupon_id'].value_counts()

print(count1)
print(type(count2))
'''
plt1=count1.plot(kind="bar").get_figure()
plt1.savefig("plot1.png")
plt2=count2.plot(kind="bar").get_figure()
plt2.savefig("plot2.png")
'''
