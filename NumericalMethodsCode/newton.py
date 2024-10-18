def newton(f, fder, p0, tol, maxN):
    """
    Newton's method for finding roots.
    f: function for which root is sought
    fder: derivative of f
    p0: initial guess
    tol:  tolerance level
    maxN: maximum number of iterations
    """
    p = p0
    i = 1
    while i <= maxN:
        # update initial guess with Newton's method
        p_new = p - f(p) / fder(p)

        if abs(p_new - p) < tol:
            return p_new, i
        p = p_new
        i += 1
        
    print("The method failed after", maxN, "iterations.")
    return p