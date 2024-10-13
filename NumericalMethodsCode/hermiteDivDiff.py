import numpy as np

def hermiteDivDiff(xx, ff, ffd):
    # find number of points (n+1)
    n = len(xx) - 1
    # reserve space for B(2n+2, 2n+2)
    B = np.zeros((2*n+2, 2*n+2))
    # make z array
    z = np.zeros(2*n+2)
    # fill xx's in the z array
    z[0::2] = xx
    z[1::2] = xx
    # fill ff's in the 0th column of B
    B[0::2,0] = ff
    B[1::2,0] = ff
    # 1st column of B w/ f'
    B[1::2,1] = ffd
    # rest of 1st col of B with 1
    for i in range(2, 2*n + 2, 2):
        B[i, 1] = (B[i, 0] - B[i-1, 0]) / (z[i] - z[i-1])
    # rest of B
    for i in range(2, 2*n + 2):
        for j in range(2, i+1):
            # div-diff from last time
            B[i, j] = (B[i, j-1] - B[i-1, j-1]) / (z[i] - z[i-j])
    # take diagonal of B as output
    diag = np.diag(B)
    return diag