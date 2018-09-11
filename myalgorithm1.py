import math
import sklearn

# normal data [[75:90,75:90]]
data = [[78,87],[83,85],[60,47],[88,90],[95,97],[65,78],[60,86],[79,88],[90,81]]


# calculate aver
feature1 = 0
feature2 = 0
for i in data:
    feature1 = i[0] +feature1
    feature2 = i[1] +feature2

aveone = feature1/len(data)
avetwo = feature2/len(data)
print(aveone,avetwo)
print(len(data))

def getdistance(aveone,avetwo,a,b,c):

    a = pow(aveone - a[0], 2) + pow(avetwo - a[1], 2)
    a_total = pow(a,0.5)

    b = pow(aveone - b[0], 2) + pow(avetwo - b[1], 2)
    b_total = pow(b,0.5)

    c = pow(aveone - c[0], 2) + pow(avetwo - c[1], 2)
    c_total = pow(c,0.5)

    total = a_total+b_total+c_total
    return total

# pop list
pop = []
# record outlier number
record = []

# circle  = 3
for b in range(len(data)):
    if b>=2:
        now = data[b]
        last = data[b-1]
        lastoflast = data[b-2]
        if last in record:
            # last = math.sqrt((last-ave)*(last-ave))
            last = [aveone,avetwo]
        if lastoflast in record:
            # lastoflast = math.sqrt((lastoflast - ave) * (lastoflast - ave))
            lastoflast = [aveone,avetwo]


        distance = getdistance(aveone,avetwo,now,last,lastoflast)

        # hyper paremeter
        if distance > 25:
            print('outlier',data[b])
            # add label
            record.append(data[b])
            print('now', now)
            print('last', last)
            print('lastoflast', lastoflast)
            print('current record',record)
            print('current index', b)
            print('===============')


        else:
            pop.append(data[b])

print('outlier',record)
