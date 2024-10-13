import numpy as np

from hermiteDivDiff import hermiteDivDiff
def hermiteInterp(xx, ff, ffd, xp):
    FDcoeff = hermiteDivDiff(xx, ff, ffd)
     # make z array
    z = np.zeros(2 * len(xx))
    # fill xx's in the z array
    z[0::2] = xx
    z[1::2] = xx
    n = len(z)

    FDapprox = FDcoeff[0]
    for k in range(1, n):
        prod = (xp - z[0])
        for m in range(1, k):
            prod *= (xp - z[m])
        FDapprox += FDcoeff[k] * prod
    return FDapprox