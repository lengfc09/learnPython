def americanPut(T, S, K, r, sigma, q, n):
    # T... expiration time
    # S... stock price
    # K... strike price
    # q... dividend yield
    # n... height of the binomial tree
    from math import exp
    from math import sqrt
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
    from math import exp
    from math import sqrt
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
    from math import exp
    from math import sqrt
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
    from math import exp
    from math import sqrt
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


if __name__ == "__main__":
    print(americanCall(1, 100, 102, 0.02, 0.03, 0, 250))
    print(americanPut(1, 100, 102, 0.02, 0.03, 0, 250))
    # call_put parity
    print(euroCall(1, 100, 102, 0.02, 0.03, 0, 250))
    print(euroPut(1, 100, 102, 0.02, 0.03, 0, 250))
    print(call_put(1, 100, 102, 0.02, 0.03, 0, 250))
else:
    pass
