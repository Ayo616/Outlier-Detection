import pandas as pd
from sklearn.ensemble import IsolationForest

hah = ['f7','f8','f9','f10','f11','f12','f13','f14','f15','f16','f17','f18','label']
haha = ['f7','f8','f9','f10','f11','f12','f13','f14','f15','f16','f17','f18']


data = pd.read_csv('./dataset/newdata2.csv')
features = pd.DataFrame(data,columns=hah)
triandata = features[features.label.isin([1,2])]



train = pd.DataFrame(triandata,columns= ['f7','f8','f9','f10','f11',
                                              'f12','f13','f14','f15','f16','f17','f18'])
ifr = IsolationForest()
ifr.fit(train)

test = pd.DataFrame(data,columns=haha)


result = ifr.predict(test)

outlier = pd.DataFrame()
for i in range(len(result)):
    if result[i] == -1:
        outlier = outlier.append(data.iloc[i])

print(outlier['label'].value_counts())
print(data['label'].value_counts())
