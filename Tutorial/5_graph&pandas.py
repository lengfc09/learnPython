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

fig.add_subplot(3, 1, 1)
ts.plot()
fig.add_subplot(3, 1, 2)
ts.resample("3M").mean().plot()
fig.add_subplot(3, 1, 3)
ts.resample("M").sum().plot()
plt.show()


#-------

x = np.random.randn(1000)
plt.hist(x, bins=40, edgecolor="#000000")
data = pd.read_excel("GPV_VALUES.xls", sheetname="新模型")
print(data.head())
plt.show()
