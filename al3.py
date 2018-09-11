from pandas import Series
import pandas as  pd

list = []
a = [1,2,3]

x = Series([1,2,3,4])
content = pd.DataFrame([1,2,3,4])

if __name__ == '__main__':

    if x not in content:
        print('no')


