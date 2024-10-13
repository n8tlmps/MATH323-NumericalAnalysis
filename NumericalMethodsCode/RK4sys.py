# this program solves first order system of odes using Runge-Kutta 4th
# order method
#
# Nate Talampas, 4/24/2024
import numpy as np
def RK4sys(F,a,b,alpha,m,N):

    # step size
    h = (b - a) / N
    

    # set t
    t = np.linspace(a, b, N+1)

    # reserve space for w, (N+1)-by-m zero matrix
    w = np.zeros((N+1, m))

    # w_i0 = alpha
    w[0] = alpha
    

    # reserve space for k1, k2, k3, k4
    k1 = np.zeros(m)
    k2 = np.zeros(m)
    k3 = np.zeros(m)
    k4 = np.zeros(m)

    # advance in time
    for i in range(N):
        
        # k1i = h*fi(tj,w1j,w2j,...)
        for j in range(m):
            k1[j] = h * F[j](t[i], w[i])
    
        # k2i = hfi(tj+h/2, w1j+1/2*k11,w2j+1/2*k12,...)
        for j in range(m):
            k2[j] = h * F[j](t[i] + h/2, w[i] + 0.5*k1)
        
    
        # k3i = hfi(tj+h/2, w1j+1/2*k21,w2j+1/2*k22,...)
        for j in range(m):
            k3[j] = h * F[j](t[i] + h/2, w[i] + 0.5*k2)
    
        # k4i = hfi(t_j+1, w1j+k31,w2j+k32,...)
        for j in range(m):
            k4[j] = h * F[j](t[i] + h, w[i] + k3)
    
        # w_{i,j+1} = w_{i,j} + 1/6*(k1i+2k2i+2k3i+k4i)
        for j in range(m):
            w[i+1, j] = w[i,j] + (k1[j] + 2*k2[j] + 2*k3[j] + k4[j]) / 6
    

    return t, w
