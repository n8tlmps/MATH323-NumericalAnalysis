import numpy as np

def naturalSpline(xx, ff):
    a = ff
    n = len(xx)
    h = np.zeros(n)
    alpha = np.zeros(n)
    b = np.zeros(n-1)
    c = np.zeros(n)
    d = np.zeros(n-1)

    # Step 1: computing h
    # h is the array storing differences between consecutive elements
    # reproesents the intervals between the given points
    for i in range(n-1):
        h[i] = xx[i+1] - xx[i]

    # Step 2: computing alpha
    # alpha is a parameter used in the spline calculations
    # based on the differences between consecutive function values in ff and the corresponding intervals in h
    for i in range(1, n-1):
         alpha[i] = (3 / h[i]) * (ff[i + 1] - ff[i]) - (3 / h[i - 1]) * (ff[i] - ff[i - 1])

    # Step 3: initialize l0, mu0, and z0
    # auxiliary ovariables used in the computation process
    l = np.zeros(n)
    mu = np.zeros(n)
    z = np.zeros(n)

    l[0] = 1
    mu[0] = 0
    z[0] = 0

    # Step 4 compute l, mu, and z
    # intermediate coefficients used to solve the tridiagonal linear system of equations formed by the second derivatives of the spline at each data point
    for i in range(1, n-1):
        l[i] = 2 * (xx[i + 1] - xx[i - 1]) - h[i - 1] * mu[i - 1]
        mu[i] = h[i] / l[i]
        z[i] = (alpha[i] - h[i - 1] * z[i - 1]) / l[i]

    # Step 5: boundary conditions
    # last elements of l and z to 1 and 0, according to natural spline boundary conditions
    l[n-1] = 1
    z[n-1] = 0

    # Step 6: Backward sub
    # solves for the coefficients of the cubic spline. Starting from the last data point, and moving backward, it computes the coefficient c, b, and d.
    for j in range(n - 2, -1, -1):
        c[j] = z[j] - mu[j]*c[j+1]
        b[j] = (a[j+1] - a[j]) / h[j]-h[j]*(c[j+1] + 2*c[j])/3
        d[j] = (c[j+1] - c[j])/(3*h[j])
    a = a[:-1]
    c = c[:-1]

    # Step 7
    return a, b, c, d