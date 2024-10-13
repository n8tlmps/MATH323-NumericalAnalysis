# this function does Gaussian Elimination with scaled partial pivoting 
# on the augmented matrix A and use backward substitution to solve the 
# system
#
# Nate Talampas, 5-1-2024
import numpy as np
def gaussianElimScaledPivot(A):
    # find the number of equations
    n = np.shape(A)[0]

    # find scale factor for every row
    s = np.max(abs(A[:,:-1]), axis = 1) # take max across columns (axis = 1) for each row

    # check if there is a row of zeros (some s entries are 0), if so, return a message stating there is no unique solution.
    if (any(s==0)):
        return "No unique solution exists."

    ## Gaussian Elimination
    # loop through rows
    for i in range(n):

        # look for the largest scaled entry in i-th col
        M = abs(A[i:,i])/s[i:]
        p = np.argmax(abs(M))

        
        # if the max scaled entry in i-th col is 0, there is no solution. return a message stating there is no unique solution
        if (M[p] == 0):
            return "No unique solution exists."


        # if the scaled max entry is below row i swaping rows i and p
        if p > 0:
            A[[i, i + p]] = A[[i + p, i]]
            s[i], s[i + p] = s[i + p], s[i]

        # use row operation to zero out the entries below the pivot
        for j in range(i + 1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]

    ## backward substitution
    # reserve space for x
    x = np.zeros(n)

    # xn = A(n,n+1)/A(n,n)
    x[n -1] = A[n - 1, n] / A[n - 1, n - 1]

    # go backward in rows to solve for x
    for k in reversed(range(n-1)):
        x[k] = (A[k, n] - np.dot(A[k, k + 1:n], x[k + 1:])) / A[k, k]

    return x
