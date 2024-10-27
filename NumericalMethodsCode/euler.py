# this program does the Euler method on ODE IVPs
#

import numpy as np
def euler(f,a,b,alpha,N):
    # step size
    h = (b - a) / N
    
    # time steps
    t = np.linspace(a, b, N+1)

    # allocate space for w
    w = np.zeros(N+1)

    # initial condition
    w[0] = alpha

    # loop through ti
    for i in range(1, N+1):
        # calculate w_{i+1}
        w[i] = w[i-1] + h * f(t[i-1], w[i-1])
        t[i] = a + i * h
    
    return t,w
