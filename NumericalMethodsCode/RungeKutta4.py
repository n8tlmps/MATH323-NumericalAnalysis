# this function numerically solve the IVP 
# y'= f(t,y), a<= t <= b, y(a) = alpha
# using Runge-Kutta of order 4
#
# Last update Name, Date 
import numpy as np
def RungeKutta4(f,a,b,alpha,N):

    # step size
    h = (b - a) / N

    # the time steps 
    t = np.linspace(a, b, N+1)

    # reserve space for w
    w = np.zeros(N+1)

    # w0 = alpha
    w[0] = alpha
   

    # for other time steps
    for i in range(1, N+1):
    
        # calculate k1, k2, k3, k4
        k1 = h*f(t[i-1],w[i-1])
        k2 = h*f(t[i-1]+h/2, w[i-1]+k1/2)
        k3 = h*f(t[i-1]+h/2, w[i-1]+k2/2)
        k4 = h*f(t[i-1]+h, w[i-1]+k3)
        

        # calculate next step
        w[i] = w[i-1] + (k1 + 2*k2 + 2*k3 + k4)/6

    return t,w