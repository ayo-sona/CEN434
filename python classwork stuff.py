print('Hello World')

import numpy as np

b = [1, 0, 0, 1]
a = np.array(b)
a = a.reshape(2,2)
print(a)

d = dict()
d ={'Age': 20,
    'Height': 1.7,
    'Color': 'black',
    }
d['Age'] = 21
d['Height'] = 1.8
d['Color'] = 'white'
print(d)

if 'Age' in d:
  print(d['Age'])

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
xp = np.array(x)
yp = np.array(y)
plt.plot(xp, yp)
plt.show()

import pandas as pd

data = {'x': [1,2,3,4,5], 'y': [2,4,6,8,10]}
df = pd.DataFrame(data)
print(df)

a = df.to_numpy()
print(a)

a.reshape(2,5)
a.reshape(5,2)
