
import random
import numpy as np

ls = [0, 1, 2, 3, 5, 7, 10, 15, 20, 30, 50]
rates = [0.35, 0.2, 0.6, 0.1, 0.4]
disc = []
for item in range(ls[-1]):
    disc.append(random.choice(rates))

cashflows = [8 for item in range(ls[-1])]


def changerates(ls, n, dv, rates):
    e_pd = np.arange(ls[n - 1], ls[n + 1], 1)
    rates_pd = []
    for tt in e_pd:
        if tt < ls[n]:
            rates_pd.append((tt - ls[n - 1]) / (ls[n] - ls[n - 1]) * dv)
        else:
            rates_pd.append((ls[n + 1] - tt) / (ls[n + 1] - ls[n]) * dv)
    if ls[n - 1] > 0:
        rates[ls[n - 1] - 1:ls[n + 1] - 1] = rates[ls[n - 1] - 1:ls[n + 1] - 1] + rates_pd
    else:
        rates[ls[n - 1]:ls[n + 1] - 1] = rates[ls[n - 1]:ls[n + 1] - 1] + rates_pd[1:]
    return rates


print(rates[6])
rates2


dd = [1., 3]
ff = [4, 5]


# for d, f in dd, ff:
#     print("{} and {}".format(f, d))

def present_value(cashflows, discrates):
    pv = 0
    for i, (cf, disc) in enumerate(zip(cashflows, discrates)):
        pv = pv + cf / (1 + disc / 100)**(i + 1)
    return pv


print(present_value(cashflows, disc))
