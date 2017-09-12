"""
This is for Binomial Tree model
"""
# from binomial_tree import americanPut
# from binomial_tree import americanCall


# print(americanPut(1, 100, 102, 0.02, 0.03, 0, 250))
# print(americanCall(1, 100, 102, 0.02, 0.03, 0, 250))

"""
This is for Thomas Algorithm
"""
import numpy as np
import Thomas
a = np.ones(300, dtype=np.float)
b = 2 * np.ones(300, dtype=np.float)
c = 0.5 * np.ones(300)
dd = np.random.randn(300, 1)
import time
t1 = time.clock()
xxx = Thomas.TDMAsolver(a, b, c, dd, mode=1)
t2 = time.clock()
print("Thomas Algorithem takes {} to finish".format(t2 - t1))
# print(xxx)

N = 300
diagonals = np.zeros((3, N))   # 3 diagonals
diagonals[0, :] = a
diagonals[1, :] = b
diagonals[2, :] = c

# Scipy Sparse
import scipy.sparse
A = scipy.sparse.diags(diagonals, [-1, 0, 1], [N, N], 'csc')
# print(A.toarray())    # look at corresponding dense matrix
import scipy.sparse.linalg
t3 = time.clock()
x = scipy.sparse.linalg.spsolve(A, dd)
t4 = time.clock()
print("the sparse linear algorithem takes {} to finish".format(t4 - t3))
# print(x)


# Standard Linear system Solver
A_d = A.toarray()
std_b = np.dot(A_d, x)
t5 = time.clock()
std_x = np.linalg.solve(A_d, std_b)
t6 = time.clock()
print("the standard linear algorithem takes {} to finish".format(t6 - t5))
# print(x)
