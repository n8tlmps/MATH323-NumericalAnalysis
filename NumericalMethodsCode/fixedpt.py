import numpy as np
def fixedpt(g, p0, tol, maxN):
    iter = 1
    p = g(p0)
    while (iter < maxN) and (np.abs(p - p0) > tol):
        p0 = p
        p = g(p0)
        iter += 1
    return p, iter
    