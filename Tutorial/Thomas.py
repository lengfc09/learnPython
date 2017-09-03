try:
    import numpypy as np    # for compatibility with numpy in
    # print("import numpypy")
except:
    import numpy as np      # if using numpy in cpython
    print("Using Thomas Here")
    # print("import numpy")

# Tri Diagonal Matrix Algorithm(a.k.a Thomas algorithm) solver


def TDMAsolver(a, b, c, d, mode=0):
    '''
    TDMA solver, a b c d can be NumPy array type or Python list type.
    refer to http://en.wikipedia.org/wiki/Tridiagonal_matrix_algorithm
    Mode:0
    b_0      c_0
    a_1      b_1      c_1
                a_2      b_2
    a[0]==0, c[n]==0; they will not be read
    Mode:1, all starts form the first element
    b_0      c_0
    a_0      b_1      c_1
                a_1      b_2
    '''
    if mode == 1:
        tem = [0]
        tem.extend(a)
        a = tem
    nf = len(b)     # number of equations
    ac, bc, cc, dc = map(np.array, (a, b, c, d))     # copy the array
    for it in range(1, nf):
        mc = ac[it] / bc[it - 1]
        bc[it] = bc[it] - mc * cc[it - 1]
        dc[it] = dc[it] - mc * dc[it - 1]

    xc = bc
    xc[-1] = dc[-1] / bc[-1]

    for il in range(nf - 2, -1, -1):
        xc[il] = (dc[il] - cc[il] * xc[il + 1]) / bc[il]

    del bc, cc, dc  # delete variables from memory

    return xc
