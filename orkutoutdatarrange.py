import numpy as np
import pandas as pd
data = pd.read_csv('orkut/data.csv')
data = np.array(data)
labels = pd.read_csv('orkut/outputCom2d.csv')
labels = np.array(labels)
x= np.zeros(5001,dtype=np.int64)
for i in data:
    x[int(i[0])] = 1
    x[int(i[1])] = 1
print(x)
counter = 0
for i in range(len(x)):
    if(x[i]==1):
        x[i] = labels[counter]
        counter=counter+1
print(x)
Com = {'communities':x}
df = pd.DataFrame(Com, columns = ['communities'])
df.to_csv('orkut/outputCom2d.csv')
