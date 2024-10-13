# This program implements the Implicit Trapezoidal method
# to solve ODE IVP
# Nate Talampas, 4/24/2024
import numpy as np
from newton import newton


def ImTrapezoidal(f, fdery, a, b, alpha, N, tol, maxN):
    # step size
    h = (b - a) / N
    
    # time steps
    t = np.linspace(a, b, N+1)

    # allocate space for w
    w = np.zeros(N+1)

    # initial condition
    w[0] = alpha

    # loop through 1,..,N
    for i in range(N):

        k1 = w[i] + (h/2) * f(t[i], w[i])

        w0 = k1
        j = 1
        FLAG = 0

        # Newton's method
        while FLAG == 0:
            w_new = w0 - (w0 - (h/2) * f(t[i+1], w0) - k1) / (1 - (h/2) * fdery(t[i+1], w0))

            if abs(w_new - w0) < tol:
                FLAG = 1
            else:
                j += 1
                w0 = w_new
                if j > maxN:
                    print("The maximum number of iterations exceeded")
                    return t, w
                
        w[i+1] = w_new
        t[i+1] = a + (i+1) * h

    return t, w
