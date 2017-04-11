import pandas as pd
import numpy as np
data1=pd.read_csv("ccf_offline_stage1_test_revised(3).csv",low_memory=False);
data1.columns=[['User_id','Merchant_id','Coupon_id','Discount_rate','Distance','Date_received']]
del data1['Merchant_id']
del data1['Discount_rate']
del data1['Distance']
data1.to_csv("result.csv")
