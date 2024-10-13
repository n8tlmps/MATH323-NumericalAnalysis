# this program implements the Adams fourth order Predictor-Corrector
# algorithm with Runge-Kutta 4 to find initial values
#
# Last update: Nate Talampas, 4-17-24

import numpy as np
def Adams4PredictCorrect(f,a,b,alpha,N):
    # set step size
    h = (b - a) / N

    # set all ti
    t = np.linspace(a, b, N+1)
    t[0] = a
    
    # reserve space for w
    w = np.zeros(N+1)
    w[0] = alpha

    # find w0, w1, w2, w3 by Runge-Kutta 4th order program
    # for other time steps
    for i in range(1, N+1):
    
        # calculate k1, k2, k3, k4
        k1 = h*f(t[i-1],w[i-1])
        k2 = h*f(t[i-1]+h/2, w[i-1]+k1/2)
        k3 = h*f(t[i-1]+h/2, w[i-1]+k2/2)
        k4 = h*f(t[i-1]+h, w[i-1]+k3)

    # put w0, w1, w2, w3 into w
        w[i] = w[i-1] + (k1 + 2*k2 + 2*k3 + k4)/6
        t[i] = a + i*h

    # advance in time from ti = 4,...,N 
    for i in range(3, N):
    
        # do Adams-Bashforth to predict
        w[i+1] = w[i] + h*(55*f(t[i], w[i]) - 59*f(t[i-1], w[i-1]) + 37*f(t[i-2], w[i-2]) -9*f(t[i-3], w[i-3])) / 24
    
        # do Adams-Moulton to correct
        w[i+1] = w[i] + h*(9*f(t[i+1], w[i+1]) + 19*f(t[i], w[i]) - 5*f(t[i-1], w[i-1]) + f(t[i-2], w[i-2])) / 24

    return t, w
