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

col = ['Temperature','Humidity','Light','CO2','HumidityRatio']
aa = pd.read_csv('./dataset/newdata.csv')
# df = pd.DataFrame(aa,columns=col)
df = pd.DataFrame(aa,columns=['f1','f2','f3'])


average = np.mean(df,axis=0)
raw = df.values
raw = np.insert(raw,0,values=average,axis=0)


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


print('每个列的平均数：',average.values)
print('原始数据：',raw)
print('每行数据距离：',getDistance(df))
print('/////////////////////////////////////////////')






def compareProcess(now,last,lastoflast):
    return (now[0]+ last[0] + lastoflast[0])



# ===========================================
import time
threld = [2.96332,2.9,3.15,3.18,3.6]
if __name__ == '__main__':
    currenttime = time.time()
    # p op list
    pop = []
    # record outlier number
    record = []
    index = []
    # 加载数据
    data = getDistance(df).values.tolist()

    for epoch in range(4):
        print('length of data ', len(data))
        for b in range(len(data)):
            if b > 2:
                now = data[b]
                last = data[b - 1]
                lastoflast = data[b - 2]

                if b - 1 in index:
                    last = [0]
                if b - 2 in index:
                    # lastoflast = math.sqrt((lastoflast - ave) * (lastoflast - ave))
                    lastoflast = [0]

                distance = compareProcess(now, last, lastoflast)

                # hyper paremeter
                if distance > threld[epoch]:
                    print('outlier', raw[b])
                    # add label
                    record.append(raw[b])
                    index.append(b)
                    print('now', now)
                    print('last', last)
                    print('lastoflast', lastoflast)
                    print('current record', record)
                    print('current index', b)
                    print('===============')

                else:
                    pop.append(raw[b])

        data = np.delete(data, index, axis=0)
        raw = np.delete(raw,index,axis=0)

    print(record)
    print(index)
    newindex = [i - 1 for i in index]
    result = pd.DataFrame(aa, index=newindex)
    print(result)
    print(result['label'].value_counts())
    print(aa['label'].value_counts())






    print('spending time : ',time.time()-currenttime)


    import matplotlib.pyplot as plt
    from mpl_toolkits.mplot3d import Axes3D
    aab = aa.drop(newindex)
    x,y,z = aab['f1'],aab['f2'],aab['f3']

    ax = plt.figure().add_subplot(111,projection = '3d')

    ax.scatter(x,y,z,c='g')

    ox,oy,oz = result['f1'],result['f2'],result['f3']
    ax.scatter(ox,oy,oz,c ='r')

    ax.set_xlabel('x_feature')
    ax.set_ylabel('y_feature')
    ax.set_zlabel('z_feature')

    plt.savefig('3d_dataset2.png')

    plt.show()


