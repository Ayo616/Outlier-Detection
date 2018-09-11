import pandas as pd
from sklearn.ensemble import IsolationForest

hah = ['f7','f8','f9','f10','f11','f12','f13','f14','f15','f16','f17','f18']

data = pd.read_csv('./dataset/newdata.csv')
all = pd.DataFrame(data,columns=['f1','f2','f3','label'])
# print(all.iloc[0]['label']==1)

ilf = IsolationForest()
a = all.loc[all['label']==1]
features = pd.DataFrame(a,columns=['f1','f2','f3'])
ilf.fit(features)

test = pd.DataFrame(data,columns=['f1','f2','f3'])
result = ilf.predict(test)
print(result)
# print(type(result))


outlier = pd.DataFrame()
for i in range(len(result)):
    if result[i] == -1:
        outlier = outlier.append(data.iloc[i])

print(outlier['label'].value_counts())
# print(outlier['label'].value_counts())

print(all['label'].value_counts())