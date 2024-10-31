import numpy as np
def compSimpson2D(f,a,b,c,d,n,m):
    h = (b-a)/n
    J1 = 0
    J2 = 0
    J3 = 0

    for i in range(n + 1):
        x = a + i*h
        HX = (d(x) - c(x)) / m
        K1 = f(x, c(x)) + f(x, d(x))
        K2 = 0
        K3 = 0

        for j in range(1, m):
            y = c(x) + j*HX
            Q = f(x, y)
            if j % 2 == 0:
                K2 = K2 + Q
            else:
                K3 = K3 + Q
        
        L = (K1 + 2*K2 + 4*K3) * HX / 3

        if i == 0 or i == n:
            J1 = J1 + L
        elif i % 2 == 0:
            J2 += L
        else:
            J3 += L

    J = h * (J1 + 2*J2 + 4*J3) / 3
    return J
