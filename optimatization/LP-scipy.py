"""
Using scipy for optimizations:

-sciPy’s linear programming capabilities are useful mainly for smaller problems. For larger and more complex problems, you might find other libraries more suitable for the following reasons:

- SciPy can’t run various external solvers.

- SciPy can’t work with integer decision variables.

- SciPy doesn’t provide classes or functions that facilitate model building. You have to define arrays and matrices, which might be a tedious and error-prone task for large problems.

- SciPy doesn’t allow you to define maximization problems directly. You must convert them to minimization problems.

- SciPy doesn’t allow you to define constraints using the greater-than-or-equal-to sign directly. You must use the less-than-or-equal-to instead.

"""

from scipy.optimize import linprog
import numpy as np


def resource_allocation_2():
    obj = [-20, -12, -40, -25]

    lhs_ineq = [[1, 1, 1, 1],  # Manpower
                [3, 2, 1, 0],  # Material A
                [0, 1, 2, 3]]  # Material B

    rhs_ineq = [ 50,  # Manpower
                100,  # Material A
                90]  # Material B

    opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq,
                method="revised simplex")
    print(opt)


def resource_allocation_1():
    c = [-1,-2]
    A_ub=[
        [2,  1], 
        [-4, 5], 
        [1, -2]]

    b_ub=[
        20,
        10,
        2]

    A_eq=[[-1,5]]
    b_eq=[15]
    bounds=[
        (0, float("inf")), 
        (0, float("inf"))]

    opt = linprog(c,A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, method="revised simplex")
    print(opt)

if __name__ == "__main__":
    resource_allocation_1()

