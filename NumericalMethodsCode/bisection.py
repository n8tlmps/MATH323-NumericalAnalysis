import numpy as np

def bisection(f, a, b, tol, maxN):
    if (f(a) * f(b) > 0):
        print("There may not be a root.")
        p = np.NaN
    elif (f(a) * f(b) == 0):
        if f(a) == 0:
            p = a
        elif f(b) == 0:
            p = b
    else:
        iter = 0
        p = 1
        while (np.abs(f(p)) > 0) and (iter < maxN) and (np.abs((b-a)/2) > tol):
            p = (a+b)/2
            if f(a) * f(p) < 0:
                b = p
            else:
                a = p
            iter += 1
    return p, iter