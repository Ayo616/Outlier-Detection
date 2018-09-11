import  pandas as pd
import numpy as np

#
# aa = pd.DataFrame([[5,6,7,1],
#                   [6,7,8,1],
#                   [5,18,16,0],
#                   [7,8,5,1],
#                   [5,7,8,1],
#                   [5,17,12,0],
#                    [5,5,6,1]],
#                   columns=['f1','f2','f3','label'])
#
# df = pd.DataFrame(aa,columns=['f1','f2','f3'])

aa = pd.read_csv('./dataset/newdata2.csv')

hah = ['f7','f8','f9','f10','f11','f12','f13','f14','f15','f16','f17','f18']
df = pd.DataFrame(aa[0:1320],columns=hah)
average = np.mean(df,axis=0)
raw = df.values
raw = np.insert(raw,0,values=average,axis=0)

# boy
df2 = pd.DataFrame(aa[1322:2642],columns=hah)
average2 = np.mean(df2,axis=0)
raw2 = df2.values
raw2 = np.insert(raw2,0,values=average2,axis=0)

def getDistance(df):
    df = df.values
    # calculate the mean of each column
    average = np.mean(df,axis=0)

    # minus the mean
    df = df - average
    # insert average value into first column
    df = np.insert(df,0,values=average,axis=0)
    # calculate the square of each column
    df = np.square(df)
    # sum up all the value of each column
    df = np.sum(df,axis=1)
    #  sqrt the value
    df = np.sqrt(df)
    # transpose the matrix
    df = np.reshape(df,[-1,1])
    content = pd.DataFrame(df, columns=['Distance'])
    return content

def getDistanceFromOthers(df,df2):
    df = df.values
    # calculate the mean of each column
    average = np.mean(df2,axis=0).values

    # minus the mean

    df = df - average

    # insert average value into first column
    df = np.insert(df,0,values=average,axis=0)
    # calculate the square of each column
    df = np.square(df)
    # sum up all the value of each column
    df = np.sum(df,axis=1)
    #  sqrt the value
    df = np.sqrt(df)
    # transpose the matrix
    df = np.reshape(df,[-1,1])
    content = pd.DataFrame(df, columns=['Distance'])
    return content



print('每个列的平均数：',average.values)
print('原始数据：',raw)
print('每行数据距离：',getDistance(df))
print('/////////////////////////////////////////////')






def compareProcess(now,last,lastoflast):
    return (now[0]+ last[0] + lastoflast[0])



# ===========================================
import time
if __name__ == '__main__':
    currenttime = time.time()
    # pop list
    pop = []
    # record outlier number
    record = []
    index = []
    index2 = []
    # 加载数据
    matrix1 = getDistance(df).values.tolist()
    matrix2 = getDistance(df2).values.tolist()

    matrix3 = getDistanceFromOthers(df,df2).values.tolist()
    matrix4 = getDistanceFromOthers(df2,df).values.tolist()


    print('shapeeeeeee',matrix1)
    for b in range(len(matrix1)):
        if b>2:
            now = matrix1[b]
            last = matrix1[b-1]
            lastoflast = matrix1[b-2]

            now2 = matrix2[b]
            last2 = matrix2[b-1]
            lastoflast2 = matrix2[b-2]

            now3 = matrix3[b]
            last3 = matrix3[b-1]
            lastoflast3 = matrix3[b-2]

            now4 = matrix4[b]
            last4 = matrix4[b-1]
            lastoflast4 = matrix4[b-2]



            if b-1 in index:
                last = [0]
            if b-2 in index:
                lastoflast = [0]

            if b-1 in index2:
                last2 = raw2[0]
            if b-2 in index2:
                lastoflast2 = [0]


            # girl
            distance1 = compareProcess(now,last,lastoflast)
            # boy
            distance2 = compareProcess(now2,last2,lastoflast2)
            # girl - boy
            distance3 = compareProcess(now3,last2,lastoflast2)
            # boy - girl
            distance4 = compareProcess(now4,last,lastoflast)

            Adistance = 0
            Bdistance = 0
            if distance1 > distance3:
                Adistance = distance3
            else:
                Adistance = distance1

            if distance2 > distance4:
                Bdistance = distance4
            else:
                Bdistance = distance2

            # print('distanceA',Adistance)
            # print('distanceB',Bdistance)

            # hyper paremeter
            if (Adistance > 934.8) :
                print('outlier',raw[b])
                # add label
                record.append(raw[b])
                index.append(b)
                print('now', now)
                print('last', last)
                print('lastoflast', lastoflast)
                print('current index', b)
                print('finnal Adisntance ',Adistance)
                print('===============')

                print('outlier',raw2[b])
                # add label
                record.append(raw2[b])
                index2.append(b)
                print('now', now2)
                print('last', last2)
                print('lastoflast', lastoflast2)
                print('current index', b)
                print('finnal Bdisntance ',Bdistance)
                print('===============')


            else:
                pop.append(raw[b])
                pop.append(raw2[b])


    print(record)
    print(index)
    print(index2)
    newindex = [i - 1 for i in index]
    newindex2 = [i - 1 +30 for i in index2]

    all = pd.DataFrame(aa, index=newindex)
    all2 = pd.DataFrame(aa,index=newindex2)
    result = pd.concat([all,all2],axis=0)
    print(result)
    print(result['label'].value_counts())
    print(aa['label'].value_counts())






















    print('spending time : ',time.time()-currenttime)


