def mueller(f, p0, p1, p2, tol, maxN):
    """
    Finds a solution to the function using Mueller's method.

    Parameters:
        f: The function whose root is to be found.
        p0, p1, p2: Initial guesses for the root.
        tol: The tolerance for the root.
        maxN: The maximum number of iterations.

    Returns:
        The approximate root of the function and the number of iterations.
    """
    
    # Calculate initial differences and derivatives
    h1 = p1 - p0
    h2 = p2 - p1
    d1 = (f(p1) - f(p0)) / h1
    d2 = (f(p2) - f(p1)) / h2
    d = (d2 - d1) / (h2 + h1)
    i = 1

    while i <= maxN:
        # Compute coefficients for the quadratic approximation
        b = d2 + h2 * d
        D_squared = b**2 - 4 * f(p2) * d  # Use squared D to avoid complex numbers

        # Check if D_squared is negative
        if D_squared < 0:
            print("Warning: D squared is negative; computation may be invalid.")
            return None, i  # Return None if computation is invalid

        D = D_squared**0.5

        # Determine E based on the signs of b and D
        E = b + D if abs(b - D) < abs(b + D) else b - D

        h = -2 * f(p2) / E
        p = p2 + h  # New approximation of the root

        # Check if the result is within the desired tolerance
        if abs(h) < tol:
            return p, i
        
        # Update the points for the next iteration
        p0, p1, p2 = p1, p2, p  # Shift points
        h1, h2 = p1 - p0, p2 - p1  # Update differences
        d1 = (f(p1) - f(p0)) / h1
        d2 = (f(p2) - f(p1)) / h2
        d = (d2 - d1) / (h2 + h1)  # Update derivative approximation
        i += 1

    print("Method failed to converge.")
    return None, i  # Return None if max iterations are reached




