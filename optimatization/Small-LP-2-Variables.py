
from scipy.optimize import linprog
import numpy as np

def simple_example():
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
    simple_example()
