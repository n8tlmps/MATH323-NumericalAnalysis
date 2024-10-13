import numpy as np
def compositeSimpson(f, a, b, n):
    # check if n is even
    if n % 2 > 0:
        return np.empty(0)


    h = (b - a) / n
    XI0 = f(a) + f(b)
    XI1 = 0
    XI2 = 0

    for i in range(1, n):
        X = a + i * h
        if i % 2 == 0:
            XI2 += f(X)
        else:
            XI1 += f(X)

    XI = h * (XI0 + 2 * XI2 + 4 *XI1) / 3
    l = XI
    return l