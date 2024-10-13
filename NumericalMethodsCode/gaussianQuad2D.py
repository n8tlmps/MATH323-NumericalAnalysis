import numpy as np
# this program finds the approximated value of a 2-D integral using
# Gaussian quadrature in 2-D
# Last update: Name, Date
def gaussianQuad2D(f,a,b,c,d,n,m):
# store the coefficients and roots used for Gaussian Quadrature
# declare space for coefficients, use 4-by-5 zero array
    coef = np.zeros((4, 5))
# put coefficients for n = 2, 3, 4, 5 into the coefficient array
    coef[0][0] = 1.0000000000
    coef[0][1] = 1.0000000000
    coef[1][0] = 0.5555555556
    coef[1][1] = 0.8888888889
    coef[1][2] = 0.5555555556
    coef[2][0] = 0.3478548451
    coef[2][1] = 0.6521451549
    coef[2][2] = 0.6521451549
    coef[2][3] = 0.3478548451
    coef[3][0] = 0.2369268850
    coef[3][1] = 0.4786286705
    coef[3][2] = 0.5688888889
    coef[3][3] = 0.4786286705
    coef[3][4] = 0.2369268850
# declare space for integration points, use 4-by-5 zero array
    integPt = np.zeros((4, 5))
# put integration points for n = 2, 3, 4, 5 into the integration points array
    integPt[0][0] = .5773502692
    integPt[0][1] = -.5773502692
    integPt[1][0] = 0.7745966692
    integPt[1][1] = 0.0000000000
    integPt[1][2] = -0.7745966692
    integPt[2][0] = 0.8611363116
    integPt[2][1] = 0.3399810436
    integPt[2][2] = -0.3399810436
    integPt[2][3] = -0.8611363116
    integPt[3][0] = 0.9061798459
    integPt[3][1] = 0.5384693101
    integPt[3][2] = 0.0000000000
    integPt[3][3] = -0.5384693101
    integPt[3][4] = -0.9061798459

    # change variable of y, f(x,y) -> g(x,v)
    g = lambda x, v: f(x, (d(x) - c(x)) / 2)*v + ((d(x) + c(x)) / 2)*(d(x)-c(x))/2
# change variable of x. g(x,v) -> h(u,v)
    h = lambda u, v: g((b-a)/2 * u + (b+a)/2,v) * (b-a)/2
# now the integral is int_[-1 1] int_[-1 1] h(u,v) dv du
# start I as 0
    I = 0
# loop through the integration points and add the function values to I
# loop thorugh u_i
    for i in range(n):
# loop through v_j
        for j in range(m):
            I += coef[n-2][i] * coef[m-2][j] * h(integPt[n-2][i], integPt[m-2][j])
    return I

#import numpy as np
f1 = lambda x,y: np.cos(3*x**2+y) - np.sqrt(4*abs(y)) + 1/(x**2+y**2)
I1 = gaussianQuad2D(f1, -1.3, 4.1, lambda x: 2*x, lambda x: x**3, 3, 5)
I2 = gaussianQuad2D(f1, -1.3, 4.1, lambda x: -5*x, lambda x: x+4, 4, 2)
I3 = gaussianQuad2D(f1, 5.3, 10.1, lambda x: x**2, lambda x: np.cos(x), 4, 2)
print(f'I1 = {I1}, I2 = {I2}, I3 = {I3}')

