"""
Binomial_tree method include:
1. americanPut
2. americanCall
3. euroCall
4. euroPut
=============
For Comparion, the analytic solution are also given for euro type options
5. PutOption
6. CallOption
"""
from math import exp
from math import sqrt


def americanPut(T, S, K, r, sigma, q, n):
    # T... expiration time
    # S... stock price
    # K... strike price
    # q... dividend yield
    # n... height of the binomial tree
    # from math import exp
    # from math import sqrt
    deltaT = T / n
    up = exp(sigma * sqrt(deltaT))
    p0 = (up * exp(-q * deltaT) - exp(-r * deltaT)) / (up**2 - 1)
    p1 = exp(-r * deltaT) - p0

    # initial values at time T
    p = []
    for i in range(n + 1):
        p.append(max(K - S * up**(2 * i - n), 0))
    # move to earlier times
    for j in range(n - 1, -1, -1):
        for i in range(j + 1):
            p[i] = p0 * p[i + 1] + p1 * p[i]
            exercise = K - S * up**(2 * i - j)
            p[i] = max(p[i], exercise)
    return p[0]


def americanCall(T, S, K, r, sigma, q, n):
    # from math import exp
    # from math import sqrt
    deltaT = T / n
    up = exp(sigma * sqrt(deltaT))
    p0 = (up * exp(-q * deltaT) - exp(-r * deltaT)) / (up**2 - 1)
    p1 = exp(-r * deltaT) - p0

    # initial values at time T
    p = []
    for i in range(n + 1):
        p.append(max(S * up**(2 * i - n) - K, 0))

    # move to earlier times
    for j in range(n - 1, -1, -1):
        for i in range(j + 1):
            p[i] = p0 * p[i + 1] + p1 * p[i]
            exercise = S * up**(2 * i - j) - K
            p[i] = max(p[i], exercise)
    return p[0]


def call_put(T, S, K, r, sigma, q, n):
    from math import exp
    return S - K * exp(-r * T)


def euroCall(T, S, K, r, sigma, q, n):
    # from math import exp
    # from math import sqrt
    deltaT = T / n
    up = exp(sigma * sqrt(deltaT))
    p0 = (up * exp(-q * deltaT) - exp(-r * deltaT)) / (up**2 - 1)
    p1 = exp(-r * deltaT) - p0
    # initial values at time T
    p = []
    for i in range(n + 1):
        p.append(max(S * up**(2 * i - n) - K, 0))
    # move to earlier times
    for j in range(n - 1, -1, -1):
        for i in range(j + 1):
            p[i] = p0 * p[i + 1] + p1 * p[i]
    return p[0]


def euroPut(T, S, K, r, sigma, q, n):
    # from math import exp
    # from math import sqrt
    deltaT = T / n
    up = exp(sigma * sqrt(deltaT))
    p0 = (up * exp(-q * deltaT) - exp(-r * deltaT)) / (up**2 - 1)
    p1 = exp(-r * deltaT) - p0
    # initial values at time T
    p = []
    for i in range(n + 1):
        p.append(max(K - S * up**(2 * i - n), 0))
    # move to earlier times
    for j in range(n - 1, -1, -1):
        for i in range(j + 1):
            p[i] = p0 * p[i + 1] + p1 * p[i]
    return p[0]


from math import log
import matplotlib.pyplot as plt
import scipy.stats


def d1(S, K, r, sigma, T, q=0):
    """ the dividend yield is set to be zero by default
    """
    return (log(S / float(K)) + (r - q + sigma**2 / 2) * T) / (sigma * sqrt(T))


def d2(S, K, r, sigma, T, q=0):
    return d1(S, K, r, sigma, T, q) - (sigma * sqrt(T))


def PutOption(S, K, r, sigma, T, q=0):
    return (K * exp(-r * T) * scipy.stats.norm.cdf(-d2(S, K, r, sigma, T, q))) - (S * exp(-q * T) * scipy.stats.norm.cdf(-d1(S, K, r, sigma, T, q)))


def CallOption(S, K, r, sigma, T, q=0):
    return S * exp(-q * T) * scipy.stats.norm.cdf(d1(S, K, r, sigma, T, q)) - K * exp(-r * T) * scipy.stats.norm.cdf(d2(S, K, r, sigma, T, q))


if __name__ == "__main__":
    # americanPut(T, S, K, r, sigma, q, n):
    T = 5 / 12.0
    NNN = 1000  # The periods in Binomial model
    q = 0
    S = 100
    K = 100
    r = 0.1
    sigma = 0.25

    print(americanCall(T, S, K, r, sigma, q, NNN))
    print(americanPut(T, S, K, r, sigma, q, NNN))
    # call_put parity
    print("Euro Put call price by Binomial Tree:")
    print(euroCall(T, S, K, r, sigma, q, NNN))
    print("Euro Put option price by Binomial Tree:")
    print(euroPut(T, S, K, r, sigma, q, NNN))
    print("Euro Put option price by analytic solution:")
    print(PutOption(S, K, r, sigma, T, q))
    print("Euro call option price by analytic solution:")
    print(CallOption(S, K, r, sigma, T, q))
    print(call_put(T, S, K, r, sigma, q, NNN))
else:
    pass
