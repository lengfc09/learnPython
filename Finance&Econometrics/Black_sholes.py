import numpy as np
import scipy.sparse.linalg
import Thomas
"""
PDE solver for American style Options with Black-Sholes Model
Use Thomas method if N<=500, otherwise scipy.sparse.linalg.spsolve()

Parameters:
Method:
0: Thomas Method by default
1: standard np.linalg.solve
2. Sparse method:  scipy.sparse.linalg.spsolve
3. Let the program decide

"""

############
#               American Call
############


def AmericanCall_CN(Smax, M, T, N, K, r, sigma, method=3):

    # discretization
    M = int(M)
    N = int(N)
    dt = T / float(N)  # The time step
    dS = Smax / float(M)  # The price step

    # initializing the risk neutral probabilities

    P = [0.25 * sigma**2 * i**2 * dt - 0.25 * r * i * dt for i in range(1, M)]
    Q = [-0.5 * sigma**2 * i**2 * dt - 0.5 * r * dt for i in range(1, M)]
    # Q the main diagonal: 1+Q for u^(n+1), 1-Q for u^(n-1)
    R = [0.25 * sigma**2 * i**2 * dt + 0.25 * r * i * dt for i in range(1, M)]

    # computes the matrices A and B

    x = np.array
    A = np.diag(1 - x(Q)) + np.diag(-x(P[1:M - 1]), k=-1) + np.diag(-x(R[0:M - 2]), k=1)
    B = np.diag(1 + x(Q)) + np.diag(x(P[1:M - 1]), k=-1) + np.diag(x(R[0:M - 2]), k=1)

    # For Thomas method, we use mode=0, so that P,Q,R=a,b,c
    # For Scipy.sparse.linalg.spsolve, we need to construct the sparse matrix:

    diagonals = np.zeros((3, M - 1))
    diagonals[0, :-1] = -x(P[1:M - 1])
    diagonals[1, :] = 1 - x(Q)
    diagonals[2, :] = -x(R)

    f = np.zeros((N + 1, M + 1))  # the matrix for the option price

    # boundary conditions
    f[:, 0] = 0
    f[:, M] = [Smax - K * np.exp(-r * (N - j) * dt) for j in range(N + 1)]  # ignore the K?
    f[N, :] = np.maximum(np.arange(0, Smax + dS / 2.0, dS, dtype=np.float) - K, 0)

    f = np.matrix(np.array(f))

    for j in range(N - 1, -1, -1):  # the discounting process
        b = np.zeros((M - 1, 1))  # computes the matrix b

        # inserts the first and the last element
        b[0] = (0.25 * sigma**2 * dt - 0.25 * r * 1 * dt) * (f[j, 0] + f[j + 1, 0]) * 0.5
        b[M - 2] = (0.25 * dt * (sigma**2 * (M - 1)**2 + r * (M - 1))) * (f[j, M] + f[j + 1, M]) * 0.5
        # The Standard Linalg sovler
        Right_bb = (B * f[j + 1, 1:M].transpose() + b)
        if method == 0:
            # The Thomas Solver
            G = Thomas.TDMAsolver(-x(P), 1 - x(Q), -x(R), Right_bb, mode=0)
        elif method == 1:
            G = (np.linalg.inv(A)) * Right_bb   # solves for f_{i,j}
        elif method == 2:
            # The Sparse Solver
            A_sparse = scipy.sparse.diags(diagonals, [-1, 0, 1], [M - 1, M - 1], format='csc')
            G = scipy.sparse.linalg.spsolve(A_sparse, Right_bb)
        else:
            if M * N >= 25000:
                A_sparse = scipy.sparse.diags(diagonals, [-1, 0, 1], [M - 1, M - 1], format='csc')
                G = scipy.sparse.linalg.spsolve(A_sparse, Right_bb)
            else:
                G = Thomas.TDMAsolver(-x(P), 1 - x(Q), -x(R), Right_bb, mode=0)

        f[j, 1:M] = G.transpose()
        f[j, :] = np.maximum(np.matrix(np.arange(0, Smax + dS / 2.0, dS, dtype=np.float)) - K, f[j, :])
    return f[0, (M + 1) / 2.0]


############
#               American Put
############

def AmericanPut_CN(Smax, M, T, N, K, r, sigma, method=3):

    # discretization
    M = int(M)
    N = int(N)
    dt = T / float(N)  # The time step
    dS = Smax / float(M)  # The price step

    # initializing the risk neutral probabilities

    P = [0.25 * sigma**2 * i**2 * dt - 0.25 * r * i * dt for i in range(1, M)]
    Q = [-0.5 * sigma**2 * i**2 * dt - 0.5 * r * dt for i in range(1, M)]
    # Q the main diagonal: 1+Q for u^(n+1), 1-Q for u^(n-1)
    R = [0.25 * sigma**2 * i**2 * dt + 0.25 * r * i * dt for i in range(1, M)]

    # computes the matrices A and B

    x = np.array
    A = np.diag(1 - x(Q)) + np.diag(-x(P[1:M - 1]), k=-1) + np.diag(-x(R[0:M - 2]), k=1)
    B = np.diag(1 + x(Q)) + np.diag(x(P[1:M - 1]), k=-1) + np.diag(x(R[0:M - 2]), k=1)

    # For Thomas method, we use mode=0, so that P,Q,R=a,b,c
    # For Scipy.sparse.linalg.spsolve, we need to construct the sparse matrix:

    diagonals = np.zeros((3, M - 1))
    diagonals[0, :-1] = -x(P[1:M - 1])
    diagonals[1, :] = 1 - x(Q)
    diagonals[2, :] = -x(R)

    f = np.zeros((N + 1, M + 1))  # the matrix for the option price

    # boundary conditions
    f[:, 0] = [K * np.exp(-r * (N - j) * dt) for j in range(N + 1)]
    f[:, M] = 0
    f[N, :] = np.maximum(K - np.arange(0, Smax + dS / 2.0, dS, dtype=np.float), 0)

    f = np.matrix(np.array(f))

    for j in range(N - 1, -1, -1):  # the discounting process
        b = np.zeros((M - 1, 1))  # computes the matrix b

        # inserts the first and the last element
        b[0] = (0.25 * sigma**2 * dt - 0.25 * r * 1 * dt) * (f[j, 0] + f[j + 1, 0]) * 0.5
        b[M - 2] = (0.25 * dt * (sigma**2 * (M - 1)**2 + r * (M - 1))) * (f[j, M] + f[j + 1, M]) * 0.5
        # The Standard Linalg sovler
        Right_bb = (B * f[j + 1, 1:M].transpose() + b)
        if method == 0:
            # The Thomas Solver
            G = Thomas.TDMAsolver(-x(P), 1 - x(Q), -x(R), Right_bb, mode=0)
        elif method == 1:
            G = (np.linalg.inv(A)) * Right_bb   # solves for f_{i,j}
        elif method == 2:
            # The Sparse Solver
            A_sparse = scipy.sparse.diags(diagonals, [-1, 0, 1], [M - 1, M - 1], format='csc')
            G = scipy.sparse.linalg.spsolve(A_sparse, Right_bb)
        else:
            if M * N >= 25000:
                A_sparse = scipy.sparse.diags(diagonals, [-1, 0, 1], [M - 1, M - 1], format='csc')
                G = scipy.sparse.linalg.spsolve(A_sparse, Right_bb)
            else:
                G = Thomas.TDMAsolver(-x(P), 1 - x(Q), -x(R), Right_bb, mode=0)

        f[j, 1:M] = G.transpose()
        f[j, :] = np.maximum(K - np.matrix(np.arange(0, Smax + dS / 2.0, dS, dtype=np.float)), f[j, :])
    return f[0, (M + 1) / 2.0]


if __name__ == "__main__":
    print("The value of an American call option is", AmericanCall_CN(150, 500, 5 / 12.0, 100, 50, 0.1, 0.25, method=1))
else:
    pass
