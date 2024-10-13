# This function gives approximations of function values using natural cubic spline
# Last update: Chung-min Lee, Feb 28, 2024

import numpy as np
from naturalSpline import naturalSpline

def naturalSplineInterp(xx, ff, xp):
    #find the coefficents of the piecewise cubic polynomials
    a, b, c, d = naturalSpline(xx,ff)

    # number of intervals
    nspline = len(xx)-1

    # set up an array to hold approximations
    NSapprox = np.zeros(xp.size)

    # first cubic polynomial S_0(x)
    ind1 = (xp < xx[1])
    NSapprox[ind1] = a[0] + b[0]*(xp[ind1]-xx[0]) + c[0]*(xp[ind1]-xx[0])**2 + d[0]*(xp[ind1]-xx[0])**3

    # cubic polynomials S_1(x) to S_{n-2}(x)
    for i in range(1,nspline):
        ind = np.logical_and((xp >= xx[i]), (xp < xx[i+1]))
        NSapprox[ind] = a[i] + b[i]*(xp[ind]-xx[i]) + c[i]*(xp[ind]-xx[i])**2 + d[i]*(xp[ind]-xx[i])**3
    # endfor

    # last cubic polynomial S_{n-1}(x)
    inde = (xp >= xx[-2])
    NSapprox[inde] = a[-1] + b[-1]*(xp[inde]-xx[-2]) + c[-1]*(xp[inde]-xx[-2])**2 + d[-1]*(xp[inde]-xx[-2])**3
    
    return NSapprox


