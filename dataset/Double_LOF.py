import pandas as pd
from sklearn.neighbors import LocalOutlierFactor

data = pd.read_csv('./newdata2.csv')
features = pd.DataFrame(data,columns=['f1','f2','f3'])
# print(features)


clf = LocalOutlierFactor(n_neighbors=15)
y = clf.fit_predict(features)
print(y)

outlier = pd.DataFrame()
for i in range(len(y)):
    if y[i] == -1:
        outlier = outlier.append(data.iloc[i])

print(outlier['label'].value_counts())
print(data['label'].value_counts())