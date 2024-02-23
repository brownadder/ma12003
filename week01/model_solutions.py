import numpy as np
import collections

"""
*** model solutions for MA10276 ***

This file contain any code which will be used throughout the course, but
which is not explicitly made available to the students. To achieve this,
this file is compiled to .pyc bytecode on the server and then copied to the
.tools directory, from where it can be loaded with

import model_solutions

"""

##################################################################
# fast power method
##################################################################


def fast_power(x, n):
    """Compute x^n using recursion

    input:
      * x value to raise to the n-th power
      * n power n
    output:
      x^n
    """
    if n == 0:
        return 1
    elif n == 1:
        return x
    elif n == 2 * (n // 2):
        return fast_power(x * x, n // 2)
    else:
        return x * fast_power(x * x, (n - 1) // 2)


def fast_power_mat(A, n):
    """Compute matrix power A^n using recursion

    input:
      * A matrix to raise to the n-th power
      * n power n
    output:
      A^n
    """
    nrow, ncol = A.shape
    if not (n == int(n)):
        raise Exception("Can only raise matrix to integer powers.")
    elif n < 0:
        raise Exception("Can only raise matrix to non-negative powers.")
    elif not (nrow == ncol):
        raise Exception("Matrix must be square.")
    elif n == 0:
        return np.identity(nrow)
    elif n == 1:
        return A
    elif n == 2 * (n // 2):
        return fast_power_mat(A @ A, n // 2)
    else:
        return A @ fast_power_mat(A @ A, (n - 1) // 2)


##################################################################
# slow power method for matrices
##################################################################


def slow_power_mat(A, n):
    """Compute matrix power A^n using recursion

    input:
      * A matrix to raise to the n-th power
      * n power n
    output:
      A^n
    """
    nrow, ncol = A.shape
    if not (n == int(n)):
        raise Exception("Can only raise matrix to integer powers.")
    elif n < 0:
        raise Exception("Can only raise matrix to non-negative powers.")
    elif not (nrow == ncol):
        raise Exception("Matrix must be square.")
    elif n == 0:
        return np.identity(nrow)
    elif n == 1:
        return A
    else:
        return A @ slow_power_mat(A, n - 1)


##################################################################
# Fibonacci
##################################################################

### Tickable 4 ###


def fib_rec(n):
    """Compute n-th Fibonacci number recursively.

    The Fibonacci numbers are defined as:
    F_0 = 0, F_1 = 1, F_n = F_{n-1}+ F_{n-2} for n >= 2

    input: Number n
    output: n-th Fibonacci number F_n
    """
    if not (n == int(n)):
        raise Exception("Fibonacci number F_n not defined for non-integer values")
    elif n < 0:
        raise Exception("Fibonacci number F_n not defined for negative values")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)


def fib_iter(n):
    """Compute n-th Fibonacci number iteratively

    input: Number n
    output: n-th Fibonacci number F_n
    """

    if not (n == int(n)):
        raise Exception("Fibonacci number F_n not defined for non-integer values")
    elif n < 0:
        raise Exception("Fibonacci number F_n not defined for negative values")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        alpha = 0
        beta = 1
        for k in range(1, n):
            gamma = beta + alpha
            alpha = beta
            beta = gamma
        return gamma


### Tickable 5 ###


def fib_rec_mat_vec(n):
    """Compute the n-th Fibonacci vector (F_n, F_{n-1})

    input: Number n
    output: n-th Fibonacci vector (F_n, F_{n-1})
    """
    if not (n == int(n)):
        raise Exception("Fibonacci number F_n not defined for non-integer values")
    elif n < 0:
        raise Exception("Fibonacci number F_n not defined for negative values")
    elif n == 0:
        return np.array([0, 1])
    else:
        A_fib = np.array([[1, 1], [1, 0]])
        return A_fib @ fib_rec_mat_vec(n - 1)


def fib_rec_mat(n):
    """Compute the n-th Fibonacci number by extracting the first component
    of the n-th Fibonacci vector (F_n, F_{n-1})

    input: Number n
    output: n-th Fibonacci number F_n
    """
    if not (n == int(n)):
        raise Exception("Fibonacci number F_n not defined for non-integer values")
    elif n < 0:
        raise Exception("Fibonacci number F_n not defined for negative values")
    f_fib = fib_rec_mat_vec(n)
    return f_fib[0]


### Tickable 6 ###


def fib_rec_fast_mat(n):
    """Compute the n-th Fibonacci number by extracting the first component
    of the n-th Fibonacci vector (F_n, F_{n-1}).

    The Fibonacci vector is computed by raing the matrix A_fib = [[1,1],[1,0]]
    to the n-th power with the fast_power_mat() method.

    input: Number n
    output: n-th Fibonacci vector (F_n, F_{n-1})
    """
    if not (n == int(n)):
        raise Exception("Fibonacci number F_n not defined for non-integer values")
    elif n < 0:
        raise Exception("Fibonacci number F_n not defined for negative values")
    A_fib = np.array([[1, 1], [1, 0]])
    f_fib0 = np.array([0, 1])
    f_fib = fast_power_mat(A_fib, n) @ f_fib0
    return f_fib[0]


### Tickable 7 ###


def binary_search(a, x):
    """Find x in list a=[a_0,a_1,...,a_{n-1}] with a the binary search method

    input:
      * list a=[a_0,a_1,...,a_{n-1}] of length n
      * number x to be found
    returns:
      index j such that a_j = x or infinity if the list does not contain x
    """
    n = len(a)
    if n == 0:
        return np.infty
    elif n == 1:
        if a[0] == x:
            return 0
        else:
            return np.infty
    else:
        n_star = n // 2
        if x < a[n_star]:
            a_star = a[:n_star]
            return binary_search(a_star, x)
        else:
            a_star = a[n_star:]
            return n_star + binary_search(a_star, x)


##################################################################
# Sorting
##################################################################


def insertion_sort(a):
    """Sort list a using insertion sort and return sorted list

    input:
        a = list to be sorted
    output:
        sorted list containing all elements from a
    """
    # make a copy to avoid overwriting elements in the original list
    b = a.copy()
    for k in range(1, len(b)):
        x = b[k]
        j = k - 1
        while (j >= 0) and (b[j] > x):
            b[j + 1] = b[j]
            j = j - 1
        b[j + 1] = x
    return b


def merge(a1, a2):
    """Merge two sorted lists a1 and a2 and return merged list

    input:
        a1 = first sorted list
        a2 = second sorted list
    output:
        sorted list containing all elements from a1 and a2
    """
    a = []
    _a1 = collections.deque(a1)
    _a2 = collections.deque(a2)
    while (len(_a1) > 0) and (len(_a2) > 0):
        # Pick the smaller of the two elements
        if _a1[0] < _a2[0]:
            a.append(_a1.popleft())
        else:
            a.append(_a2.popleft())
    a += _a1
    a += _a2
    return a


def merge_sort(a):
    """Sort the list a in ascending order and return sorted list

    input:
        a = unsorted list
    output:
        sorted list containing all elements from a
    """
    n = len(a)
    if n == 1:
        return a
    else:
        a1 = a[: n // 2]
        a2 = a[n // 2 :]
        return merge(merge_sort(a1), merge_sort(a2))
