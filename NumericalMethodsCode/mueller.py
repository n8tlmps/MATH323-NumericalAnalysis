def mueller(f,p0,p1,p2,tol,maxN):
    h1 = p1 - p0
    h2 = p2 - p1
    d1 = (f(p1) - f(p0)) / h1
    d2 = (f(p2) - f(p1)) / h2
    d = (d2 - d1) / (h2 + h1)
    i = 1

    while i <= maxN:
        b = d2 + h2*d
        D = (b**2 - 4*f(p2)*d)**0.5

        if abs(b - D) < abs(b + D):
            E = b + D
        else:
            E = b - D

        h = -2 * f(p2) / E
        p = p2 + h

        if abs(h) < tol:
            return p, i
        p0 = p1
        p1 = p2
        p2 = p
        h1 = p1-p0
        h2 = p2-p1
        d1 = (f(p1) - f(p0)) / h1
        d2 = (f(p2) - f(p1)) / h2
        d = (d2 - d1)/(h2 + h1)
        i += 1

    print("Method failed.")



