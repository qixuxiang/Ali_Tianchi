import pandas as pd


data1=pd.read_csv("ccf_offline_stage1_train(table 1).csv",low_memory=False);
data1.columns=[['User_id','Merchant_id','Coupon_id','Discount_rate','Distance','Date_received','Date']]

couple_data=data1[(data1['Coupon_id']!='null')]#filter no Coupon_id data
nega_data=couple_data[(couple_data['Date']=='null')&(couple_data['Coupon_id']!='null')]#does not use couple
nega_data['Result']=0
#nutral_data=couple_data[(couple_data['Date']!='null')&(couple_data['Coupon_id']=='null')]
posi_data=couple_data[(couple_data['Date']!='null')&(couple_data['Coupon_id']!='null')]
posi_data['Result']=1
#print(data1.head(20))
test_posi=posi_data[:100]
test_nega=nega_data[:100]
posi=test_posi.iloc[:,1:8]
nega=test_nega.iloc[:,1:8]
#disc=couple_data.Discount_rate
#print(disc)
#disc.to_csv('disc.csv')
print("total rows:{0}".format(len(data1)))
print("useful rows:{0}".format(len(couple_data)))
print("negative rows:{0}".format(len(nega_data)))
#print("nutral rows:{0}".format(len(nutral_data)))
print("positive rows:{0}".format(len(posi_data)))
#del nega_data[0]
#del posi_data[0]
nega_data.to_csv('nega_data.csv')
posi_data.to_csv('posi_data.csv')
print(posi)
print(nega)
#test_nega.to_csv('test_nega.csv')
#test_posi.to_csv('test_posi.csv')
