# this function does Gaussian Elimination on the augmented matrix A
# and use backward substitution to solve the system
#
# Nate Talampas, 5-1-2024
import numpy as np
def gaussianElim(A):
    # find the number of equations, take the # of rows from A.shape
    n = np.shape(A)[0]

    ## Gaussian Elimination
    # going through rows, for loop through rows i = 0:n-1
    for i in range(n):
        # find the first nonzero entry in the i-th row from a_ii to a_in
        p_all = np.nonzero(A[i:,i])[0] # all indices of the nonzeros entries

        # if there is no nonzero entry, make x = message about no unique solution
        if p_all.size == 0:
            return "No unique solution exists"
        
        p = p_all[0] + i

        # if the nonzero entry is not at a_ii (p > 0), swap rows (row i and row p+i)
        if p > i:
            A[[i, p]] = A[[p, i]]

        # do row operations to zero out the entries below a_ii, for loop j = i+1:n-1, E_j <= E_j - a_{ji}/a_{ii} E_i
        for j in range(i + 1, n):
            A[j] -= A[i] * A[j, i] / A[i, i]

    ## backward substitution
    # reserve space for x
    x = np.zeros(n)
    
    # xn = A(n,n+1)/A(n,n)
    x[n - 1] = A[n - 1, n] / A[n - 1, n -1]
    
    # backward substitution, k = n-2, n-3,...,0
    for k in reversed(range(n-1)):
        x[k] = (A[k, n] - np.dot(A[k, k + 1:n], x[k + 1:])) / A[k, k]
    
    return x