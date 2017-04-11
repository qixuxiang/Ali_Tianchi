import pandas as pd
import copy
import statsmodels.api as sm
import pylab as pl
import numpy as np
df = pd.read_csv("all03.csv")
df.columns=[['Coupon_id','Discount_rate','Distance','Result']]

# prestige   1   2   3   4
# admit
# 0         28  97  93  55
# 1         33  54  28  12

# plot all of the columns
'''
df.hist()
pl.show()
'''

dummy_ranks = pd.get_dummies(df['Coupon_id'], prefix='Coupon_id')
print(dummy_ranks.head())
#    prestige_1  prestige_2  prestige_3  prestige_4
# 0           0           0           1           0
# 1           0           0           1           0
# 2           1           0           0           0
# 3           0           0           0           1
# 4           0           0           0           1

# 为逻辑回归创建所需的data frame
# 除admit、gre、gpa外，加入了上面常见的虚拟变量（注意，引入的虚拟变量列数应为虚拟变量总列数减1，减去的1列作为基准）
cols_to_keep = ['Discount_rate','Distance','Result']
data = df[cols_to_keep].join(dummy_ranks.ix[:, 'Coupon_id_2':])
print(data.head())
# 需要自行添加逻辑回归所需的intercept变量
data['intercept'] = 0.3
train_cols = data.columns[-1:]
# Index([gre, gpa, prestige_2, prestige_3, prestige_4], dtype=object)

logit = sm.Logit(data['Result'], data[train_cols])

# 拟合模型
result = logit.fit()
combos =pd.read_csv("for_test03.csv")
combos.columns=[['Coupon_id','Discount_rate','Distance']]

# 数据中的列要跟预测时用到的列一致
predict_cols = combos.columns[-1:]

# 预测集也要添加intercept变量
combos['intercept'] = 0.3

# 进行预测，并将预测评分存入 predict 列中
combos['predict'] = result.predict(combos[predict_cols])

# 预测完成后，predict 的值是介于 [0, 1] 间的概率值
# 我们可以根据需要，提取预测结果
# 例如，假定 predict > 0.5，则表示会被录取
# 在这边我们检验一下上述选取结果的精确度
count=0
lst=[]
for value in combos.values:

  # 预测分数 predict, 是数据中的最后一列
    predict = value[-1]

  # 实际录取结果
    #print(predict)
    lst.append(predict)
    count+=1
print(count)
print(lst)
