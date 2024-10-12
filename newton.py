def newton(f, fder, p0, tol, maxN):
    i = 1
    while i <= maxN:
        p = p0 - f(p0) / fder(p0)
        if abs(p - p0) < tol:
            return p, i
        i += 1
        p0 = p
    print("The method failed after", maxN, "iterations.")
    return p