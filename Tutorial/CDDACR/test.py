import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt
# dates = pd.date_range("20130101", periods=6, freq='M')
# print(dates)
# timdeta = dates[4] - dates[1]
# print(timdeta)
# df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
# print(df['A'])
# print(df.A)

num = [1, 2, 3, 4, 5]


def myfun(n):
    return n * n

for i in map(myfun, num):
    print(i)

num2 = list(map(myfun, num))
print(num2)

rng = pd.date_range("1/1/2012", periods=1000, freq="D")
ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
fig = plt.figure()

fig.add_subplot(1, 2, 1)
ts.plot()
fig.add_subplot(1, 2, 2)
ts.resample("11M").sum().plot()
plt.show()
