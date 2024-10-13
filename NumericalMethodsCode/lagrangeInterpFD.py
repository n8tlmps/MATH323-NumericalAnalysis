# Lab Assignment 5
# Nate Talampas
# FDapprox is an array that gives approximation of function values at points xp
# xp is an array that consists of x-coordinates where we want the function values approximated

import numpy as np
from newtonDivDiff import newtonDivDiff
def lagrangeInterpFD(xx, ff, ffd, xp):
    FDcoeff, _ = newtonDivDiff(xx, ff) # call newtonDivDiff to get coeff a0, a1, ..., an
    n = len(xx)

    FDapprox = FDcoeff[0] # give a0 to FDapprox
    for k in range(1, n): # loop through k = 1, ..., n
        prod = (xp - xx[0])
        for m in range(1, k): # loop over m = 1, ..., k-1
            prod *= (xp - xx[m])
        FDapprox += FDcoeff[k] * prod
    return FDapprox

