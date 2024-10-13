# this program does the Euler method on ODE IVPs
#
# Last update: Name, Date
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

from CashKarpSys import CashKarpSys
f1 = lambda t,u: np.cos(4*u[0]**2 - t**3) -4*t +u[2]
f2 = lambda t,u: np.exp(-t)*u[0]*u[1]
f3 = lambda t,u: u[0]*u[2]-4*t**2
F1 = np.array([f1, f2, f3])
a1 = -1.4
b1 = 0.5
alpha1 = np.array([-6, 20.1, 2.1])
m1 = 3
h10 = 0.2
tol1 = 1e-2
t1, w1 = CashKarpSys(F1, a1, b1, alpha1, m1, h10, tol1)
print(f'[t1,w1] = ')
print(f'{np.hstack((t1.reshape(len(t1),1),w1))}')