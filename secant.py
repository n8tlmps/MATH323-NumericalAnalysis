def secant(f, p0, p1, tol, maxN):
    i = 1
    q0 = f(p0)
    q1 = f(p1)
    while i <= maxN:
        p = p1 - q1*(p1 - p0) / (q1 - q0)
        if abs(p - p1) < tol:
            return p, i
        i += 1
        p0 = p1
        q0 = q1
        p1 = p
        q1 = f(p)
    print("The method failed after", maxN, "iterations.")
    return p

