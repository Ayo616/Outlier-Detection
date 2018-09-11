import math


# normal data [15-25]
# outlier data [1-3] [50-55]
data = [16,17,3,2,5,2,2,2,2,23,2,21,19,20,4,100,24,26,1,23,26]


# calculate aver
sum = 0
for i in data:
    sum = sum + i

ave = sum/len(data)
print(ave)
def getdistance(ave,a,b,c):
    total =(ave-a)*(ave-a)+(ave-b)*(ave-b)+(ave-c)*(ave-c)
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
            last = ave
        if lastoflast in record:
            # lastoflast = math.sqrt((lastoflast - ave) * (lastoflast - ave))
            lastoflast = ave

        distance = getdistance(ave,now,last,lastoflast)


        if distance > 100:
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

