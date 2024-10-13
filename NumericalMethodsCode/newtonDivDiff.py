# Lab Assignment 5
# Nate Talampas

# FDcoeff, BDcoeff are arrays that consist of the coefficients of the Lagrange interpolating polynomial.
# FDcoeff(i+1) = f[x0, x1, ..., xi]
# BDcoeff(i+1) = f[xn, x1, ..., xn-1]
# xx consists of x0, x1, ..., xn
# ff consists of f(x0), f(x1), ..., f(xn)

import numpy as np

def newtonDivDiff(xx, ff):
    n = len(xx)
    # find num of rows & cols of A
    rows = n
    columns = n
    #initialize matrix A
    A = np.empty(shape=(rows, columns))
    # fill the 1st column with ff
    A[:, 0] = ff
    # loop over i from 1 to n
    for i in range(1, n):
        for j in range(1, i+1): # and loop over j from 1 to i
            A[i, j] = (A[i, j-1] - A[i-1, j-1]) / (xx[i] - xx[i-j])

    FDcoeff = np.diag(A) # coefficient of forward diff
    BDcoeff = A[-1, :] # coefficient of backward diff

    return FDcoeff, BDcoeff
